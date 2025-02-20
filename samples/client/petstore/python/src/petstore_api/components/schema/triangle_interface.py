# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class ShapeTypeEnums:

    @schemas.classproperty
    def TRIANGLE(cls) -> typing.Literal["Triangle"]:
        return ShapeType.validate("Triangle")


@dataclasses.dataclass(frozen=True)
class ShapeType(
    schemas.Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "Triangle": "TRIANGLE",
        }
    )
    enums = ShapeTypeEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["Triangle"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["Triangle"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["Triangle",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "Triangle",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                "Triangle",
            ],
            validated_arg
        )
TriangleType: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing.TypedDict(
    'Properties',
    {
        "shapeType": typing.Type[ShapeType],
        "triangleType": typing.Type[TriangleType],
    }
)


class TriangleInterfaceDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "shapeType",
        "triangleType",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        shapeType: typing.Literal[
            "Triangle"
        ],
        triangleType: str,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "shapeType": shapeType,
            "triangleType": triangleType,
        }
        arg_.update(kwargs)
        used_arg_ = typing.cast(TriangleInterfaceDictInput, arg_)
        return TriangleInterface.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            TriangleInterfaceDictInput,
            TriangleInterfaceDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> TriangleInterfaceDict:
        return TriangleInterface.validate(arg, configuration=configuration)
    
    @property
    def shapeType(self) -> typing.Literal["Triangle"]:
        return typing.cast(
            typing.Literal["Triangle"],
            self.__getitem__("shapeType")
        )
    
    @property
    def triangleType(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("triangleType")
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
TriangleInterfaceDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class TriangleInterface(
    schemas.AnyTypeSchema[TriangleInterfaceDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    required: typing.FrozenSet[str] = frozenset({
        "shapeType",
        "triangleType",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: TriangleInterfaceDict,
        }
    )

