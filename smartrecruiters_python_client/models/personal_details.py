# coding: utf-8

"""
    Customer API - version 1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PersonalDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, first_name=None, last_name=None, email=None, phone_number=None, location=None, web=None):
        """
        PersonalDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'first_name': 'str',
            'last_name': 'str',
            'email': 'str',
            'phone_number': 'str',
            'location': 'CandidateLocation',
            'web': 'WebProfile'
        }

        self.attribute_map = {
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email': 'email',
            'phone_number': 'phoneNumber',
            'location': 'location',
            'web': 'web'
        }

        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone_number = phone_number
        self._location = location
        self._web = web

    @property
    def first_name(self):
        """
        Gets the first_name of this PersonalDetails.

        :return: The first_name of this PersonalDetails.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this PersonalDetails.

        :param first_name: The first_name of this PersonalDetails.
        :type: str
        """
        if first_name is not None and len(first_name) < 1:
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `1`")

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this PersonalDetails.

        :return: The last_name of this PersonalDetails.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this PersonalDetails.

        :param last_name: The last_name of this PersonalDetails.
        :type: str
        """
        if last_name is not None and len(last_name) < 1:
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `1`")

        self._last_name = last_name

    @property
    def email(self):
        """
        Gets the email of this PersonalDetails.

        :return: The email of this PersonalDetails.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this PersonalDetails.

        :param email: The email of this PersonalDetails.
        :type: str
        """

        self._email = email

    @property
    def phone_number(self):
        """
        Gets the phone_number of this PersonalDetails.

        :return: The phone_number of this PersonalDetails.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this PersonalDetails.

        :param phone_number: The phone_number of this PersonalDetails.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def location(self):
        """
        Gets the location of this PersonalDetails.

        :return: The location of this PersonalDetails.
        :rtype: CandidateLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this PersonalDetails.

        :param location: The location of this PersonalDetails.
        :type: CandidateLocation
        """

        self._location = location

    @property
    def web(self):
        """
        Gets the web of this PersonalDetails.

        :return: The web of this PersonalDetails.
        :rtype: WebProfile
        """
        return self._web

    @web.setter
    def web(self, web):
        """
        Sets the web of this PersonalDetails.

        :param web: The web of this PersonalDetails.
        :type: WebProfile
        """

        self._web = web

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PersonalDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
