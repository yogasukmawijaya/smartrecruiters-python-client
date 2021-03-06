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


class CandidatePrimaryAssignmentJob(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, title=None, actions=None):
        """
        CandidatePrimaryAssignmentJob - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'title': 'str',
            'actions': 'CandidatePrimaryAssignmentJobActions'
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'actions': 'actions'
        }

        self._id = id
        self._title = title
        self._actions = actions

    @property
    def id(self):
        """
        Gets the id of this CandidatePrimaryAssignmentJob.

        :return: The id of this CandidatePrimaryAssignmentJob.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CandidatePrimaryAssignmentJob.

        :param id: The id of this CandidatePrimaryAssignmentJob.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this CandidatePrimaryAssignmentJob.

        :return: The title of this CandidatePrimaryAssignmentJob.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CandidatePrimaryAssignmentJob.

        :param title: The title of this CandidatePrimaryAssignmentJob.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def actions(self):
        """
        Gets the actions of this CandidatePrimaryAssignmentJob.

        :return: The actions of this CandidatePrimaryAssignmentJob.
        :rtype: CandidatePrimaryAssignmentJobActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this CandidatePrimaryAssignmentJob.

        :param actions: The actions of this CandidatePrimaryAssignmentJob.
        :type: CandidatePrimaryAssignmentJobActions
        """

        self._actions = actions

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
        if not isinstance(other, CandidatePrimaryAssignmentJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
