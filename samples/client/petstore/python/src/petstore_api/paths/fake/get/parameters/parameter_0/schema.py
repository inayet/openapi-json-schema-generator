# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class ItemsEnums:

    @schemas.classproperty
    def GREATER_THAN_SIGN(cls) -> typing.Literal[">"]:
        return Items.validate(">")

    @schemas.classproperty
    def DOLLAR_SIGN(cls) -> typing.Literal["$"]:
        return Items.validate("$")


@dataclasses.dataclass(frozen=True)
class Items(
    schemas.Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    default: typing.Literal["$"] = "$"
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            ">": "GREATER_THAN_SIGN",
            "$": "DOLLAR_SIGN",
        }
    )
    enums = ItemsEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal[">"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[">"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["$"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["$"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[">","$",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        ">",
        "$",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                ">",
                "$",
            ],
            validated_arg
        )


class SchemaTuple(
    typing.Tuple[
        typing.Literal[">", "$"],
        ...
    ]
):

    def __new__(cls, arg: typing.Union[SchemaTupleInput, SchemaTuple], configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return Schema.validate(arg, configuration=configuration)
SchemaTupleInput = typing.Union[
    typing.List[
        typing.Literal[
            ">",
            "$"
        ],
    ],
    typing.Tuple[
        typing.Literal[
            ">",
            "$"
        ],
        ...
    ]
]


@dataclasses.dataclass(frozen=True)
class Schema(
    schemas.Schema[schemas.immutabledict, SchemaTuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: SchemaTuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            SchemaTupleInput,
            SchemaTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> SchemaTuple:
        return super().validate_base(
            arg,
            configuration=configuration,
        )
