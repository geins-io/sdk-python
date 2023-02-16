<a name="__pageTop"></a>
# openapi_client.apis.tags.brand_api.BrandApi

All URIs are relative to *https://mgmtapi.geins.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_brand**](#create_brand) | **post** /API/Brand | Create a new brand
[**get_brand_by_id**](#get_brand_by_id) | **get** /API/Brand/{id} | Get a specific brand
[**query_brands**](#query_brands) | **post** /API/Brand/Query | Query brands
[**update_brand**](#update_brand) | **put** /API/Brand/{id} | Updates a brand

# **create_brand**
<a name="create_brand"></a>
> EnvelopeBrandModelsReadBrand create_brand(brand)

Create a new brand

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import brand_api
from openapi_client.model.brand_models_write_brand import BrandModelsWriteBrand
from openapi_client.model.envelope_brand_models_read_brand import EnvelopeBrandModelsReadBrand
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.geins.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.geins.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brand_api.BrandApi(api_client)

    # example passing only required values which don't have defaults set
    body = BrandModelsWriteBrand(
        name="name_example",
        external_id="external_id_example",
        descriptions=[
            SharedModelsLocalizableContent(
                language_code="language_code_example",
                content="content_example",
            )
        ],
    )
    try:
        # Create a new brand
        api_response = api_instance.create_brand(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BrandApi->create_brand: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextXml, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/json', 'application/xml', 'text/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsWriteBrand**](../../models/BrandModelsWriteBrand.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsWriteBrand**](../../models/BrandModelsWriteBrand.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsWriteBrand**](../../models/BrandModelsWriteBrand.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsWriteBrand**](../../models/BrandModelsWriteBrand.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsWriteBrand**](../../models/BrandModelsWriteBrand.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_brand.ApiResponseFor200) | OK

#### create_brand.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeBrandModelsReadBrand**](../../models/EnvelopeBrandModelsReadBrand.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeBrandModelsReadBrand**](../../models/EnvelopeBrandModelsReadBrand.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeBrandModelsReadBrand**](../../models/EnvelopeBrandModelsReadBrand.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeBrandModelsReadBrand**](../../models/EnvelopeBrandModelsReadBrand.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_brand_by_id**
<a name="get_brand_by_id"></a>
> EnvelopeBrandModelsReadBrand get_brand_by_id(id)

Get a specific brand

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import brand_api
from openapi_client.model.envelope_brand_models_read_brand import EnvelopeBrandModelsReadBrand
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.geins.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.geins.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brand_api.BrandApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Get a specific brand
        api_response = api_instance.get_brand_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BrandApi->get_brand_by_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/json', 'application/xml', 'text/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_brand_by_id.ApiResponseFor200) | OK

#### get_brand_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeBrandModelsReadBrand**](../../models/EnvelopeBrandModelsReadBrand.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeBrandModelsReadBrand**](../../models/EnvelopeBrandModelsReadBrand.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeBrandModelsReadBrand**](../../models/EnvelopeBrandModelsReadBrand.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeBrandModelsReadBrand**](../../models/EnvelopeBrandModelsReadBrand.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **query_brands**
<a name="query_brands"></a>
> [BrandModelsReadBrand] query_brands(query)

Query brands

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import brand_api
from openapi_client.model.brand_models_read_brand import BrandModelsReadBrand
from openapi_client.model.brand_models_brand_query import BrandModelsBrandQuery
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.geins.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.geins.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brand_api.BrandApi(api_client)

    # example passing only required values which don't have defaults set
    body = BrandModelsBrandQuery(
        created_after="1970-01-01T00:00:00.00Z",
        brand_ids=[
            1
        ],
        external_ids=[
            "external_ids_example"
        ],
    )
    try:
        # Query brands
        api_response = api_instance.query_brands(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BrandApi->query_brands: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextXml, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/json', 'application/xml', 'text/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsBrandQuery**](../../models/BrandModelsBrandQuery.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsBrandQuery**](../../models/BrandModelsBrandQuery.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsBrandQuery**](../../models/BrandModelsBrandQuery.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsBrandQuery**](../../models/BrandModelsBrandQuery.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsBrandQuery**](../../models/BrandModelsBrandQuery.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#query_brands.ApiResponseFor200) | OK

#### query_brands.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BrandModelsReadBrand**]({{complexTypePrefix}}BrandModelsReadBrand.md) | [**BrandModelsReadBrand**]({{complexTypePrefix}}BrandModelsReadBrand.md) | [**BrandModelsReadBrand**]({{complexTypePrefix}}BrandModelsReadBrand.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BrandModelsReadBrand**]({{complexTypePrefix}}BrandModelsReadBrand.md) | [**BrandModelsReadBrand**]({{complexTypePrefix}}BrandModelsReadBrand.md) | [**BrandModelsReadBrand**]({{complexTypePrefix}}BrandModelsReadBrand.md) |  | 

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BrandModelsReadBrand**]({{complexTypePrefix}}BrandModelsReadBrand.md) | [**BrandModelsReadBrand**]({{complexTypePrefix}}BrandModelsReadBrand.md) | [**BrandModelsReadBrand**]({{complexTypePrefix}}BrandModelsReadBrand.md) |  | 

# SchemaFor200ResponseBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BrandModelsReadBrand**]({{complexTypePrefix}}BrandModelsReadBrand.md) | [**BrandModelsReadBrand**]({{complexTypePrefix}}BrandModelsReadBrand.md) | [**BrandModelsReadBrand**]({{complexTypePrefix}}BrandModelsReadBrand.md) |  | 

### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_brand**
<a name="update_brand"></a>
> EnvelopeBrandModelsReadBrand update_brand(idbrand)

Updates a brand

Leaving out a property will ensure no changes are made to that property.  Collection properties will delete and/or add as necessary to match the supplied data.

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import brand_api
from openapi_client.model.brand_models_write_brand import BrandModelsWriteBrand
from openapi_client.model.envelope_brand_models_read_brand import EnvelopeBrandModelsReadBrand
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.geins.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.geins.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure HTTP basic authorization: basicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = brand_api.BrandApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    body = BrandModelsWriteBrand(
        name="name_example",
        external_id="external_id_example",
        descriptions=[
            SharedModelsLocalizableContent(
                language_code="language_code_example",
                content="content_example",
            )
        ],
    )
    try:
        # Updates a brand
        api_response = api_instance.update_brand(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BrandApi->update_brand: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextXml, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/json', 'application/xml', 'text/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsWriteBrand**](../../models/BrandModelsWriteBrand.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsWriteBrand**](../../models/BrandModelsWriteBrand.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsWriteBrand**](../../models/BrandModelsWriteBrand.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsWriteBrand**](../../models/BrandModelsWriteBrand.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**BrandModelsWriteBrand**](../../models/BrandModelsWriteBrand.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_brand.ApiResponseFor200) | OK

#### update_brand.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeBrandModelsReadBrand**](../../models/EnvelopeBrandModelsReadBrand.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeBrandModelsReadBrand**](../../models/EnvelopeBrandModelsReadBrand.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeBrandModelsReadBrand**](../../models/EnvelopeBrandModelsReadBrand.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeBrandModelsReadBrand**](../../models/EnvelopeBrandModelsReadBrand.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

