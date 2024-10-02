# IcoadsSstService

A list of all methods in the `IcoadsSstService` service. Click on the method name to view detailed information about that method.

| Methods                                                           | Description                                                    |
| :---------------------------------------------------------------- | :------------------------------------------------------------- |
| [describe_icoads_sst_collection](#describe_icoads_sst_collection) | International Comprehensive Ocean-Atmosphere Data Set (ICOADS) |
| [query_cube_icoads_sst](#query_cube_icoads_sst)                   | International Comprehensive Ocean-Atmosphere Data Set (ICOADS) |
| [query_position_icoads_sst](#query_position_icoads_sst)           | International Comprehensive Ocean-Atmosphere Data Set (ICOADS) |

## describe_icoads_sst_collection

International Comprehensive Ocean-Atmosphere Data Set (ICOADS)

- HTTP Method: `GET`
- Endpoint: `/collections/icoads-sst`

**Parameters**

| Name | Type                                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :--- | :---------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f    | [GetLandingPageF](../models/GetLandingPageF.md) | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| lang | [Lang](../models/Lang.md)                       | ❌       | The optional lang parameter instructs the server return a response in a certain language, if supported. If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language. Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion. |

**Return Type**

`Collection`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment
from geobeyond_sdk.models import GetLandingPageF, Lang

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.icoads_sst.describe_icoads_sst_collection(
    f="json",
    lang="en-US"
)

print(result)
```

## query_cube_icoads_sst

International Comprehensive Ocean-Atmosphere Data Set (ICOADS)

- HTTP Method: `GET`
- Endpoint: `/collections/icoads-sst/cube`

**Parameters**

| Name           | Type                                                          | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :------------- | :------------------------------------------------------------ | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bbox           | [QueryCubeIcoadsSstBbox](../models/QueryCubeIcoadsSstBbox.md) | ❌       | Only features that have a geometry that intersects the bounding box are selected. The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth): _ Lower left corner, coordinate axis 1 _ Lower left corner, coordinate axis 2 _ Minimum value, coordinate axis 3 (optional) _ Upper right corner, coordinate axis 1 _ Upper right corner, coordinate axis 2 _ Maximum value, coordinate axis 3 (optional) The coordinate reference system of the values is WGS 84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate reference system is specified in the parameter `bbox-crs`. For WGS 84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge). If the vertical axis is included, the third and the sixth number are the bottom and the top of the 3-dimensional bounding box. If a feature has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the extent or all relevant geometries. |
| datetime\_     | str                                                           | ❌       | Either a date-time or an interval. Date and time expressions adhere to RFC 3339. Intervals may be bounded or half-bounded (double-dots at start or end). Examples: _ A date-time: "2018-02-12T23:20:50Z" _ A bounded interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z" \* Half-bounded intervals: "2018-02-12T00:00:00Z/.." or "../2018-03-18T12:31:12Z" Only features that have a temporal property that intersects the value of `datetime` are selected. If a feature has multiple temporal properties, it is the decision of the server whether only a single temporal property is used to determine the extent or all relevant temporal properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| parameter_name | str                                                           | ❌       | comma delimited list of parameters to retrieve data for. Valid parameters are listed in the collections metadata                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| z              | str                                                           | ❌       | Define the vertical level to return data from i.e. z=level for instance if the 850hPa pressure level is being queried z=850 or a range to return data for all levels between and including 2 defined levels i.e. z=minimum value/maximum value for instance if all values between and including 10m and 100m z=10/100 finally a list of height values can be specified i.e. z=value1,value2,value3 for instance if values at 2m, 10m and 80m are required z=2,10,80 An Arithmetic sequence using Recurring height intervals, the difference is the number of recurrences is defined at the start and the amount to increment the height by is defined at the end i.e. z=Rn/min height/height interval so if the request was for 20 height levels 50m apart starting at 100m: z=R20/100/50 When not specified data from all available heights SHOULD be returned                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| f              | [GetLandingPageF](../models/GetLandingPageF.md)               | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

**Return Type**

`CoverageJson`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment
from geobeyond_sdk.models import GetLandingPageF

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
bbox=[
    4.58
]

result = sdk.icoads_sst.query_cube_icoads_sst(
    bbox=bbox,
    datetime_="datetime",
    parameter_name="parameter-name",
    z="z",
    f="json"
)

print(result)
```

## query_position_icoads_sst

International Comprehensive Ocean-Atmosphere Data Set (ICOADS)

- HTTP Method: `GET`
- Endpoint: `/collections/icoads-sst/position`

**Parameters**

| Name           | Type                                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :------------- | :---------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| coords         | str                                             | ✅       | location(s) to return data for, the coordinates are defined by a Well Known Text (wkt) string. to retrieve a single location : POINT(x y) i.e. POINT(0 51.48) for Greenwich, London And for a list of locations MULTIPOINT((x y),(x1 y1),(x2 y2),(x3 y3)) i.e. MULTIPOINT((38.9 -77),(48.85 2.35),(39.92 116.38),(-35.29 149.1),(51.5 -0.1)) see http://portal.opengeospatial.org/files/?artifact_id=25355 and https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry the coordinate values will depend on the CRS parameter, if this is not defined the values will be assumed to WGS84 values (i.e x=longitude and y=latitude)                                                                                                                                                                                                              |
| datetime\_     | str                                             | ❌       | Either a date-time or an interval. Date and time expressions adhere to RFC 3339. Intervals may be bounded or half-bounded (double-dots at start or end). Examples: _ A date-time: "2018-02-12T23:20:50Z" _ A bounded interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z" \* Half-bounded intervals: "2018-02-12T00:00:00Z/.." or "../2018-03-18T12:31:12Z" Only features that have a temporal property that intersects the value of `datetime` are selected. If a feature has multiple temporal properties, it is the decision of the server whether only a single temporal property is used to determine the extent or all relevant temporal properties.                                                                                                                                                                                                     |
| parameter_name | str                                             | ❌       | comma delimited list of parameters to retrieve data for. Valid parameters are listed in the collections metadata                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| z              | str                                             | ❌       | Define the vertical level to return data from i.e. z=level for instance if the 850hPa pressure level is being queried z=850 or a range to return data for all levels between and including 2 defined levels i.e. z=minimum value/maximum value for instance if all values between and including 10m and 100m z=10/100 finally a list of height values can be specified i.e. z=value1,value2,value3 for instance if values at 2m, 10m and 80m are required z=2,10,80 An Arithmetic sequence using Recurring height intervals, the difference is the number of recurrences is defined at the start and the amount to increment the height by is defined at the end i.e. z=Rn/min height/height interval so if the request was for 20 height levels 50m apart starting at 100m: z=R20/100/50 When not specified data from all available heights SHOULD be returned |
| f              | [GetLandingPageF](../models/GetLandingPageF.md) | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

**Return Type**

`CoverageJson`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment
from geobeyond_sdk.models import GetLandingPageF

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.icoads_sst.query_position_icoads_sst(
    coords="coords",
    datetime_="datetime",
    parameter_name="parameter-name",
    z="z",
    f="json"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
