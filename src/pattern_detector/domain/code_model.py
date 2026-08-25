"""Domain AST and structural model for Julia codebases (.jl)."""

from __future__ import annotations

from dataclasses import dataclass, field
from pattern_detector.domain.value_objects import SourceLocation


@dataclass
class JuliaField:
    """Represents a field in a Julia struct."""

    name: str
    type_name: str = "Any"
    is_const: bool = False  # Julia 1.8+ const struct fields
    location: SourceLocation | None = None
    raw_text: str = ""


@dataclass
class JuliaStruct:
    """Represents a `struct` or `mutable struct` in Julia."""

    name: str
    is_mutable: bool = False
    is_parametric: bool = False
    type_parameters: list[str] = field(default_factory=list)
    super_type: str | None = None
    fields: list[JuliaField] = field(default_factory=list)
    inner_constructors: list[str] = field(default_factory=list)
    location: SourceLocation | None = None
    line_count: int = 1
    raw_text: str = ""

    @property
    def is_singleton(self) -> bool:
        return len(self.fields) == 0 and not self.is_mutable


@dataclass
class JuliaAbstractType:
    """Represents an `abstract type Foo <: Bar end` declaration."""

    name: str
    is_parametric: bool = False
    type_parameters: list[str] = field(default_factory=list)
    super_type: str | None = None
    location: SourceLocation | None = None
    raw_text: str = ""


@dataclass
class JuliaFunction:
    """Represents a function, method, macro, or callable struct functor in Julia."""

    name: str
    signature: str = ""
    is_macro: bool = False
    is_mutating: bool = False  # ends with '!'
    is_callable_struct: bool = False
    parameters: list[tuple[str, str]] = field(default_factory=list)  # (arg_name, type_annotation)
    return_type: str = "Any"
    body: str = ""
    branch_count: int = 1
    location: SourceLocation | None = None
    raw_text: str = ""

    @property
    def is_operator(self) -> bool:
        return self.name.startswith("Base.") or self.name in ("+", "-", "*", "/", "==", "<", ">", "iterate", "show", "convert", "promote_rule")


@dataclass
class JuliaModule:
    """Represents a `module ... end` in Julia."""

    name: str
    exported_symbols: list[str] = field(default_factory=list)
    structs: list[JuliaStruct] = field(default_factory=list)
    abstract_types: list[JuliaAbstractType] = field(default_factory=list)
    functions: list[JuliaFunction] = field(default_factory=list)
    location: SourceLocation | None = None


@dataclass
class JuliaFile:
    """Represents a single parsed Julia source file (.jl)."""

    file_path: str
    modules: list[JuliaModule] = field(default_factory=list)
    structs: list[JuliaStruct] = field(default_factory=list)
    abstract_types: list[JuliaAbstractType] = field(default_factory=list)
    functions: list[JuliaFunction] = field(default_factory=list)
    includes: list[str] = field(default_factory=list)
    usings: list[str] = field(default_factory=list)
    imports: list[str] = field(default_factory=list)
    lines: list[str] = field(default_factory=list)
    raw_content: str = ""


@dataclass
class CodeModel:
    """Aggregate model representing all parsed Julia files in the target codebase."""

    files: list[JuliaFile] = field(default_factory=list)
    target_path: str = ""

    @property
    def all_structs(self) -> list[JuliaStruct]:
        structs: list[JuliaStruct] = []
        for f in self.files:
            structs.extend(f.structs)
            for m in f.modules:
                structs.extend(m.structs)
        return structs

    @property
    def all_abstract_types(self) -> list[JuliaAbstractType]:
        absts: list[JuliaAbstractType] = []
        for f in self.files:
            absts.extend(f.abstract_types)
            for m in f.modules:
                absts.extend(m.abstract_types)
        return absts

    @property
    def all_functions(self) -> list[JuliaFunction]:
        fns: list[JuliaFunction] = []
        for f in self.files:
            fns.extend(f.functions)
            for m in f.modules:
                fns.extend(m.functions)
        return fns

    @property
    def all_macros(self) -> list[JuliaFunction]:
        return [fn for fn in self.all_functions if fn.is_macro]

    @property
    def all_modules(self) -> list[JuliaModule]:
        mods: list[JuliaModule] = []
        for f in self.files:
            mods.extend(f.modules)
        return mods
