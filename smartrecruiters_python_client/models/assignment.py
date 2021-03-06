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


class Assignment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, job=None, status=None, sub_status=None, starts_on=None, source=None, reason_of_rejection=None, actions=None):
        """
        Assignment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'job': 'AssignmentJob',
            'status': 'CandidateStatusEnum',
            'sub_status': 'str',
            'starts_on': 'datetime',
            'source': 'str',
            'reason_of_rejection': 'ModelProperty',
            'actions': 'AssignmentActions'
        }

        self.attribute_map = {
            'job': 'job',
            'status': 'status',
            'sub_status': 'subStatus',
            'starts_on': 'startsOn',
            'source': 'source',
            'reason_of_rejection': 'reasonOfRejection',
            'actions': 'actions'
        }

        self._job = job
        self._status = status
        self._sub_status = sub_status
        self._starts_on = starts_on
        self._source = source
        self._reason_of_rejection = reason_of_rejection
        self._actions = actions

    @property
    def job(self):
        """
        Gets the job of this Assignment.

        :return: The job of this Assignment.
        :rtype: AssignmentJob
        """
        return self._job

    @job.setter
    def job(self, job):
        """
        Sets the job of this Assignment.

        :param job: The job of this Assignment.
        :type: AssignmentJob
        """

        self._job = job

    @property
    def status(self):
        """
        Gets the status of this Assignment.

        :return: The status of this Assignment.
        :rtype: CandidateStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Assignment.

        :param status: The status of this Assignment.
        :type: CandidateStatusEnum
        """

        self._status = status

    @property
    def sub_status(self):
        """
        Gets the sub_status of this Assignment.

        :return: The sub_status of this Assignment.
        :rtype: str
        """
        return self._sub_status

    @sub_status.setter
    def sub_status(self, sub_status):
        """
        Sets the sub_status of this Assignment.

        :param sub_status: The sub_status of this Assignment.
        :type: str
        """

        self._sub_status = sub_status

    @property
    def starts_on(self):
        """
        Gets the starts_on of this Assignment.

        :return: The starts_on of this Assignment.
        :rtype: datetime
        """
        return self._starts_on

    @starts_on.setter
    def starts_on(self, starts_on):
        """
        Sets the starts_on of this Assignment.

        :param starts_on: The starts_on of this Assignment.
        :type: datetime
        """

        self._starts_on = starts_on

    @property
    def source(self):
        """
        Gets the source of this Assignment.

        :return: The source of this Assignment.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this Assignment.

        :param source: The source of this Assignment.
        :type: str
        """

        self._source = source

    @property
    def reason_of_rejection(self):
        """
        Gets the reason_of_rejection of this Assignment.

        :return: The reason_of_rejection of this Assignment.
        :rtype: ModelProperty
        """
        return self._reason_of_rejection

    @reason_of_rejection.setter
    def reason_of_rejection(self, reason_of_rejection):
        """
        Sets the reason_of_rejection of this Assignment.

        :param reason_of_rejection: The reason_of_rejection of this Assignment.
        :type: ModelProperty
        """

        self._reason_of_rejection = reason_of_rejection

    @property
    def actions(self):
        """
        Gets the actions of this Assignment.

        :return: The actions of this Assignment.
        :rtype: AssignmentActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this Assignment.

        :param actions: The actions of this Assignment.
        :type: AssignmentActions
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
        if not isinstance(other, Assignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
