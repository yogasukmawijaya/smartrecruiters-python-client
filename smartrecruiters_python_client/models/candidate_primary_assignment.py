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


class CandidatePrimaryAssignment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, job=None, status=None, sub_status=None):
        """
        CandidatePrimaryAssignment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'job': 'CandidatePrimaryAssignmentJob',
            'status': 'CandidateStatusEnum',
            'sub_status': 'str'
        }

        self.attribute_map = {
            'job': 'job',
            'status': 'status',
            'sub_status': 'subStatus'
        }

        self._job = job
        self._status = status
        self._sub_status = sub_status

    @property
    def job(self):
        """
        Gets the job of this CandidatePrimaryAssignment.

        :return: The job of this CandidatePrimaryAssignment.
        :rtype: CandidatePrimaryAssignmentJob
        """
        return self._job

    @job.setter
    def job(self, job):
        """
        Sets the job of this CandidatePrimaryAssignment.

        :param job: The job of this CandidatePrimaryAssignment.
        :type: CandidatePrimaryAssignmentJob
        """

        self._job = job

    @property
    def status(self):
        """
        Gets the status of this CandidatePrimaryAssignment.

        :return: The status of this CandidatePrimaryAssignment.
        :rtype: CandidateStatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CandidatePrimaryAssignment.

        :param status: The status of this CandidatePrimaryAssignment.
        :type: CandidateStatusEnum
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def sub_status(self):
        """
        Gets the sub_status of this CandidatePrimaryAssignment.

        :return: The sub_status of this CandidatePrimaryAssignment.
        :rtype: str
        """
        return self._sub_status

    @sub_status.setter
    def sub_status(self, sub_status):
        """
        Sets the sub_status of this CandidatePrimaryAssignment.

        :param sub_status: The sub_status of this CandidatePrimaryAssignment.
        :type: str
        """

        self._sub_status = sub_status

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
        if not isinstance(other, CandidatePrimaryAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
