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
Cultivar: typing_extensions.TypeAlias = schemas.StrSchema
Mealy: typing_extensions.TypeAlias = schemas.BoolSchema
Properties = typing.TypedDict(
    'Properties',
    {
        "cultivar": typing.Type[Cultivar],
        "mealy": typing.Type[Mealy],
    }
)
AppleReqRequiredDictInput = typing.TypedDict(
    'AppleReqRequiredDictInput',
    {
        "cultivar": str,
    }
)
AppleReqOptionalDictInput = typing.TypedDict(
    'AppleReqOptionalDictInput',
    {
        "mealy": bool,
    },
    total=False
)


class AppleReqDict(schemas.immutabledict[str, typing.Union[
    bool,
    str,
]]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "cultivar",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "mealy",
    })
    
    def __new__(
        cls,
        *,
        cultivar: str,
        mealy: typing.Union[
            bool,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "cultivar": cultivar,
        }
        for key_, val in (
            ("mealy", mealy),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        used_arg_ = typing.cast(AppleReqDictInput, arg_)
        return AppleReq.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            AppleReqDictInput,
            AppleReqDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AppleReqDict:
        return AppleReq.validate(arg, configuration=configuration)
    
    @property
    def cultivar(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("cultivar")
        )
    
    @property
    def mealy(self) -> typing.Union[bool, schemas.Unset]:
        val = self.get("mealy", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            bool,
            val
        )


class AppleReqDictInput(AppleReqRequiredDictInput, AppleReqOptionalDictInput):
    pass


@dataclasses.dataclass(frozen=True)
class AppleReq(
    schemas.Schema[AppleReqDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "cultivar",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: AppleReqDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            AppleReqDictInput,
            AppleReqDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> AppleReqDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

