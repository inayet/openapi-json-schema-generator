# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import datetime  # noqa: F401
import decimal  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class GmFruit(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        # any type
        
        class Properties:
            Color = schemas.StrSchema
            __annotations__ = {
                "color": Color,
            }
        
        class AnyOf:
        
            @staticmethod
            def _0() -> typing.Type['apple.Apple']:
                return apple.Apple
        
            @staticmethod
            def _1() -> typing.Type['banana.Banana']:
                return banana.Banana
            classes = [
                _0,
                _1,
            ]

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> Schema_.Properties.Color: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["color"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)


from petstore_api.components.schema import apple
from petstore_api.components.schema import banana
