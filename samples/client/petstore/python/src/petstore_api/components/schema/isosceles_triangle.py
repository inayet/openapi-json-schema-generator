# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class TriangleTypeEnums:

    @schemas.classproperty
    def ISOSCELES_TRIANGLE(cls) -> typing.Literal["IsoscelesTriangle"]:
        return TriangleType.validate("IsoscelesTriangle")


@dataclasses.dataclass(frozen=True)
class TriangleType(
    schemas.Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "IsoscelesTriangle": "ISOSCELES_TRIANGLE",
        }
    )
    enums = TriangleTypeEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["IsoscelesTriangle"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["IsoscelesTriangle"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["IsoscelesTriangle",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "IsoscelesTriangle",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                "IsoscelesTriangle",
            ],
            validated_arg
        )
Properties = typing.TypedDict(
    'Properties',
    {
        "triangleType": typing.Type[TriangleType],
    }
)


class _1Dict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "triangleType",
    })
    
    def __new__(
        cls,
        *,
        triangleType: typing.Union[
            typing.Literal[
                "IsoscelesTriangle"
            ],
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key_, val in (
            ("triangleType", triangleType),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(_1DictInput, arg_)
        return _1.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            _1DictInput,
            _1Dict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> _1Dict:
        return _1.validate(arg, configuration=configuration)
    
    @property
    def triangleType(self) -> typing.Union[typing.Literal["IsoscelesTriangle"], schemas.Unset]:
        val = self.get("triangleType", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            typing.Literal["IsoscelesTriangle"],
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
_1DictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class _1(
    schemas.Schema[_1Dict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: _1Dict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            _1DictInput,
            _1Dict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> _1Dict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass(frozen=True)
class IsoscelesTriangle(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    all_of: AllOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(AllOf)) # type: ignore


from petstore_api.components.schema import triangle_interface
AllOf = typing.Tuple[
    typing.Type[triangle_interface.TriangleInterface],
    typing.Type[_1],
]
