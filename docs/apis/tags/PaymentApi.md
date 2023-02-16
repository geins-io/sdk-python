<a name="__pageTop"></a>
# openapi_client.apis.tags.payment_api.PaymentApi

All URIs are relative to *https://mgmtapi.geins.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_payment_options**](#query_payment_options) | **post** /API/Payment/Query | Query payment options

# **query_payment_options**
<a name="query_payment_options"></a>
> [PaymentModelsPaymentOption] query_payment_options(query)

Query payment options

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import payment_api
from openapi_client.model.payment_models_payment_option import PaymentModelsPaymentOption
from openapi_client.model.payment_models_payment_option_query import PaymentModelsPaymentOptionQuery
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
    api_instance = payment_api.PaymentApi(api_client)

    # example passing only required values which don't have defaults set
    body = PaymentModelsPaymentOptionQuery(
        site_id=1,
        email="email_example",
        customer_type_id=1,
        country_id=1,
        sum=3.14,
    )
    try:
        # Query payment options
        api_response = api_instance.query_payment_options(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentApi->query_payment_options: %s\n" % e)
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
[**PaymentModelsPaymentOptionQuery**](../../models/PaymentModelsPaymentOptionQuery.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PaymentModelsPaymentOptionQuery**](../../models/PaymentModelsPaymentOptionQuery.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**PaymentModelsPaymentOptionQuery**](../../models/PaymentModelsPaymentOptionQuery.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**PaymentModelsPaymentOptionQuery**](../../models/PaymentModelsPaymentOptionQuery.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**PaymentModelsPaymentOptionQuery**](../../models/PaymentModelsPaymentOptionQuery.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#query_payment_options.ApiResponseFor200) | OK

#### query_payment_options.ApiResponseFor200
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
[**PaymentModelsPaymentOption**]({{complexTypePrefix}}PaymentModelsPaymentOption.md) | [**PaymentModelsPaymentOption**]({{complexTypePrefix}}PaymentModelsPaymentOption.md) | [**PaymentModelsPaymentOption**]({{complexTypePrefix}}PaymentModelsPaymentOption.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PaymentModelsPaymentOption**]({{complexTypePrefix}}PaymentModelsPaymentOption.md) | [**PaymentModelsPaymentOption**]({{complexTypePrefix}}PaymentModelsPaymentOption.md) | [**PaymentModelsPaymentOption**]({{complexTypePrefix}}PaymentModelsPaymentOption.md) |  | 

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PaymentModelsPaymentOption**]({{complexTypePrefix}}PaymentModelsPaymentOption.md) | [**PaymentModelsPaymentOption**]({{complexTypePrefix}}PaymentModelsPaymentOption.md) | [**PaymentModelsPaymentOption**]({{complexTypePrefix}}PaymentModelsPaymentOption.md) |  | 

# SchemaFor200ResponseBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PaymentModelsPaymentOption**]({{complexTypePrefix}}PaymentModelsPaymentOption.md) | [**PaymentModelsPaymentOption**]({{complexTypePrefix}}PaymentModelsPaymentOption.md) | [**PaymentModelsPaymentOption**]({{complexTypePrefix}}PaymentModelsPaymentOption.md) |  | 

### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

