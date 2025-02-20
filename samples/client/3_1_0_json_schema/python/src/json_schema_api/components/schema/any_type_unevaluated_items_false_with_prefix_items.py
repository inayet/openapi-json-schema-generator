# coding: utf-8

"""
    Example
    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from json_schema_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

_0: typing_extensions.TypeAlias = schemas.StrSchema
_Not: typing_extensions.TypeAlias = schemas.AnyTypeSchema


@dataclasses.dataclass(frozen=True)
class UnevaluatedItems(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    not_: typing.Type[_Not] = dataclasses.field(default_factory=lambda: _Not) # type: ignore



@dataclasses.dataclass(frozen=True)
class AnyTypeUnevaluatedItemsFalseWithPrefixItems(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    prefix_items: typing.Tuple[
        typing.Type[_0],
    ] = (
        _0,
    )
    unevaluated_items: typing.Type[UnevaluatedItems] = dataclasses.field(default_factory=lambda: UnevaluatedItems) # type: ignore

