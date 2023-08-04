# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

B: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "b": typing.Type[B],
    }
)


class ObjWithRequiredPropsBaseDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "b",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    @staticmethod
    def from_dict_(
        arg: ObjWithRequiredPropsBaseDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ObjWithRequiredPropsBaseDict:
        return ObjWithRequiredPropsBase.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        *,
        b: str,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "b": b,
        }
        arg_.update(kwargs)
        used_arg_ = typing.cast(ObjWithRequiredPropsBaseDictInput, arg_)
        return ObjWithRequiredPropsBase.validate(used_arg_, configuration=configuration_)

    
    @property
    def b(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("b")
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
ObjWithRequiredPropsBaseDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class ObjWithRequiredPropsBase(
    schemas.Schema[ObjWithRequiredPropsBaseDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "b",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ObjWithRequiredPropsBaseDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ObjWithRequiredPropsBaseDictInput,
            ObjWithRequiredPropsBaseDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ObjWithRequiredPropsBaseDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

