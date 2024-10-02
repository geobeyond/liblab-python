# This file was generated by liblab | https://liblab.com/

from enum import Enum


class GetObsFeaturesProperties(Enum):
    """An enumeration representing different categories.

    :cvar ID: "id"
    :vartype ID: str
    :cvar STNID: "stn_id"
    :vartype STNID: str
    :cvar DATETIME: "datetime"
    :vartype DATETIME: str
    :cvar VALUE: "value"
    :vartype VALUE: str
    """

    ID = "id"
    STNID = "stn_id"
    DATETIME = "datetime"
    VALUE = "value"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, GetObsFeaturesProperties._member_map_.values())
        )