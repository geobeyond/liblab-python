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
    GetLakesFeaturesProperties,
    GetLakesTilesF,
    GetLandingPageF,
    Lang,
    Queryables,
    TileMatrixSets,
    Tiles,
)


class LakesService(BaseService):

    @cast_models
    def describe_lakes_collection(
        self, f: GetLandingPageF = None, lang: Lang = None
    ) -> Collection:
        """lakes of the world, public domain

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
            Serializer(f"{self.base_url}/collections/lakes", self.get_default_headers())
            .add_query("f", f, explode=False)
            .add_query("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return Collection._unmap(response)

    @cast_models
    def get_lakes_features(
        self,
        f: GetLandingPageF = None,
        lang: Lang = None,
        bbox: List[float] = None,
        limit: int = None,
        crs: str = None,
        bbox_crs: str = None,
        properties: List[GetLakesFeaturesProperties] = None,
        vendor_specific_parameters: dict = None,
        skip_geometry: bool = None,
        sortby: List[str] = None,
        offset: int = None,
        id_: int = None,
        scalerank: int = None,
        name: str = None,
        name_alt: str = None,
        admin: str = None,
        featureclass: str = None,
    ) -> FeatureCollectionGeoJson:
        """lakes of the world, public domain

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
        :type properties: List[GetLakesFeaturesProperties], optional
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
        :param id_: id_, defaults to None
        :type id_: int, optional
        :param scalerank: scalerank, defaults to None
        :type scalerank: int, optional
        :param name: name, defaults to None
        :type name: str, optional
        :param name_alt: name_alt, defaults to None
        :type name_alt: str, optional
        :param admin: admin, defaults to None
        :type admin: str, optional
        :param featureclass: featureclass, defaults to None
        :type featureclass: str, optional
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
        Validator(GetLakesFeaturesProperties).is_array().is_optional().validate(
            properties
        )
        Validator(dict).is_optional().validate(vendor_specific_parameters)
        Validator(bool).is_optional().validate(skip_geometry)
        Validator(str).is_array().is_optional().validate(sortby)
        Validator(int).is_optional().min(0).validate(offset)
        Validator(int).is_optional().validate(id_)
        Validator(int).is_optional().validate(scalerank)
        Validator(str).is_optional().validate(name)
        Validator(str).is_optional().validate(name_alt)
        Validator(str).is_optional().validate(admin)
        Validator(str).is_optional().validate(featureclass)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/lakes/items", self.get_default_headers()
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
            .add_query("id", id_, explode=False)
            .add_query("scalerank", scalerank, explode=False)
            .add_query("name", name, explode=False)
            .add_query("name_alt", name_alt, explode=False)
            .add_query("admin", admin, explode=False)
            .add_query("featureclass", featureclass, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return FeatureCollectionGeoJson._unmap(response)

    @cast_models
    def options_lakes_features(self) -> Any:
        """lakes of the world, public domain

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/lakes/items", self.get_default_headers()
            )
            .serialize()
            .set_method("OPTIONS")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def get_lakes_feature(
        self,
        feature_id: str,
        crs: str = None,
        f: GetLandingPageF = None,
        lang: Lang = None,
    ) -> FeatureGeoJson:
        """lakes of the world, public domain

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
                f"{self.base_url}/collections/lakes/items/{{featureId}}",
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
    def options_lakes_feature(self, feature_id: str) -> Any:
        """lakes of the world, public domain

        :param feature_id: local identifier of a feature
        :type feature_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(feature_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/lakes/items/{{featureId}}",
                self.get_default_headers(),
            )
            .add_path("featureId", feature_id)
            .serialize()
            .set_method("OPTIONS")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def get_lakes_queryables(
        self, f: GetLandingPageF = None, lang: Lang = None
    ) -> Queryables:
        """lakes of the world, public domain

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
                f"{self.base_url}/collections/lakes/queryables",
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
    def get_lakes_schema(
        self, f: GetLandingPageF = None, lang: Lang = None
    ) -> Queryables:
        """lakes of the world, public domain

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
                f"{self.base_url}/collections/lakes/schema", self.get_default_headers()
            )
            .add_query("f", f, explode=False)
            .add_query("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return Queryables._unmap(response)

    @cast_models
    def describe_lakes_tiles(
        self, f: GetLandingPageF = None, lang: Lang = None
    ) -> Tiles:
        """lakes of the world, public domain

        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        :param lang: The optional lang parameter instructs the server return a response in a certain language, if supported.  If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language.  Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion., defaults to None
        :type lang: Lang, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Retrieves the tiles description for this collection
        :rtype: Tiles
        """

        Validator(GetLandingPageF).is_optional().validate(f)
        Validator(Lang).is_optional().validate(lang)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/lakes/tiles", self.get_default_headers()
            )
            .add_query("f", f, explode=False)
            .add_query("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return Tiles._unmap(response)

    @cast_models
    def get_lakes_tiles(
        self,
        tile_matrix_set_id: TileMatrixSets,
        tile_matrix: str,
        tile_row: int,
        tile_col: int,
        f: GetLakesTilesF = None,
    ) -> any:
        """lakes of the world, public domain

        :param tile_matrix_set_id: Identifier for a supported TileMatrixSet
        :type tile_matrix_set_id: TileMatrixSets
        :param tile_matrix: Identifier selecting one of the scales defined in the TileMatrixSet and representing the scaleDenominator the tile. For example,
        Ireland is fully within the Tile at WebMercatorQuad tileMatrix=5, tileRow=10 and tileCol=15.
        :type tile_matrix: str
        :param tile_row: Row index of the tile on the selected TileMatrix. It cannot exceed the MatrixWidth-1 for the selected TileMatrix. For example, Ireland is fully within the Tile at WebMercatorQuad tileMatrix=5, tileRow=10 and tileCol=15.
        :type tile_row: int
        :param tile_col: Column index of the tile on the selected TileMatrix. It cannot exceed the MatrixHeight-1 for the selected TileMatrix. For example, Ireland is fully within the Tile at WebMercatorQuad tileMatrix=5, tileRow=10 and tileCol=15.
        :type tile_col: int
        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document., defaults to None
        :type f: GetLakesTilesF, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: successful operation
        :rtype: any
        """

        Validator(TileMatrixSets).validate(tile_matrix_set_id)
        Validator(str).validate(tile_matrix)
        Validator(int).min(0).validate(tile_row)
        Validator(int).min(0).validate(tile_col)
        Validator(GetLakesTilesF).is_optional().validate(f)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/lakes/tiles/{{tileMatrixSetId}}/{{tileMatrix}}/{{tileRow}}/{{tileCol}}",
                self.get_default_headers(),
            )
            .add_path("tileMatrixSetId", tile_matrix_set_id)
            .add_path("tileMatrix", tile_matrix)
            .add_path("tileRow", tile_row)
            .add_path("tileCol", tile_col)
            .add_query("f", f, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return response
