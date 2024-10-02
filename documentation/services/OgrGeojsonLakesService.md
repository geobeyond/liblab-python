# OgrGeojsonLakesService

A list of all methods in the `OgrGeojsonLakesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                       |
| :------------------------------------------------------------------------------ | :-------------------------------- |
| [describe_ogr_geojson_lakes_collection](#describe_ogr_geojson_lakes_collection) | lakes of the world, public domain |
| [get_ogr_geojson_lakes_features](#get_ogr_geojson_lakes_features)               | lakes of the world, public domain |
| [options_ogr_geojson_lakes_features](#options_ogr_geojson_lakes_features)       | lakes of the world, public domain |
| [get_ogr_geojson_lakes_feature](#get_ogr_geojson_lakes_feature)                 | lakes of the world, public domain |
| [options_ogr_geojson_lakes_feature](#options_ogr_geojson_lakes_feature)         | lakes of the world, public domain |
| [get_ogr_geojson_lakes_queryables](#get_ogr_geojson_lakes_queryables)           | lakes of the world, public domain |
| [get_ogr_geojson_lakes_schema](#get_ogr_geojson_lakes_schema)                   | lakes of the world, public domain |

## describe_ogr_geojson_lakes_collection

lakes of the world, public domain

- HTTP Method: `GET`
- Endpoint: `/collections/ogr_geojson_lakes`

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

result = sdk.ogr_geojson_lakes.describe_ogr_geojson_lakes_collection(
    f="json",
    lang="en-US"
)

print(result)
```

## get_ogr_geojson_lakes_features

lakes of the world, public domain

- HTTP Method: `GET`
- Endpoint: `/collections/ogr_geojson_lakes/items`

**Parameters**

| Name                       | Type                                                                                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :------------------------- | :---------------------------------------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f                          | [GetLandingPageF](../models/GetLandingPageF.md)                                                 | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| lang                       | [Lang](../models/Lang.md)                                                                       | ❌       | The optional lang parameter instructs the server return a response in a certain language, if supported. If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language. Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion. |
| bbox                       | List[float]                                                                                     | ❌       | Only features that have a geometry that intersects the bounding box are selected.The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth).                                                                                                                                                                                                                                                                                                                                                               |
| limit                      | int                                                                                             | ❌       | The optional limit parameter limits the number of items that are presented in the response document. Only items are counted that are on the first level of the collection in the response document. Nested objects contained within the explicitly requested items shall not be counted. Minimum = 1. Maximum = 10000. Default = 10.                                                                                                                                                                                                                                                                 |
| crs                        | str                                                                                             | ❌       | Indicates the coordinate reference system for the results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| bbox_crs                   | str                                                                                             | ❌       | Indicates the coordinate reference system for the given bbox coordinates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| properties                 | [List[GetOgrGeojsonLakesFeaturesProperties]](../models/GetOgrGeojsonLakesFeaturesProperties.md) | ❌       | The properties that should be included for each feature. The parameter value is a comma-separated list of property names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| vendor_specific_parameters | dict                                                                                            | ❌       | Additional "free-form" parameters that are not explicitly defined                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| skip_geometry              | bool                                                                                            | ❌       | This option can be used to skip response geometries for each feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sortby                     | List[str]                                                                                       | ❌       | Specifies a comma-separated list of property names by which the response shall be sorted. If the property name is preceded by a plus (+) sign it indicates an ascending sort for that property. If the property name is preceded by a minus (-) sign it indicates a descending sort for that property. If the property is not preceded by a plus or minus, then the default sort order implied is ascending (+).                                                                                                                                                                                     |
| offset                     | int                                                                                             | ❌       | The optional offset parameter indicates the index within the result set from which the server shall begin presenting results in the response document. The first element has an index of 0 (default).                                                                                                                                                                                                                                                                                                                                                                                                |
| id\_                       | int                                                                                             | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| scalerank                  | int                                                                                             | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| name                       | str                                                                                             | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| name_alt                   | str                                                                                             | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| admin                      | str                                                                                             | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| featureclass               | str                                                                                             | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

