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


class Sources(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, total_found=None, limit=None, offset=None, content=None):
        """
        Sources - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total_found': 'int',
            'limit': 'int',
            'offset': 'int',
            'content': 'list[Source]'
        }

        self.attribute_map = {
            'total_found': 'totalFound',
            'limit': 'limit',
            'offset': 'offset',
            'content': 'content'
        }

        self._total_found = total_found
        self._limit = limit
        self._offset = offset
        self._content = content

    @property
    def total_found(self):
        """
        Gets the total_found of this Sources.

        :return: The total_found of this Sources.
        :rtype: int
        """
        return self._total_found

    @total_found.setter
    def total_found(self, total_found):
        """
        Sets the total_found of this Sources.

        :param total_found: The total_found of this Sources.
        :type: int
        """
        if total_found is None:
            raise ValueError("Invalid value for `total_found`, must not be `None`")

        self._total_found = total_found

    @property
    def limit(self):
        """
        Gets the limit of this Sources.

        :return: The limit of this Sources.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this Sources.

        :param limit: The limit of this Sources.
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")

        self._limit = limit

    @property
    def offset(self):
        """
        Gets the offset of this Sources.

        :return: The offset of this Sources.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this Sources.

        :param offset: The offset of this Sources.
        :type: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")

        self._offset = offset

    @property
    def content(self):
        """
        Gets the content of this Sources.

        :return: The content of this Sources.
        :rtype: list[Source]
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this Sources.

        :param content: The content of this Sources.
        :type: list[Source]
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")

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
        if not isinstance(other, Sources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
