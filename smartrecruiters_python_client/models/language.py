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


class Language(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, code=None, label=None, label_native=None):
        """
        Language - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'code': 'str',
            'label': 'str',
            'label_native': 'str'
        }

        self.attribute_map = {
            'code': 'code',
            'label': 'label',
            'label_native': 'labelNative'
        }

        self._code = code
        self._label = label
        self._label_native = label_native

    @property
    def code(self):
        """
        Gets the code of this Language.

        :return: The code of this Language.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this Language.

        :param code: The code of this Language.
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def label(self):
        """
        Gets the label of this Language.

        :return: The label of this Language.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this Language.

        :param label: The label of this Language.
        :type: str
        """

        self._label = label

    @property
    def label_native(self):
        """
        Gets the label_native of this Language.

        :return: The label_native of this Language.
        :rtype: str
        """
        return self._label_native

    @label_native.setter
    def label_native(self, label_native):
        """
        Sets the label_native of this Language.

        :param label_native: The label_native of this Language.
        :type: str
        """

        self._label_native = label_native

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
        if not isinstance(other, Language):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other