**Return Type**

`FeatureCollectionGeoJson`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment
from geobeyond_sdk.models import GetLandingPageF, Lang, dict

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
bbox=[
    0.11
]
properties=[
    "id"
]
vendor_specific_parameters=dict(
    {}
)
sortby=[
    "|T"
]

result = sdk.ogr_geojson_lakes.get_ogr_geojson_lakes_features(
    f="json",
    lang="en-US",
    bbox=bbox,
    limit=10,
    crs="crs",
    bbox_crs="bbox-crs",
    properties=properties,
    vendor_specific_parameters=vendor_specific_parameters,
    skip_geometry=True,
    sortby=sortby,
    offset=4,
    id_=5,
    scalerank=2,
    name="name",
    name_alt="name_alt",
    admin="admin",
    featureclass="featureclass"
)

print(result)
```

## options_ogr_geojson_lakes_features

lakes of the world, public domain

- HTTP Method: `OPTIONS`
- Endpoint: `/collections/ogr_geojson_lakes/items`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.ogr_geojson_lakes.options_ogr_geojson_lakes_features()

print(result)
```

## get_ogr_geojson_lakes_feature

lakes of the world, public domain

- HTTP Method: `GET`
- Endpoint: `/collections/ogr_geojson_lakes/items/{featureId}`

**Parameters**

| Name       | Type                                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :--------- | :---------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| feature_id | str                                             | ✅       | local identifier of a feature                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| crs        | str                                             | ❌       | Indicates the coordinate reference system for the results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| f          | [GetLandingPageF](../models/GetLandingPageF.md) | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| lang       | [Lang](../models/Lang.md)                       | ❌       | The optional lang parameter instructs the server return a response in a certain language, if supported. If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language. Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion. |

**Return Type**

`FeatureGeoJson`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment
from geobeyond_sdk.models import GetLandingPageF, Lang

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.ogr_geojson_lakes.get_ogr_geojson_lakes_feature(
    feature_id="featureId",
    crs="crs",
    f="json",
    lang="en-US"
)

print(result)
```

## options_ogr_geojson_lakes_feature

lakes of the world, public domain

- HTTP Method: `OPTIONS`
- Endpoint: `/collections/ogr_geojson_lakes/items/{featureId}`

**Parameters**

| Name       | Type | Required | Description                   |
| :--------- | :--- | :------- | :---------------------------- |
| feature_id | str  | ✅       | local identifier of a feature |

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.ogr_geojson_lakes.options_ogr_geojson_lakes_feature(feature_id="featureId")

print(result)
```

## get_ogr_geojson_lakes_queryables

lakes of the world, public domain

- HTTP Method: `GET`
- Endpoint: `/collections/ogr_geojson_lakes/queryables`

**Parameters**

| Name | Type                                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :--- | :---------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f    | [GetLandingPageF](../models/GetLandingPageF.md) | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| lang | [Lang](../models/Lang.md)                       | ❌       | The optional lang parameter instructs the server return a response in a certain language, if supported. If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language. Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion. |

**Return Type**

`Queryables`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment
from geobeyond_sdk.models import GetLandingPageF, Lang

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.ogr_geojson_lakes.get_ogr_geojson_lakes_queryables(
    f="json",
    lang="en-US"
)

print(result)
```

## get_ogr_geojson_lakes_schema

lakes of the world, public domain

- HTTP Method: `GET`
- Endpoint: `/collections/ogr_geojson_lakes/schema`

**Parameters**

| Name | Type                                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :--- | :---------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f    | [GetLandingPageF](../models/GetLandingPageF.md) | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| lang | [Lang](../models/Lang.md)                       | ❌       | The optional lang parameter instructs the server return a response in a certain language, if supported. If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language. Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion. |

**Return Type**

`Queryables`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment
from geobeyond_sdk.models import GetLandingPageF, Lang

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.ogr_geojson_lakes.get_ogr_geojson_lakes_schema(
    f="json",
    lang="en-US"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
