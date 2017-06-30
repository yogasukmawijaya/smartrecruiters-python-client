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


class HiringTeamMember(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, role=None):
        """
        HiringTeamMember - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'role': 'HiringTeamMemberRole'
        }

        self.attribute_map = {
            'id': 'id',
            'role': 'role'
        }

        self._id = id
        self._role = role

    @property
    def id(self):
        """
        Gets the id of this HiringTeamMember.

        :return: The id of this HiringTeamMember.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HiringTeamMember.

        :param id: The id of this HiringTeamMember.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")
        if id is not None and len(id) > 256:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `256`")
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")

        self._id = id

    @property
    def role(self):
        """
        Gets the role of this HiringTeamMember.

        :return: The role of this HiringTeamMember.
        :rtype: HiringTeamMemberRole
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this HiringTeamMember.

        :param role: The role of this HiringTeamMember.
        :type: HiringTeamMemberRole
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")

        self._role = role

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
        if not isinstance(other, HiringTeamMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other