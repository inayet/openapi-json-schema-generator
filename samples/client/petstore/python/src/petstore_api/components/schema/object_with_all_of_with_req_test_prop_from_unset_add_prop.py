# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

Name: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "name": typing.Type[Name],
    }
)


class _1Dict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "test",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "name",
    })
    @staticmethod
    def from_dict_(
        arg: _1DictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> _1Dict:
        return _1.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        *,
        test: typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES
        ],
        name: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "test": test,
        }
        for key, val in (
            ("name", name),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(_1DictInput, arg_)
        return _1.validate(used_arg_, configuration=configuration_)

    
    @property
    def test(self) -> schemas.OUTPUT_BASE_TYPES:
        return typing.cast(
            schemas.OUTPUT_BASE_TYPES,
            self.__getitem__("test")
        )
    
    @property
    def name(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("name", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
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
    required: typing.FrozenSet[str] = frozenset({
        "test",
    })
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
class ObjectWithAllOfWithReqTestPropFromUnsetAddProp(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    all_of: AllOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(AllOf)) # type: ignore


from petstore_api.components.schema import object_with_optional_test_prop
AllOf = typing.Tuple[
    typing.Type[object_with_optional_test_prop.ObjectWithOptionalTestProp],
    typing.Type[_1],
]
