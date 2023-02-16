<a name="__pageTop"></a>
# openapi_client.apis.tags.variant_api.VariantApi

All URIs are relative to *https://mgmtapi.carismar.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_product_to_variant_group**](#add_product_to_variant_group) | **put** /API/VariantGroup/{groupId}/{productId} | Adds a product to an existing group
[**add_product_to_variant_group_by_product_id**](#add_product_to_variant_group_by_product_id) | **put** /API/Variant/{productId1}/{productId2} | Adds a product to an existing group
[**create_variant_group**](#create_variant_group) | **post** /API/VariantGroup | Create a new variant group
[**create_variant_group_with_product**](#create_variant_group_with_product) | **post** /API/Variant/{productId}/VariantGroup | Create a new group for the provided product id
[**delete_variant_group**](#delete_variant_group) | **delete** /API/VariantGroup/{groupId} | Delete an entire variant group
[**delete_variant_group_by_product_id**](#delete_variant_group_by_product_id) | **delete** /API/Variant/{productId}/VariantGroup | Delete an entire variant group
[**get_variant_group**](#get_variant_group) | **get** /API/VariantGroup/{groupId} | Get a specific variant group
[**get_variant_group_by_product_id**](#get_variant_group_by_product_id) | **get** /API/Variant/{productId}/VariantGroup | Get the variant group for the provided id
[**get_variant_labels**](#get_variant_labels) | **get** /API/Variant/Labels | Get all valid variant labels
[**remove_product_from_variant_group**](#remove_product_from_variant_group) | **delete** /API/Variant/{productId} | Remove a product from its variant group
[**update_variant**](#update_variant) | **put** /API/Variant/{productId} | Adds the variant details for the product with the provided ID
[**update_variant_group**](#update_variant_group) | **put** /API/VariantGroup/{groupId} | Updates the settings of a group

# **add_product_to_variant_group**
<a name="add_product_to_variant_group"></a>
> EnvelopeVariantModelsReadVariantGroup add_product_to_variant_group(group_idproduct_idvariant)

Adds a product to an existing group

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import variant_api
from openapi_client.model.envelope_variant_models_read_variant_group import EnvelopeVariantModelsReadVariantGroup
from openapi_client.model.variant_models_write_variant import VariantModelsWriteVariant
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
    api_instance = variant_api.VariantApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': 1,
        'productId': "productId_example",
    }
    query_params = {
    }
    body = [
        VariantModelsWriteVariant(
            label="label_example",
            value="value_example",
        )
    ]
    try:
        # Adds a product to an existing group
        api_response = api_instance.add_product_to_variant_group(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->add_product_to_variant_group: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': 1,
        'productId': "productId_example",
    }
    query_params = {
        'productIdType': 0,
        'include': "include_example",
    }
    body = [
        VariantModelsWriteVariant(
            label="label_example",
            value="value_example",
        )
    ]
    try:
        # Adds a product to an existing group
        api_response = api_instance.add_product_to_variant_group(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->add_product_to_variant_group: %s\n" % e)
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
[**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) |  | 

# SchemaForRequestBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) |  | 

# SchemaForRequestBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) |  | 

# SchemaForRequestBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) |  | 

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) |  | 

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
groupId | GroupIdSchema | | 
productId | ProductIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# ProductIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_product_to_variant_group.ApiResponseFor200) | OK

#### add_product_to_variant_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **add_product_to_variant_group_by_product_id**
<a name="add_product_to_variant_group_by_product_id"></a>
> EnvelopeVariantModelsReadVariantGroup add_product_to_variant_group_by_product_id(product_id1product_id2)

Adds a product to an existing group

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import variant_api
from openapi_client.model.envelope_variant_models_read_variant_group import EnvelopeVariantModelsReadVariantGroup
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
    api_instance = variant_api.VariantApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'productId1': "productId1_example",
        'productId2': "productId2_example",
    }
    query_params = {
    }
    try:
        # Adds a product to an existing group
        api_response = api_instance.add_product_to_variant_group_by_product_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->add_product_to_variant_group_by_product_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'productId1': "productId1_example",
        'productId2': "productId2_example",
    }
    query_params = {
        'productIdType': 0,
        'include': "include_example",
    }
    try:
        # Adds a product to an existing group
        api_response = api_instance.add_product_to_variant_group_by_product_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->add_product_to_variant_group_by_product_id: %s\n" % e)
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
productId1 | ProductId1Schema | | 
productId2 | ProductId2Schema | | 

# ProductId1Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProductId2Schema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#add_product_to_variant_group_by_product_id.ApiResponseFor200) | OK

#### add_product_to_variant_group_by_product_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_variant_group**
<a name="create_variant_group"></a>
> EnvelopeVariantModelsReadVariantGroup create_variant_group(variant_group)

Create a new variant group

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import variant_api
from openapi_client.model.envelope_variant_models_read_variant_group import EnvelopeVariantModelsReadVariantGroup
from openapi_client.model.variant_models_write_variant_group import VariantModelsWriteVariantGroup
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
    api_instance = variant_api.VariantApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = VariantModelsWriteVariantGroup(
        name="name_example",
        collapse_in_lists=True,
        variant_labels=[
            "variant_labels_example"
        ],
        products=[
            ProductModelsWriteProduct(
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
        ],
    )
    try:
        # Create a new variant group
        api_response = api_instance.create_variant_group(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->create_variant_group: %s\n" % e)

    # example passing only optional values
    query_params = {
        'include': "include_example",
    }
    body = VariantModelsWriteVariantGroup(
        name="name_example",
        collapse_in_lists=True,
        variant_labels=[
            "variant_labels_example"
        ],
        products=[
            ProductModelsWriteProduct(
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
        ],
    )
    try:
        # Create a new variant group
        api_response = api_instance.create_variant_group(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->create_variant_group: %s\n" % e)
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
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


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
200 | [ApiResponseFor200](#create_variant_group.ApiResponseFor200) | OK

#### create_variant_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_variant_group_with_product**
<a name="create_variant_group_with_product"></a>
> EnvelopeVariantModelsReadVariantGroup create_variant_group_with_product(product_idvariant_group)

Create a new group for the provided product id

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import variant_api
from openapi_client.model.envelope_variant_models_read_variant_group import EnvelopeVariantModelsReadVariantGroup
from openapi_client.model.variant_models_write_variant_group import VariantModelsWriteVariantGroup
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
    api_instance = variant_api.VariantApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
    }
    body = VariantModelsWriteVariantGroup(
        name="name_example",
        collapse_in_lists=True,
        variant_labels=[
            "variant_labels_example"
        ],
        products=[
            ProductModelsWriteProduct(
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
        ],
    )
    try:
        # Create a new group for the provided product id
        api_response = api_instance.create_variant_group_with_product(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->create_variant_group_with_product: %s\n" % e)

    # example passing only optional values
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
        'productIdType': 0,
        'include': "include_example",
    }
    body = VariantModelsWriteVariantGroup(
        name="name_example",
        collapse_in_lists=True,
        variant_labels=[
            "variant_labels_example"
        ],
        products=[
            ProductModelsWriteProduct(
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
        ],
    )
    try:
        # Create a new group for the provided product id
        api_response = api_instance.create_variant_group_with_product(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->create_variant_group_with_product: %s\n" % e)
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
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


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
200 | [ApiResponseFor200](#create_variant_group_with_product.ApiResponseFor200) | OK

#### create_variant_group_with_product.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_variant_group**
<a name="delete_variant_group"></a>
> EnvelopeVariantModelsReadVariantGroup delete_variant_group(group_id)

Delete an entire variant group

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import variant_api
from openapi_client.model.envelope_variant_models_read_variant_group import EnvelopeVariantModelsReadVariantGroup
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
    api_instance = variant_api.VariantApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': 1,
    }
    try:
        # Delete an entire variant group
        api_response = api_instance.delete_variant_group(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->delete_variant_group: %s\n" % e)
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
groupId | GroupIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_variant_group.ApiResponseFor200) | OK

#### delete_variant_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_variant_group_by_product_id**
<a name="delete_variant_group_by_product_id"></a>
> Envelope delete_variant_group_by_product_id(product_id)

Delete an entire variant group

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import variant_api
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
    api_instance = variant_api.VariantApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
    }
    try:
        # Delete an entire variant group
        api_response = api_instance.delete_variant_group_by_product_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->delete_variant_group_by_product_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
        'productIdType': 0,
    }
    try:
        # Delete an entire variant group
        api_response = api_instance.delete_variant_group_by_product_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->delete_variant_group_by_product_id: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_variant_group_by_product_id.ApiResponseFor200) | OK

#### delete_variant_group_by_product_id.ApiResponseFor200
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

# **get_variant_group**
<a name="get_variant_group"></a>
> EnvelopeVariantModelsReadVariantGroup get_variant_group(group_id)

Get a specific variant group

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import variant_api
from openapi_client.model.envelope_variant_models_read_variant_group import EnvelopeVariantModelsReadVariantGroup
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
    api_instance = variant_api.VariantApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': 1,
    }
    query_params = {
    }
    try:
        # Get a specific variant group
        api_response = api_instance.get_variant_group(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->get_variant_group: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': 1,
    }
    query_params = {
        'include': "include_example",
    }
    try:
        # Get a specific variant group
        api_response = api_instance.get_variant_group(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->get_variant_group: %s\n" % e)
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
groupId | GroupIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_variant_group.ApiResponseFor200) | OK

#### get_variant_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_variant_group_by_product_id**
<a name="get_variant_group_by_product_id"></a>
> EnvelopeVariantModelsReadVariantGroup get_variant_group_by_product_id(product_id)

Get the variant group for the provided id

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import variant_api
from openapi_client.model.envelope_variant_models_read_variant_group import EnvelopeVariantModelsReadVariantGroup
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
    api_instance = variant_api.VariantApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
    }
    try:
        # Get the variant group for the provided id
        api_response = api_instance.get_variant_group_by_product_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->get_variant_group_by_product_id: %s\n" % e)

    # example passing only optional values
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
        'productIdType': 0,
        'include': "include_example",
    }
    try:
        # Get the variant group for the provided id
        api_response = api_instance.get_variant_group_by_product_id(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->get_variant_group_by_product_id: %s\n" % e)
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
200 | [ApiResponseFor200](#get_variant_group_by_product_id.ApiResponseFor200) | OK

#### get_variant_group_by_product_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_variant_labels**
<a name="get_variant_labels"></a>
> EnvelopeString get_variant_labels()

Get all valid variant labels

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import variant_api
from openapi_client.model.envelope_string import EnvelopeString
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
    api_instance = variant_api.VariantApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all valid variant labels
        api_response = api_instance.get_variant_labels()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->get_variant_labels: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_variant_labels.ApiResponseFor200) | OK

#### get_variant_labels.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeString**](../../models/EnvelopeString.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeString**](../../models/EnvelopeString.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeString**](../../models/EnvelopeString.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeString**](../../models/EnvelopeString.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove_product_from_variant_group**
<a name="remove_product_from_variant_group"></a>
> EnvelopeVariantModelsReadVariantGroup remove_product_from_variant_group(product_id)

Remove a product from its variant group

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import variant_api
from openapi_client.model.envelope_variant_models_read_variant_group import EnvelopeVariantModelsReadVariantGroup
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
    api_instance = variant_api.VariantApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
    }
    try:
        # Remove a product from its variant group
        api_response = api_instance.remove_product_from_variant_group(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->remove_product_from_variant_group: %s\n" % e)

    # example passing only optional values
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
        'productIdType': 0,
        'include': "include_example",
    }
    try:
        # Remove a product from its variant group
        api_response = api_instance.remove_product_from_variant_group(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->remove_product_from_variant_group: %s\n" % e)
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
200 | [ApiResponseFor200](#remove_product_from_variant_group.ApiResponseFor200) | OK

#### remove_product_from_variant_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_variant**
<a name="update_variant"></a>
> EnvelopeVariantModelsReadVariant update_variant(product_idvariant)

Adds the variant details for the product with the provided ID

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import variant_api
from openapi_client.model.envelope_variant_models_read_variant import EnvelopeVariantModelsReadVariant
from openapi_client.model.variant_models_write_variant import VariantModelsWriteVariant
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
    api_instance = variant_api.VariantApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
    }
    body = [
        VariantModelsWriteVariant(
            label="label_example",
            value="value_example",
        )
    ]
    try:
        # Adds the variant details for the product with the provided ID
        api_response = api_instance.update_variant(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->update_variant: %s\n" % e)

    # example passing only optional values
    path_params = {
        'productId': "productId_example",
    }
    query_params = {
        'productIdType': 0,
    }
    body = [
        VariantModelsWriteVariant(
            label="label_example",
            value="value_example",
        )
    ]
    try:
        # Adds the variant details for the product with the provided ID
        api_response = api_instance.update_variant(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->update_variant: %s\n" % e)
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
[**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) |  | 

# SchemaForRequestBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) |  | 

# SchemaForRequestBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) |  | 

# SchemaForRequestBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) |  | 

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**]({{complexTypePrefix}}VariantModelsWriteVariant.md) |  | 

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
200 | [ApiResponseFor200](#update_variant.ApiResponseFor200) | OK

#### update_variant.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariant**](../../models/EnvelopeVariantModelsReadVariant.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariant**](../../models/EnvelopeVariantModelsReadVariant.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariant**](../../models/EnvelopeVariantModelsReadVariant.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariant**](../../models/EnvelopeVariantModelsReadVariant.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_variant_group**
<a name="update_variant_group"></a>
> EnvelopeVariantModelsReadVariantGroup update_variant_group(group_idvariant_group)

Updates the settings of a group

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import variant_api
from openapi_client.model.envelope_variant_models_read_variant_group import EnvelopeVariantModelsReadVariantGroup
from openapi_client.model.variant_models_write_variant_group import VariantModelsWriteVariantGroup
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
    api_instance = variant_api.VariantApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': 1,
    }
    query_params = {
    }
    body = VariantModelsWriteVariantGroup(
        name="name_example",
        collapse_in_lists=True,
        variant_labels=[
            "variant_labels_example"
        ],
        products=[
            ProductModelsWriteProduct(
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
        ],
    )
    try:
        # Updates the settings of a group
        api_response = api_instance.update_variant_group(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->update_variant_group: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': 1,
    }
    query_params = {
        'include': "include_example",
    }
    body = VariantModelsWriteVariantGroup(
        name="name_example",
        collapse_in_lists=True,
        variant_labels=[
            "variant_labels_example"
        ],
        products=[
            ProductModelsWriteProduct(
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
        ],
    )
    try:
        # Updates the settings of a group
        api_response = api_instance.update_variant_group(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VariantApi->update_variant_group: %s\n" % e)
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
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**VariantModelsWriteVariantGroup**](../../models/VariantModelsWriteVariantGroup.md) |  | 


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
groupId | GroupIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_variant_group.ApiResponseFor200) | OK

#### update_variant_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeVariantModelsReadVariantGroup**](../../models/EnvelopeVariantModelsReadVariantGroup.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

