# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.integer_type_matches_integers import IntegerTypeMatchesIntegers
from unit_test_api.configurations import schema_configuration


class TestIntegerTypeMatchesIntegers(unittest.TestCase):
    """IntegerTypeMatchesIntegers unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration()

    def test_an_object_is_not_an_integer_fails(self):
        # an object is not an integer
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            IntegerTypeMatchesIntegers.validate(
                {
                },
                configuration=self.configuration
            )

    def test_a_string_is_not_an_integer_fails(self):
        # a string is not an integer
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            IntegerTypeMatchesIntegers.validate(
                "foo",
                configuration=self.configuration
            )

    def test_null_is_not_an_integer_fails(self):
        # null is not an integer
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            IntegerTypeMatchesIntegers.validate(
                None,
                configuration=self.configuration
            )

    def test_a_float_with_zero_fractional_part_is_an_integer_passes(self):
        # a float with zero fractional part is an integer
        IntegerTypeMatchesIntegers.validate(
            1.0,
            configuration=self.configuration
        )

    def test_a_float_is_not_an_integer_fails(self):
        # a float is not an integer
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            IntegerTypeMatchesIntegers.validate(
                1.1,
                configuration=self.configuration
            )

    def test_a_boolean_is_not_an_integer_fails(self):
        # a boolean is not an integer
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            IntegerTypeMatchesIntegers.validate(
                True,
                configuration=self.configuration
            )

    def test_an_integer_is_an_integer_passes(self):
        # an integer is an integer
        IntegerTypeMatchesIntegers.validate(
            1,
            configuration=self.configuration
        )

    def test_a_string_is_still_not_an_integer_even_if_it_looks_like_one_fails(self):
        # a string is still not an integer, even if it looks like one
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            IntegerTypeMatchesIntegers.validate(
                "1",
                configuration=self.configuration
            )

    def test_an_array_is_not_an_integer_fails(self):
        # an array is not an integer
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            IntegerTypeMatchesIntegers.validate(
                [
                ],
                configuration=self.configuration
            )


if __name__ == '__main__':
    unittest.main()
