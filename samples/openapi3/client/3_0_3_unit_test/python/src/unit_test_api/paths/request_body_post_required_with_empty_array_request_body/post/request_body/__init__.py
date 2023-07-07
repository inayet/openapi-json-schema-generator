# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from unit_test_api.shared_imports.header_imports import *

from .content.application_json import schema as application_json_schema

class RequestBody(api_client.RequestBody):


    class ApplicationJsonMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_json_schema.Schema
    Content = typing_extensions.TypedDict(
        'Content',
        {
            'application/json': typing.Type[ApplicationJsonMediaType],
        }
    )
    content: Content = {
        'application/json': ApplicationJsonMediaType,
    }
    required = True
