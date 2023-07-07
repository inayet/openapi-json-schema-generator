# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from unit_test_api.shared_imports.schema_imports import *



class _0Dict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @property
    def bar(self) -> schemas.OUTPUT_BASE_TYPES:
        return self.__getitem__("bar")
    
    @property
    def foo(self) -> schemas.OUTPUT_BASE_TYPES:
        return self.__getitem__("foo")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bar"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foo"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.OUTPUT_BASE_TYPES: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["bar"],
            typing_extensions.Literal["foo"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: _0DictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return _0.validate(arg, configuration=configuration)
_0DictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


@dataclasses.dataclass(frozen=True)
class _0(
    schemas.AnyTypeSchema[_0Dict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    required: typing.FrozenSet[str] = frozenset({
        "bar",
        "foo",
    })
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: _0Dict,
        }
    )



class _1Dict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    @property
    def baz(self) -> schemas.OUTPUT_BASE_TYPES:
        return self.__getitem__("baz")
    
    @property
    def foo(self) -> schemas.OUTPUT_BASE_TYPES:
        return self.__getitem__("foo")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["baz"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foo"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.OUTPUT_BASE_TYPES: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["baz"],
            typing_extensions.Literal["foo"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(cls, arg: _1DictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return _1.validate(arg, configuration=configuration)
_1DictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


@dataclasses.dataclass(frozen=True)
class _1(
    schemas.AnyTypeSchema[_1Dict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    required: typing.FrozenSet[str] = frozenset({
        "baz",
        "foo",
    })
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: _1Dict,
        }
    )

OneOf = typing.Tuple[
    typing.Type[_0],
    typing.Type[_1],
]


@dataclasses.dataclass(frozen=True)
class OneofWithRequired(
    schemas.DictSchema[schemas.immutabledict]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({
        schemas.immutabledict,
    })
    one_of: OneOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(OneOf)) # type: ignore

    @classmethod
    def validate(
        cls,
        arg: typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> schemas.immutabledict[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]:
        return super().validate(
            arg,
            configuration=configuration,
        )
