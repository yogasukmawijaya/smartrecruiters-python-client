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


class JobPositionInput(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, position_id=None, incumbent_name=None, type=None, position_open_date=None, target_start_date=None):
        """
        JobPositionInput - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'position_id': 'str',
            'incumbent_name': 'str',
            'type': 'str',
            'position_open_date': 'datetime',
            'target_start_date': 'datetime'
        }

        self.attribute_map = {
            'position_id': 'positionId',
            'incumbent_name': 'incumbentName',
            'type': 'type',
            'position_open_date': 'positionOpenDate',
            'target_start_date': 'targetStartDate'
        }

        self._position_id = position_id
        self._incumbent_name = incumbent_name
        self._type = type
        self._position_open_date = position_open_date
        self._target_start_date = target_start_date

    @property
    def position_id(self):
        """
        Gets the position_id of this JobPositionInput.

        :return: The position_id of this JobPositionInput.
        :rtype: str
        """
        return self._position_id

    @position_id.setter
    def position_id(self, position_id):
        """
        Sets the position_id of this JobPositionInput.

        :param position_id: The position_id of this JobPositionInput.
        :type: str
        """

        self._position_id = position_id

    @property
    def incumbent_name(self):
        """
        Gets the incumbent_name of this JobPositionInput.

        :return: The incumbent_name of this JobPositionInput.
        :rtype: str
        """
        return self._incumbent_name

    @incumbent_name.setter
    def incumbent_name(self, incumbent_name):
        """
        Sets the incumbent_name of this JobPositionInput.

        :param incumbent_name: The incumbent_name of this JobPositionInput.
        :type: str
        """

        self._incumbent_name = incumbent_name

    @property
    def type(self):
        """
        Gets the type of this JobPositionInput.

        :return: The type of this JobPositionInput.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this JobPositionInput.

        :param type: The type of this JobPositionInput.
        :type: str
        """
        allowed_values = ["NEW", "REPLACEMENT"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def position_open_date(self):
        """
        Gets the position_open_date of this JobPositionInput.

        :return: The position_open_date of this JobPositionInput.
        :rtype: datetime
        """
        return self._position_open_date

    @position_open_date.setter
    def position_open_date(self, position_open_date):
        """
        Sets the position_open_date of this JobPositionInput.

        :param position_open_date: The position_open_date of this JobPositionInput.
        :type: datetime
        """
        if position_open_date is None:
            raise ValueError("Invalid value for `position_open_date`, must not be `None`")

        self._position_open_date = position_open_date

    @property
    def target_start_date(self):
        """
        Gets the target_start_date of this JobPositionInput.

        :return: The target_start_date of this JobPositionInput.
        :rtype: datetime
        """
        return self._target_start_date

    @target_start_date.setter
    def target_start_date(self, target_start_date):
        """
        Sets the target_start_date of this JobPositionInput.

        :param target_start_date: The target_start_date of this JobPositionInput.
        :type: datetime
        """
        if target_start_date is None:
            raise ValueError("Invalid value for `target_start_date`, must not be `None`")

        self._target_start_date = target_start_date

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
        if not isinstance(other, JobPositionInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
