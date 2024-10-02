# GeobeyondSdk Python SDK 1.0.0

Welcome to the GeobeyondSdk SDK documentation. This guide will help you get started with integrating and using the GeobeyondSdk SDK in your project.

## Versions

- API version: `0.18.0`
- SDK version: `1.0.0`

## About the API

pygeoapi provides an API to geospatial data

## Table of Contents

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Setting a Custom Timeout](#setting-a-custom-timeout)
- [Sample Usage](#sample-usage)
- [Services](#services)
- [Models](#models)
  - [Using Union Types](#using-union-types)
- [License](#license)

## Setup & Configuration

### Supported Language Versions

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install geobeyond
```

## Setting a Custom Timeout

You can set a custom timeout for the SDK's HTTP requests as follows:

```py
from geobeyond_sdk import GeobeyondSdk

sdk = GeobeyondSdk(timeout=10000)
```

# Sample Usage

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

## Services

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services with links to their detailed documentation:</summary>

| Name                                                                                         |
| :------------------------------------------------------------------------------------------- |
| [ServerService](documentation/services/ServerService.md)                                     |
| [DutchMetadataService](documentation/services/DutchMetadataService.md)                       |
| [DutchCastlesService](documentation/services/DutchCastlesService.md)                         |
| [DutchGeorefStationsService](documentation/services/DutchGeorefStationsService.md)           |
| [DutchWindmillsService](documentation/services/DutchWindmillsService.md)                     |
| [GdpsTemperatureService](documentation/services/GdpsTemperatureService.md)                   |
| [IcoadsSstService](documentation/services/IcoadsSstService.md)                               |
| [LakesService](documentation/services/LakesService.md)                                       |
| [MapserverWorldMapService](documentation/services/MapserverWorldMapService.md)               |
| [ObsService](documentation/services/ObsService.md)                                           |
| [OgrAddressesGpkgService](documentation/services/OgrAddressesGpkgService.md)                 |
| [OgrAddressesSqliteService](documentation/services/OgrAddressesSqliteService.md)             |
| [OgrGeojsonLakesService](documentation/services/OgrGeojsonLakesService.md)                   |
| [OgrGpkgPoiService](documentation/services/OgrGpkgPoiService.md)                             |
| [OgrGpkgWalesRailwayLinesService](documentation/services/OgrGpkgWalesRailwayLinesService.md) |
| [OgrGpkgWalesStationsService](documentation/services/OgrGpkgWalesStationsService.md)         |
| [UnescoPoisItalyService](documentation/services/UnescoPoisItalyService.md)                   |
| [UtahCityLocationsService](documentation/services/UtahCityLocationsService.md)               |
| [JobsService](documentation/services/JobsService.md)                                         |
| [HelloWorldService](documentation/services/HelloWorldService.md)                             |
| [StacService](documentation/services/StacService.md)                                         |

</details>

## Models

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models with links to their detailed documentation:</summary>

| Name                                                                                                                   | Description                                                                                                                                                                                                                                           |
| :--------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [LandingPage](documentation/models/LandingPage.md)                                                                     |                                                                                                                                                                                                                                                       |
| [GetLandingPageF](documentation/models/GetLandingPageF.md)                                                             |                                                                                                                                                                                                                                                       |
| [Lang](documentation/models/Lang.md)                                                                                   |                                                                                                                                                                                                                                                       |
| [Ui](documentation/models/Ui.md)                                                                                       |                                                                                                                                                                                                                                                       |
| [ProcessList](documentation/models/ProcessList.md)                                                                     |                                                                                                                                                                                                                                                       |
| [Collection](documentation/models/Collection.md)                                                                       |                                                                                                                                                                                                                                                       |
| [FeatureCollectionGeoJson](documentation/models/FeatureCollectionGeoJson.md)                                           |                                                                                                                                                                                                                                                       |
| [GetDutchMetadataFeaturesProperties](documentation/models/GetDutchMetadataFeaturesProperties.md)                       |                                                                                                                                                                                                                                                       |
| [FeatureGeoJson](documentation/models/FeatureGeoJson.md)                                                               |                                                                                                                                                                                                                                                       |
| [Queryables](documentation/models/Queryables.md)                                                                       |                                                                                                                                                                                                                                                       |
| [GetDutchCastlesFeaturesProperties](documentation/models/GetDutchCastlesFeaturesProperties.md)                         |                                                                                                                                                                                                                                                       |
| [GetDutchGeorefStationsFeaturesProperties](documentation/models/GetDutchGeorefStationsFeaturesProperties.md)           |                                                                                                                                                                                                                                                       |
| [GetDutchWindmillsFeaturesProperties](documentation/models/GetDutchWindmillsFeaturesProperties.md)                     |                                                                                                                                                                                                                                                       |
| [CoverageJson](documentation/models/CoverageJson.md)                                                                   | A geospatial coverage interchange format based on JavaScript Object Notation (JSON)                                                                                                                                                                   |
| [GetLakesFeaturesProperties](documentation/models/GetLakesFeaturesProperties.md)                                       |                                                                                                                                                                                                                                                       |
| [Tiles](documentation/models/Tiles.md)                                                                                 |                                                                                                                                                                                                                                                       |
| [TileMatrixSets](documentation/models/TileMatrixSets.md)                                                               |                                                                                                                                                                                                                                                       |
| [GetLakesTilesF](documentation/models/GetLakesTilesF.md)                                                               |                                                                                                                                                                                                                                                       |
| [GetMapF](documentation/models/GetMapF.md)                                                                             |                                                                                                                                                                                                                                                       |
| [GetObsFeaturesProperties](documentation/models/GetObsFeaturesProperties.md)                                           |                                                                                                                                                                                                                                                       |
| [GetOgrAddressesGpkgFeaturesProperties](documentation/models/GetOgrAddressesGpkgFeaturesProperties.md)                 |                                                                                                                                                                                                                                                       |
| [GetOgrAddressesSqliteFeaturesProperties](documentation/models/GetOgrAddressesSqliteFeaturesProperties.md)             |                                                                                                                                                                                                                                                       |
| [GetOgrGeojsonLakesFeaturesProperties](documentation/models/GetOgrGeojsonLakesFeaturesProperties.md)                   |                                                                                                                                                                                                                                                       |
| [GetOgrGpkgPoiFeaturesProperties](documentation/models/GetOgrGpkgPoiFeaturesProperties.md)                             |                                                                                                                                                                                                                                                       |
| [GetOgrGpkgWalesRailwayLinesFeaturesProperties](documentation/models/GetOgrGpkgWalesRailwayLinesFeaturesProperties.md) |                                                                                                                                                                                                                                                       |
| [GetOgrGpkgWalesStationsFeaturesProperties](documentation/models/GetOgrGpkgWalesStationsFeaturesProperties.md)         |                                                                                                                                                                                                                                                       |
| [GetUnescoPoisItalyFeaturesProperties](documentation/models/GetUnescoPoisItalyFeaturesProperties.md)                   |                                                                                                                                                                                                                                                       |
| [GetUtahCityLocationsFeaturesProperties](documentation/models/GetUtahCityLocationsFeaturesProperties.md)               |                                                                                                                                                                                                                                                       |
| [Execute](documentation/models/Execute.md)                                                                             |                                                                                                                                                                                                                                                       |
| [StatusInfo](documentation/models/StatusInfo.md)                                                                       |                                                                                                                                                                                                                                                       |
| [Link](documentation/models/Link.md)                                                                                   |                                                                                                                                                                                                                                                       |
| [ProcessSummary](documentation/models/ProcessSummary.md)                                                               |                                                                                                                                                                                                                                                       |
| [Link_3](documentation/models/Link3.md)                                                                                |                                                                                                                                                                                                                                                       |
| [Metadata](documentation/models/Metadata.md)                                                                           |                                                                                                                                                                                                                                                       |
| [JobControlOptions](documentation/models/JobControlOptions.md)                                                         |                                                                                                                                                                                                                                                       |
| [TransmissionMode](documentation/models/TransmissionMode.md)                                                           |                                                                                                                                                                                                                                                       |
| [AdditionalParameter](documentation/models/AdditionalParameter.md)                                                     |                                                                                                                                                                                                                                                       |
| [Extent](documentation/models/Extent.md)                                                                               | The extent of the features in the collection. In the Core only spatial and temporal extents are specified. Extensions may add additional members to represent other extents, for example, thermal or pressure ranges.                                 |
| [PointGeoJson](documentation/models/PointGeoJson.md)                                                                   |                                                                                                                                                                                                                                                       |
| [MultipointGeoJson](documentation/models/MultipointGeoJson.md)                                                         |                                                                                                                                                                                                                                                       |
| [LinestringGeoJson](documentation/models/LinestringGeoJson.md)                                                         |                                                                                                                                                                                                                                                       |
| [MultilinestringGeoJson](documentation/models/MultilinestringGeoJson.md)                                               |                                                                                                                                                                                                                                                       |
| [PolygonGeoJson](documentation/models/PolygonGeoJson.md)                                                               |                                                                                                                                                                                                                                                       |
| [MultipolygonGeoJson](documentation/models/MultipolygonGeoJson.md)                                                     |                                                                                                                                                                                                                                                       |
| [GeometrycollectionGeoJson](documentation/models/GeometrycollectionGeoJson.md)                                         |                                                                                                                                                                                                                                                       |
| [Queryable](documentation/models/Queryable.md)                                                                         |                                                                                                                                                                                                                                                       |
| [NdArray](documentation/models/NdArray.md)                                                                             | Object representing a multidimensional (>= 0D) array with named axes, encoded as a flat one-dimensional array in row-major order                                                                                                                      |
| [ReferenceSystemConnection](documentation/models/ReferenceSystemConnection.md)                                         | Reference System Connection object: connects coordinates to reference systems                                                                                                                                                                         |
| [Domain](documentation/models/Domain.md)                                                                               | A Domain, which defines a set of positions and their extent in one or more referencing systems                                                                                                                                                        |
| [ReferenceSystem](documentation/models/ReferenceSystem.md)                                                             |                                                                                                                                                                                                                                                       |
| [Link_2](documentation/models/Link2.md)                                                                                |                                                                                                                                                                                                                                                       |
| [Tilematrixsetlink](documentation/models/Tilematrixsetlink.md)                                                         |                                                                                                                                                                                                                                                       |
| [Subscriber](documentation/models/Subscriber.md)                                                                       | Optional URIs for callbacks for this job. Support for this parameter is not required and the parameter may be removed from the API definition, if conformance class **'callback'** is not listed in the conformance declaration under `/conformance`. |
| [StatusCode](documentation/models/StatusCode.md)                                                                       |                                                                                                                                                                                                                                                       |

</details>

### Using Union Types

Union types allow you to specify that a variable can have more than one type. This is particularly useful when a function can accept multiple types of inputs. The Union type hint is used for this purpose.

#### Example Function with Union Types

You can call service method with an instance of `TypeA`, `TypeB`, or a dictionary that can be converted to an instance of either type.

```python
# Model Definition
ParamType = Union[TypeA, TypeB]

# Service Method
def service_method(param: ParamType):
...

## Usage
type_a = TypeA(key="value")
type_b = TypeB(key="value")

sdk.service.service_method(type_a)
sdk.service.service_method(type_b)
sdk.service.service_method({"key": "value"})
```

You cannot create an instance of a `Union` type itself. Instead, pass an instance of one of the types in the `Union`, or a dictionary that can be converted to one of those types.

## License

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.

<!-- This file was generated by liblab | https://liblab.com/ -->
