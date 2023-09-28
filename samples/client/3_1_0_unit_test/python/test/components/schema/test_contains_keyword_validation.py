# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.contains_keyword_validation import ContainsKeywordValidation
from unit_test_api.configurations import schema_configuration


class TestContainsKeywordValidation(unittest.TestCase):
    """ContainsKeywordValidation unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration(
        disabled_json_schema_keywords={'format'}
    )

    def test_empty_array_is_invalid_fails(self):
        # empty array is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ContainsKeywordValidation.validate(
                [
                ],
                configuration=self.configuration
            )

    def test_array_with_item_matching_schema5_is_valid_passes(self):
        # array with item matching schema (5) is valid
        ContainsKeywordValidation.validate(
            [
                3,
                4,
                5,
            ],
            configuration=self.configuration
        )

    def test_array_with_two_items_matching_schema56_is_valid_passes(self):
        # array with two items matching schema (5, 6) is valid
        ContainsKeywordValidation.validate(
            [
                3,
                4,
                5,
                6,
            ],
            configuration=self.configuration
        )

    def test_not_array_is_valid_passes(self):
        # not array is valid
        ContainsKeywordValidation.validate(
            {
            },
            configuration=self.configuration
        )

    def test_array_without_items_matching_schema_is_invalid_fails(self):
        # array without items matching schema is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ContainsKeywordValidation.validate(
                [
                    2,
                    3,
                    4,
                ],
                configuration=self.configuration
            )

    def test_array_with_item_matching_schema6_is_valid_passes(self):
        # array with item matching schema (6) is valid
        ContainsKeywordValidation.validate(
            [
                3,
                4,
                6,
            ],
            configuration=self.configuration
        )


if __name__ == '__main__':
    unittest.main()
