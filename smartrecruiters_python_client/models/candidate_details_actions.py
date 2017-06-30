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


class CandidateDetailsActions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, properties=None, attachments=None):
        """
        CandidateDetailsActions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'properties': 'Action',
            'attachments': 'Action'
        }

        self.attribute_map = {
            'properties': 'properties',
            'attachments': 'attachments'
        }

        self._properties = properties
        self._attachments = attachments

    @property
    def properties(self):
        """
        Gets the properties of this CandidateDetailsActions.

        :return: The properties of this CandidateDetailsActions.
        :rtype: Action
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CandidateDetailsActions.

        :param properties: The properties of this CandidateDetailsActions.
        :type: Action
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties

    @property
    def attachments(self):
        """
        Gets the attachments of this CandidateDetailsActions.

        :return: The attachments of this CandidateDetailsActions.
        :rtype: Action
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this CandidateDetailsActions.

        :param attachments: The attachments of this CandidateDetailsActions.
        :type: Action
        """

        self._attachments = attachments

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
        if not isinstance(other, CandidateDetailsActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other