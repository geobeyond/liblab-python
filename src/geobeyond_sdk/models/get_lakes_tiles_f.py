# This file was generated by liblab | https://liblab.com/

from enum import Enum


class GetLakesTilesF(Enum):
    """An enumeration representing different categories.

    :cvar PBF: "pbf"
    :vartype PBF: str
    """

    PBF = "pbf"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GetLakesTilesF._member_map_.values()))
