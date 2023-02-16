<a name="__pageTop"></a>
# openapi_client.apis.tags.shipping_api.ShippingApi

All URIs are relative to *https://mgmtapi.geins.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_parcel_group**](#create_parcel_group) | **post** /API/Shipping/ParcelGroup | Create a new parcel group
[**query_shipping_options**](#query_shipping_options) | **post** /API/Shipping/Query | Query shipping options

# **create_parcel_group**
<a name="create_parcel_group"></a>
> EnvelopeInt create_parcel_group(parcel_group_options)

Create a new parcel group

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import shipping_api
from openapi_client.model.envelope_int import EnvelopeInt
from openapi_client.model.shipping_models_parcel_group_options import ShippingModelsParcelGroupOptions
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
    api_instance = shipping_api.ShippingApi(api_client)

    # example passing only required values which don't have defaults set
    body = ShippingModelsParcelGroupOptions(
        order_ids=[
            1
        ],
        mark_as_delivered=True,
        signal_captures_created=True,
    )
    try:
        # Create a new parcel group
        api_response = api_instance.create_parcel_group(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ShippingApi->create_parcel_group: %s\n" % e)
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
[**ShippingModelsParcelGroupOptions**](../../models/ShippingModelsParcelGroupOptions.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShippingModelsParcelGroupOptions**](../../models/ShippingModelsParcelGroupOptions.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ShippingModelsParcelGroupOptions**](../../models/ShippingModelsParcelGroupOptions.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ShippingModelsParcelGroupOptions**](../../models/ShippingModelsParcelGroupOptions.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ShippingModelsParcelGroupOptions**](../../models/ShippingModelsParcelGroupOptions.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_parcel_group.ApiResponseFor200) | OK

#### create_parcel_group.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyTextJson, SchemaFor200ResponseBodyApplicationXml, SchemaFor200ResponseBodyTextXml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeInt**](../../models/EnvelopeInt.md) |  | 


# SchemaFor200ResponseBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeInt**](../../models/EnvelopeInt.md) |  | 


# SchemaFor200ResponseBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeInt**](../../models/EnvelopeInt.md) |  | 


# SchemaFor200ResponseBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**EnvelopeInt**](../../models/EnvelopeInt.md) |  | 


### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **query_shipping_options**
<a name="query_shipping_options"></a>
> [ShippingModelsShippingOption] query_shipping_options(shipping_query)

Query shipping options

No response envelope.

### Example

* Api Key Authentication (apiKey):
* Basic Authentication (basicAuth):
```python
import openapi_client
from openapi_client.apis.tags import shipping_api
from openapi_client.model.shipping_models_shipping_query import ShippingModelsShippingQuery
from openapi_client.model.shipping_models_shipping_option import ShippingModelsShippingOption
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
    api_instance = shipping_api.ShippingApi(api_client)

    # example passing only required values which don't have defaults set
    body = ShippingModelsShippingQuery(
        site_id=1,
        country_id=1,
        shipping_id=1,
        delivery_option_id="00000000-0000-0000-0000-000000000000",
        order=OrderCheckoutOrder(
            order_id="order_id_example",
            external_order_id="external_order_id_example",
            cart_id="cart_id_example",
            session_id="session_id_example",
            site_id=1,
            currency="currency_example",
            status="status_example",
            ip_address="ip_address_example",
            message="message_example",
            internal_message="internal_message_example",
            locale="locale_example",
            rows=[
                OrderCheckoutOrderRow(
                    sku="sku_example",
                    product_id=1,
                    external_id="external_id_example",
                    discount_rate=3.14,
                    cart_row_id=1,
                    product_container_build_id=1,
                    message="message_example",
                    article_number="article_number_example",
                    gtin="gtin_example",
                    brand="brand_example",
                    categories=[
                        "categories_example"
                    ],
                    name="name_example",
                    variant="variant_example",
                    quantity=1,
                    price_inc_vat=3.14,
                    price_ex_vat=3.14,
                    expected_total_price_inc_vat=3.14,
                    discount_inc_vat=3.14,
                    discount_ex_vat=3.14,
                    expected_total_discount_inc_vat=3.14,
                    product_url="product_url_example",
                    image_url="image_url_example",
                    weight=1,
                    height=1,
                    width=1,
                    length=1,
,
                    campaign_group_data="campaign_group_data_example",
,
                    product_price_campaign_id=1,
                    product_price_list_id=1,
                )
            ],
            campaign_id=1,
            campaign_code="campaign_code_example",
            campaign_name="campaign_name_example",
,
,
            customer_id=1,
            customer_type_id=1,
            gender=0,
            date_of_birth="1970-01-01T00:00:00.00Z",
            personal_id="personal_id_example",
            user_agent="user_agent_example",
            meta_data=dict(
                "key": "key_example",
            ),
            payment_id=1,
            transaction_id="transaction_id_example",
            secondary_transaction_id="secondary_transaction_id_example",
            country="country_example",
            company="company_example",
            organization_number="organization_number_example",
            first_name="first_name_example",
            last_name="last_name_example",
            email="email_example",
            address1="address1_example",
            address2="address2_example",
            zip="zip_example",
            city="city_example",
            region="region_example",
            phone="phone_example",
            mobile_phone="mobile_phone_example",
            care_of="care_of_example",
            shipping_id=1,
            shipping_country="shipping_country_example",
            shipping_company="shipping_company_example",
            shipping_organization_number="shipping_organization_number_example",
            shipping_first_name="shipping_first_name_example",
            shipping_last_name="shipping_last_name_example",
            shipping_email="shipping_email_example",
            shipping_address1="shipping_address1_example",
            shipping_address2="shipping_address2_example",
            shipping_zip="shipping_zip_example",
            shipping_city="shipping_city_example",
            shipping_region="shipping_region_example",
            shipping_phone="shipping_phone_example",
            shipping_mobile_phone="shipping_mobile_phone_example",
            shipping_care_of="shipping_care_of_example",
            pickup_point="pickup_point_example",
            desired_delivery_date="1970-01-01T00:00:00.00Z",
            freight_class=OrderFreightClass(
                id=1,
                type=1,
                name="name_example",
                type_as_enum=0,
            ),
            sum=3.14,
            expected_sum=3.14,
            order_value_inc_vat=3.14,
            order_value_ex_vat=3.14,
            item_value_inc_vat=3.14,
            item_value_ex_vat=3.14,
            discount_inc_vat=3.14,
            discount_ex_vat=3.14,
            percent_discount=1,
            balance=3.14,
            shipping_fee_inc_vat=3.14,
            shipping_fee_ex_vat=3.14,
            payment_fee_inc_vat=3.14,
            payment_fee_ex_vat=3.14,
        ),
        minimum_free_shipping_limit=3.14,
    )
    try:
        # Query shipping options
        api_response = api_instance.query_shipping_options(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ShippingApi->query_shipping_options: %s\n" % e)
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
[**ShippingModelsShippingQuery**](../../models/ShippingModelsShippingQuery.md) |  | 


# SchemaForRequestBodyTextJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ShippingModelsShippingQuery**](../../models/ShippingModelsShippingQuery.md) |  | 


# SchemaForRequestBodyApplicationXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ShippingModelsShippingQuery**](../../models/ShippingModelsShippingQuery.md) |  | 


# SchemaForRequestBodyTextXml
Type | Description  | Notes
------------- | ------------- | -------------
[**ShippingModelsShippingQuery**](../../models/ShippingModelsShippingQuery.md) |  | 


# SchemaForRequestBodyApplicationXWwwFormUrlencoded
Type | Description  | Notes
------------- | ------------- | -------------
[**ShippingModelsShippingQuery**](../../models/ShippingModelsShippingQuery.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#query_shipping_options.ApiResponseFor200) | OK

#### query_shipping_options.ApiResponseFor200
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
[**ShippingModelsShippingOption**]({{complexTypePrefix}}ShippingModelsShippingOption.md) | [**ShippingModelsShippingOption**]({{complexTypePrefix}}ShippingModelsShippingOption.md) | [**ShippingModelsShippingOption**]({{complexTypePrefix}}ShippingModelsShippingOption.md) |  | 

# SchemaFor200ResponseBodyTextJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShippingModelsShippingOption**]({{complexTypePrefix}}ShippingModelsShippingOption.md) | [**ShippingModelsShippingOption**]({{complexTypePrefix}}ShippingModelsShippingOption.md) | [**ShippingModelsShippingOption**]({{complexTypePrefix}}ShippingModelsShippingOption.md) |  | 

# SchemaFor200ResponseBodyApplicationXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShippingModelsShippingOption**]({{complexTypePrefix}}ShippingModelsShippingOption.md) | [**ShippingModelsShippingOption**]({{complexTypePrefix}}ShippingModelsShippingOption.md) | [**ShippingModelsShippingOption**]({{complexTypePrefix}}ShippingModelsShippingOption.md) |  | 

# SchemaFor200ResponseBodyTextXml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ShippingModelsShippingOption**]({{complexTypePrefix}}ShippingModelsShippingOption.md) | [**ShippingModelsShippingOption**]({{complexTypePrefix}}ShippingModelsShippingOption.md) | [**ShippingModelsShippingOption**]({{complexTypePrefix}}ShippingModelsShippingOption.md) |  | 

### Authorization

[apiKey](../../../README.md#apiKey), [basicAuth](../../../README.md#basicAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

