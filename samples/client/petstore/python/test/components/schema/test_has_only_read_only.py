# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import petstore_api
from petstore_api.components.schema.has_only_read_only import HasOnlyReadOnly
from petstore_api.configurations import schema_configuration


class TestHasOnlyReadOnly(unittest.TestCase):
    """HasOnlyReadOnly unit test stubs"""
    configuration_ = schema_configuration.SchemaConfiguration()


if __name__ == '__main__':
    unittest.main()
