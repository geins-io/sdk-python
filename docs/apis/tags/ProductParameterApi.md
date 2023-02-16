<a name="__pageTop"></a>
# openapi_client.apis.tags.product_parameter_api.ProductParameterApi

All URIs are relative to *https://mgmtapi.carismar.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_replace_product_parameter_values**](#batch_replace_product_parameter_values) | **post** /API/ProductParameter/Values | Replace multiple product parameter values
[**batch_update_product_parameter_values**](#batch_update_product_parameter_values) | **put** /API/ProductParameter/Values | Update multiple product parameter values
[**create_or_update_product_parameter_value**](#create_or_update_product_parameter_value) | **post** /API/ProductParameter/Value | Create or update a new product parameter value
[**create_product_parameter**](#create_product_parameter) | **post** /API/ProductParameter | Create a new product parameter
[**create_product_parameter_group**](#create_product_parameter_group) | **post** /API/ProductParameter/Group | Create a new product parameter group
[**create_product_parameter_predefined_value**](#create_product_parameter_predefined_value) | **post** /API/ProductParameter/PredefinedValue | Create a new predefined value for a product parameter
[**get_product_parameter_by_id**](#get_product_parameter_by_id) | **get** /API/ProductParameter/{id} | Get a specific product parameter
[**get_product_parameter_group_by_id**](#get_product_parameter_group_by_id) | **get** /API/ProductParameter/Group/{id} | Get a specific product parameter group
[**get_product_parameter_predefined_value**](#get_product_parameter_predefined_value) | **get** /API/ProductParameter/PredefinedValue/{id} | Get a specific predefined value for a product parameter
[**get_product_parameter_value**](#get_product_parameter_value) | **get** /API/ProductParameter/Value/{id} | Get a specific product parameter value
[**update_product_parameter**](#update_product_parameter) | **put** /API/ProductParameter/{id} | Updates a product parameter
[**update_product_parameter_group**](#update_product_parameter_group) | **put** /API/ProductParameter/Group/{id} | Update a product parameter group

# **batch_replace_product_parameter_values**
<a name="batch_replace_product_parameter_values"></a>
> Envelope batch_replace_product_parameter_values(product_parameter_batch)

Replace multiple product parameter values

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_parameter_api
from openapi_client.model.product_parameter_models_write_product_parameter_value_batch import ProductParameterModelsWriteProductParameterValueBatch
from openapi_client.model.envelope import Envelope
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.carismar.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.carismar.io"
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
    api_instance = product_parameter_api.ProductParameterApi(api_client)

    # example passing only required values which don't have defaults set
    body = ProductParameterModelsWriteProductParameterValueBatch(
        product_parameter_values=[
            ProductParameterModelsWriteProductParameterValue(
                product_id=1,
                parameter_id=1,
                value="value_example",
                localized_descriptions=[
                    SharedModelsLocalizableContent(
                        language_code="language_code_example",
                        content="content_example",
                    )
                ],
            )
        ],
    )
    try:
        # Replace multiple product parameter values
        api_response = api_instance.batch_replace_product_parameter_values(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductParameterApi->batch_replace_product_parameter_values: %s\n" % e)
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
[**ProductParameterModelsWriteProductParameterValueBatch**](../../models/ProductParameterModelsWriteProductParameterValueBatch.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterValueBatch**](../../models/ProductParameterModelsWriteProductParameterValueBatch.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterValueBatch**](../../models/ProductParameterModelsWriteProductParameterValueBatch.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterValueBatch**](../../models/ProductParameterModelsWriteProductParameterValueBatch.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterValueBatch**](../../models/ProductParameterModelsWriteProductParameterValueBatch.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#batch_replace_product_parameter_values.ApiResponseFor200) | OK

#### batch_replace_product_parameter_values.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Envelope**](../../models/Envelope.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Envelope**](../../models/Envelope.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**Envelope**](../../models/Envelope.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**Envelope**](../../models/Envelope.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **batch_update_product_parameter_values**
<a name="batch_update_product_parameter_values"></a>
> Envelope batch_update_product_parameter_values(product_parameter_batch)

Update multiple product parameter values

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_parameter_api
from openapi_client.model.product_parameter_models_write_product_parameter_value_batch import ProductParameterModelsWriteProductParameterValueBatch
from openapi_client.model.envelope import Envelope
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.carismar.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.carismar.io"
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
    api_instance = product_parameter_api.ProductParameterApi(api_client)

    # example passing only required values which don't have defaults set
    body = ProductParameterModelsWriteProductParameterValueBatch(
        product_parameter_values=[
            ProductParameterModelsWriteProductParameterValue(
                product_id=1,
                parameter_id=1,
                value="value_example",
                localized_descriptions=[
                    SharedModelsLocalizableContent(
                        language_code="language_code_example",
                        content="content_example",
                    )
                ],
            )
        ],
    )
    try:
        # Update multiple product parameter values
        api_response = api_instance.batch_update_product_parameter_values(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductParameterApi->batch_update_product_parameter_values: %s\n" % e)
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
[**ProductParameterModelsWriteProductParameterValueBatch**](../../models/ProductParameterModelsWriteProductParameterValueBatch.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterValueBatch**](../../models/ProductParameterModelsWriteProductParameterValueBatch.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterValueBatch**](../../models/ProductParameterModelsWriteProductParameterValueBatch.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterValueBatch**](../../models/ProductParameterModelsWriteProductParameterValueBatch.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterValueBatch**](../../models/ProductParameterModelsWriteProductParameterValueBatch.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#batch_update_product_parameter_values.ApiResponseFor200) | OK

#### batch_update_product_parameter_values.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Envelope**](../../models/Envelope.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Envelope**](../../models/Envelope.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**Envelope**](../../models/Envelope.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**Envelope**](../../models/Envelope.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_or_update_product_parameter_value**
<a name="create_or_update_product_parameter_value"></a>
> EnvelopeProductParameterModelsReadProductParameterValue create_or_update_product_parameter_value(product_parameter_value)

Create or update a new product parameter value

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_parameter_api
from openapi_client.model.product_parameter_models_write_product_parameter_value import ProductParameterModelsWriteProductParameterValue
from openapi_client.model.envelope_product_parameter_models_read_product_parameter_value import EnvelopeProductParameterModelsReadProductParameterValue
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.carismar.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.carismar.io"
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
    api_instance = product_parameter_api.ProductParameterApi(api_client)

    # example passing only required values which don't have defaults set
    body = ProductParameterModelsWriteProductParameterValue(
        product_id=1,
        parameter_id=1,
        value="value_example",
        localized_descriptions=[
            SharedModelsLocalizableContent(
                language_code="language_code_example",
                content="content_example",
            )
        ],
    )
    try:
        # Create or update a new product parameter value
        api_response = api_instance.create_or_update_product_parameter_value(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductParameterApi->create_or_update_product_parameter_value: %s\n" % e)
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
[**ProductParameterModelsWriteProductParameterValue**](../../models/ProductParameterModelsWriteProductParameterValue.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterValue**](../../models/ProductParameterModelsWriteProductParameterValue.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterValue**](../../models/ProductParameterModelsWriteProductParameterValue.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterValue**](../../models/ProductParameterModelsWriteProductParameterValue.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterValue**](../../models/ProductParameterModelsWriteProductParameterValue.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_or_update_product_parameter_value.ApiResponseFor200) | OK

#### create_or_update_product_parameter_value.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterValue**](../../models/EnvelopeProductParameterModelsReadProductParameterValue.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterValue**](../../models/EnvelopeProductParameterModelsReadProductParameterValue.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterValue**](../../models/EnvelopeProductParameterModelsReadProductParameterValue.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterValue**](../../models/EnvelopeProductParameterModelsReadProductParameterValue.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_product_parameter**
<a name="create_product_parameter"></a>
> EnvelopeProductParameterModelsReadProductParameter create_product_parameter(product_parameter)

Create a new product parameter

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_parameter_api
from openapi_client.model.envelope_product_parameter_models_read_product_parameter import EnvelopeProductParameterModelsReadProductParameter
from openapi_client.model.product_parameter_models_write_product_parameter import ProductParameterModelsWriteProductParameter
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.carismar.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.carismar.io"
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
    api_instance = product_parameter_api.ProductParameterApi(api_client)

    # example passing only required values which don't have defaults set
    body = ProductParameterModelsWriteProductParameter(
        parameter_id=1,
        group_id=1,
        parameter_type=1,
        name="name_example",
        localized_names=[
            SharedModelsLocalizableContent(
                language_code="language_code_example",
                content="content_example",
            )
        ],
    )
    try:
        # Create a new product parameter
        api_response = api_instance.create_product_parameter(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductParameterApi->create_product_parameter: %s\n" % e)
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
[**ProductParameterModelsWriteProductParameter**](../../models/ProductParameterModelsWriteProductParameter.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameter**](../../models/ProductParameterModelsWriteProductParameter.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameter**](../../models/ProductParameterModelsWriteProductParameter.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameter**](../../models/ProductParameterModelsWriteProductParameter.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameter**](../../models/ProductParameterModelsWriteProductParameter.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_product_parameter.ApiResponseFor200) | OK

#### create_product_parameter.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameter**](../../models/EnvelopeProductParameterModelsReadProductParameter.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameter**](../../models/EnvelopeProductParameterModelsReadProductParameter.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameter**](../../models/EnvelopeProductParameterModelsReadProductParameter.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameter**](../../models/EnvelopeProductParameterModelsReadProductParameter.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_product_parameter_group**
<a name="create_product_parameter_group"></a>
> EnvelopeProductParameterModelsReadProductParameterGroup create_product_parameter_group(product_parameter_group)

Create a new product parameter group

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_parameter_api
from openapi_client.model.envelope_product_parameter_models_read_product_parameter_group import EnvelopeProductParameterModelsReadProductParameterGroup
from openapi_client.model.product_parameter_models_write_product_parameter_group import ProductParameterModelsWriteProductParameterGroup
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.carismar.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.carismar.io"
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
    api_instance = product_parameter_api.ProductParameterApi(api_client)

    # example passing only required values which don't have defaults set
    body = ProductParameterModelsWriteProductParameterGroup(
        name="name_example",
        localized_names=[
            SharedModelsLocalizableContent(
                language_code="language_code_example",
                content="content_example",
            )
        ],
        parameter_ids=[
            1
        ],
    )
    try:
        # Create a new product parameter group
        api_response = api_instance.create_product_parameter_group(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductParameterApi->create_product_parameter_group: %s\n" % e)
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
[**ProductParameterModelsWriteProductParameterGroup**](../../models/ProductParameterModelsWriteProductParameterGroup.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterGroup**](../../models/ProductParameterModelsWriteProductParameterGroup.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterGroup**](../../models/ProductParameterModelsWriteProductParameterGroup.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterGroup**](../../models/ProductParameterModelsWriteProductParameterGroup.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterGroup**](../../models/ProductParameterModelsWriteProductParameterGroup.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_product_parameter_group.ApiResponseFor200) | OK

#### create_product_parameter_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterGroup**](../../models/EnvelopeProductParameterModelsReadProductParameterGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterGroup**](../../models/EnvelopeProductParameterModelsReadProductParameterGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterGroup**](../../models/EnvelopeProductParameterModelsReadProductParameterGroup.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterGroup**](../../models/EnvelopeProductParameterModelsReadProductParameterGroup.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_product_parameter_predefined_value**
<a name="create_product_parameter_predefined_value"></a>
> EnvelopeProductParameterModelsReadProductParameterPredefinedValue create_product_parameter_predefined_value(product_parameter_predefined_value)

Create a new predefined value for a product parameter

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_parameter_api
from openapi_client.model.product_parameter_models_write_product_parameter_predefined_value import ProductParameterModelsWriteProductParameterPredefinedValue
from openapi_client.model.envelope_product_parameter_models_read_product_parameter_predefined_value import EnvelopeProductParameterModelsReadProductParameterPredefinedValue
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.carismar.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.carismar.io"
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
    api_instance = product_parameter_api.ProductParameterApi(api_client)

    # example passing only required values which don't have defaults set
    body = ProductParameterModelsWriteProductParameterPredefinedValue(
        parameter_id=1,
        predefined_value_id=1,
        name="name_example",
        localized_names=[
            SharedModelsLocalizableContent(
                language_code="language_code_example",
                content="content_example",
            )
        ],
    )
    try:
        # Create a new predefined value for a product parameter
        api_response = api_instance.create_product_parameter_predefined_value(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductParameterApi->create_product_parameter_predefined_value: %s\n" % e)
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
[**ProductParameterModelsWriteProductParameterPredefinedValue**](../../models/ProductParameterModelsWriteProductParameterPredefinedValue.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterPredefinedValue**](../../models/ProductParameterModelsWriteProductParameterPredefinedValue.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterPredefinedValue**](../../models/ProductParameterModelsWriteProductParameterPredefinedValue.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterPredefinedValue**](../../models/ProductParameterModelsWriteProductParameterPredefinedValue.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterPredefinedValue**](../../models/ProductParameterModelsWriteProductParameterPredefinedValue.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_product_parameter_predefined_value.ApiResponseFor200) | OK

#### create_product_parameter_predefined_value.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterPredefinedValue**](../../models/EnvelopeProductParameterModelsReadProductParameterPredefinedValue.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterPredefinedValue**](../../models/EnvelopeProductParameterModelsReadProductParameterPredefinedValue.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterPredefinedValue**](../../models/EnvelopeProductParameterModelsReadProductParameterPredefinedValue.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterPredefinedValue**](../../models/EnvelopeProductParameterModelsReadProductParameterPredefinedValue.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_product_parameter_by_id**
<a name="get_product_parameter_by_id"></a>
> EnvelopeProductParameterModelsReadProductParameter get_product_parameter_by_id(id)

Get a specific product parameter

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_parameter_api
from openapi_client.model.envelope_product_parameter_models_read_product_parameter import EnvelopeProductParameterModelsReadProductParameter
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.carismar.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.carismar.io"
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
    api_instance = product_parameter_api.ProductParameterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Get a specific product parameter
        api_response = api_instance.get_product_parameter_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductParameterApi->get_product_parameter_by_id: %s\n" % e)
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
200 | [ApiResponseFor200](#get_product_parameter_by_id.ApiResponseFor200) | OK

#### get_product_parameter_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameter**](../../models/EnvelopeProductParameterModelsReadProductParameter.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameter**](../../models/EnvelopeProductParameterModelsReadProductParameter.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameter**](../../models/EnvelopeProductParameterModelsReadProductParameter.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameter**](../../models/EnvelopeProductParameterModelsReadProductParameter.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_product_parameter_group_by_id**
<a name="get_product_parameter_group_by_id"></a>
> EnvelopeProductParameterModelsReadProductParameterGroup get_product_parameter_group_by_id(id)

Get a specific product parameter group

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_parameter_api
from openapi_client.model.envelope_product_parameter_models_read_product_parameter_group import EnvelopeProductParameterModelsReadProductParameterGroup
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.carismar.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.carismar.io"
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
    api_instance = product_parameter_api.ProductParameterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Get a specific product parameter group
        api_response = api_instance.get_product_parameter_group_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductParameterApi->get_product_parameter_group_by_id: %s\n" % e)
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
200 | [ApiResponseFor200](#get_product_parameter_group_by_id.ApiResponseFor200) | OK

#### get_product_parameter_group_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterGroup**](../../models/EnvelopeProductParameterModelsReadProductParameterGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterGroup**](../../models/EnvelopeProductParameterModelsReadProductParameterGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterGroup**](../../models/EnvelopeProductParameterModelsReadProductParameterGroup.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterGroup**](../../models/EnvelopeProductParameterModelsReadProductParameterGroup.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_product_parameter_predefined_value**
<a name="get_product_parameter_predefined_value"></a>
> EnvelopeProductParameterModelsReadProductParameterValue get_product_parameter_predefined_value(id)

Get a specific predefined value for a product parameter

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_parameter_api
from openapi_client.model.envelope_product_parameter_models_read_product_parameter_value import EnvelopeProductParameterModelsReadProductParameterValue
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.carismar.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.carismar.io"
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
    api_instance = product_parameter_api.ProductParameterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    try:
        # Get a specific predefined value for a product parameter
        api_response = api_instance.get_product_parameter_predefined_value(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductParameterApi->get_product_parameter_predefined_value: %s\n" % e)
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
200 | [ApiResponseFor200](#get_product_parameter_predefined_value.ApiResponseFor200) | OK

#### get_product_parameter_predefined_value.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterValue**](../../models/EnvelopeProductParameterModelsReadProductParameterValue.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterValue**](../../models/EnvelopeProductParameterModelsReadProductParameterValue.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterValue**](../../models/EnvelopeProductParameterModelsReadProductParameterValue.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterValue**](../../models/EnvelopeProductParameterModelsReadProductParameterValue.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_product_parameter_value**
<a name="get_product_parameter_value"></a>
> EnvelopeProductParameterModelsReadProductParameterValue get_product_parameter_value(id)

Get a specific product parameter value

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_parameter_api
from openapi_client.model.envelope_product_parameter_models_read_product_parameter_value import EnvelopeProductParameterModelsReadProductParameterValue
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.carismar.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.carismar.io"
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
    api_instance = product_parameter_api.ProductParameterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    query_params = {
    }
    try:
        # Get a specific product parameter value
        api_response = api_instance.get_product_parameter_value(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductParameterApi->get_product_parameter_value: %s\n" % e)

    # example passing only optional values
    path_params = {
        'id': 1,
    }
    query_params = {
        'predefinedValueId': "predefinedValueId_example",
    }
    try:
        # Get a specific product parameter value
        api_response = api_instance.get_product_parameter_value(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductParameterApi->get_product_parameter_value: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/json', 'application/xml', 'text/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
predefinedValueId | PredefinedValueIdSchema | | optional


# PredefinedValueIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#get_product_parameter_value.ApiResponseFor200) | OK

#### get_product_parameter_value.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterValue**](../../models/EnvelopeProductParameterModelsReadProductParameterValue.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterValue**](../../models/EnvelopeProductParameterModelsReadProductParameterValue.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterValue**](../../models/EnvelopeProductParameterModelsReadProductParameterValue.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterValue**](../../models/EnvelopeProductParameterModelsReadProductParameterValue.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_product_parameter**
<a name="update_product_parameter"></a>
> EnvelopeProductParameterModelsReadProductParameter update_product_parameter(idproduct_parameter)

Updates a product parameter

Leaving out a property will ensure no changes are made to that property. Collection properties will delete and/or add as necessary to match the supplied data.

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_parameter_api
from openapi_client.model.envelope_product_parameter_models_read_product_parameter import EnvelopeProductParameterModelsReadProductParameter
from openapi_client.model.product_parameter_models_write_product_parameter import ProductParameterModelsWriteProductParameter
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.carismar.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.carismar.io"
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
    api_instance = product_parameter_api.ProductParameterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    body = ProductParameterModelsWriteProductParameter(
        parameter_id=1,
        group_id=1,
        parameter_type=1,
        name="name_example",
        localized_names=[
            SharedModelsLocalizableContent(
                language_code="language_code_example",
                content="content_example",
            )
        ],
    )
    try:
        # Updates a product parameter
        api_response = api_instance.update_product_parameter(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductParameterApi->update_product_parameter: %s\n" % e)
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
[**ProductParameterModelsWriteProductParameter**](../../models/ProductParameterModelsWriteProductParameter.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameter**](../../models/ProductParameterModelsWriteProductParameter.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameter**](../../models/ProductParameterModelsWriteProductParameter.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameter**](../../models/ProductParameterModelsWriteProductParameter.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameter**](../../models/ProductParameterModelsWriteProductParameter.md) |  | 


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
200 | [ApiResponseFor200](#update_product_parameter.ApiResponseFor200) | OK

#### update_product_parameter.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameter**](../../models/EnvelopeProductParameterModelsReadProductParameter.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameter**](../../models/EnvelopeProductParameterModelsReadProductParameter.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameter**](../../models/EnvelopeProductParameterModelsReadProductParameter.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameter**](../../models/EnvelopeProductParameterModelsReadProductParameter.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_product_parameter_group**
<a name="update_product_parameter_group"></a>
> EnvelopeProductParameterModelsReadProductParameterGroup update_product_parameter_group(idproduct_parameter_group)

Update a product parameter group

Leaving out a property will ensure no changes are made to that property. Collection properties will delete and/or add as necessary to match the supplied data.

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_parameter_api
from openapi_client.model.envelope_product_parameter_models_read_product_parameter_group import EnvelopeProductParameterModelsReadProductParameterGroup
from openapi_client.model.product_parameter_models_write_product_parameter_group import ProductParameterModelsWriteProductParameterGroup
from pprint import pprint
# Defining the host is optional and defaults to https://mgmtapi.carismar.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://mgmtapi.carismar.io"
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
    api_instance = product_parameter_api.ProductParameterApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'id': 1,
    }
    body = ProductParameterModelsWriteProductParameterGroup(
        name="name_example",
        localized_names=[
            SharedModelsLocalizableContent(
                language_code="language_code_example",
                content="content_example",
            )
        ],
        parameter_ids=[
            1
        ],
    )
    try:
        # Update a product parameter group
        api_response = api_instance.update_product_parameter_group(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductParameterApi->update_product_parameter_group: %s\n" % e)
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
[**ProductParameterModelsWriteProductParameterGroup**](../../models/ProductParameterModelsWriteProductParameterGroup.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterGroup**](../../models/ProductParameterModelsWriteProductParameterGroup.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterGroup**](../../models/ProductParameterModelsWriteProductParameterGroup.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterGroup**](../../models/ProductParameterModelsWriteProductParameterGroup.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterGroup**](../../models/ProductParameterModelsWriteProductParameterGroup.md) |  | 


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
200 | [ApiResponseFor200](#update_product_parameter_group.ApiResponseFor200) | OK

#### update_product_parameter_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterGroup**](../../models/EnvelopeProductParameterModelsReadProductParameterGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterGroup**](../../models/EnvelopeProductParameterModelsReadProductParameterGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterGroup**](../../models/EnvelopeProductParameterModelsReadProductParameterGroup.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductParameterModelsReadProductParameterGroup**](../../models/EnvelopeProductParameterModelsReadProductParameterGroup.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

