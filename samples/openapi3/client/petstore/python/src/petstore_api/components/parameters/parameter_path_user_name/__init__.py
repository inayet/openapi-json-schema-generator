# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.header_imports import *

from . import schema


class PathUserName(api_client.PathParameter):
    name = "username"
    style = api_client.ParameterStyle.SIMPLE
    schema: typing_extensions.TypeAlias = schema.Schema
    required = True
