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


class Publication(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, aggregators=True, visibility='PUBLIC'):
        """
        Publication - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'aggregators': 'bool',
            'visibility': 'str'
        }

        self.attribute_map = {
            'aggregators': 'aggregators',
            'visibility': 'visibility'
        }

        self._aggregators = aggregators
        self._visibility = visibility

    @property
    def aggregators(self):
        """
        Gets the aggregators of this Publication.

        :return: The aggregators of this Publication.
        :rtype: bool
        """
        return self._aggregators

    @aggregators.setter
    def aggregators(self, aggregators):
        """
        Sets the aggregators of this Publication.

        :param aggregators: The aggregators of this Publication.
        :type: bool
        """

        self._aggregators = aggregators

    @property
    def visibility(self):
        """
        Gets the visibility of this Publication.

        :return: The visibility of this Publication.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """
        Sets the visibility of this Publication.

        :param visibility: The visibility of this Publication.
        :type: str
        """
        allowed_values = ["PUBLIC", "INTERNAL"]
        if visibility not in allowed_values:
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

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
        if not isinstance(other, Publication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other