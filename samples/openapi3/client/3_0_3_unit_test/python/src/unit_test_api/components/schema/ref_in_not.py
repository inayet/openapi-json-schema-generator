# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from unit_test_api.shared_imports.schema_imports import *



@dataclasses.dataclass(frozen=True)
class RefInNot(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    not_: typing.Type[property_named_ref_that_is_not_a_reference.PropertyNamedRefThatIsNotAReference] = dataclasses.field(default_factory=lambda: property_named_ref_that_is_not_a_reference.PropertyNamedRefThatIsNotAReference) # type: ignore


from unit_test_api.components.schema import property_named_ref_that_is_not_a_reference
