# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.StrSchema


class MapPropertyDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    def __new__(
        cls,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: str,
    ):
        used_kwargs = typing.cast(MapPropertyDictInput, kwargs)
        return MapProperty.validate(used_kwargs, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            MapPropertyDictInput,
            MapPropertyDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapPropertyDict:
        return MapProperty.validate(arg, configuration=configuration)
    
    def get_additional_property_(self, name: str) -> typing.Union[str, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        val = self.get(name, schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
MapPropertyDictInput = typing.Mapping[
    str,
    str,
]


@dataclasses.dataclass(frozen=True)
class MapProperty(
    schemas.Schema[MapPropertyDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: MapPropertyDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            MapPropertyDictInput,
            MapPropertyDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapPropertyDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

AdditionalProperties3: typing_extensions.TypeAlias = schemas.StrSchema


class AdditionalPropertiesDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    def __new__(
        cls,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: str,
    ):
        used_kwargs = typing.cast(AdditionalPropertiesDictInput, kwargs)
        return AdditionalProperties2.validate(used_kwargs, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            AdditionalPropertiesDictInput,
            AdditionalPropertiesDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AdditionalPropertiesDict:
        return AdditionalProperties2.validate(arg, configuration=configuration)
    
    def get_additional_property_(self, name: str) -> typing.Union[str, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        val = self.get(name, schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
AdditionalPropertiesDictInput = typing.Mapping[
    str,
    str,
]


@dataclasses.dataclass(frozen=True)
class AdditionalProperties2(
    schemas.Schema[AdditionalPropertiesDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    additional_properties: typing.Type[AdditionalProperties3] = dataclasses.field(default_factory=lambda: AdditionalProperties3) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: AdditionalPropertiesDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            AdditionalPropertiesDictInput,
            AdditionalPropertiesDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AdditionalPropertiesDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )



class MapOfMapPropertyDict(schemas.immutabledict[str, AdditionalPropertiesDict]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    def __new__(
        cls,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            AdditionalPropertiesDictInput,
            AdditionalPropertiesDict,
        ],
    ):
        used_kwargs = typing.cast(MapOfMapPropertyDictInput, kwargs)
        return MapOfMapProperty.validate(used_kwargs, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            MapOfMapPropertyDictInput,
            MapOfMapPropertyDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapOfMapPropertyDict:
        return MapOfMapProperty.validate(arg, configuration=configuration)
    
    def get_additional_property_(self, name: str) -> typing.Union[AdditionalPropertiesDict, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        val = self.get(name, schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            AdditionalPropertiesDict,
            val
        )
MapOfMapPropertyDictInput = typing.Mapping[
    str,
    typing.Union[
        AdditionalPropertiesDictInput,
        AdditionalPropertiesDict,
    ],
]


@dataclasses.dataclass(frozen=True)
class MapOfMapProperty(
    schemas.Schema[MapOfMapPropertyDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    additional_properties: typing.Type[AdditionalProperties2] = dataclasses.field(default_factory=lambda: AdditionalProperties2) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: MapOfMapPropertyDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            MapOfMapPropertyDictInput,
            MapOfMapPropertyDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapOfMapPropertyDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

Anytype1: typing_extensions.TypeAlias = schemas.AnyTypeSchema
MapWithUndeclaredPropertiesAnytype1: typing_extensions.TypeAlias = schemas.DictSchema
MapWithUndeclaredPropertiesAnytype2: typing_extensions.TypeAlias = schemas.DictSchema
AdditionalProperties4: typing_extensions.TypeAlias = schemas.AnyTypeSchema


class MapWithUndeclaredPropertiesAnytype3Dict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    def __new__(
        cls,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        used_kwargs = typing.cast(MapWithUndeclaredPropertiesAnytype3DictInput, kwargs)
        return MapWithUndeclaredPropertiesAnytype3.validate(used_kwargs, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            MapWithUndeclaredPropertiesAnytype3DictInput,
            MapWithUndeclaredPropertiesAnytype3Dict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapWithUndeclaredPropertiesAnytype3Dict:
        return MapWithUndeclaredPropertiesAnytype3.validate(arg, configuration=configuration)
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        val = self.get(name, schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schemas.OUTPUT_BASE_TYPES,
            val
        )
MapWithUndeclaredPropertiesAnytype3DictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class MapWithUndeclaredPropertiesAnytype3(
    schemas.Schema[MapWithUndeclaredPropertiesAnytype3Dict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    additional_properties: typing.Type[AdditionalProperties4] = dataclasses.field(default_factory=lambda: AdditionalProperties4) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: MapWithUndeclaredPropertiesAnytype3Dict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            MapWithUndeclaredPropertiesAnytype3DictInput,
            MapWithUndeclaredPropertiesAnytype3Dict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapWithUndeclaredPropertiesAnytype3Dict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

AdditionalProperties5: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema


class EmptyMapDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    # map with no key value pairs
    def __new__(
        cls,
        arg: EmptyMapDictInput,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        return EmptyMap.validate(arg, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            EmptyMapDictInput,
            EmptyMapDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> EmptyMapDict:
        return EmptyMap.validate(arg, configuration=configuration)
EmptyMapDictInput = typing.Mapping # mapping must be empty


@dataclasses.dataclass(frozen=True)
class EmptyMap(
    schemas.Schema[EmptyMapDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    additional_properties: typing.Type[AdditionalProperties5] = dataclasses.field(default_factory=lambda: AdditionalProperties5) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: EmptyMapDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            EmptyMapDictInput,
            EmptyMapDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> EmptyMapDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

AdditionalProperties6: typing_extensions.TypeAlias = schemas.StrSchema


class MapWithUndeclaredPropertiesStringDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    def __new__(
        cls,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: str,
    ):
        used_kwargs = typing.cast(MapWithUndeclaredPropertiesStringDictInput, kwargs)
        return MapWithUndeclaredPropertiesString.validate(used_kwargs, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            MapWithUndeclaredPropertiesStringDictInput,
            MapWithUndeclaredPropertiesStringDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapWithUndeclaredPropertiesStringDict:
        return MapWithUndeclaredPropertiesString.validate(arg, configuration=configuration)
    
    def get_additional_property_(self, name: str) -> typing.Union[str, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        val = self.get(name, schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
MapWithUndeclaredPropertiesStringDictInput = typing.Mapping[
    str,
    str,
]


@dataclasses.dataclass(frozen=True)
class MapWithUndeclaredPropertiesString(
    schemas.Schema[MapWithUndeclaredPropertiesStringDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    additional_properties: typing.Type[AdditionalProperties6] = dataclasses.field(default_factory=lambda: AdditionalProperties6) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: MapWithUndeclaredPropertiesStringDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            MapWithUndeclaredPropertiesStringDictInput,
            MapWithUndeclaredPropertiesStringDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MapWithUndeclaredPropertiesStringDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

Properties = typing.TypedDict(
    'Properties',
    {
        "map_property": typing.Type[MapProperty],
        "map_of_map_property": typing.Type[MapOfMapProperty],
        "anytype_1": typing.Type[Anytype1],
        "map_with_undeclared_properties_anytype_1": typing.Type[MapWithUndeclaredPropertiesAnytype1],
        "map_with_undeclared_properties_anytype_2": typing.Type[MapWithUndeclaredPropertiesAnytype2],
        "map_with_undeclared_properties_anytype_3": typing.Type[MapWithUndeclaredPropertiesAnytype3],
        "empty_map": typing.Type[EmptyMap],
        "map_with_undeclared_properties_string": typing.Type[MapWithUndeclaredPropertiesString],
    }
)


class AdditionalPropertiesClassDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "map_property",
        "map_of_map_property",
        "anytype_1",
        "map_with_undeclared_properties_anytype_1",
        "map_with_undeclared_properties_anytype_2",
        "map_with_undeclared_properties_anytype_3",
        "empty_map",
        "map_with_undeclared_properties_string",
    })
    
    def __new__(
        cls,
        *,
        map_property: typing.Union[
            MapPropertyDictInput,
            MapPropertyDict,
            schemas.Unset
        ] = schemas.unset,
        map_of_map_property: typing.Union[
            MapOfMapPropertyDictInput,
            MapOfMapPropertyDict,
            schemas.Unset
        ] = schemas.unset,
        anytype_1: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        map_with_undeclared_properties_anytype_1: typing.Union[
            typing.Mapping[str, schemas.INPUT_TYPES_ALL],
            schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
            schemas.Unset
        ] = schemas.unset,
        map_with_undeclared_properties_anytype_2: typing.Union[
            typing.Mapping[str, schemas.INPUT_TYPES_ALL],
            schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
            schemas.Unset
        ] = schemas.unset,
        map_with_undeclared_properties_anytype_3: typing.Union[
            MapWithUndeclaredPropertiesAnytype3DictInput,
            MapWithUndeclaredPropertiesAnytype3Dict,
            schemas.Unset
        ] = schemas.unset,
        empty_map: typing.Union[
            EmptyMapDictInput,
            EmptyMapDict,
            schemas.Unset
        ] = schemas.unset,
        map_with_undeclared_properties_string: typing.Union[
            MapWithUndeclaredPropertiesStringDictInput,
            MapWithUndeclaredPropertiesStringDict,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key_, val in (
            ("map_property", map_property),
            ("map_of_map_property", map_of_map_property),
            ("anytype_1", anytype_1),
            ("map_with_undeclared_properties_anytype_1", map_with_undeclared_properties_anytype_1),
            ("map_with_undeclared_properties_anytype_2", map_with_undeclared_properties_anytype_2),
            ("map_with_undeclared_properties_anytype_3", map_with_undeclared_properties_anytype_3),
            ("empty_map", empty_map),
            ("map_with_undeclared_properties_string", map_with_undeclared_properties_string),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(AdditionalPropertiesClassDictInput, arg_)
        return AdditionalPropertiesClass.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            AdditionalPropertiesClassDictInput,
            AdditionalPropertiesClassDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AdditionalPropertiesClassDict:
        return AdditionalPropertiesClass.validate(arg, configuration=configuration)
    
    @property
    def map_property(self) -> typing.Union[MapPropertyDict, schemas.Unset]:
        val = self.get("map_property", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            MapPropertyDict,
            val
        )
    
    @property
    def map_of_map_property(self) -> typing.Union[MapOfMapPropertyDict, schemas.Unset]:
        val = self.get("map_of_map_property", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            MapOfMapPropertyDict,
            val
        )
    
    @property
    def anytype_1(self) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        val = self.get("anytype_1", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return val
    
    @property
    def map_with_undeclared_properties_anytype_1(self) -> typing.Union[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], schemas.Unset]:
        val = self.get("map_with_undeclared_properties_anytype_1", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
            val
        )
    
    @property
    def map_with_undeclared_properties_anytype_2(self) -> typing.Union[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], schemas.Unset]:
        val = self.get("map_with_undeclared_properties_anytype_2", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
            val
        )
    
    @property
    def map_with_undeclared_properties_anytype_3(self) -> typing.Union[MapWithUndeclaredPropertiesAnytype3Dict, schemas.Unset]:
        val = self.get("map_with_undeclared_properties_anytype_3", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            MapWithUndeclaredPropertiesAnytype3Dict,
            val
        )
    
    @property
    def empty_map(self) -> typing.Union[EmptyMapDict, schemas.Unset]:
        val = self.get("empty_map", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            EmptyMapDict,
            val
        )
    
    @property
    def map_with_undeclared_properties_string(self) -> typing.Union[MapWithUndeclaredPropertiesStringDict, schemas.Unset]:
        val = self.get("map_with_undeclared_properties_string", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            MapWithUndeclaredPropertiesStringDict,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
AdditionalPropertiesClassDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class AdditionalPropertiesClass(
    schemas.Schema[AdditionalPropertiesClassDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: AdditionalPropertiesClassDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            AdditionalPropertiesClassDictInput,
            AdditionalPropertiesClassDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AdditionalPropertiesClassDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

