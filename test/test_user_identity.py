# coding: utf-8

"""
    Customer API - version 1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import smartrecruiters_python_client
from smartrecruiters_python_client.rest import ApiException
from smartrecruiters_python_client.models.user_identity import UserIdentity


class TestUserIdentity(unittest.TestCase):
    """ UserIdentity unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserIdentity(self):
        """
        Test UserIdentity
        """
        model = smartrecruiters_python_client.models.user_identity.UserIdentity()


if __name__ == '__main__':
    unittest.main()