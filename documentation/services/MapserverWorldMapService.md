# MapserverWorldMapService

A list of all methods in the `MapserverWorldMapService` service. Click on the method name to view detailed information about that method.

| Methods                                                                             | Description                      |
| :---------------------------------------------------------------------------------- | :------------------------------- |
| [describe_mapserver_world_map_collection](#describe_mapserver_world_map_collection) | MapServer demo WMS world map     |
| [get_map](#get_map)                                                                 | MapServer demo WMS world map map |

## describe_mapserver_world_map_collection

MapServer demo WMS world map

- HTTP Method: `GET`
- Endpoint: `/collections/mapserver_world_map`

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

result = sdk.mapserver_world_map.describe_mapserver_world_map_collection(
    f="json",
    lang="en-US"
)

print(result)
```

## get_map

MapServer demo WMS world map map

- HTTP Method: `GET`
- Endpoint: `/collections/mapserver_world_map/map`

**Parameters**

| Name        | Type                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :---------- | :------------------------------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bbox        | List[float]                     | ❌       | Only features that have a geometry that intersects the bounding box are selected.The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth).                                                                                                                                                                                                                                                                                                                                                                                                                      |
| datetime\_  | str                             | ❌       | Either a date-time or an interval. Date and time expressions adhere to RFC 3339. Intervals may be bounded or half-bounded (double-dots at start or end). Examples: _ A date-time: "2018-02-12T23:20:50Z" _ A bounded interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z" \* Half-bounded intervals: "2018-02-12T00:00:00Z/.." or "../2018-03-18T12:31:12Z" Only features that have a temporal property that intersects the value of `datetime` are selected. If a feature has multiple temporal properties, it is the decision of the server whether only a single temporal property is used to determine the extent or all relevant temporal properties. |
| width       | int                             | ❌       | Response image width                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| height      | int                             | ❌       | Response image height                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| transparent | bool                            | ❌       | Background transparency of map (default=true).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| bbox_crs    | int                             | ❌       | Indicates the EPSG for the given bbox coordinates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| f           | [GetMapF](../models/GetMapF.md) | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

**Return Type**

`any`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment
from geobeyond_sdk.models import GetMapF

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
bbox=[
    8.78
]

result = sdk.mapserver_world_map.get_map(
    bbox=bbox,
    datetime_="datetime",
    width=0,
    height=10,
    transparent=True,
    bbox_crs=4326,
    f="png"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
