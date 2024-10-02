# DutchMetadataService

A list of all methods in the `DutchMetadataService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                              |
| :------------------------------------------------------------------------ | :------------------------------------------------------- |
| [describe_dutch_metadata_collection](#describe_dutch_metadata_collection) | Sample metadata records from Dutch Nationaal georegister |
| [get_dutch_metadata_features](#get_dutch_metadata_features)               | Sample metadata records from Dutch Nationaal georegister |
| [options_dutch_metadata_features](#options_dutch_metadata_features)       | Sample metadata records from Dutch Nationaal georegister |
| [get_dutch_metadata_feature](#get_dutch_metadata_feature)                 | Sample metadata records from Dutch Nationaal georegister |
| [options_dutch_metadata_feature](#options_dutch_metadata_feature)         | Sample metadata records from Dutch Nationaal georegister |
| [get_dutch_metadata_queryables](#get_dutch_metadata_queryables)           | Sample metadata records from Dutch Nationaal georegister |
| [get_dutch_metadata_schema](#get_dutch_metadata_schema)                   | Sample metadata records from Dutch Nationaal georegister |

## describe_dutch_metadata_collection

Sample metadata records from Dutch Nationaal georegister

- HTTP Method: `GET`
- Endpoint: `/collections/dutch-metadata`

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

result = sdk.dutch_metadata.describe_dutch_metadata_collection(
    f="json",
    lang="en-US"
)

print(result)
```

## get_dutch_metadata_features

Sample metadata records from Dutch Nationaal georegister

- HTTP Method: `GET`
- Endpoint: `/collections/dutch-metadata/items`

**Parameters**

| Name                       | Type                                                                                        | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :------------------------- | :------------------------------------------------------------------------------------------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f                          | [GetLandingPageF](../models/GetLandingPageF.md)                                             | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| lang                       | [Lang](../models/Lang.md)                                                                   | ❌       | The optional lang parameter instructs the server return a response in a certain language, if supported. If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language. Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion.                                                        |
| bbox                       | List[float]                                                                                 | ❌       | Only features that have a geometry that intersects the bounding box are selected.The bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth).                                                                                                                                                                                                                                                                                                                                                                                                                      |
| limit                      | int                                                                                         | ❌       | The optional limit parameter limits the number of items that are presented in the response document. Only items are counted that are on the first level of the collection in the response document. Nested objects contained within the explicitly requested items shall not be counted. Minimum = 1. Maximum = 10000. Default = 10.                                                                                                                                                                                                                                                                                                                        |
| crs                        | str                                                                                         | ❌       | Indicates the coordinate reference system for the results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| bbox_crs                   | str                                                                                         | ❌       | Indicates the coordinate reference system for the given bbox coordinates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| properties                 | [List[GetDutchMetadataFeaturesProperties]](../models/GetDutchMetadataFeaturesProperties.md) | ❌       | The properties that should be included for each feature. The parameter value is a comma-separated list of property names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| vendor_specific_parameters | dict                                                                                        | ❌       | Additional "free-form" parameters that are not explicitly defined                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| skip_geometry              | bool                                                                                        | ❌       | This option can be used to skip response geometries for each feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| sortby                     | List[str]                                                                                   | ❌       | Specifies a comma-separated list of property names by which the response shall be sorted. If the property name is preceded by a plus (+) sign it indicates an ascending sort for that property. If the property name is preceded by a minus (-) sign it indicates a descending sort for that property. If the property is not preceded by a plus or minus, then the default sort order implied is ascending (+).                                                                                                                                                                                                                                            |
| offset                     | int                                                                                         | ❌       | The optional offset parameter indicates the index within the result set from which the server shall begin presenting results in the response document. The first element has an index of 0 (default).                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| q                          | List[str]                                                                                   | ❌       | The optional q parameter supports keyword searching. Only records whose text fields contain one or more of the specified search terms are selected. The specific set of text keys/fields/properties of a record to which the q operator is applied is up to the description of the server. Implementations should, however, apply the q operator to the title, description and keywords keys/fields/properties.                                                                                                                                                                                                                                             |
| datetime\_                 | str                                                                                         | ❌       | Either a date-time or an interval. Date and time expressions adhere to RFC 3339. Intervals may be bounded or half-bounded (double-dots at start or end). Examples: _ A date-time: "2018-02-12T23:20:50Z" _ A bounded interval: "2018-02-12T00:00:00Z/2018-03-18T12:31:12Z" \* Half-bounded intervals: "2018-02-12T00:00:00Z/.." or "../2018-03-18T12:31:12Z" Only features that have a temporal property that intersects the value of `datetime` are selected. If a feature has multiple temporal properties, it is the decision of the server whether only a single temporal property is used to determine the extent or all relevant temporal properties. |
| created                    | str                                                                                         | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| updated                    | str                                                                                         | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| type\_                     | str                                                                                         | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| title                      | str                                                                                         | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| description                | str                                                                                         | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| providers                  | str                                                                                         | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| external_ids               | str                                                                                         | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| themes                     | str                                                                                         | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| extent                     | str                                                                                         | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

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
    1.2
]
properties=[
    "created"
]
vendor_specific_parameters=dict(
    {}
)
sortby=[
    "|hWP@M289R"
]
q=[
    "q"
]

result = sdk.dutch_metadata.get_dutch_metadata_features(
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
    offset=8,
    q=q,
    datetime_="datetime",
    created="created",
    updated="updated",
    type_="type",
    title="title",
    description="description",
    providers="providers",
    external_ids="externalIds",
    themes="themes",
    extent="extent"
)

print(result)
```

## options_dutch_metadata_features

Sample metadata records from Dutch Nationaal georegister

- HTTP Method: `OPTIONS`
- Endpoint: `/collections/dutch-metadata/items`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.dutch_metadata.options_dutch_metadata_features()

print(result)
```

## get_dutch_metadata_feature

Sample metadata records from Dutch Nationaal georegister

- HTTP Method: `GET`
- Endpoint: `/collections/dutch-metadata/items/{featureId}`

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

result = sdk.dutch_metadata.get_dutch_metadata_feature(
    feature_id="featureId",
    crs="crs",
    f="json",
    lang="en-US"
)

print(result)
```

## options_dutch_metadata_feature

Sample metadata records from Dutch Nationaal georegister

- HTTP Method: `OPTIONS`
- Endpoint: `/collections/dutch-metadata/items/{featureId}`

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

result = sdk.dutch_metadata.options_dutch_metadata_feature(feature_id="featureId")

print(result)
```

## get_dutch_metadata_queryables

Sample metadata records from Dutch Nationaal georegister

- HTTP Method: `GET`
- Endpoint: `/collections/dutch-metadata/queryables`

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

result = sdk.dutch_metadata.get_dutch_metadata_queryables(
    f="json",
    lang="en-US"
)

print(result)
```

## get_dutch_metadata_schema

Sample metadata records from Dutch Nationaal georegister

- HTTP Method: `GET`
- Endpoint: `/collections/dutch-metadata/schema`

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

result = sdk.dutch_metadata.get_dutch_metadata_schema(
    f="json",
    lang="en-US"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
