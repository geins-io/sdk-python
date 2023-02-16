<a name="__pageTop"></a>
# openapi_client.apis.tags.price_list_api.PriceListApi

All URIs are relative to *https://mgmtapi.geins.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_price_lists**](#list_price_lists) | **get** /API/PriceList/List | Get all price list definitions
[**update_pricelist_prices**](#update_pricelist_prices) | **put** /API/PriceList/Price | Updates price list prices

# **list_price_lists**
<a name="list_price_lists"></a>
> [PriceListModelsPriceList] list_price_lists()

Get all price list definitions

- Prices on campaign price lists (id: xxxxxx2) can not be updated. Any such entries will be ignored.  - ID for Ordinary, Sale and Campaign price lists starts from 1000000.   The ID is calculated by this formula, Market ID * 1000000 + Type of price list (Ordinary=0, Sale=1, Capaign=2)  So :  Ordinary price list for market with ID 1 has ID = 1000000  Sale price list for market with ID 1 has ID = 1000001  Campaign price list for market with ID 1 has ID = 1000002  Ordinary price list for market with ID 2 has ID = 2000000  And so on ...

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import price_list_api
from openapi_client.model.price_list_models_price_list import PriceListModelsPriceList
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
    api_instance = price_list_api.PriceListApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all price list definitions
        api_response = api_instance.list_price_lists()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PriceListApi->list_price_lists: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_price_lists.ApiResponseFor200) | OK

#### list_price_lists.ApiResponseFor200
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
[**PriceListModelsPriceList**]({{complexTypePrefix}}PriceListModelsPriceList.md) | [**PriceListModelsPriceList**]({{complexTypePrefix}}PriceListModelsPriceList.md) | [**PriceListModelsPriceList**]({{complexTypePrefix}}PriceListModelsPriceList.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PriceListModelsPriceList**]({{complexTypePrefix}}PriceListModelsPriceList.md) | [**PriceListModelsPriceList**]({{complexTypePrefix}}PriceListModelsPriceList.md) | [**PriceListModelsPriceList**]({{complexTypePrefix}}PriceListModelsPriceList.md) |  | 

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PriceListModelsPriceList**]({{complexTypePrefix}}PriceListModelsPriceList.md) | [**PriceListModelsPriceList**]({{complexTypePrefix}}PriceListModelsPriceList.md) | [**PriceListModelsPriceList**]({{complexTypePrefix}}PriceListModelsPriceList.md) |  | 

# SchemaFor200ResponseBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PriceListModelsPriceList**]({{complexTypePrefix}}PriceListModelsPriceList.md) | [**PriceListModelsPriceList**]({{complexTypePrefix}}PriceListModelsPriceList.md) | [**PriceListModelsPriceList**]({{complexTypePrefix}}PriceListModelsPriceList.md) |  | 

### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_pricelist_prices**
<a name="update_pricelist_prices"></a>
> PriceListModelsPriceListPriceResponse update_pricelist_prices(price_list_prices)

Updates price list prices

- Prices on campaign price lists (id: xxxxxx2) can not be updated. Any such entries will be ignored.  - ID for Ordinary, Sale and Campaign price lists starts from 1000000.   The ID is calculated by this formula, Market ID * 1000000 + Type of price list (Ordinary=0, Sale=1, Capaign=2)  So :  Ordinary price list for market with ID 1 has ID = 1000000  Sale price list for market with ID 1 has ID = 1000001  Campaign price list for market with ID 1 has ID = 1000002  Ordinary price list for market with ID 2 has ID = 2000000  And so on ...

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import price_list_api
from openapi_client.model.price_list_models_write_price_list_price import PriceListModelsWritePriceListPrice
from openapi_client.model.price_list_models_price_list_price_response import PriceListModelsPriceListPriceResponse
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
    api_instance = price_list_api.PriceListApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = [
        PriceListModelsWritePriceListPrice(
            price_list_id=1,
            price=3.14,
            product_id="product_id_example",
            currency="currency_example",
            staggered_count=1,
        )
    ]
    try:
        # Updates price list prices
        api_response = api_instance.update_pricelist_prices(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PriceListApi->update_pricelist_prices: %s\n" % e)

    # example passing only optional values
    query_params = {
        'productIdType': 0,
        'pricesIncVat': True,
    }
    body = [
        PriceListModelsWritePriceListPrice(
            price_list_id=1,
            price=3.14,
            product_id="product_id_example",
            currency="currency_example",
            staggered_count=1,
        )
    ]
    try:
        # Updates price list prices
        api_response = api_instance.update_pricelist_prices(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PriceListApi->update_pricelist_prices: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextXml, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'text/json', 'application/xml', 'text/xml', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) |  | 

# SchemaForRequestBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) |  | 

# SchemaForRequestBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) |  | 

# SchemaForRequestBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) |  | 

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**]({{complexTypePrefix}}PriceListModelsWritePriceListPrice.md) |  | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productIdType | ProductIdTypeSchema | | optional
pricesIncVat | PricesIncVatSchema | | optional


# ProductIdTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | must be one of [0, 1, 2, 3, ] value must be a 32 bit integer

# PricesIncVatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_pricelist_prices.ApiResponseFor200) | OK

#### update_pricelist_prices.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PriceListModelsPriceListPriceResponse**](../../models/PriceListModelsPriceListPriceResponse.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PriceListModelsPriceListPriceResponse**](../../models/PriceListModelsPriceListPriceResponse.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**PriceListModelsPriceListPriceResponse**](../../models/PriceListModelsPriceListPriceResponse.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**PriceListModelsPriceListPriceResponse**](../../models/PriceListModelsPriceListPriceResponse.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

