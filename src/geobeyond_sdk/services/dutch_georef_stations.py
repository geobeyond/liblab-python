# This file was generated by liblab | https://liblab.com/

from typing import Any, List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import (
    Collection,
    FeatureCollectionGeoJson,
    FeatureGeoJson,
    GetDutchGeorefStationsFeaturesProperties,
    GetLandingPageF,
    Lang,
    Queryables,
)


class DutchGeorefStationsService(BaseService):

    @cast_models
    def describe_dutch_georef_stations_collection(
        self, f: GetLandingPageF = None, lang: Lang = None
    ) -> Collection:
        """Locations of RD/GNSS-reference stations from Dutch Kadaster PDOK a.k.a RDInfo. Uses MapServer WFS v2 backend via OGRProvider.

        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        :param lang: The optional lang parameter instructs the server return a response in a certain language, if supported.  If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language.  Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion., defaults to None
        :type lang: Lang, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Information about the feature collection with id `collectionId`.

        The response contains a link to the items in the collection
        (path `/collections/{collectionId}/items`, link relation `items`)
        as well as key information about the collection. This information
        includes:

        * A local identifier for the collection that is unique for the dataset;
        * A list of coordinate reference systems (CRS) in which geometries may be returned by the server. The first CRS is the default coordinate reference system (the default is always WGS 84 with axis order longitude/latitude);
        * An optional title and description for the collection;
        * An optional extent that can be used to provide an indication of the spatial and temporal extent of the collection - typically derived from the data;
        * An optional indicator about the type of the items in the collection (the default value, if the indicator is not provided, is 'feature').
        :rtype: Collection
        """

        Validator(GetLandingPageF).is_optional().validate(f)
        Validator(Lang).is_optional().validate(lang)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/dutch_georef_stations",
                self.get_default_headers(),
            )
            .add_query("f", f, explode=False)
            .add_query("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return Collection._unmap(response)

    @cast_models
    def get_dutch_georef_stations_features(
        self,
        f: GetLandingPageF = None,
        lang: Lang = None,
        bbox: List[float] = None,
        limit: int = None,
        crs: str = None,
        bbox_crs: str = None,
        properties: List[GetDutchGeorefStationsFeaturesProperties] = None,
        vendor_specific_parameters: dict = None,
        skip_geometry: bool = None,
        sortby: List[str] = None,
        offset: int = None,
        gml_id: str = None,
        gid: int = None,
        blad: str = None,
        punt: int = None,
        station: str = None,
        jaar: int = None,
        maand: str = None,
        dag: str = None,
        omschrext: str = None,
        omschrint: str = None,
        xrd: float = None,
        yrd: float = None,
        phi: str = None,
        lambda_: str = None,
        h: float = None,
        gps: int = None,
        peilmerk: str = None,
        fuuid: str = None,
    ) -> FeatureCollectionGeoJson:
        """Locations of RD/GNSS-reference stations from Dutch Kadaster PDOK a.k.a RDInfo. Uses MapServer WFS v2 backend via OGRProvider.

        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        :param lang: The optional lang parameter instructs the server return a response in a certain language, if supported.  If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language.  Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion., defaults to None
        :type lang: Lang, optional
        :param bbox: Only features that have a geometry that intersects the bounding box are selected.The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth)., defaults to None
        :type bbox: List[float], optional
        :param limit: The optional limit parameter limits the number of items that are presented in the response document.

        Only items are counted that are on the first level of the collection in the response document.
        Nested objects contained within the explicitly requested items shall not be counted.

        Minimum = 1. Maximum = 10000. Default = 10., defaults to None
        :type limit: int, optional
        :param crs: Indicates the coordinate reference system for the results., defaults to None
        :type crs: str, optional
        :param bbox_crs: Indicates the coordinate reference system for the given bbox coordinates., defaults to None
        :type bbox_crs: str, optional
        :param properties: The properties that should be included for each feature. The parameter value is a comma-separated list of property names., defaults to None
        :type properties: List[GetDutchGeorefStationsFeaturesProperties], optional
        :param vendor_specific_parameters: Additional "free-form" parameters that are not explicitly defined, defaults to None
        :type vendor_specific_parameters: dict, optional
        :param skip_geometry: This option can be used to skip response geometries for each feature., defaults to None
        :type skip_geometry: bool, optional
        :param sortby: Specifies a comma-separated list of property names by which the response shall
        be sorted.  If the property name is preceded by a plus (+) sign it indicates
        an ascending sort for that property.  If the property name is preceded by a
        minus (-) sign it indicates a descending sort for that property.  If the
        property is not preceded by a plus or minus, then the default sort order
        implied is ascending (+)., defaults to None
        :type sortby: List[str], optional
        :param offset: The optional offset parameter indicates the index within the result set from which the server shall begin presenting results in the response document.  The first element has an index of 0 (default)., defaults to None
        :type offset: int, optional
        :param gml_id: gml_id, defaults to None
        :type gml_id: str, optional
        :param gid: gid, defaults to None
        :type gid: int, optional
        :param blad: blad, defaults to None
        :type blad: str, optional
        :param punt: punt, defaults to None
        :type punt: int, optional
        :param station: station, defaults to None
        :type station: str, optional
        :param jaar: jaar, defaults to None
        :type jaar: int, optional
        :param maand: maand, defaults to None
        :type maand: str, optional
        :param dag: dag, defaults to None
        :type dag: str, optional
        :param omschrext: omschrext, defaults to None
        :type omschrext: str, optional
        :param omschrint: omschrint, defaults to None
        :type omschrint: str, optional
        :param xrd: xrd, defaults to None
        :type xrd: float, optional
        :param yrd: yrd, defaults to None
        :type yrd: float, optional
        :param phi: phi, defaults to None
        :type phi: str, optional
        :param lambda_: lambda_, defaults to None
        :type lambda_: str, optional
        :param h: h, defaults to None
        :type h: float, optional
        :param gps: gps, defaults to None
        :type gps: int, optional
        :param peilmerk: peilmerk, defaults to None
        :type peilmerk: str, optional
        :param fuuid: fuuid, defaults to None
        :type fuuid: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The response is a document consisting of features in the collection.
        The features included in the response are determined by the server
        based on the query parameters of the request. To support access to
        larger collections without overloading the client, the API supports
        paged access with links to the next page, if more features are selected
        that the page size.

        The `bbox` and `datetime` parameter can be used to select only a
        subset of the features in the collection (the features that are in the
        bounding box or time interval). The `bbox` parameter matches all features
        in the collection that are not associated with a location, too. The
        `datetime` parameter matches all features in the collection that are
        not associated with a time stamp or interval, too.

        The `limit` parameter may be used to control the subset of the
        selected features that should be returned in the response, the page size.
        Each page may include information about the number of selected and
        returned features (`numberMatched` and `numberReturned`) as well as
        links to support paging (link relation `next`).
        :rtype: FeatureCollectionGeoJson
        """

        Validator(GetLandingPageF).is_optional().validate(f)
        Validator(Lang).is_optional().validate(lang)
        Validator(float).is_array().is_optional().validate(bbox)
        Validator(int).is_optional().min(1).max(10000).validate(limit)
        Validator(str).is_optional().validate(crs)
        Validator(str).is_optional().validate(bbox_crs)
        Validator(
            GetDutchGeorefStationsFeaturesProperties
        ).is_array().is_optional().validate(properties)
        Validator(dict).is_optional().validate(vendor_specific_parameters)
        Validator(bool).is_optional().validate(skip_geometry)
        Validator(str).is_array().is_optional().validate(sortby)
        Validator(int).is_optional().min(0).validate(offset)
        Validator(str).is_optional().validate(gml_id)
        Validator(int).is_optional().validate(gid)
        Validator(str).is_optional().validate(blad)
        Validator(int).is_optional().validate(punt)
        Validator(str).is_optional().validate(station)
        Validator(int).is_optional().validate(jaar)
        Validator(str).is_optional().validate(maand)
        Validator(str).is_optional().validate(dag)
        Validator(str).is_optional().validate(omschrext)
        Validator(str).is_optional().validate(omschrint)
        Validator(float).is_optional().validate(xrd)
        Validator(float).is_optional().validate(yrd)
        Validator(str).is_optional().validate(phi)
        Validator(str).is_optional().validate(lambda_)
        Validator(float).is_optional().validate(h)
        Validator(int).is_optional().validate(gps)
        Validator(str).is_optional().validate(peilmerk)
        Validator(str).is_optional().validate(fuuid)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/dutch_georef_stations/items",
                self.get_default_headers(),
            )
            .add_query("f", f, explode=False)
            .add_query("lang", lang)
            .add_query("bbox", bbox, explode=False)
            .add_query("limit", limit, explode=False)
            .add_query("crs", crs, explode=False)
            .add_query("bbox-crs", bbox_crs, explode=False)
            .add_query("properties", properties, explode=False)
            .add_query("vendorSpecificParameters", vendor_specific_parameters)
            .add_query("skipGeometry", skip_geometry, explode=False)
            .add_query("sortby", sortby, explode=False)
            .add_query("offset", offset, explode=False)
            .add_query("gml_id", gml_id, explode=False)
            .add_query("gid", gid, explode=False)
            .add_query("blad", blad, explode=False)
            .add_query("punt", punt, explode=False)
            .add_query("station", station, explode=False)
            .add_query("jaar", jaar, explode=False)
            .add_query("maand", maand, explode=False)
            .add_query("dag", dag, explode=False)
            .add_query("omschrext", omschrext, explode=False)
            .add_query("omschrint", omschrint, explode=False)
            .add_query("xrd", xrd, explode=False)
            .add_query("yrd", yrd, explode=False)
            .add_query("phi", phi, explode=False)
            .add_query("lambda", lambda_, explode=False)
            .add_query("h", h, explode=False)
            .add_query("gps", gps, explode=False)
            .add_query("peilmerk", peilmerk, explode=False)
            .add_query("fuuid", fuuid, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return FeatureCollectionGeoJson._unmap(response)

    @cast_models
    def options_dutch_georef_stations_features(self) -> Any:
        """Locations of RD/GNSS-reference stations from Dutch Kadaster PDOK a.k.a RDInfo. Uses MapServer WFS v2 backend via OGRProvider.

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/dutch_georef_stations/items",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("OPTIONS")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def get_dutch_georef_stations_feature(
        self,
        feature_id: str,
        crs: str = None,
        f: GetLandingPageF = None,
        lang: Lang = None,
    ) -> FeatureGeoJson:
        """Locations of RD/GNSS-reference stations from Dutch Kadaster PDOK a.k.a RDInfo. Uses MapServer WFS v2 backend via OGRProvider.

        :param feature_id: local identifier of a feature
        :type feature_id: str
        :param crs: Indicates the coordinate reference system for the results., defaults to None
        :type crs: str, optional
        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        :param lang: The optional lang parameter instructs the server return a response in a certain language, if supported.  If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language.  Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion., defaults to None
        :type lang: Lang, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: fetch the feature with id `featureId` in the feature collection
        with id `collectionId`
        :rtype: FeatureGeoJson
        """

        Validator(str).validate(feature_id)
        Validator(str).is_optional().validate(crs)
        Validator(GetLandingPageF).is_optional().validate(f)
        Validator(Lang).is_optional().validate(lang)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/dutch_georef_stations/items/{{featureId}}",
                self.get_default_headers(),
            )
            .add_path("featureId", feature_id)
            .add_query("crs", crs, explode=False)
            .add_query("f", f, explode=False)
            .add_query("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return FeatureGeoJson._unmap(response)

    @cast_models
    def options_dutch_georef_stations_feature(self, feature_id: str) -> Any:
        """Locations of RD/GNSS-reference stations from Dutch Kadaster PDOK a.k.a RDInfo. Uses MapServer WFS v2 backend via OGRProvider.

        :param feature_id: local identifier of a feature
        :type feature_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(feature_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/dutch_georef_stations/items/{{featureId}}",
                self.get_default_headers(),
            )
            .add_path("featureId", feature_id)
            .serialize()
            .set_method("OPTIONS")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def get_dutch_georef_stations_queryables(
        self, f: GetLandingPageF = None, lang: Lang = None
    ) -> Queryables:
        """Locations of RD/GNSS-reference stations from Dutch Kadaster PDOK a.k.a RDInfo. Uses MapServer WFS v2 backend via OGRProvider.

        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        :param lang: The optional lang parameter instructs the server return a response in a certain language, if supported.  If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language.  Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion., defaults to None
        :type lang: Lang, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: successful queryables operation
        :rtype: Queryables
        """

        Validator(GetLandingPageF).is_optional().validate(f)
        Validator(Lang).is_optional().validate(lang)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/dutch_georef_stations/queryables",
                self.get_default_headers(),
            )
            .add_query("f", f, explode=False)
            .add_query("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return Queryables._unmap(response)

    @cast_models
    def get_dutch_georef_stations_schema(
        self, f: GetLandingPageF = None, lang: Lang = None
    ) -> Queryables:
        """Locations of RD/GNSS-reference stations from Dutch Kadaster PDOK a.k.a RDInfo. Uses MapServer WFS v2 backend via OGRProvider.

        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        :param lang: The optional lang parameter instructs the server return a response in a certain language, if supported.  If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language.  Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion., defaults to None
        :type lang: Lang, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: successful queryables operation
        :rtype: Queryables
        """

        Validator(GetLandingPageF).is_optional().validate(f)
        Validator(Lang).is_optional().validate(lang)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/dutch_georef_stations/schema",
                self.get_default_headers(),
            )
            .add_query("f", f, explode=False)
            .add_query("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return Queryables._unmap(response)
