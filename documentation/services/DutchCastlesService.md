# DutchCastlesService

A list of all methods in the `DutchCastlesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                                                                                                                               |
| :---------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [describe_dutch_castles_collection](#describe_dutch_castles_collection) | Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider. |
| [get_dutch_castles_features](#get_dutch_castles_features)               | Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider. |
| [options_dutch_castles_features](#options_dutch_castles_features)       | Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider. |
| [get_dutch_castles_feature](#get_dutch_castles_feature)                 | Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider. |
| [options_dutch_castles_feature](#options_dutch_castles_feature)         | Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider. |
| [get_dutch_castles_queryables](#get_dutch_castles_queryables)           | Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider. |
| [get_dutch_castles_schema](#get_dutch_castles_schema)                   | Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider. |

## describe_dutch_castles_collection

Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider.

- HTTP Method: `GET`
- Endpoint: `/collections/dutch_castles`

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

result = sdk.dutch_castles.describe_dutch_castles_collection(
    f="json",
    lang="en-US"
)

print(result)
```

## get_dutch_castles_features

Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider.

- HTTP Method: `GET`
- Endpoint: `/collections/dutch_castles/items`

**Parameters**

| Name                       | Type                                                                                      | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :------------------------- | :---------------------------------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f                          | [GetLandingPageF](../models/GetLandingPageF.md)                                           | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| lang                       | [Lang](../models/Lang.md)                                                                 | ❌       | The optional lang parameter instructs the server return a response in a certain language, if supported. If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language. Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion. |
| bbox                       | List[float]                                                                               | ❌       | Only features that have a geometry that intersects the bounding box are selected.The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth).                                                                                                                                                                                                                                                                                                                                                               |
| limit                      | int                                                                                       | ❌       | The optional limit parameter limits the number of items that are presented in the response document. Only items are counted that are on the first level of the collection in the response document. Nested objects contained within the explicitly requested items shall not be counted. Minimum = 1. Maximum = 10000. Default = 10.                                                                                                                                                                                                                                                                 |
| crs                        | str                                                                                       | ❌       | Indicates the coordinate reference system for the results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| bbox_crs                   | str                                                                                       | ❌       | Indicates the coordinate reference system for the given bbox coordinates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| properties                 | [List[GetDutchCastlesFeaturesProperties]](../models/GetDutchCastlesFeaturesProperties.md) | ❌       | The properties that should be included for each feature. The parameter value is a comma-separated list of property names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| vendor_specific_parameters | dict                                                                                      | ❌       | Additional "free-form" parameters that are not explicitly defined                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| skip_geometry              | bool                                                                                      | ❌       | This option can be used to skip response geometries for each feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sortby                     | List[str]                                                                                 | ❌       | Specifies a comma-separated list of property names by which the response shall be sorted. If the property name is preceded by a plus (+) sign it indicates an ascending sort for that property. If the property name is preceded by a minus (-) sign it indicates a descending sort for that property. If the property is not preceded by a plus or minus, then the default sort order implied is ascending (+).                                                                                                                                                                                     |
| offset                     | int                                                                                       | ❌       | The optional offset parameter indicates the index within the result set from which the server shall begin presenting results in the response document. The first element has an index of 0 (default).                                                                                                                                                                                                                                                                                                                                                                                                |
| gml_id                     | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| gid                        | int                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| cchin                      | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| naam                       | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| plaats                     | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| info_link                  | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| datering                   | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| rijksmonnr                 | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| provincie                  | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| foto_thumb                 | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| foto_groot                 | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| bijschrift                 | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| zichtbaar                  | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| legenda                    | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| typering                   | str                                                                                       | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

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
    9.33
]
properties=[
    "gml_id"
]
vendor_specific_parameters=dict(
    {}
)
sortby=[
    "bRsp*b&"
]

result = sdk.dutch_castles.get_dutch_castles_features(
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
    offset=3,
    gml_id="gml_id",
    gid=4,
    cchin="cchin",
    naam="naam",
    plaats="plaats",
    info_link="info_link",
    datering="datering",
    rijksmonnr="rijksmonnr",
    provincie="provincie",
    foto_thumb="foto_thumb",
    foto_groot="foto_groot",
    bijschrift="bijschrift",
    zichtbaar="zichtbaar",
    legenda="legenda",
    typering="typering"
)

print(result)
```

## options_dutch_castles_features

Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider.

- HTTP Method: `OPTIONS`
- Endpoint: `/collections/dutch_castles/items`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.dutch_castles.options_dutch_castles_features()

print(result)
```

## get_dutch_castles_feature

Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider.

- HTTP Method: `GET`
- Endpoint: `/collections/dutch_castles/items/{featureId}`

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

result = sdk.dutch_castles.get_dutch_castles_feature(
    feature_id="featureId",
    crs="crs",
    f="json",
    lang="en-US"
)

print(result)
```

## options_dutch_castles_feature

Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider.

- HTTP Method: `OPTIONS`
- Endpoint: `/collections/dutch_castles/items/{featureId}`

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

result = sdk.dutch_castles.options_dutch_castles_feature(feature_id="featureId")

print(result)
```

## get_dutch_castles_queryables

Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider.

- HTTP Method: `GET`
- Endpoint: `/collections/dutch_castles/queryables`

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

result = sdk.dutch_castles.get_dutch_castles_queryables(
    f="json",
    lang="en-US"
)

print(result)
```

## get_dutch_castles_schema

Locations of castles within the Netherlands from Rijksdienst voor het Cultureel Erfgoed (RCE) INSPIRE WFS. Uses GeoServer WFS v2 backend via OGRProvider.

- HTTP Method: `GET`
- Endpoint: `/collections/dutch_castles/schema`

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

result = sdk.dutch_castles.get_dutch_castles_schema(
    f="json",
    lang="en-US"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
