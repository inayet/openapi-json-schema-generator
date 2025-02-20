# coding: utf-8

"""
    Example
    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import json_schema_api
from json_schema_api.components.schema.object_dependent_required import ObjectDependentRequired


class TestObjectDependentRequired(unittest.TestCase):
    """ObjectDependentRequired unit test stubs"""

    def test_success_with_key_and_conditionally_required_keys(self):
        inst = ObjectDependentRequired.validate({'a': 1, 'b': 2})
        assert inst == {'a': 1, 'b': 2}

    def test_success_without_key(self):
        inst = ObjectDependentRequired.validate({'b': 2})
        assert inst == {'b': 2}

    def test_failure(self):
        with self.assertRaises(json_schema_api.ApiValueError):
            ObjectDependentRequired.validate({'a': 1, 'c': 2})

if __name__ == '__main__':
    unittest.main()
