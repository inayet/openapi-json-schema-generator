# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema
Amount: typing_extensions.TypeAlias = schemas.DecimalSchema

from petstore_api.components.schema import currency
Properties = typing.TypedDict(
    'Properties',
    {
        "amount": typing.Type[Amount],
        "currency": typing.Type[currency.Currency],
    }
)


class MoneyDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "amount",
        "currency",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        amount: str,
        currency: typing.Literal[
            "eur",
            "usd"
        ],
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "amount": amount,
            "currency": currency,
        }
        used_arg_ = typing.cast(MoneyDictInput, arg_)
        return Money.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            MoneyDictInput,
            MoneyDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MoneyDict:
        return Money.validate(arg, configuration=configuration)
    
    @property
    def amount(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("amount")
        )
    
    @property
    def currency(self) -> typing.Literal["eur", "usd"]:
        return typing.cast(
            typing.Literal["eur", "usd"],
            self.__getitem__("currency")
        )
MoneyDictInput = typing.TypedDict(
    'MoneyDictInput',
    {
        "amount": str,
        "currency": typing.Literal[
            "eur",
            "usd"
        ],
    }
)


@dataclasses.dataclass(frozen=True)
class Money(
    schemas.Schema[MoneyDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "amount",
        "currency",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: MoneyDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            MoneyDictInput,
            MoneyDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> MoneyDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

