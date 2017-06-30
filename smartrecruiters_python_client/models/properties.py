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


class Properties(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, total_found=None, content=None):
        """
        Properties - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total_found': 'int',
            'content': 'list[ModelProperty]'
        }

        self.attribute_map = {
            'total_found': 'totalFound',
            'content': 'content'
        }

        self._total_found = total_found
        self._content = content

    @property
    def total_found(self):
        """
        Gets the total_found of this Properties.

        :return: The total_found of this Properties.
        :rtype: int
        """
        return self._total_found

    @total_found.setter
    def total_found(self, total_found):
        """
        Sets the total_found of this Properties.

        :param total_found: The total_found of this Properties.
        :type: int
        """

        self._total_found = total_found

    @property
    def content(self):
        """
        Gets the content of this Properties.

        :return: The content of this Properties.
        :rtype: list[ModelProperty]
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this Properties.

        :param content: The content of this Properties.
        :type: list[ModelProperty]
        """

        self._content = content

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
        if not isinstance(other, Properties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
