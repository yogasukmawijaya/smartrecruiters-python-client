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


class JobAdContent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, title=None, language=None, job_ad=None):
        """
        JobAdContent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'title': 'str',
            'language': 'JobAdLanguage',
            'job_ad': 'JobAdSections'
        }

        self.attribute_map = {
            'title': 'title',
            'language': 'language',
            'job_ad': 'jobAd'
        }

        self._title = title
        self._language = language
        self._job_ad = job_ad

    @property
    def title(self):
        """
        Gets the title of this JobAdContent.

        :return: The title of this JobAdContent.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this JobAdContent.

        :param title: The title of this JobAdContent.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")
        if title is not None and len(title) < 1:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")

        self._title = title

    @property
    def language(self):
        """
        Gets the language of this JobAdContent.

        :return: The language of this JobAdContent.
        :rtype: JobAdLanguage
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this JobAdContent.

        :param language: The language of this JobAdContent.
        :type: JobAdLanguage
        """

        self._language = language

    @property
    def job_ad(self):
        """
        Gets the job_ad of this JobAdContent.

        :return: The job_ad of this JobAdContent.
        :rtype: JobAdSections
        """
        return self._job_ad

    @job_ad.setter
    def job_ad(self, job_ad):
        """
        Sets the job_ad of this JobAdContent.

        :param job_ad: The job_ad of this JobAdContent.
        :type: JobAdSections
        """

        self._job_ad = job_ad

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
        if not isinstance(other, JobAdContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other