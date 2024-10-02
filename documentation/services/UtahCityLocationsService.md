# UtahCityLocationsService

A list of all methods in the `UtahCityLocationsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                             | Description                                                                                                 |
| :---------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| [describe_utah_city_locations_collection](#describe_utah_city_locations_collection) | Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS. |
| [get_utah_city_locations_features](#get_utah_city_locations_features)               | Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS. |
| [options_utah_city_locations_features](#options_utah_city_locations_features)       | Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS. |
| [get_utah_city_locations_feature](#get_utah_city_locations_feature)                 | Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS. |
| [options_utah_city_locations_feature](#options_utah_city_locations_feature)         | Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS. |
| [get_utah_city_locations_queryables](#get_utah_city_locations_queryables)           | Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS. |
| [get_utah_city_locations_schema](#get_utah_city_locations_schema)                   | Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS. |

## describe_utah_city_locations_collection

Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS.

- HTTP Method: `GET`
- Endpoint: `/collections/utah_city_locations`

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

result = sdk.utah_city_locations.describe_utah_city_locations_collection(
    f="json",
    lang="en-US"
)

print(result)
```

## get_utah_city_locations_features

Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS.

- HTTP Method: `GET`
- Endpoint: `/collections/utah_city_locations/items`

**Parameters**

| Name                       | Type                                                                                                | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :------------------------- | :-------------------------------------------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f                          | [GetLandingPageF](../models/GetLandingPageF.md)                                                     | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| lang                       | [Lang](../models/Lang.md)                                                                           | ❌       | The optional lang parameter instructs the server return a response in a certain language, if supported. If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language. Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion. |
| bbox                       | List[float]                                                                                         | ❌       | Only features that have a geometry that intersects the bounding box are selected.The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth).                                                                                                                                                                                                                                                                                                                                                               |
| limit                      | int                                                                                                 | ❌       | The optional limit parameter limits the number of items that are presented in the response document. Only items are counted that are on the first level of the collection in the response document. Nested objects contained within the explicitly requested items shall not be counted. Minimum = 1. Maximum = 10000. Default = 10.                                                                                                                                                                                                                                                                 |
| crs                        | str                                                                                                 | ❌       | Indicates the coordinate reference system for the results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| bbox_crs                   | str                                                                                                 | ❌       | Indicates the coordinate reference system for the given bbox coordinates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| properties                 | [List[GetUtahCityLocationsFeaturesProperties]](../models/GetUtahCityLocationsFeaturesProperties.md) | ❌       | The properties that should be included for each feature. The parameter value is a comma-separated list of property names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| vendor_specific_parameters | dict                                                                                                | ❌       | Additional "free-form" parameters that are not explicitly defined                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| skip_geometry              | bool                                                                                                | ❌       | This option can be used to skip response geometries for each feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sortby                     | List[str]                                                                                           | ❌       | Specifies a comma-separated list of property names by which the response shall be sorted. If the property name is preceded by a plus (+) sign it indicates an ascending sort for that property. If the property name is preceded by a minus (-) sign it indicates a descending sort for that property. If the property is not preceded by a plus or minus, then the default sort order implied is ascending (+).                                                                                                                                                                                     |
| offset                     | int                                                                                                 | ❌       | The optional offset parameter indicates the index within the result set from which the server shall begin presenting results in the response document. The first element has an index of 0 (default).                                                                                                                                                                                                                                                                                                                                                                                                |
| gml_id                     | str                                                                                                 | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| name                       | str                                                                                                 | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| co_seat                    | str                                                                                                 | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| pop_1999                   | float                                                                                               | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| pop_sym_99                 | float                                                                                               | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| pop_2000                   | float                                                                                               | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| pop_sym_00                 | float                                                                                               | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| state                      | str                                                                                                 | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

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
    6.33
]
properties=[
    "gml_id"
]
vendor_specific_parameters=dict(
    {}
)
sortby=[
    "q=\\>37Ai("
]

result = sdk.utah_city_locations.get_utah_city_locations_features(
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
    offset=2,
    gml_id="gml_id",
    name="NAME",
    co_seat="CO_SEAT",
    pop_1999=9.19,
    pop_sym_99=1.7,
    pop_2000=8.36,
    pop_sym_00=4.64,
    state="STATE"
)

print(result)
```

## options_utah_city_locations_features

Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS.

- HTTP Method: `OPTIONS`
- Endpoint: `/collections/utah_city_locations/items`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.utah_city_locations.options_utah_city_locations_features()

print(result)
```

## get_utah_city_locations_feature

Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS.

- HTTP Method: `GET`
- Endpoint: `/collections/utah_city_locations/items/{featureId}`

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

result = sdk.utah_city_locations.get_utah_city_locations_feature(
    feature_id="featureId",
    crs="crs",
    f="json",
    lang="en-US"
)

print(result)
```

## options_utah_city_locations_feature

Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS.

- HTTP Method: `OPTIONS`
- Endpoint: `/collections/utah_city_locations/items/{featureId}`

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

result = sdk.utah_city_locations.options_utah_city_locations_feature(feature_id="featureId")

print(result)
```

## get_utah_city_locations_queryables

Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS.

- HTTP Method: `GET`
- Endpoint: `/collections/utah_city_locations/queryables`

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

result = sdk.utah_city_locations.get_utah_city_locations_queryables(
    f="json",
    lang="en-US"
)

print(result)
```

## get_utah_city_locations_schema

Data from the state of Utah. Standard demo dataset from the deegree WFS server that is used as backend WFS.

- HTTP Method: `GET`
- Endpoint: `/collections/utah_city_locations/schema`

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

result = sdk.utah_city_locations.get_utah_city_locations_schema(
    f="json",
    lang="en-US"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
