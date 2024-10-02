# This file was generated by liblab | https://liblab.com/

from enum import Enum


class Ui(Enum):
    """An enumeration representing different categories.

    :cvar SWAGGER: "swagger"
    :vartype SWAGGER: str
    :cvar REDOC: "redoc"
    :vartype REDOC: str
    """

    SWAGGER = "swagger"
    REDOC = "redoc"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Ui._member_map_.values()))
