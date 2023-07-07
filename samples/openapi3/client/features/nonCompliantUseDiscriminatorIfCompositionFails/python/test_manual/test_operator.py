# coding: utf-8

"""
    discriminator-test

    No description provided (generated by Openapi Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

from this_package import schemas
from this_package.components.schema import operator
from this_package.components.schema.addition_operator import AdditionOperator
from this_package.components.schema.subtraction_operator import SubtractionOperator


class TestOperator(unittest.TestCase):
    """Operator unit test stubs"""

    def test_discriminator_works(self):
        op = operator.Operator.validate({
            'operator_id': 'ADD',
            'a': 3.14,
            'b': 3.14
        })
        assert op == dict(
            operator_id='ADD',
            a=3.14,
            b=3.14
        )
        """
        even though the payload validates with AdditionOperator + SubtractionOperator
        only AdditionOperator is used because nonCompliantUseDiscriminatorIfCompositionFails=true
        and discriminator validation was used when composed schema validation failed
        """
        assert isinstance(op, schemas.immutabledict)


if __name__ == '__main__':
    unittest.main()
