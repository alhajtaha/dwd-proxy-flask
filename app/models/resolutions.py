# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.model_ import Model
from app import util


class Resolutions(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _10_MINUTES = "10_minutes"
    _1_MINUTE = "1_minute"
    DAILY = "daily"
    HOURLY = "hourly"
    MONTHLY = "monthly"
    ANNUAL = "annual"
    MULTI_ANNUAL = "multi_annual"
    SUBDAILY = "subdaily"

    def __init__(self):  # noqa: E501
        """Resolutions - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'Resolutions':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Resolutions of this Resolutions.  # noqa: E501
        :rtype: Resolutions
        """
        return util.deserialize_model(dikt, cls)
