# coding: utf-8

"""
    Unofficial python library for the SmartRecruiters API

    The SmartRecruiters API provides a platform to integrate services or applications, build apps and create fully customizable career sites. It exposes SmartRecruiters functionality and allows to connect and build software enhancing it.

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class JobPositions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, total_found=None, content=None):
        """
        JobPositions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total_found': 'int',
            'content': 'list[JobPosition]'
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
        Gets the total_found of this JobPositions.

        :return: The total_found of this JobPositions.
        :rtype: int
        """
        return self._total_found

    @total_found.setter
    def total_found(self, total_found):
        """
        Sets the total_found of this JobPositions.

        :param total_found: The total_found of this JobPositions.
        :type: int
        """
        if total_found is None:
            raise ValueError("Invalid value for `total_found`, must not be `None`")

        self._total_found = total_found

    @property
    def content(self):
        """
        Gets the content of this JobPositions.

        :return: The content of this JobPositions.
        :rtype: list[JobPosition]
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this JobPositions.

        :param content: The content of this JobPositions.
        :type: list[JobPosition]
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
        if not isinstance(other, JobPositions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
