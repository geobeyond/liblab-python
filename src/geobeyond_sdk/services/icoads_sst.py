# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import (
    Collection,
    CoverageJson,
    GetLandingPageF,
    Lang,
    QueryCubeIcoadsSstBbox,
)


class IcoadsSstService(BaseService):

    @cast_models
    def describe_icoads_sst_collection(
        self, f: GetLandingPageF = None, lang: Lang = None
    ) -> Collection:
        """International Comprehensive Ocean-Atmosphere Data Set (ICOADS)

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
                f"{self.base_url}/collections/icoads-sst", self.get_default_headers()
            )
            .add_query("f", f, explode=False)
            .add_query("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return Collection._unmap(response)

    @cast_models
    def query_cube_icoads_sst(
        self,
        bbox: QueryCubeIcoadsSstBbox = None,
        datetime_: str = None,
        parameter_name: str = None,
        z: str = None,
        f: GetLandingPageF = None,
    ) -> CoverageJson:
        """International Comprehensive Ocean-Atmosphere Data Set (ICOADS)

        :param bbox: Only features that have a geometry that intersects the bounding box are selected.
        The bounding box is provided as four or six numbers, depending on whether the
        coordinate reference system includes a vertical axis (height or depth):
        * Lower left corner, coordinate axis 1
        * Lower left corner, coordinate axis 2
        * Minimum value, coordinate axis 3 (optional)
        * Upper right corner, coordinate axis 1
        * Upper right corner, coordinate axis 2
        * Maximum value, coordinate axis 3 (optional)
        The coordinate reference system of the values is WGS 84 longitude/latitude
        (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate
        reference system is specified in the parameter `bbox-crs`.
        For WGS 84 longitude/latitude the values are in most cases the sequence of
        minimum longitude, minimum latitude, maximum longitude and maximum latitude.
        However, in cases where the box spans the antimeridian the first value
        (west-most box edge) is larger than the third value (east-most box edge).
        If the vertical axis is included, the third and the sixth number are the
        bottom and the top of the 3-dimensional bounding box.
        If a feature has multiple spatial geometry properties, it is the decision of the
        server whether only a single spatial geometry property is used to determine
        the extent or all relevant geometries., defaults to None
        :type bbox: QueryCubeIcoadsSstBbox, optional
        :param datetime_: Either a date-time or an interval. Date and time expressions adhere to RFC 3339.
        Intervals may be bounded or half-bounded (double-dots at start or end).

        Examples:

        * A date-time: "2018-02-12T23:20:50Z"
        * A bounded interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"
        * Half-bounded intervals: "2018-02-12T00:00:00Z/.." or "../2018-03-18T12:31:12Z"

        Only features that have a temporal property that intersects the value of
        `datetime` are selected.

        If a feature has multiple temporal properties, it is the decision of the
        server whether only a single temporal property is used to determine
        the extent or all relevant temporal properties., defaults to None
        :type datetime_: str, optional
        :param parameter_name: comma delimited list of parameters to retrieve data for.  Valid parameters are listed in the collections metadata, defaults to None
        :type parameter_name: str, optional
        :param z: Define the vertical level to return data from
        i.e. z=level

        for instance if the 850hPa pressure level is being queried

        z=850

        or a range to return data for all levels between and including 2 defined levels
        i.e. z=minimum value/maximum value

        for instance if all values between and including 10m and 100m

        z=10/100

        finally a list of height values can be specified
        i.e. z=value1,value2,value3

        for instance if values at 2m, 10m and 80m are required

        z=2,10,80

        An Arithmetic sequence using Recurring height intervals, the difference is the number of recurrences is defined at the start
        and the amount to increment the height by is defined at the end

        i.e. z=Rn/min height/height interval

        so if the request was for 20 height levels 50m apart starting at 100m:

        z=R20/100/50

        When not specified data from all available heights SHOULD be returned, defaults to None
        :type z: str, optional
        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Response
        :rtype: CoverageJson
        """

        Validator(QueryCubeIcoadsSstBbox).is_optional().validate(bbox)
        Validator(str).is_optional().validate(datetime_)
        Validator(str).is_optional().validate(parameter_name)
        Validator(str).is_optional().validate(z)
        Validator(GetLandingPageF).is_optional().validate(f)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/icoads-sst/cube",
                self.get_default_headers(),
            )
            .add_query("bbox", bbox, explode=False)
            .add_query("datetime", datetime_, explode=False)
            .add_query("parameter-name", parameter_name, explode=False)
            .add_query("z", z, explode=False)
            .add_query("f", f, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return CoverageJson._unmap(response)

    @cast_models
    def query_position_icoads_sst(
        self,
        coords: str,
        datetime_: str = None,
        parameter_name: str = None,
        z: str = None,
        f: GetLandingPageF = None,
    ) -> CoverageJson:
        """International Comprehensive Ocean-Atmosphere Data Set (ICOADS)

        :param coords: location(s) to return data for, the coordinates are defined by a Well Known Text
        (wkt) string. to retrieve a single location :

        POINT(x y) i.e. POINT(0 51.48) for Greenwich, London

        And for a list of locations

        MULTIPOINT((x y),(x1 y1),(x2 y2),(x3 y3))

        i.e.
        MULTIPOINT((38.9 -77),(48.85 2.35),(39.92 116.38),(-35.29 149.1),(51.5 -0.1))

        see http://portal.opengeospatial.org/files/?artifact_id=25355 and
        https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry

        the coordinate values will depend on the CRS parameter, if this is not defined
        the values will be assumed to WGS84 values (i.e x=longitude and y=latitude)
        :type coords: str
        :param datetime_: Either a date-time or an interval. Date and time expressions adhere to RFC 3339.
        Intervals may be bounded or half-bounded (double-dots at start or end).

        Examples:

        * A date-time: "2018-02-12T23:20:50Z"
        * A bounded interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z"
        * Half-bounded intervals: "2018-02-12T00:00:00Z/.." or "../2018-03-18T12:31:12Z"

        Only features that have a temporal property that intersects the value of
        `datetime` are selected.

        If a feature has multiple temporal properties, it is the decision of the
        server whether only a single temporal property is used to determine
        the extent or all relevant temporal properties., defaults to None
        :type datetime_: str, optional
        :param parameter_name: comma delimited list of parameters to retrieve data for.  Valid parameters are listed in the collections metadata, defaults to None
        :type parameter_name: str, optional
        :param z: Define the vertical level to return data from
        i.e. z=level

        for instance if the 850hPa pressure level is being queried

        z=850

        or a range to return data for all levels between and including 2 defined levels
        i.e. z=minimum value/maximum value

        for instance if all values between and including 10m and 100m

        z=10/100

        finally a list of height values can be specified
        i.e. z=value1,value2,value3

        for instance if values at 2m, 10m and 80m are required

        z=2,10,80

        An Arithmetic sequence using Recurring height intervals, the difference is the number of recurrences is defined at the start
        and the amount to increment the height by is defined at the end

        i.e. z=Rn/min height/height interval

        so if the request was for 20 height levels 50m apart starting at 100m:

        z=R20/100/50

        When not specified data from all available heights SHOULD be returned, defaults to None
        :type z: str, optional
        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Response
        :rtype: CoverageJson
        """

        Validator(str).validate(coords)
        Validator(str).is_optional().validate(datetime_)
        Validator(str).is_optional().validate(parameter_name)
        Validator(str).is_optional().validate(z)
        Validator(GetLandingPageF).is_optional().validate(f)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/icoads-sst/position",
                self.get_default_headers(),
            )
            .add_query("coords", coords)
            .add_query("datetime", datetime_, explode=False)
            .add_query("parameter-name", parameter_name, explode=False)
            .add_query("z", z, explode=False)
            .add_query("f", f, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return CoverageJson._unmap(response)
