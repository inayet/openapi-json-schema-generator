# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

A: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing.TypedDict(
    'Properties',
    {
        "a": typing.Type[A],
    }
)


class ObjWithRequiredPropsDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "a",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        a: str,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "a": a,
        }
        arg_.update(kwargs)
        used_arg_ = typing.cast(ObjWithRequiredPropsDictInput, arg_)
        return ObjWithRequiredProps.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            ObjWithRequiredPropsDictInput,
            ObjWithRequiredPropsDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ObjWithRequiredPropsDict:
        return ObjWithRequiredProps.validate(arg, configuration=configuration)
    
    @property
    def a(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("a")
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
ObjWithRequiredPropsDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class ObjWithRequiredProps(
    schemas.Schema[ObjWithRequiredPropsDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "a",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    all_of: AllOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(AllOf)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ObjWithRequiredPropsDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ObjWithRequiredPropsDictInput,
            ObjWithRequiredPropsDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ObjWithRequiredPropsDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )


from petstore_api.components.schema import obj_with_required_props_base
AllOf = typing.Tuple[
    typing.Type[obj_with_required_props_base.ObjWithRequiredPropsBase],
]
