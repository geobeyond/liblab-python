# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .feature_geo_json import FeatureGeoJson
from .link import Link


class FeatureCollectionGeoJsonType(Enum):
    """An enumeration representing different categories.

    :cvar FEATURECOLLECTION: "FeatureCollection"
    :vartype FEATURECOLLECTION: str
    """

    FEATURECOLLECTION = "FeatureCollection"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, FeatureCollectionGeoJsonType._member_map_.values())
        )


@JsonMap(
    {
        "type_": "type",
        "time_stamp": "timeStamp",
        "number_matched": "numberMatched",
        "number_returned": "numberReturned",
    }
)
class FeatureCollectionGeoJson(BaseModel):
    """FeatureCollectionGeoJson

    :param type_: type_
    :type type_: FeatureCollectionGeoJsonType
    :param features: features
    :type features: List[FeatureGeoJson]
    :param links: links, defaults to None
    :type links: List[Link], optional
    :param time_stamp: This property indicates the time and date when the response was generated., defaults to None
    :type time_stamp: str, optional
    :param number_matched: The number of features of the feature type that match the selection parameters like `bbox`., defaults to None
    :type number_matched: int, optional
    :param number_returned: The number of features in the feature collection. A server may omit this information in a response, if the information about the number of features is not known or difficult to compute. If the value is provided, the value shall be identical to the number of items in the "features" array., defaults to None
    :type number_returned: int, optional
    """

    def __init__(
        self,
        type_: FeatureCollectionGeoJsonType,
        features: List[FeatureGeoJson],
        links: List[Link] = None,
        time_stamp: str = None,
        number_matched: int = None,
        number_returned: int = None,
    ):
        """FeatureCollectionGeoJson

        :param type_: type_
        :type type_: FeatureCollectionGeoJsonType
        :param features: features
        :type features: List[FeatureGeoJson]
        :param links: links, defaults to None
        :type links: List[Link], optional
        :param time_stamp: This property indicates the time and date when the response was generated., defaults to None
        :type time_stamp: str, optional
        :param number_matched: The number of features of the feature type that match the selection parameters like `bbox`., defaults to None
        :type number_matched: int, optional
        :param number_returned: The number of features in the feature collection. A server may omit this information in a response, if the information about the number of features is not known or difficult to compute. If the value is provided, the value shall be identical to the number of items in the "features" array., defaults to None
        :type number_returned: int, optional
        """
        self.type_ = self._enum_matching(
            type_, FeatureCollectionGeoJsonType.list(), "type_"
        )
        self.features = self._define_list(features, FeatureGeoJson)
        if links is not None:
            self.links = self._define_list(links, Link)
        if time_stamp is not None:
            self.time_stamp = time_stamp
        if number_matched is not None:
            self.number_matched = self._define_number(
                "number_matched", number_matched, ge=0
            )
        if number_returned is not None:
            self.number_returned = self._define_number(
                "number_returned", number_returned, ge=0
            )