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
class Pig(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    discriminator: typing.Mapping[str, typing.Mapping[str, typing.Type[schemas.Schema]]] = dataclasses.field(
        default_factory=lambda: {
            'className': {
                'BasquePig': basque_pig.BasquePig,
                'DanishPig': danish_pig.DanishPig,
            }
        }
    )
    one_of: OneOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(OneOf)) # type: ignore


from petstore_api.components.schema import basque_pig
from petstore_api.components.schema import danish_pig
OneOf = typing.Tuple[
    typing.Type[basque_pig.BasquePig],
    typing.Type[danish_pig.DanishPig],
]
