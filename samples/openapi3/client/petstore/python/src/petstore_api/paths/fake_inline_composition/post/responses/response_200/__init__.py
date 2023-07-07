# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.response_imports import *

from .content.application_json import schema as application_json_schema
from .content.multipart_form_data import schema as multipart_form_data_schema


@dataclasses.dataclass
class ApiResponseFor200(api_response.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        schemas.OUTPUT_BASE_TYPES,
        multipart_form_data_schema.SchemaDict,
    ]
    headers: schemas.Unset = schemas.unset


class ResponseFor200(api_client.OpenApiResponse[ApiResponseFor200]):
    response_cls = ApiResponseFor200


    class ApplicationJsonMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_json_schema.Schema


    class MultipartFormDataMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = multipart_form_data_schema.Schema
    Content = typing_extensions.TypedDict(
        'Content',
        {
            'application/json': typing.Type[ApplicationJsonMediaType],
            'multipart/form-data': typing.Type[MultipartFormDataMediaType],
        }
    )
    content: Content = {
        'application/json': ApplicationJsonMediaType,
        'multipart/form-data': MultipartFormDataMediaType,
    }
