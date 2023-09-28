# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from unit_test_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema
Bar: typing_extensions.TypeAlias = schemas.AnyTypeSchema
Properties2 = typing.TypedDict(
    'Properties2',
    {
        "bar": typing.Type[Bar],
    }
)


class FooDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "bar",
    })
    
    def __new__(
        cls,
        *,
        bar: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("bar", bar),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        used_arg_ = typing.cast(FooDictInput, arg_)
        return Foo2.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            FooDictInput,
            FooDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> FooDict:
        return Foo2.validate(arg, configuration=configuration)
    
    @property
    def bar(self) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        val = self.get("bar", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schemas.OUTPUT_BASE_TYPES,
            val
        )
FooDictInput = typing.TypedDict(
    'FooDictInput',
    {
        "bar": typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES
        ],
    },
    total=False
)


@dataclasses.dataclass(frozen=True)
class Foo2(
    schemas.Schema[FooDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties2 = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties2)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: FooDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            FooDictInput,
            FooDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> FooDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

DependentSchemas = typing.TypedDict(
    'DependentSchemas',
    {
        "foo": typing.Type[Foo2],
    }
)
Foo: typing_extensions.TypeAlias = schemas.AnyTypeSchema
Properties = typing.TypedDict(
    'Properties',
    {
        "foo": typing.Type[Foo],
    }
)


class DependentSchemasDependentSubschemaIncompatibleWithRootDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "foo",
    })
    
    def __new__(
        cls,
        *,
        foo: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("foo", foo),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(DependentSchemasDependentSubschemaIncompatibleWithRootDictInput, arg_)
        return DependentSchemasDependentSubschemaIncompatibleWithRoot.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            DependentSchemasDependentSubschemaIncompatibleWithRootDictInput,
            DependentSchemasDependentSubschemaIncompatibleWithRootDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> DependentSchemasDependentSubschemaIncompatibleWithRootDict:
        return DependentSchemasDependentSubschemaIncompatibleWithRoot.validate(arg, configuration=configuration)
    
    @property
    def foo(self) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        val = self.get("foo", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schemas.OUTPUT_BASE_TYPES,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
DependentSchemasDependentSubschemaIncompatibleWithRootDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class DependentSchemasDependentSubschemaIncompatibleWithRoot(
    schemas.AnyTypeSchema[DependentSchemasDependentSubschemaIncompatibleWithRootDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    dependent_schemas: DependentSchemas = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(DependentSchemas)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: DependentSchemasDependentSubschemaIncompatibleWithRootDict,
        }
    )

