# GeobeyondSdk Python SDK 1.0.0<a id="geobeyondsdk-python-sdk-100"></a>

Welcome to the GeobeyondSdk SDK documentation. This guide will help you get started with integrating and using the GeobeyondSdk SDK in your project.

## Versions<a id="versions"></a>

- API version: `0.18.0`
- SDK version: `1.0.0`

## About the API<a id="about-the-api"></a>

pygeoapi provides an API to geospatial data

## Table of Contents<a id="table-of-contents"></a>

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Setting a Custom Timeout](#setting-a-custom-timeout)
- [Sample Usage](#sample-usage)
- [Services](#services)
- [Models](#models)
  - [Using Union Types](#using-union-types)
- [License](#license)

## Setup & Configuration<a id="setup--configuration"></a>

### Supported Language Versions<a id="supported-language-versions"></a>

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation<a id="installation"></a>

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install geobeyond
```

## Setting a Custom Timeout<a id="setting-a-custom-timeout"></a>

You can set a custom timeout for the SDK's HTTP requests as follows:

```py
from geobeyond_sdk import GeobeyondSdk

sdk = GeobeyondSdk(timeout=10000)
```

# Sample Usage<a id="sample-usage"></a>

Below is a comprehensive example demonstrating how to authenticate and call a simple endpoint:

```py
from geobeyond_sdk import GeobeyondSdk, Environment
from geobeyond_sdk.models import GetLandingPageF, Lang

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.server.get_landing_page(
    f="json",
    lang="en-US"
)

print(result)

```

## Services<a id="services"></a>

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services:</summary>

| Name                         |
| :--------------------------- |
| server                       |
| dutch_metadata               |
| dutch_castles                |
| dutch_georef_stations        |
| dutch_windmills              |
| gdps_temperature             |
| icoads_sst                   |
| lakes                        |
| mapserver_world_map          |
| obs                          |
| ogr_addresses_gpkg           |
| ogr_addresses_sqlite         |
| ogr_geojson_lakes            |
| ogr_gpkg_poi                 |
| ogr_gpkg_wales_railway_lines |
| ogr_gpkg_wales_stations      |
| unesco_pois_italy            |
| utah_city_locations          |
| jobs                         |
| hello_world                  |
| stac                         |

</details>

## Models<a id="models"></a>

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models:</summary>

| Name                                          | Description                                                                                                                                                                                                                                           |
| :-------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LandingPage                                   |                                                                                                                                                                                                                                                       |
| GetLandingPageF                               |                                                                                                                                                                                                                                                       |
| Lang                                          |                                                                                                                                                                                                                                                       |
| Ui                                            |                                                                                                                                                                                                                                                       |
| ProcessList                                   |                                                                                                                                                                                                                                                       |
| Collection                                    |                                                                                                                                                                                                                                                       |
| FeatureCollectionGeoJson                      |                                                                                                                                                                                                                                                       |
| GetDutchMetadataFeaturesProperties            |                                                                                                                                                                                                                                                       |
| FeatureGeoJson                                |                                                                                                                                                                                                                                                       |
| Queryables                                    |                                                                                                                                                                                                                                                       |
| GetDutchCastlesFeaturesProperties             |                                                                                                                                                                                                                                                       |
| GetDutchGeorefStationsFeaturesProperties      |                                                                                                                                                                                                                                                       |
| GetDutchWindmillsFeaturesProperties           |                                                                                                                                                                                                                                                       |
| CoverageJson                                  | A geospatial coverage interchange format based on JavaScript Object Notation (JSON)                                                                                                                                                                   |
| GetLakesFeaturesProperties                    |                                                                                                                                                                                                                                                       |
| Tiles                                         |                                                                                                                                                                                                                                                       |
| TileMatrixSets                                |                                                                                                                                                                                                                                                       |
| GetLakesTilesF                                |                                                                                                                                                                                                                                                       |
| GetMapF                                       |                                                                                                                                                                                                                                                       |
| GetObsFeaturesProperties                      |                                                                                                                                                                                                                                                       |
| GetOgrAddressesGpkgFeaturesProperties         |                                                                                                                                                                                                                                                       |
| GetOgrAddressesSqliteFeaturesProperties       |                                                                                                                                                                                                                                                       |
| GetOgrGeojsonLakesFeaturesProperties          |                                                                                                                                                                                                                                                       |
| GetOgrGpkgPoiFeaturesProperties               |                                                                                                                                                                                                                                                       |
| GetOgrGpkgWalesRailwayLinesFeaturesProperties |                                                                                                                                                                                                                                                       |
| GetOgrGpkgWalesStationsFeaturesProperties     |                                                                                                                                                                                                                                                       |
| GetUnescoPoisItalyFeaturesProperties          |                                                                                                                                                                                                                                                       |
| GetUtahCityLocationsFeaturesProperties        |                                                                                                                                                                                                                                                       |
| Execute                                       |                                                                                                                                                                                                                                                       |
| StatusInfo                                    |                                                                                                                                                                                                                                                       |
| Link                                          |                                                                                                                                                                                                                                                       |
| ProcessSummary                                |                                                                                                                                                                                                                                                       |
| Link3                                         |                                                                                                                                                                                                                                                       |
| Metadata                                      |                                                                                                                                                                                                                                                       |
| JobControlOptions                             |                                                                                                                                                                                                                                                       |
| TransmissionMode                              |                                                                                                                                                                                                                                                       |
| AdditionalParameter                           |                                                                                                                                                                                                                                                       |
| Extent                                        | The extent of the features in the collection. In the Core only spatial and temporal extents are specified. Extensions may add additional members to represent other extents, for example, thermal or pressure ranges.                                 |
| PointGeoJson                                  |                                                                                                                                                                                                                                                       |
| MultipointGeoJson                             |                                                                                                                                                                                                                                                       |
| LinestringGeoJson                             |                                                                                                                                                                                                                                                       |
| MultilinestringGeoJson                        |                                                                                                                                                                                                                                                       |
| PolygonGeoJson                                |                                                                                                                                                                                                                                                       |
| MultipolygonGeoJson                           |                                                                                                                                                                                                                                                       |
| GeometrycollectionGeoJson                     |                                                                                                                                                                                                                                                       |
| Queryable                                     |                                                                                                                                                                                                                                                       |
| NdArray                                       | Object representing a multidimensional (>= 0D) array with named axes, encoded as a flat one-dimensional array in row-major order                                                                                                                      |
| ReferenceSystemConnection                     | Reference System Connection object: connects coordinates to reference systems                                                                                                                                                                         |
| Domain                                        | A Domain, which defines a set of positions and their extent in one or more referencing systems                                                                                                                                                        |
| ReferenceSystem                               |                                                                                                                                                                                                                                                       |
| Link2                                         |                                                                                                                                                                                                                                                       |
| Tilematrixsetlink                             |                                                                                                                                                                                                                                                       |
| Subscriber                                    | Optional URIs for callbacks for this job. Support for this parameter is not required and the parameter may be removed from the API definition, if conformance class **'callback'** is not listed in the conformance declaration under `/conformance`. |
| StatusCode                                    |                                                                                                                                                                                                                                                       |

</details>

### Using Union Types<a id="using-union-types"></a>

Union types allow you to specify that a variable can have more than one type. This is particularly useful when a function can accept multiple types of inputs. The Union type hint is used for this purpose.

#### Example Function with Union Types<a id="example-function-with-union-types"></a>

You can call service method with an instance of `TypeA`, `TypeB`, or a dictionary that can be converted to an instance of either type.

```python
# Model Definition<a id="model-definition"></a>
ParamType = Union[TypeA, TypeB]

# Service Method<a id="service-method"></a>
def service_method(param: ParamType):
...

## Usage<a id="usage"></a>
type_a = TypeA(key="value")
type_b = TypeB(key="value")

sdk.service.service_method(type_a)
sdk.service.service_method(type_b)
sdk.service.service_method({"key": "value"})
```

You cannot create an instance of a `Union` type itself. Instead, pass an instance of one of the types in the `Union`, or a dictionary that can be converted to one of those types.

## License<a id="license"></a>

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.

<!-- This file was generated by liblab | https://liblab.com/ -->
