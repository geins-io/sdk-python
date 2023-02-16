<a name="__pageTop"></a>
# openapi_client.apis.tags.product_api.ProductApi

All URIs are relative to *https://mgmtapi.carismar.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_availability_monitor**](#add_availability_monitor) | **post** /API/Product/MonitorAvailability | Add a product availability monitor
[**add_category_to_product**](#add_category_to_product) | **put** /API/Product/{productId}/Category | Adds a category relation to a product
[**add_image_to_product**](#add_image_to_product) | **put** /API/Product/{productId}/Image/{imageName} | Adds an image relation to a product
[**add_related_products_to_product**](#add_related_products_to_product) | **put** /API/Product/{productId}/Related | Add related products to a product
[**batch_update_product_items**](#batch_update_product_items) | **put** /API/Product/Items | Updates product items in batch
[**batch_update_stock_values**](#batch_update_stock_values) | **put** /API/Product/Stock | Update stock values for multiple product items
[**create_product**](#create_product) | **post** /API/Product | Create a new product
[**create_product_items**](#create_product_items) | **post** /API/Product/{productId}/Item | Create a new product item
[**get_product_by_id**](#get_product_by_id) | **get** /API/Product/{productId} | Get a specific product
[**get_product_item_by_id**](#get_product_item_by_id) | **get** /API/Product/Item/{itemId} | Get a specific product item
[**link_related_products_by_relation_id**](#link_related_products_by_relation_id) | **put** /API/Product/{productId}/Related/{relationTypeId} | Add related products to a product using a fixed relation type
[**list_all_product_items_paged**](#list_all_product_items_paged) | **get** /API/Product/Items/{page} | Get all product items with pagination
[**list_feeds**](#list_feeds) | **get** /API/Product/Feeds | Gets a list of all feeds
[**list_product_items**](#list_product_items) | **get** /API/Product/Items | Get all product items
[**list_product_relation_types**](#list_product_relation_types) | **get** /API/Product/RelationTypes | Gets a list of product relation types
[**query_products**](#query_products) | **post** /API/Product/Query | Query products
[**query_products_paged**](#query_products_paged) | **post** /API/Product/Query/{page} | Query products with pagination
[**query_stock**](#query_stock) | **post** /API/Product/Stock/Query | Query stock
[**update_product**](#update_product) | **put** /API/Product/{productId} | Updates a product
[**update_product_item**](#update_product_item) | **put** /API/Product/Item/{itemId} | Updates a product item

# **add_availability_monitor**
<a name="add_availability_monitor"></a>
> Envelope add_availability_monitor(model)

Add a product availability monitor

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.product_models_monitor_sku import ProductModelsMonitorSku
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    body = ProductModelsMonitorSku(
        site_id=1,
        language_code="language_code_example",
        email="email_example",
        sku_id=1,
    )
    try:
        # Add a product availability monitor
        api_response = api_instance.add_availability_monitor(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->add_availability_monitor: %s\n" % e)
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
[**ProductModelsMonitorSku**](../../models/ProductModelsMonitorSku.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsMonitorSku**](../../models/ProductModelsMonitorSku.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsMonitorSku**](../../models/ProductModelsMonitorSku.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsMonitorSku**](../../models/ProductModelsMonitorSku.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsMonitorSku**](../../models/ProductModelsMonitorSku.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_availability_monitor.ApiResponseFor200) | OK

#### add_availability_monitor.ApiResponseFor200
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

# **add_category_to_product**
<a name="add_category_to_product"></a>
> Envelope add_category_to_product(product_idproduct_category)

Adds a category relation to a product

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.product_models_product_category import ProductModelsProductCategory
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
    }
    body = ProductModelsProductCategory(
        category_id=1,
    )
    try:
        # Adds a category relation to a product
        api_response = api_instance.add_category_to_product(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->add_category_to_product: %s\n" % e)

    # example passing only optional values
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
        'productIdType': 0,
    }
    body = ProductModelsProductCategory(
        category_id=1,
    )
    try:
        # Adds a category relation to a product
        api_response = api_instance.add_category_to_product(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->add_category_to_product: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextXml, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
query_params | RequestQueryParams | |
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
[**ProductModelsProductCategory**](../../models/ProductModelsProductCategory.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsProductCategory**](../../models/ProductModelsProductCategory.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsProductCategory**](../../models/ProductModelsProductCategory.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsProductCategory**](../../models/ProductModelsProductCategory.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsProductCategory**](../../models/ProductModelsProductCategory.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productIdType | ProductIdTypeSchema | | optional


# ProductIdTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | must be one of [0, 1, 2, 3, ] value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productId | ProductIdSchema | | 

# ProductIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_category_to_product.ApiResponseFor200) | OK

#### add_category_to_product.ApiResponseFor200
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

# **add_image_to_product**
<a name="add_image_to_product"></a>
> Envelope add_image_to_product(product_idimage_name)

Adds an image relation to a product

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'productId': "productId_example",
        'imageName': "imageName_example",
    }
    query_params = {
    }
    try:
        # Adds an image relation to a product
        api_response = api_instance.add_image_to_product(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->add_image_to_product: %s\n" % e)

    # example passing only optional values
    path_params = {
        'productId': "productId_example",
        'imageName': "imageName_example",
    }
    query_params = {
        'isPrimaryImage': True,
        'productIdType': 0,
    }
    try:
        # Adds an image relation to a product
        api_response = api_instance.add_image_to_product(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->add_image_to_product: %s\n" % e)
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
isPrimaryImage | IsPrimaryImageSchema | | optional
productIdType | ProductIdTypeSchema | | optional


# IsPrimaryImageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ProductIdTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | must be one of [0, 1, 2, 3, ] value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productId | ProductIdSchema | | 
imageName | ImageNameSchema | | 

# ProductIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ImageNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_image_to_product.ApiResponseFor200) | OK

#### add_image_to_product.ApiResponseFor200
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

# **add_related_products_to_product**
<a name="add_related_products_to_product"></a>
> ProductModelsRelatedProductEnvelope add_related_products_to_product(product_idrelated_products)

Add related products to a product

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.product_models_related_product_envelope import ProductModelsRelatedProductEnvelope
from openapi_client.model.product_models_write_related_product import ProductModelsWriteRelatedProduct
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
    }
    body = [
        ProductModelsWriteRelatedProduct(
            related_product_id="related_product_id_example",
            relation_type_id=1,
        )
    ]
    try:
        # Add related products to a product
        api_response = api_instance.add_related_products_to_product(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->add_related_products_to_product: %s\n" % e)

    # example passing only optional values
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
        'productIdType': 0,
    }
    body = [
        ProductModelsWriteRelatedProduct(
            related_product_id="related_product_id_example",
            relation_type_id=1,
        )
    ]
    try:
        # Add related products to a product
        api_response = api_instance.add_related_products_to_product(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->add_related_products_to_product: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextXml, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
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
[**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) |  | 

# SchemaForRequestBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) |  | 

# SchemaForRequestBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) |  | 

# SchemaForRequestBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) |  | 

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) |  | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productIdType | ProductIdTypeSchema | | optional


# ProductIdTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | must be one of [0, 1, 2, 3, ] value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productId | ProductIdSchema | | 

# ProductIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_related_products_to_product.ApiResponseFor200) | OK

#### add_related_products_to_product.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsRelatedProductEnvelope**](../../models/ProductModelsRelatedProductEnvelope.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsRelatedProductEnvelope**](../../models/ProductModelsRelatedProductEnvelope.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsRelatedProductEnvelope**](../../models/ProductModelsRelatedProductEnvelope.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsRelatedProductEnvelope**](../../models/ProductModelsRelatedProductEnvelope.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **batch_update_product_items**
<a name="batch_update_product_items"></a>
> Envelope batch_update_product_items(product_items)

Updates product items in batch

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.envelope import Envelope
from openapi_client.model.product_models_write_product_item import ProductModelsWriteProductItem
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = [
        ProductModelsWriteProductItem(
            item_id=1,
            article_number="article_number_example",
            name="name_example",
            shelf="shelf_example",
            weight=1,
            length=1,
            width=1,
            height=1,
            gtin="gtin_example",
            active=True,
            external_id="external_id_example",
        )
    ]
    try:
        # Updates product items in batch
        api_response = api_instance.batch_update_product_items(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->batch_update_product_items: %s\n" % e)

    # example passing only optional values
    query_params = {
        'productItemIdType': 0,
    }
    body = [
        ProductModelsWriteProductItem(
            item_id=1,
            article_number="article_number_example",
            name="name_example",
            shelf="shelf_example",
            weight=1,
            length=1,
            width=1,
            height=1,
            gtin="gtin_example",
            active=True,
            external_id="external_id_example",
        )
    ]
    try:
        # Updates product items in batch
        api_response = api_instance.batch_update_product_items(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->batch_update_product_items: %s\n" % e)
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
[**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) | [**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) | [**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) |  | 

# SchemaForRequestBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) | [**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) | [**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) |  | 

# SchemaForRequestBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) | [**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) | [**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) |  | 

# SchemaForRequestBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) | [**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) | [**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) |  | 

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) | [**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) | [**ProductModelsWriteProductItem**]({{complexTypePrefix}}ProductModelsWriteProductItem.md) |  | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productItemIdType | ProductItemIdTypeSchema | | optional


# ProductItemIdTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | must be one of [0, 1, 2, 3, 4, ] value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#batch_update_product_items.ApiResponseFor200) | OK

#### batch_update_product_items.ApiResponseFor200
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

# **batch_update_stock_values**
<a name="batch_update_stock_values"></a>
> ProductModelsStockEnvelope batch_update_stock_values(product_item_stocks)

Update stock values for multiple product items

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.product_models_stock_envelope import ProductModelsStockEnvelope
from openapi_client.model.product_models_write_product_item_stock import ProductModelsWriteProductItemStock
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = [
        ProductModelsWriteProductItemStock(
            id="id_example",
            stock=1,
            stock_sellable=1,
            stock_type=0,
        )
    ]
    try:
        # Update stock values for multiple product items
        api_response = api_instance.batch_update_stock_values(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->batch_update_stock_values: %s\n" % e)

    # example passing only optional values
    query_params = {
        'productItemIdType': 0,
    }
    body = [
        ProductModelsWriteProductItemStock(
            id="id_example",
            stock=1,
            stock_sellable=1,
            stock_type=0,
        )
    ]
    try:
        # Update stock values for multiple product items
        api_response = api_instance.batch_update_stock_values(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->batch_update_stock_values: %s\n" % e)
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
[**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) |  | 

# SchemaForRequestBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) |  | 

# SchemaForRequestBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) |  | 

# SchemaForRequestBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) |  | 

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**]({{complexTypePrefix}}ProductModelsWriteProductItemStock.md) |  | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productItemIdType | ProductItemIdTypeSchema | | optional


# ProductItemIdTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | must be one of [0, 1, 2, 3, 4, ] value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#batch_update_stock_values.ApiResponseFor200) | OK

#### batch_update_stock_values.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsStockEnvelope**](../../models/ProductModelsStockEnvelope.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsStockEnvelope**](../../models/ProductModelsStockEnvelope.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsStockEnvelope**](../../models/ProductModelsStockEnvelope.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsStockEnvelope**](../../models/ProductModelsStockEnvelope.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_product**
<a name="create_product"></a>
> EnvelopeProductModelsReadProduct create_product(product)

Create a new product

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.product_models_write_product import ProductModelsWriteProduct
from openapi_client.model.envelope_product_models_read_product import EnvelopeProductModelsReadProduct
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = ProductModelsWriteProduct(
        article_number="article_number_example",
        names=[
            SharedModelsLocalizableContent(
                language_code="language_code_example",
                content="content_example",
            )
        ],
        active=True,
        purchase_price=3.14,
        purchase_price_currency="purchase_price_currency_example",
        short_texts=[
            SharedModelsLocalizableContent()
        ],
        long_texts=[
            SharedModelsLocalizableContent()
        ],
        tech_texts=[
            SharedModelsLocalizableContent()
        ],
        brand_id=1,
        supplier_id=1,
        items=[
            ProductModelsWriteProductItem(
                item_id=1,
                article_number="article_number_example",
                name="name_example",
                shelf="shelf_example",
                weight=1,
                length=1,
                width=1,
                height=1,
                gtin="gtin_example",
                active=True,
                external_id="external_id_example",
            )
        ],
        category_ids=[
            1
        ],
        parameter_values=[
            ProductParameterModelsWriteProductParameterValue(
                product_id=1,
                parameter_id=1,
                value="value_example",
                localized_descriptions=[
                    SharedModelsLocalizableContent()
                ],
            )
        ],
        variants=[
            VariantModelsWriteVariant(
                label="label_example",
                value="value_example",
            )
        ],
        markets=[
            MarketModelsMarket(
                id=1,
                name="name_example",
                display_name="display_name_example",
                currency="currency_example",
                vat_rate=3.14,
                market_prefix="market_prefix_example",
                country_id=1,
                currency_id=1,
                currency_rate=3.14,
                language_id=1,
                language="language_example",
            )
        ],
        freight_class_id=1,
        intrastat_code="intrastat_code_example",
        country_of_origin="country_of_origin_example",
        variant_group_id=1,
        vat=1,
        vat_type="vat_type_example",
        external_id="external_id_example",
        activation_date="1970-01-01T00:00:00.00Z",
    )
    try:
        # Create a new product
        api_response = api_instance.create_product(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->create_product: %s\n" % e)

    # example passing only optional values
    query_params = {
        'include': "include_example",
    }
    body = ProductModelsWriteProduct(
        article_number="article_number_example",
        names=[
            SharedModelsLocalizableContent(
                language_code="language_code_example",
                content="content_example",
            )
        ],
        active=True,
        purchase_price=3.14,
        purchase_price_currency="purchase_price_currency_example",
        short_texts=[
            SharedModelsLocalizableContent()
        ],
        long_texts=[
            SharedModelsLocalizableContent()
        ],
        tech_texts=[
            SharedModelsLocalizableContent()
        ],
        brand_id=1,
        supplier_id=1,
        items=[
            ProductModelsWriteProductItem(
                item_id=1,
                article_number="article_number_example",
                name="name_example",
                shelf="shelf_example",
                weight=1,
                length=1,
                width=1,
                height=1,
                gtin="gtin_example",
                active=True,
                external_id="external_id_example",
            )
        ],
        category_ids=[
            1
        ],
        parameter_values=[
            ProductParameterModelsWriteProductParameterValue(
                product_id=1,
                parameter_id=1,
                value="value_example",
                localized_descriptions=[
                    SharedModelsLocalizableContent()
                ],
            )
        ],
        variants=[
            VariantModelsWriteVariant(
                label="label_example",
                value="value_example",
            )
        ],
        markets=[
            MarketModelsMarket(
                id=1,
                name="name_example",
                display_name="display_name_example",
                currency="currency_example",
                vat_rate=3.14,
                market_prefix="market_prefix_example",
                country_id=1,
                currency_id=1,
                currency_rate=3.14,
                language_id=1,
                language="language_example",
            )
        ],
        freight_class_id=1,
        intrastat_code="intrastat_code_example",
        country_of_origin="country_of_origin_example",
        variant_group_id=1,
        vat=1,
        vat_type="vat_type_example",
        external_id="external_id_example",
        activation_date="1970-01-01T00:00:00.00Z",
    )
    try:
        # Create a new product
        api_response = api_instance.create_product(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->create_product: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProduct**](../../models/ProductModelsWriteProduct.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProduct**](../../models/ProductModelsWriteProduct.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProduct**](../../models/ProductModelsWriteProduct.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProduct**](../../models/ProductModelsWriteProduct.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProduct**](../../models/ProductModelsWriteProduct.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
include | IncludeSchema | | optional


# IncludeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_product.ApiResponseFor200) | OK

#### create_product.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProduct**](../../models/EnvelopeProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProduct**](../../models/EnvelopeProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProduct**](../../models/EnvelopeProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProduct**](../../models/EnvelopeProductModelsReadProduct.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_product_items**
<a name="create_product_items"></a>
> EnvelopeProductModelsReadProductItem create_product_items(product_idproduct_item)

Create a new product item

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.envelope_product_models_read_product_item import EnvelopeProductModelsReadProductItem
from openapi_client.model.product_models_write_product_item import ProductModelsWriteProductItem
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
    }
    body = ProductModelsWriteProductItem(
        item_id=1,
        article_number="article_number_example",
        name="name_example",
        shelf="shelf_example",
        weight=1,
        length=1,
        width=1,
        height=1,
        gtin="gtin_example",
        active=True,
        external_id="external_id_example",
    )
    try:
        # Create a new product item
        api_response = api_instance.create_product_items(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->create_product_items: %s\n" % e)

    # example passing only optional values
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
        'productIdType': 0,
    }
    body = ProductModelsWriteProductItem(
        item_id=1,
        article_number="article_number_example",
        name="name_example",
        shelf="shelf_example",
        weight=1,
        length=1,
        width=1,
        height=1,
        gtin="gtin_example",
        active=True,
        external_id="external_id_example",
    )
    try:
        # Create a new product item
        api_response = api_instance.create_product_items(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->create_product_items: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextXml, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
query_params | RequestQueryParams | |
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
[**ProductModelsWriteProductItem**](../../models/ProductModelsWriteProductItem.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProductItem**](../../models/ProductModelsWriteProductItem.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProductItem**](../../models/ProductModelsWriteProductItem.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProductItem**](../../models/ProductModelsWriteProductItem.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProductItem**](../../models/ProductModelsWriteProductItem.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productIdType | ProductIdTypeSchema | | optional


# ProductIdTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | must be one of [0, 1, 2, 3, ] value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productId | ProductIdSchema | | 

# ProductIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_product_items.ApiResponseFor200) | OK

#### create_product_items.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProductItem**](../../models/EnvelopeProductModelsReadProductItem.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProductItem**](../../models/EnvelopeProductModelsReadProductItem.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProductItem**](../../models/EnvelopeProductModelsReadProductItem.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProductItem**](../../models/EnvelopeProductModelsReadProductItem.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_product_by_id**
<a name="get_product_by_id"></a>
> EnvelopeProductModelsReadProduct get_product_by_id(product_id)

Get a specific product

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.envelope_product_models_read_product import EnvelopeProductModelsReadProduct
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
    }
    try:
        # Get a specific product
        api_response = api_instance.get_product_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->get_product_by_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
        'productIdType': 0,
        'include': "include_example",
    }
    try:
        # Get a specific product
        api_response = api_instance.get_product_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->get_product_by_id: %s\n" % e)
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
productIdType | ProductIdTypeSchema | | optional
include | IncludeSchema | | optional


# ProductIdTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | must be one of [0, 1, 2, 3, ] value must be a 32 bit integer

# IncludeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productId | ProductIdSchema | | 

# ProductIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_product_by_id.ApiResponseFor200) | OK

#### get_product_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProduct**](../../models/EnvelopeProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProduct**](../../models/EnvelopeProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProduct**](../../models/EnvelopeProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProduct**](../../models/EnvelopeProductModelsReadProduct.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_product_item_by_id**
<a name="get_product_item_by_id"></a>
> ProductProductItemEnvelope get_product_item_by_id(item_id)

Get a specific product item

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.product_product_item_envelope import ProductProductItemEnvelope
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'itemId': "itemId_example",
    }
    query_params = {
    }
    try:
        # Get a specific product item
        api_response = api_instance.get_product_item_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->get_product_item_by_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'itemId': "itemId_example",
    }
    query_params = {
        'productItemIdType': 0,
    }
    try:
        # Get a specific product item
        api_response = api_instance.get_product_item_by_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->get_product_item_by_id: %s\n" % e)
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
productItemIdType | ProductItemIdTypeSchema | | optional


# ProductItemIdTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | must be one of [0, 1, 2, 3, 4, ] value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
itemId | ItemIdSchema | | 

# ItemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_product_item_by_id.ApiResponseFor200) | OK

#### get_product_item_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductProductItemEnvelope**](../../models/ProductProductItemEnvelope.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductProductItemEnvelope**](../../models/ProductProductItemEnvelope.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductProductItemEnvelope**](../../models/ProductProductItemEnvelope.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductProductItemEnvelope**](../../models/ProductProductItemEnvelope.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **link_related_products_by_relation_id**
<a name="link_related_products_by_relation_id"></a>
> ProductModelsRelatedProductEnvelope link_related_products_by_relation_id(product_idrelation_type_idrelated_products)

Add related products to a product using a fixed relation type

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.product_models_related_product_envelope import ProductModelsRelatedProductEnvelope
from openapi_client.model.product_models_write_related_product import ProductModelsWriteRelatedProduct
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'productId': "productId_example",
        'relationTypeId': 1,
    }
    query_params = {
    }
    body = [
        ProductModelsWriteRelatedProduct(
            related_product_id="related_product_id_example",
            relation_type_id=1,
        )
    ]
    try:
        # Add related products to a product using a fixed relation type
        api_response = api_instance.link_related_products_by_relation_id(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->link_related_products_by_relation_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'productId': "productId_example",
        'relationTypeId': 1,
    }
    query_params = {
        'productIdType': 0,
    }
    body = [
        ProductModelsWriteRelatedProduct(
            related_product_id="related_product_id_example",
            relation_type_id=1,
        )
    ]
    try:
        # Add related products to a product using a fixed relation type
        api_response = api_instance.link_related_products_by_relation_id(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->link_related_products_by_relation_id: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextXml, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
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
[**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) |  | 

# SchemaForRequestBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) |  | 

# SchemaForRequestBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) |  | 

# SchemaForRequestBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) |  | 

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) | [**ProductModelsWriteRelatedProduct**]({{complexTypePrefix}}ProductModelsWriteRelatedProduct.md) |  | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productIdType | ProductIdTypeSchema | | optional


# ProductIdTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | must be one of [0, 1, 2, 3, ] value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productId | ProductIdSchema | | 
relationTypeId | RelationTypeIdSchema | | 

# ProductIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RelationTypeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#link_related_products_by_relation_id.ApiResponseFor200) | OK

#### link_related_products_by_relation_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsRelatedProductEnvelope**](../../models/ProductModelsRelatedProductEnvelope.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsRelatedProductEnvelope**](../../models/ProductModelsRelatedProductEnvelope.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsRelatedProductEnvelope**](../../models/ProductModelsRelatedProductEnvelope.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsRelatedProductEnvelope**](../../models/ProductModelsRelatedProductEnvelope.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_all_product_items_paged**
<a name="list_all_product_items_paged"></a>
> EnvelopeListProductModelsReadProductItem list_all_product_items_paged(page)

Get all product items with pagination

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.envelope_list_product_models_read_product_item import EnvelopeListProductModelsReadProductItem
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'page': 1,
    }
    try:
        # Get all product items with pagination
        api_response = api_instance.list_all_product_items_paged(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->list_all_product_items_paged: %s\n" % e)
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
page | PageSchema | | 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_all_product_items_paged.ApiResponseFor200) | OK

#### list_all_product_items_paged.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadProductItem**](../../models/EnvelopeListProductModelsReadProductItem.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadProductItem**](../../models/EnvelopeListProductModelsReadProductItem.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadProductItem**](../../models/EnvelopeListProductModelsReadProductItem.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadProductItem**](../../models/EnvelopeListProductModelsReadProductItem.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_feeds**
<a name="list_feeds"></a>
> EnvelopeListProductModelsReadFeed list_feeds()

Gets a list of all feeds

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.envelope_list_product_models_read_feed import EnvelopeListProductModelsReadFeed
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
    api_instance = product_api.ProductApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gets a list of all feeds
        api_response = api_instance.list_feeds()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->list_feeds: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_feeds.ApiResponseFor200) | OK

#### list_feeds.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadFeed**](../../models/EnvelopeListProductModelsReadFeed.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadFeed**](../../models/EnvelopeListProductModelsReadFeed.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadFeed**](../../models/EnvelopeListProductModelsReadFeed.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadFeed**](../../models/EnvelopeListProductModelsReadFeed.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_product_items**
<a name="list_product_items"></a>
> [ProductModelsReadProductItem] list_product_items()

Get all product items

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.product_models_read_product_item import ProductModelsReadProductItem
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
    api_instance = product_api.ProductApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all product items
        api_response = api_instance.list_product_items()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->list_product_items: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_product_items.ApiResponseFor200) | OK

#### list_product_items.ApiResponseFor200
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
[**ProductModelsReadProductItem**]({{complexTypePrefix}}ProductModelsReadProductItem.md) | [**ProductModelsReadProductItem**]({{complexTypePrefix}}ProductModelsReadProductItem.md) | [**ProductModelsReadProductItem**]({{complexTypePrefix}}ProductModelsReadProductItem.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsReadProductItem**]({{complexTypePrefix}}ProductModelsReadProductItem.md) | [**ProductModelsReadProductItem**]({{complexTypePrefix}}ProductModelsReadProductItem.md) | [**ProductModelsReadProductItem**]({{complexTypePrefix}}ProductModelsReadProductItem.md) |  | 

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsReadProductItem**]({{complexTypePrefix}}ProductModelsReadProductItem.md) | [**ProductModelsReadProductItem**]({{complexTypePrefix}}ProductModelsReadProductItem.md) | [**ProductModelsReadProductItem**]({{complexTypePrefix}}ProductModelsReadProductItem.md) |  | 

# SchemaFor200ResponseBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsReadProductItem**]({{complexTypePrefix}}ProductModelsReadProductItem.md) | [**ProductModelsReadProductItem**]({{complexTypePrefix}}ProductModelsReadProductItem.md) | [**ProductModelsReadProductItem**]({{complexTypePrefix}}ProductModelsReadProductItem.md) |  | 

### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_product_relation_types**
<a name="list_product_relation_types"></a>
> EnvelopeListProductModelsReadRelationType list_product_relation_types()

Gets a list of product relation types

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.envelope_list_product_models_read_relation_type import EnvelopeListProductModelsReadRelationType
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
    api_instance = product_api.ProductApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Gets a list of product relation types
        api_response = api_instance.list_product_relation_types()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->list_product_relation_types: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_product_relation_types.ApiResponseFor200) | OK

#### list_product_relation_types.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadRelationType**](../../models/EnvelopeListProductModelsReadRelationType.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadRelationType**](../../models/EnvelopeListProductModelsReadRelationType.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadRelationType**](../../models/EnvelopeListProductModelsReadRelationType.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadRelationType**](../../models/EnvelopeListProductModelsReadRelationType.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **query_products**
<a name="query_products"></a>
> EnvelopeListProductModelsReadProduct query_products(query)

Query products

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.envelope_list_product_models_read_product import EnvelopeListProductModelsReadProduct
from openapi_client.model.product_models_product_query import ProductModelsProductQuery
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = ProductModelsProductQuery(
        updated_after="1970-01-01T00:00:00.00Z",
        product_ids=[
            1
        ],
        article_numbers=[
            "article_numbers_example"
        ],
        only_sellable=True,
        feed_id=1,
        batch_id="00000000-0000-0000-0000-000000000000",
    )
    try:
        # Query products
        api_response = api_instance.query_products(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->query_products: %s\n" % e)

    # example passing only optional values
    query_params = {
        'include': "include_example",
    }
    body = ProductModelsProductQuery(
        updated_after="1970-01-01T00:00:00.00Z",
        product_ids=[
            1
        ],
        article_numbers=[
            "article_numbers_example"
        ],
        only_sellable=True,
        feed_id=1,
        batch_id="00000000-0000-0000-0000-000000000000",
    )
    try:
        # Query products
        api_response = api_instance.query_products(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->query_products: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsProductQuery**](../../models/ProductModelsProductQuery.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsProductQuery**](../../models/ProductModelsProductQuery.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsProductQuery**](../../models/ProductModelsProductQuery.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsProductQuery**](../../models/ProductModelsProductQuery.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsProductQuery**](../../models/ProductModelsProductQuery.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
include | IncludeSchema | | optional


# IncludeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#query_products.ApiResponseFor200) | OK

#### query_products.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadProduct**](../../models/EnvelopeListProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadProduct**](../../models/EnvelopeListProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadProduct**](../../models/EnvelopeListProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadProduct**](../../models/EnvelopeListProductModelsReadProduct.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **query_products_paged**
<a name="query_products_paged"></a>
> EnvelopeListProductModelsReadProduct query_products_paged(pagequery)

Query products with pagination

The {Product.Models.ProductQuery.BatchId} property is mandatory when fetching a page other than the first page.  If no BatchId is provided for the first page, a new batch is created and the BatchId can be found in the {Envelope.PageResult} field.

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.envelope_list_product_models_read_product import EnvelopeListProductModelsReadProduct
from openapi_client.model.product_models_product_query import ProductModelsProductQuery
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'page': 1,
    }
    query_params = {
    }
    body = ProductModelsProductQuery(
        updated_after="1970-01-01T00:00:00.00Z",
        product_ids=[
            1
        ],
        article_numbers=[
            "article_numbers_example"
        ],
        only_sellable=True,
        feed_id=1,
        batch_id="00000000-0000-0000-0000-000000000000",
    )
    try:
        # Query products with pagination
        api_response = api_instance.query_products_paged(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->query_products_paged: %s\n" % e)

    # example passing only optional values
    path_params = {
        'page': 1,
    }
    query_params = {
        'include': "include_example",
    }
    body = ProductModelsProductQuery(
        updated_after="1970-01-01T00:00:00.00Z",
        product_ids=[
            1
        ],
        article_numbers=[
            "article_numbers_example"
        ],
        only_sellable=True,
        feed_id=1,
        batch_id="00000000-0000-0000-0000-000000000000",
    )
    try:
        # Query products with pagination
        api_response = api_instance.query_products_paged(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->query_products_paged: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextXml, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
query_params | RequestQueryParams | |
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
[**ProductModelsProductQuery**](../../models/ProductModelsProductQuery.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsProductQuery**](../../models/ProductModelsProductQuery.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsProductQuery**](../../models/ProductModelsProductQuery.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsProductQuery**](../../models/ProductModelsProductQuery.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsProductQuery**](../../models/ProductModelsProductQuery.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
include | IncludeSchema | | optional


# IncludeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
page | PageSchema | | 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#query_products_paged.ApiResponseFor200) | OK

#### query_products_paged.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadProduct**](../../models/EnvelopeListProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadProduct**](../../models/EnvelopeListProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadProduct**](../../models/EnvelopeListProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeListProductModelsReadProduct**](../../models/EnvelopeListProductModelsReadProduct.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **query_stock**
<a name="query_stock"></a>
> [ProductModelsReadProductItemStock] query_stock(product_item_ids)

Query stock

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.product_models_read_product_item_stock import ProductModelsReadProductItemStock
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    body = [
        1
    ]
    try:
        # Query stock
        api_response = api_instance.query_stock(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->query_stock: %s\n" % e)
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

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# SchemaForRequestBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# SchemaForRequestBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# SchemaForRequestBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#query_stock.ApiResponseFor200) | OK

#### query_stock.ApiResponseFor200
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
[**ProductModelsReadProductItemStock**]({{complexTypePrefix}}ProductModelsReadProductItemStock.md) | [**ProductModelsReadProductItemStock**]({{complexTypePrefix}}ProductModelsReadProductItemStock.md) | [**ProductModelsReadProductItemStock**]({{complexTypePrefix}}ProductModelsReadProductItemStock.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsReadProductItemStock**]({{complexTypePrefix}}ProductModelsReadProductItemStock.md) | [**ProductModelsReadProductItemStock**]({{complexTypePrefix}}ProductModelsReadProductItemStock.md) | [**ProductModelsReadProductItemStock**]({{complexTypePrefix}}ProductModelsReadProductItemStock.md) |  | 

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsReadProductItemStock**]({{complexTypePrefix}}ProductModelsReadProductItemStock.md) | [**ProductModelsReadProductItemStock**]({{complexTypePrefix}}ProductModelsReadProductItemStock.md) | [**ProductModelsReadProductItemStock**]({{complexTypePrefix}}ProductModelsReadProductItemStock.md) |  | 

# SchemaFor200ResponseBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsReadProductItemStock**]({{complexTypePrefix}}ProductModelsReadProductItemStock.md) | [**ProductModelsReadProductItemStock**]({{complexTypePrefix}}ProductModelsReadProductItemStock.md) | [**ProductModelsReadProductItemStock**]({{complexTypePrefix}}ProductModelsReadProductItemStock.md) |  | 

### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_product**
<a name="update_product"></a>
> EnvelopeProductModelsReadProduct update_product(product_idproduct)

Updates a product

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.product_models_write_product import ProductModelsWriteProduct
from openapi_client.model.envelope_product_models_read_product import EnvelopeProductModelsReadProduct
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
    }
    body = ProductModelsWriteProduct(
        article_number="article_number_example",
        names=[
            SharedModelsLocalizableContent(
                language_code="language_code_example",
                content="content_example",
            )
        ],
        active=True,
        purchase_price=3.14,
        purchase_price_currency="purchase_price_currency_example",
        short_texts=[
            SharedModelsLocalizableContent()
        ],
        long_texts=[
            SharedModelsLocalizableContent()
        ],
        tech_texts=[
            SharedModelsLocalizableContent()
        ],
        brand_id=1,
        supplier_id=1,
        items=[
            ProductModelsWriteProductItem(
                item_id=1,
                article_number="article_number_example",
                name="name_example",
                shelf="shelf_example",
                weight=1,
                length=1,
                width=1,
                height=1,
                gtin="gtin_example",
                active=True,
                external_id="external_id_example",
            )
        ],
        category_ids=[
            1
        ],
        parameter_values=[
            ProductParameterModelsWriteProductParameterValue(
                product_id=1,
                parameter_id=1,
                value="value_example",
                localized_descriptions=[
                    SharedModelsLocalizableContent()
                ],
            )
        ],
        variants=[
            VariantModelsWriteVariant(
                label="label_example",
                value="value_example",
            )
        ],
        markets=[
            MarketModelsMarket(
                id=1,
                name="name_example",
                display_name="display_name_example",
                currency="currency_example",
                vat_rate=3.14,
                market_prefix="market_prefix_example",
                country_id=1,
                currency_id=1,
                currency_rate=3.14,
                language_id=1,
                language="language_example",
            )
        ],
        freight_class_id=1,
        intrastat_code="intrastat_code_example",
        country_of_origin="country_of_origin_example",
        variant_group_id=1,
        vat=1,
        vat_type="vat_type_example",
        external_id="external_id_example",
        activation_date="1970-01-01T00:00:00.00Z",
    )
    try:
        # Updates a product
        api_response = api_instance.update_product(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->update_product: %s\n" % e)

    # example passing only optional values
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
        'productIdType': 0,
        'include': "include_example",
    }
    body = ProductModelsWriteProduct(
        article_number="article_number_example",
        names=[
            SharedModelsLocalizableContent(
                language_code="language_code_example",
                content="content_example",
            )
        ],
        active=True,
        purchase_price=3.14,
        purchase_price_currency="purchase_price_currency_example",
        short_texts=[
            SharedModelsLocalizableContent()
        ],
        long_texts=[
            SharedModelsLocalizableContent()
        ],
        tech_texts=[
            SharedModelsLocalizableContent()
        ],
        brand_id=1,
        supplier_id=1,
        items=[
            ProductModelsWriteProductItem(
                item_id=1,
                article_number="article_number_example",
                name="name_example",
                shelf="shelf_example",
                weight=1,
                length=1,
                width=1,
                height=1,
                gtin="gtin_example",
                active=True,
                external_id="external_id_example",
            )
        ],
        category_ids=[
            1
        ],
        parameter_values=[
            ProductParameterModelsWriteProductParameterValue(
                product_id=1,
                parameter_id=1,
                value="value_example",
                localized_descriptions=[
                    SharedModelsLocalizableContent()
                ],
            )
        ],
        variants=[
            VariantModelsWriteVariant(
                label="label_example",
                value="value_example",
            )
        ],
        markets=[
            MarketModelsMarket(
                id=1,
                name="name_example",
                display_name="display_name_example",
                currency="currency_example",
                vat_rate=3.14,
                market_prefix="market_prefix_example",
                country_id=1,
                currency_id=1,
                currency_rate=3.14,
                language_id=1,
                language="language_example",
            )
        ],
        freight_class_id=1,
        intrastat_code="intrastat_code_example",
        country_of_origin="country_of_origin_example",
        variant_group_id=1,
        vat=1,
        vat_type="vat_type_example",
        external_id="external_id_example",
        activation_date="1970-01-01T00:00:00.00Z",
    )
    try:
        # Updates a product
        api_response = api_instance.update_product(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->update_product: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextXml, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
query_params | RequestQueryParams | |
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
[**ProductModelsWriteProduct**](../../models/ProductModelsWriteProduct.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProduct**](../../models/ProductModelsWriteProduct.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProduct**](../../models/ProductModelsWriteProduct.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProduct**](../../models/ProductModelsWriteProduct.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProduct**](../../models/ProductModelsWriteProduct.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productIdType | ProductIdTypeSchema | | optional
include | IncludeSchema | | optional


# ProductIdTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | must be one of [0, 1, 2, 3, ] value must be a 32 bit integer

# IncludeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productId | ProductIdSchema | | 

# ProductIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_product.ApiResponseFor200) | OK

#### update_product.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProduct**](../../models/EnvelopeProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProduct**](../../models/EnvelopeProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProduct**](../../models/EnvelopeProductModelsReadProduct.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProduct**](../../models/EnvelopeProductModelsReadProduct.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_product_item**
<a name="update_product_item"></a>
> EnvelopeProductModelsReadProductItem update_product_item(item_idproduct_item)

Updates a product item

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import product_api
from openapi_client.model.envelope_product_models_read_product_item import EnvelopeProductModelsReadProductItem
from openapi_client.model.product_models_write_product_item import ProductModelsWriteProductItem
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
    api_instance = product_api.ProductApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'itemId': "itemId_example",
    }
    query_params = {
    }
    body = ProductModelsWriteProductItem(
        item_id=1,
        article_number="article_number_example",
        name="name_example",
        shelf="shelf_example",
        weight=1,
        length=1,
        width=1,
        height=1,
        gtin="gtin_example",
        active=True,
        external_id="external_id_example",
    )
    try:
        # Updates a product item
        api_response = api_instance.update_product_item(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->update_product_item: %s\n" % e)

    # example passing only optional values
    path_params = {
        'itemId': "itemId_example",
    }
    query_params = {
        'productItemIdType': 0,
    }
    body = ProductModelsWriteProductItem(
        item_id=1,
        article_number="article_number_example",
        name="name_example",
        shelf="shelf_example",
        weight=1,
        length=1,
        width=1,
        height=1,
        gtin="gtin_example",
        active=True,
        external_id="external_id_example",
    )
    try:
        # Updates a product item
        api_response = api_instance.update_product_item(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductApi->update_product_item: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, SchemaForRequestBodyTextJson, SchemaForRequestBodyApplicationXml, SchemaForRequestBodyTextXml, SchemaForRequestBodyApplicationXWwwFormUrlencoded] | required |
query_params | RequestQueryParams | |
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
[**ProductModelsWriteProductItem**](../../models/ProductModelsWriteProductItem.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProductItem**](../../models/ProductModelsWriteProductItem.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProductItem**](../../models/ProductModelsWriteProductItem.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProductItem**](../../models/ProductModelsWriteProductItem.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ProductModelsWriteProductItem**](../../models/ProductModelsWriteProductItem.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
productItemIdType | ProductItemIdTypeSchema | | optional


# ProductItemIdTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | must be one of [0, 1, 2, 3, 4, ] value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
itemId | ItemIdSchema | | 

# ItemIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_product_item.ApiResponseFor200) | OK

#### update_product_item.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProductItem**](../../models/EnvelopeProductModelsReadProductItem.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProductItem**](../../models/EnvelopeProductModelsReadProductItem.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProductItem**](../../models/EnvelopeProductModelsReadProductItem.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeProductModelsReadProductItem**](../../models/EnvelopeProductModelsReadProductItem.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

