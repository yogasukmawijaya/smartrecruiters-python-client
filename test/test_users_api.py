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
from smartrecruiters_python_client.apis.users_api import UsersApi


class TestUsersApi(unittest.TestCase):
    """ UsersApi unit test stubs """

    def setUp(self):
        self.api = smartrecruiters_python_client.apis.users_api.UsersApi()

    def tearDown(self):
        pass

    def test_users_activation_activate(self):
        """
        Test case for users_activation_activate

        Activate a user
        """
        pass

    def test_users_activation_deactivate(self):
        """
        Test case for users_activation_deactivate

        Deactivate a user
        """
        pass

    def test_users_activation_delete(self):
        """
        Test case for users_activation_delete

        Deactivate a user
        """
        pass

    def test_users_activation_email_send(self):
        """
        Test case for users_activation_email_send

        Send an activation email to a user
        """
        pass

    def test_users_all(self):
        """
        Test case for users_all

        List users of your company
        """
        pass

    def test_users_avatar_update(self):
        """
        Test case for users_avatar_update

        Update user avatar
        """
        pass

    def test_users_create(self):
        """
        Test case for users_create

        Create a new user.
        """
        pass

    def test_users_get(self):
        """
        Test case for users_get

        Get details of a user with given id
        """
        pass

    def test_users_me(self):
        """
        Test case for users_me

        Get details of my user
        """
        pass

    def test_users_update(self):
        """
        Test case for users_update

        Update a user
        """
        pass


if __name__ == '__main__':
    unittest.main()