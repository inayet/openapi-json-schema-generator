# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api import api_client

from . import schema


class Parameter0(api_client.PathParameter):
    name = "id"
    style = api_client.ParameterStyle.SIMPLE
    schema = schema.Schema
    required = True
