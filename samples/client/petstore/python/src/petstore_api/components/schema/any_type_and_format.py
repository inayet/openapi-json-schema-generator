# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



@dataclasses.dataclass(frozen=True)
class Uuid(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'uuid'



@dataclasses.dataclass(frozen=True)
class Date(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'date'



@dataclasses.dataclass(frozen=True)
class DateTime(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'date-time'



@dataclasses.dataclass(frozen=True)
class Number(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'number'



@dataclasses.dataclass(frozen=True)
class Binary(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'binary'



@dataclasses.dataclass(frozen=True)
class Int32(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'int32'



@dataclasses.dataclass(frozen=True)
class Int64(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'int64'



@dataclasses.dataclass(frozen=True)
class Double(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'double'



@dataclasses.dataclass(frozen=True)
class _Float(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    format: str = 'float'

Properties = typing.TypedDict(
    'Properties',
    {
        "uuid": typing.Type[Uuid],
        "date": typing.Type[Date],
        "date-time": typing.Type[DateTime],
        "number": typing.Type[Number],
        "binary": typing.Type[Binary],
        "int32": typing.Type[Int32],
        "int64": typing.Type[Int64],
        "double": typing.Type[Double],
        "float": typing.Type[_Float],
    }
)


class AnyTypeAndFormatDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "uuid",
        "date",
        "date-time",
        "number",
        "binary",
        "int32",
        "int64",
        "double",
        "float",
    })
    
    def __new__(
        cls,
        *,
        uuid: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        date: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        number: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        binary: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        int32: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        int64: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        double: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key_, val in (
            ("uuid", uuid),
            ("date", date),
            ("number", number),
            ("binary", binary),
            ("int32", int32),
            ("int64", int64),
            ("double", double),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(AnyTypeAndFormatDictInput, arg_)
        return AnyTypeAndFormat.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            AnyTypeAndFormatDictInput,
            AnyTypeAndFormatDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AnyTypeAndFormatDict:
        return AnyTypeAndFormat.validate(arg, configuration=configuration)
    
    @property
    def uuid(self) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        val = self.get("uuid", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return val
    
    @property
    def date(self) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        val = self.get("date", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return val
    
    @property
    def number(self) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        val = self.get("number", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return val
    
    @property
    def binary(self) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        val = self.get("binary", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return val
    
    @property
    def int32(self) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        val = self.get("int32", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return val
    
    @property
    def int64(self) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        val = self.get("int64", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return val
    
    @property
    def double(self) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        val = self.get("double", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return val
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
AnyTypeAndFormatDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class AnyTypeAndFormat(
    schemas.Schema[AnyTypeAndFormatDict, tuple]
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
            schemas.immutabledict: AnyTypeAndFormatDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            AnyTypeAndFormatDictInput,
            AnyTypeAndFormatDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AnyTypeAndFormatDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

