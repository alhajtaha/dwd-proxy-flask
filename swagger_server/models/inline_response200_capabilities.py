# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200Capabilities(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, resolution: str=None, observation_types: List[str]=None):  # noqa: E501
        """InlineResponse200Capabilities - a model defined in Swagger

        :param resolution: The resolution of this InlineResponse200Capabilities.  # noqa: E501
        :type resolution: str
        :param observation_types: The observation_types of this InlineResponse200Capabilities.  # noqa: E501
        :type observation_types: List[str]
        """
        self.swagger_types = {
            'resolution': str,
            'observation_types': List[str]
        }

        self.attribute_map = {
            'resolution': 'resolution',
            'observation_types': 'observationTypes'
        }

        self._resolution = resolution
        self._observation_types = observation_types

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200Capabilities':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_capabilities of this InlineResponse200Capabilities.  # noqa: E501
        :rtype: InlineResponse200Capabilities
        """
        return util.deserialize_model(dikt, cls)

    @property
    def resolution(self) -> str:
        """Gets the resolution of this InlineResponse200Capabilities.


        :return: The resolution of this InlineResponse200Capabilities.
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution: str):
        """Sets the resolution of this InlineResponse200Capabilities.


        :param resolution: The resolution of this InlineResponse200Capabilities.
        :type resolution: str
        """
        allowed_values = ["10_minutes", "1_minute", "daily", "hourly", "monthly"]  # noqa: E501
        if resolution not in allowed_values:
            raise ValueError(
                "Invalid value for `resolution` ({0}), must be one of {1}"
                .format(resolution, allowed_values)
            )

        self._resolution = resolution

    @property
    def observation_types(self) -> List[str]:
        """Gets the observation_types of this InlineResponse200Capabilities.


        :return: The observation_types of this InlineResponse200Capabilities.
        :rtype: List[str]
        """
        return self._observation_types

    @observation_types.setter
    def observation_types(self, observation_types: List[str]):
        """Sets the observation_types of this InlineResponse200Capabilities.


        :param observation_types: The observation_types of this InlineResponse200Capabilities.
        :type observation_types: List[str]
        """
        allowed_values = ["air_temperature", "cloudiness", "cloud_type", "extreme_temperature", "extreme_wind", "kl", "more_precip", "precipitation", "pressure", "soil_temperature", "solar", "sun", "visibility", "water_equiv", "wind"]  # noqa: E501
        if not set(observation_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `observation_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(observation_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._observation_types = observation_types
