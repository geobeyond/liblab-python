# ServerService

A list of all methods in the `ServerService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                |
| :---------------------------------------------------------- | :------------------------- |
| [get_landing_page](#get_landing_page)                       | Landing page               |
| [get_collections](#get_collections)                         | Collections                |
| [get_conformance_declaration](#get_conformance_declaration) | API conformance definition |
| [get_openapi](#get_openapi)                                 | This document              |
| [get_processes](#get_processes)                             | Processes                  |

## get_landing_page

Landing page

- HTTP Method: `GET`
- Endpoint: `/`

**Parameters**

| Name | Type                                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :--- | :---------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f    | [GetLandingPageF](../models/GetLandingPageF.md) | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| lang | [Lang](../models/Lang.md)                       | ❌       | The optional lang parameter instructs the server return a response in a certain language, if supported. If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language. Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion. |

**Return Type**

`LandingPage`

**Example Usage Code Snippet**

```python
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

## get_collections

Collections

- HTTP Method: `GET`
- Endpoint: `/collections`

**Parameters**

| Name | Type                                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :--- | :---------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f    | [GetLandingPageF](../models/GetLandingPageF.md) | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| lang | [Lang](../models/Lang.md)                       | ❌       | The optional lang parameter instructs the server return a response in a certain language, if supported. If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language. Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion. |

**Return Type**

`LandingPage`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment
from geobeyond_sdk.models import GetLandingPageF, Lang

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.server.get_collections(
    f="json",
    lang="en-US"
)

print(result)
```

## get_conformance_declaration

API conformance definition

- HTTP Method: `GET`
- Endpoint: `/conformance`

**Parameters**

| Name | Type                                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :--- | :---------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f    | [GetLandingPageF](../models/GetLandingPageF.md) | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| lang | [Lang](../models/Lang.md)                       | ❌       | The optional lang parameter instructs the server return a response in a certain language, if supported. If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language. Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion. |

**Return Type**

`LandingPage`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment
from geobeyond_sdk.models import GetLandingPageF, Lang

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.server.get_conformance_declaration(
    f="json",
    lang="en-US"
)

print(result)
```

## get_openapi

This document

- HTTP Method: `GET`
- Endpoint: `/openapi`

**Parameters**

| Name | Type                                            | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :--- | :---------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| f    | [GetLandingPageF](../models/GetLandingPageF.md) | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| lang | [Lang](../models/Lang.md)                       | ❌       | The optional lang parameter instructs the server return a response in a certain language, if supported. If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language. Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion. |
| ui   | [Ui](../models/Ui.md)                           | ❌       | UI to render the OpenAPI document                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment
from geobeyond_sdk.models import GetLandingPageF, Lang, Ui

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.server.get_openapi(
    f="json",
    lang="en-US",
    ui="swagger"
)

print(result)
```

## get_processes

Processes

- HTTP Method: `GET`
- Endpoint: `/processes`

**Parameters**

| Name | Type                                            | Required | Description                                                                                                                                          |
| :--- | :---------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| f    | [GetLandingPageF](../models/GetLandingPageF.md) | ❌       | The optional f parameter indicates the output format which the server shall provide as part of the response document. The default format is GeoJSON. |

**Return Type**

`ProcessList`

**Example Usage Code Snippet**

```python
from geobeyond_sdk import GeobeyondSdk, Environment
from geobeyond_sdk.models import GetLandingPageF

sdk = GeobeyondSdk(
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.server.get_processes(f="json")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
