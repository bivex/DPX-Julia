"""High-speed native parser adapter for Julia source code (.jl)."""

from __future__ import annotations

import re
from pattern_detector.domain.code_model import (
    CodeModel,
    JuliaAbstractType,
    JuliaField,
    JuliaFile,
    JuliaFunction,
    JuliaModule,
    JuliaStruct,
)
from pattern_detector.domain.value_objects import SourceLocation
from pattern_detector.ports.outbound import ParserPort


class NativeJuliaParserAdapter(ParserPort):
    """Linear, robust single-pass parser extracting Julia AST semantics."""

    MODULE_START = re.compile(r"^\s*module\s+([A-Za-z0-9_]+)")
    ABSTRACT_TYPE_PATTERN = re.compile(
        r"^\s*abstract\s+type\s+(?P<name>[A-Za-z0-9_]+)(?:\{(?P<params>[^}]+)\})?(?:\s*<:\s*(?P<super>[A-Za-z0-9_.]+))?"
    )
    STRUCT_START_PATTERN = re.compile(
        r"^\s*(?P<mutable>mutable\s+)?struct\s+(?P<name>[A-Za-z0-9_]+)(?:\{(?P<params>[^}]+)\})?(?:\s*<:\s*(?P<super>[A-Za-z0-9_.]+))?"
    )
    FIELD_PATTERN = re.compile(
        r"^\s*(?P<const>const\s+)?(?P<name>[A-Za-z0-9_]+)(?:\s*::\s*(?P<type>[A-Za-z0-9_{},.\s]+))?\s*$"
    )
    FUNCTION_BLOCK_PATTERN = re.compile(
        r"^\s*(?P<kind>function|macro)\s+(?:\((?P<callable_receiver>[^)]+)\)\s*)?(?P<name>[A-Za-z0-9_.!]+)?\s*(?:\((?P<params>.*)\))?(?:\s*::\s*(?P<return_type>[A-Za-z0-9_{},.]+))?"
    )
    ONE_LINER_FUNC_PATTERN = re.compile(
        r"^\s*(?:\((?P<callable_receiver>[^)]+)\)\s*)?(?:(?P<name>[A-Za-z0-9_.!]+)\s*)?\((?P<params>[^)]*)\)(?:\s*::\s*(?P<return_type>[A-Za-z0-9_{},.]+))?\s*=\s*(?P<body>.+)$"
    )

    BLOCK_OPENERS = re.compile(r"\b(if|for|while|let|try|begin|quote|function|macro|struct)\b")
    BLOCK_CLOSERS = re.compile(r"\bend\b")

    def parse_file(self, file_path: str, content: str) -> JuliaFile:
        lines = content.splitlines()
        file_obj = JuliaFile(file_path=file_path, raw_content=content, lines=lines)

        current_module: JuliaModule | None = None
        current_struct: JuliaStruct | None = None
        current_function: JuliaFunction | None = None
        current_func_body: list[str] = []

        block_depth = 0
        struct_block_depth = 0
        func_block_depth = 0
        module_block_depth = 0

        for line_idx, raw_line in enumerate(lines, 1):
            trimmed = raw_line.strip()

            # Skip comments
            if trimmed.startswith("#") or not trimmed:
                continue

            # Check Module
            mod_m = self.MODULE_START.match(trimmed)
            if mod_m and block_depth == 0:
                current_module = JuliaModule(
                    name=mod_m.group(1),
                    location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                )
                file_obj.modules.append(current_module)
                module_block_depth = block_depth
                block_depth += 1
                continue

            # Check Abstract Type
            abst_m = self.ABSTRACT_TYPE_PATTERN.match(trimmed)
            if abst_m:
                name = abst_m.group("name")
                params_str = abst_m.group("params") or ""
                super_t = abst_m.group("super")
                params = [p.strip() for p in params_str.split(",") if p.strip()]

                abst = JuliaAbstractType(
                    name=name,
                    is_parametric=bool(params),
                    type_parameters=params,
                    super_type=super_t,
                    location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                    raw_text=raw_line,
                )
                if current_module:
                    current_module.abstract_types.append(abst)
                else:
                    file_obj.abstract_types.append(abst)
                continue

            # Check Struct Start
            struct_m = self.STRUCT_START_PATTERN.match(trimmed)
            if struct_m and not current_struct and not current_function:
                name = struct_m.group("name")
                is_mut = bool(struct_m.group("mutable"))
                params_str = struct_m.group("params") or ""
                super_t = struct_m.group("super")
                params = [p.strip() for p in params_str.split(",") if p.strip()]

                is_one_line_end = trimmed.endswith(" end") or trimmed.endswith("\tend")
                new_struct = JuliaStruct(
                    name=name,
                    is_mutable=is_mut,
                    is_parametric=bool(params),
                    type_parameters=params,
                    super_type=super_t,
                    location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                    raw_text=raw_line,
                )

                if is_one_line_end:
                    if current_module:
                        current_module.structs.append(new_struct)
                    else:
                        file_obj.structs.append(new_struct)
                    continue

                current_struct = new_struct
                struct_block_depth = block_depth
                block_depth += 1
                continue

            # Parse struct fields inside struct
            if current_struct and not current_function:
                if trimmed == "end":
                    if current_struct.location:
                        current_struct.line_count = line_idx - current_struct.location.line + 1
                    if current_module:
                        current_module.structs.append(current_struct)
                    else:
                        file_obj.structs.append(current_struct)
                    current_struct = None
                    block_depth -= 1
                    continue

                field_m = self.FIELD_PATTERN.match(trimmed)
                if field_m and not any(kw in trimmed for kw in ("function", "end", "new(", "if", "for")):
                    f_name = field_m.group("name")
                    f_type = (field_m.group("type") or "Any").strip()
                    f_const = bool(field_m.group("const"))
                    current_struct.fields.append(
                        JuliaField(
                            name=f_name,
                            type_name=f_type,
                            is_const=f_const,
                            location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                            raw_text=raw_line,
                        )
                    )
                    continue

            # Check Function Block
            fn_block_m = self.FUNCTION_BLOCK_PATTERN.match(trimmed)
            if fn_block_m and not current_function:
                is_macro = (fn_block_m.group("kind") == "macro")
                f_name = fn_block_m.group("name") or ""
                callable_rec = fn_block_m.group("callable_receiver")
                if callable_rec and not f_name:
                    f_name = callable_rec.split("::")[-1].strip() if "::" in callable_rec else callable_rec.strip()
                elif not f_name:
                    f_name = "anonymous"
                params_str = fn_block_m.group("params") or ""
                ret_t = (fn_block_m.group("return_type") or "Any").strip()

                params: list[tuple[str, str]] = []
                for p in params_str.split(","):
                    p_clean = p.strip()
                    if "::" in p_clean:
                        p_n, p_t = p_clean.split("::", 1)
                        params.append((p_n.strip(), p_t.strip()))
                    elif p_clean:
                        params.append((p_clean, "Any"))

                is_one_line_func = trimmed.endswith(" end")
                current_function = JuliaFunction(
                    name=f_name,
                    signature=trimmed,
                    is_macro=is_macro,
                    is_mutating=f_name.endswith("!"),
                    is_callable_struct=bool(callable_rec),
                    parameters=params,
                    return_type=ret_t,
                    location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                    raw_text=raw_line,
                )

                if is_one_line_func:
                    current_function.body = trimmed
                    if current_module:
                        current_module.functions.append(current_function)
                    else:
                        file_obj.functions.append(current_function)
                    current_function = None
                    continue

                current_func_body = [raw_line]
                func_block_depth = block_depth
                block_depth += 1
                continue

            # Check One-Liner Function `foo(x) = ...` or `(p::Poly)(x) = ...`
            if not current_function and not current_struct:
                one_m = self.ONE_LINER_FUNC_PATTERN.match(trimmed)
                if one_m and not trimmed.startswith("return") and not trimmed.startswith("const"):
                    callable_rec = one_m.group("callable_receiver")
                    f_name = one_m.group("name") or ""
                    if callable_rec and not f_name:
                        f_name = callable_rec.split("::")[-1].strip() if "::" in callable_rec else callable_rec.strip()
                    params_str = one_m.group("params") or ""
                    ret_t = (one_m.group("return_type") or "Any").strip()
                    body_text = one_m.group("body")

                    params = []
                    for p in params_str.split(","):
                        p_clean = p.strip()
                        if "::" in p_clean:
                            p_n, p_t = p_clean.split("::", 1)
                            params.append((p_n.strip(), p_t.strip()))
                        elif p_clean:
                            params.append((p_clean, "Any"))

                    one_fn = JuliaFunction(
                        name=f_name,
                        signature=trimmed.split("=")[0].strip(),
                        is_macro=False,
                        is_mutating=f_name.endswith("!"),
                        is_callable_struct=bool(callable_rec),
                        parameters=params,
                        return_type=ret_t,
                        body=body_text,
                        branch_count=1 + len(self.BRANCH_KEYWORDS.findall(body_text)),
                        location=SourceLocation(file_path=file_path, line=line_idx, column=1),
                        raw_text=raw_line,
                    )
                    if current_module:
                        current_module.functions.append(one_fn)
                    else:
                        file_obj.functions.append(one_fn)
                    continue

            # Accumulate function body
            if current_function:
                current_func_body.append(raw_line)
                current_function.branch_count += len(self.BRANCH_KEYWORDS.findall(raw_line))

                openers = len(self.BLOCK_OPENERS.findall(trimmed))
                closers = len(self.BLOCK_CLOSERS.findall(trimmed))
                block_depth += (openers - closers)

                if block_depth <= func_block_depth:
                    current_function.body = "\n".join(current_func_body)
                    if current_module:
                        current_module.functions.append(current_function)
                    else:
                        file_obj.functions.append(current_function)
                    current_function = None
                    current_func_body = []
                continue

            # Check Module End
            if current_module and trimmed == "end" and block_depth == module_block_depth + 1:
                current_module = None
                block_depth -= 1

        return file_obj

    def parse_codebase(self, files: list[tuple[str, str]], target_path: str = "") -> CodeModel:
        model = CodeModel(target_path=target_path)
        for fpath, content in files:
            jl_file = self.parse_file(fpath, content)
            model.files.append(jl_file)
        return model
