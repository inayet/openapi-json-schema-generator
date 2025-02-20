# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.anyof_with_base_schema import AnyofWithBaseSchema
from unit_test_api.configurations import schema_configuration


class TestAnyofWithBaseSchema(unittest.TestCase):
    """AnyofWithBaseSchema unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration()

    def test_one_anyof_valid_passes(self):
        # one anyOf valid
        AnyofWithBaseSchema.validate(
            "foobar",
            configuration=self.configuration
        )

    def test_both_anyof_invalid_fails(self):
        # both anyOf invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            AnyofWithBaseSchema.validate(
                "foo",
                configuration=self.configuration
            )

    def test_mismatch_base_schema_fails(self):
        # mismatch base schema
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            AnyofWithBaseSchema.validate(
                3,
                configuration=self.configuration
            )


if __name__ == '__main__':
    unittest.main()
