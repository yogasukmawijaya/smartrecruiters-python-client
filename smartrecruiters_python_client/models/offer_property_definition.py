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


class OfferPropertyDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, key=None, label=None, required=None, type=None):
        """
        OfferPropertyDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'key': 'str',
            'label': 'str',
            'required': 'bool',
            'type': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'label': 'label',
            'required': 'required',
            'type': 'type'
        }

        self._key = key
        self._label = label
        self._required = required
        self._type = type

    @property
    def key(self):
        """
        Gets the key of this OfferPropertyDefinition.

        :return: The key of this OfferPropertyDefinition.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this OfferPropertyDefinition.

        :param key: The key of this OfferPropertyDefinition.
        :type: str
        """

        self._key = key

    @property
    def label(self):
        """
        Gets the label of this OfferPropertyDefinition.

        :return: The label of this OfferPropertyDefinition.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this OfferPropertyDefinition.

        :param label: The label of this OfferPropertyDefinition.
        :type: str
        """

        self._label = label

    @property
    def required(self):
        """
        Gets the required of this OfferPropertyDefinition.

        :return: The required of this OfferPropertyDefinition.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this OfferPropertyDefinition.

        :param required: The required of this OfferPropertyDefinition.
        :type: bool
        """

        self._required = required

    @property
    def type(self):
        """
        Gets the type of this OfferPropertyDefinition.

        :return: The type of this OfferPropertyDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this OfferPropertyDefinition.

        :param type: The type of this OfferPropertyDefinition.
        :type: str
        """
        allowed_values = ["BOOLEAN", "COUNTRY", "CURRENCY", "DATE", "NUMBER", "PERCENT", "REGION", "TEXT", "USER", "SELECT"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, OfferPropertyDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
