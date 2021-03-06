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


class CompanyConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, identifier=None, name=None, location=None, website=None, industry=None, logo=None):
        """
        CompanyConfiguration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'identifier': 'str',
            'name': 'str',
            'location': 'Location',
            'website': 'str',
            'industry': 'Industry',
            'logo': 'str'
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'name': 'name',
            'location': 'location',
            'website': 'website',
            'industry': 'industry',
            'logo': 'logo'
        }

        self._identifier = identifier
        self._name = name
        self._location = location
        self._website = website
        self._industry = industry
        self._logo = logo

    @property
    def identifier(self):
        """
        Gets the identifier of this CompanyConfiguration.
        Identifier of a company.

        :return: The identifier of this CompanyConfiguration.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CompanyConfiguration.
        Identifier of a company.

        :param identifier: The identifier of this CompanyConfiguration.
        :type: str
        """

        self._identifier = identifier

    @property
    def name(self):
        """
        Gets the name of this CompanyConfiguration.
        Company name.

        :return: The name of this CompanyConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CompanyConfiguration.
        Company name.

        :param name: The name of this CompanyConfiguration.
        :type: str
        """

        self._name = name

    @property
    def location(self):
        """
        Gets the location of this CompanyConfiguration.
        Company location including geolocation.

        :return: The location of this CompanyConfiguration.
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this CompanyConfiguration.
        Company location including geolocation.

        :param location: The location of this CompanyConfiguration.
        :type: Location
        """

        self._location = location

    @property
    def website(self):
        """
        Gets the website of this CompanyConfiguration.
        URL to company website.

        :return: The website of this CompanyConfiguration.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this CompanyConfiguration.
        URL to company website.

        :param website: The website of this CompanyConfiguration.
        :type: str
        """

        self._website = website

    @property
    def industry(self):
        """
        Gets the industry of this CompanyConfiguration.
        Company industry information.

        :return: The industry of this CompanyConfiguration.
        :rtype: Industry
        """
        return self._industry

    @industry.setter
    def industry(self, industry):
        """
        Sets the industry of this CompanyConfiguration.
        Company industry information.

        :param industry: The industry of this CompanyConfiguration.
        :type: Industry
        """

        self._industry = industry

    @property
    def logo(self):
        """
        Gets the logo of this CompanyConfiguration.
        URL to company logo.

        :return: The logo of this CompanyConfiguration.
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """
        Sets the logo of this CompanyConfiguration.
        URL to company logo.

        :param logo: The logo of this CompanyConfiguration.
        :type: str
        """

        self._logo = logo

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
        if not isinstance(other, CompanyConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
