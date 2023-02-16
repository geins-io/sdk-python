<a name="__pageTop"></a>
# openapi_client.apis.tags.page_area_api.PageAreaApi

All URIs are relative to *https://mgmtapi.geins.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_a_page_area**](#create_or_update_a_page_area) | **post** /API/PageArea | Create or update a page area
[**create_or_update_page_area_family**](#create_or_update_page_area_family) | **post** /API/PageAreaFamily | Create or update a page area family
[**get_page_area**](#get_page_area) | **get** /API/PageArea/{name} | Get a specific page area
[**get_page_area_family**](#get_page_area_family) | **get** /API/PageAreaFamily/{familyId} | Get a specific page area family
[**list_page_area_families**](#list_page_area_families) | **get** /API/PageAreaFamily/List | Gets a list of all page area families, including nested data

# **create_or_update_a_page_area**
<a name="create_or_update_a_page_area"></a>
> EnvelopePageAreaModelsReadPageArea create_or_update_a_page_area(area)

Create or update a page area

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import page_area_api
from openapi_client.model.envelope_page_area_models_read_page_area import EnvelopePageAreaModelsReadPageArea
from openapi_client.model.page_area_models_write_page_area import PageAreaModelsWritePageArea
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
    api_instance = page_area_api.PageAreaApi(api_client)

    # example passing only required values which don't have defaults set
    body = PageAreaModelsWritePageArea(
        index=1,
        name="name_example",
        family_id=1,
        settings=SystemNullableValidationConfiguration(
            lazy_load_configuration=PageWidgetLazyLoadSetupLazyLoadConfiguration(
                enable_lazyload_mobile=True,
                eager_load_steps_mobile=1,
                enable_lazyload_desktop=True,
                eager_load_steps_desktop=1,
            ),
            lazy_load_collection_configurations=[
                PageWidgetLazyLoadSetupLazyLoadCollectionConfiguration(
                    collection_name="collection_name_example",
                    enable_lazyload_mobile=True,
                    eager_load_steps_mobile=1,
                    enable_lazyload_desktop=True,
                    eager_load_steps_desktop=1,
                )
            ],
            widget_restrictions=dict(
                "key": WidgetRestrictionSetupWidgetRestrictionConfiguration(
                    forced_responsive_mode=0,
                    allowed_sizes=[
                        1
                    ],
                ),
            ),
            container_restrictions=ContainerRestrictionSetupContainerRestrictionConfiguration(
                allowed_layouts=[
                    0
                ],
                banned_widgets=[
                    "00000000-0000-0000-0000-000000000000"
                ],
            ),
        ),
    )
    try:
        # Create or update a page area
        api_response = api_instance.create_or_update_a_page_area(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PageAreaApi->create_or_update_a_page_area: %s\n" % e)
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
[**PageAreaModelsWritePageArea**](../../models/PageAreaModelsWritePageArea.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsWritePageArea**](../../models/PageAreaModelsWritePageArea.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsWritePageArea**](../../models/PageAreaModelsWritePageArea.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsWritePageArea**](../../models/PageAreaModelsWritePageArea.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsWritePageArea**](../../models/PageAreaModelsWritePageArea.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_or_update_a_page_area.ApiResponseFor200) | OK

#### create_or_update_a_page_area.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopePageAreaModelsReadPageArea**](../../models/EnvelopePageAreaModelsReadPageArea.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopePageAreaModelsReadPageArea**](../../models/EnvelopePageAreaModelsReadPageArea.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopePageAreaModelsReadPageArea**](../../models/EnvelopePageAreaModelsReadPageArea.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopePageAreaModelsReadPageArea**](../../models/EnvelopePageAreaModelsReadPageArea.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_or_update_page_area_family**
<a name="create_or_update_page_area_family"></a>
> EnvelopePageAreaModelsReadPageAreaFamily create_or_update_page_area_family(family)

Create or update a page area family

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import page_area_api
from openapi_client.model.page_area_models_write_page_area_family import PageAreaModelsWritePageAreaFamily
from openapi_client.model.envelope_page_area_models_read_page_area_family import EnvelopePageAreaModelsReadPageAreaFamily
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
    api_instance = page_area_api.PageAreaApi(api_client)

    # example passing only required values which don't have defaults set
    body = PageAreaModelsWritePageAreaFamily(
        id=1,
        name="name_example",
        filterable_properties=[
            "filterable_properties_example"
        ],
        areas=[
            PageAreaModelsWritePageArea(
                index=1,
                name="name_example",
                family_id=1,
                settings=SystemNullableValidationConfiguration(
                    lazy_load_configuration=PageWidgetLazyLoadSetupLazyLoadConfiguration(
                        enable_lazyload_mobile=True,
                        eager_load_steps_mobile=1,
                        enable_lazyload_desktop=True,
                        eager_load_steps_desktop=1,
                    ),
                    lazy_load_collection_configurations=[
                        PageWidgetLazyLoadSetupLazyLoadCollectionConfiguration(
                            collection_name="collection_name_example",
                            enable_lazyload_mobile=True,
                            eager_load_steps_mobile=1,
                            enable_lazyload_desktop=True,
                            eager_load_steps_desktop=1,
                        )
                    ],
                    widget_restrictions=dict(
                        "key": WidgetRestrictionSetupWidgetRestrictionConfiguration(
                            forced_responsive_mode=0,
                            allowed_sizes=[
                                1
                            ],
                        ),
                    ),
                    container_restrictions=ContainerRestrictionSetupContainerRestrictionConfiguration(
                        allowed_layouts=[
                            0
                        ],
                        banned_widgets=[
                            "00000000-0000-0000-0000-000000000000"
                        ],
                    ),
                ),
            )
        ],
    )
    try:
        # Create or update a page area family
        api_response = api_instance.create_or_update_page_area_family(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PageAreaApi->create_or_update_page_area_family: %s\n" % e)
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
[**PageAreaModelsWritePageAreaFamily**](../../models/PageAreaModelsWritePageAreaFamily.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsWritePageAreaFamily**](../../models/PageAreaModelsWritePageAreaFamily.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsWritePageAreaFamily**](../../models/PageAreaModelsWritePageAreaFamily.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsWritePageAreaFamily**](../../models/PageAreaModelsWritePageAreaFamily.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsWritePageAreaFamily**](../../models/PageAreaModelsWritePageAreaFamily.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_or_update_page_area_family.ApiResponseFor200) | OK

#### create_or_update_page_area_family.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopePageAreaModelsReadPageAreaFamily**](../../models/EnvelopePageAreaModelsReadPageAreaFamily.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopePageAreaModelsReadPageAreaFamily**](../../models/EnvelopePageAreaModelsReadPageAreaFamily.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopePageAreaModelsReadPageAreaFamily**](../../models/EnvelopePageAreaModelsReadPageAreaFamily.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopePageAreaModelsReadPageAreaFamily**](../../models/EnvelopePageAreaModelsReadPageAreaFamily.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_page_area**
<a name="get_page_area"></a>
> PageAreaModelsReadPageArea get_page_area(name)

Get a specific page area

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import page_area_api
from openapi_client.model.page_area_models_read_page_area import PageAreaModelsReadPageArea
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
    api_instance = page_area_api.PageAreaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    try:
        # Get a specific page area
        api_response = api_instance.get_page_area(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PageAreaApi->get_page_area: %s\n" % e)
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
name | NameSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_page_area.ApiResponseFor200) | OK

#### get_page_area.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsReadPageArea**](../../models/PageAreaModelsReadPageArea.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsReadPageArea**](../../models/PageAreaModelsReadPageArea.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsReadPageArea**](../../models/PageAreaModelsReadPageArea.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsReadPageArea**](../../models/PageAreaModelsReadPageArea.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_page_area_family**
<a name="get_page_area_family"></a>
> PageAreaModelsReadPageAreaFamily get_page_area_family(family_id)

Get a specific page area family

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import page_area_api
from openapi_client.model.page_area_models_read_page_area_family import PageAreaModelsReadPageAreaFamily
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
    api_instance = page_area_api.PageAreaApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'familyId': 1,
    }
    try:
        # Get a specific page area family
        api_response = api_instance.get_page_area_family(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PageAreaApi->get_page_area_family: %s\n" % e)
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
familyId | FamilyIdSchema | | 

# FamilyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_page_area_family.ApiResponseFor200) | OK

#### get_page_area_family.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsReadPageAreaFamily**](../../models/PageAreaModelsReadPageAreaFamily.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsReadPageAreaFamily**](../../models/PageAreaModelsReadPageAreaFamily.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsReadPageAreaFamily**](../../models/PageAreaModelsReadPageAreaFamily.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**PageAreaModelsReadPageAreaFamily**](../../models/PageAreaModelsReadPageAreaFamily.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_page_area_families**
<a name="list_page_area_families"></a>
> [PageAreaModelsReadPageAreaFamily] list_page_area_families()

Gets a list of all page area families, including nested data

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import page_area_api
from openapi_client.model.page_area_models_read_page_area_family import PageAreaModelsReadPageAreaFamily
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
    api_instance = page_area_api.PageAreaApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gets a list of all page area families, including nested data
        api_response = api_instance.list_page_area_families()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PageAreaApi->list_page_area_families: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_page_area_families.ApiResponseFor200) | OK

#### list_page_area_families.ApiResponseFor200
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
[**PageAreaModelsReadPageAreaFamily**]({{complexTypePrefix}}PageAreaModelsReadPageAreaFamily.md) | [**PageAreaModelsReadPageAreaFamily**]({{complexTypePrefix}}PageAreaModelsReadPageAreaFamily.md) | [**PageAreaModelsReadPageAreaFamily**]({{complexTypePrefix}}PageAreaModelsReadPageAreaFamily.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PageAreaModelsReadPageAreaFamily**]({{complexTypePrefix}}PageAreaModelsReadPageAreaFamily.md) | [**PageAreaModelsReadPageAreaFamily**]({{complexTypePrefix}}PageAreaModelsReadPageAreaFamily.md) | [**PageAreaModelsReadPageAreaFamily**]({{complexTypePrefix}}PageAreaModelsReadPageAreaFamily.md) |  | 

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PageAreaModelsReadPageAreaFamily**]({{complexTypePrefix}}PageAreaModelsReadPageAreaFamily.md) | [**PageAreaModelsReadPageAreaFamily**]({{complexTypePrefix}}PageAreaModelsReadPageAreaFamily.md) | [**PageAreaModelsReadPageAreaFamily**]({{complexTypePrefix}}PageAreaModelsReadPageAreaFamily.md) |  | 

# SchemaFor200ResponseBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PageAreaModelsReadPageAreaFamily**]({{complexTypePrefix}}PageAreaModelsReadPageAreaFamily.md) | [**PageAreaModelsReadPageAreaFamily**]({{complexTypePrefix}}PageAreaModelsReadPageAreaFamily.md) | [**PageAreaModelsReadPageAreaFamily**]({{complexTypePrefix}}PageAreaModelsReadPageAreaFamily.md) |  | 

### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

