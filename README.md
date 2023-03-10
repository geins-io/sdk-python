# Python SDK for Geins Management API

Geins Management API is an RESTful api to power your applications who manages your geins services. Geins provides an easy-to-use and scalable solution for managing all aspects of an online store, from product listings and customer information to order processing and payment transactions. 

:::tip
With this API, you can build custom applications and integrate with third-party systems, dashboards and other bussiness logic apps.
:::  

## Getting started
Once you have created an account, you can start using the Management API by creating an `API key`. You can create as many API keys as you need. Each `API key` is connected to a specific account so you can keep track of operations and manage keys. You can find your `API key` in the `geins merchant center`. 

### Fast track
Use one of our [SDKs](https://docs.geins.io/docs/sdk/introduction) to get started quickly. The SDKs are available for the most popular programming languages and frameworks.

Or, if you prefer to just take it for a test run:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/25895885-aaf6598f-1a7c-4949-85d7-ba846c42d553?action=collection%2Ffork&collection-url=entityId%3D25895885-aaf6598f-1a7c-4949-85d7-ba846c42d553%26entityType%3Dcollection%26workspaceId%3Da2a179ce-158e-46b0-8d06-e9640f45112c)

### Authentication
Two authentication methods are supported:
  - `API Key`
  - `Basic Auth`


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1.7
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import brand_api
from openapi_client.model.brand_models_brand_query import BrandModelsBrandQuery
from openapi_client.model.brand_models_read_brand import BrandModelsReadBrand
from openapi_client.model.brand_models_write_brand import BrandModelsWriteBrand
from openapi_client.model.envelope_brand_models_read_brand import EnvelopeBrandModelsReadBrand
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
    brand = BrandModelsWriteBrand(
        name="name_example",
        external_id="external_id_example",
        descriptions=[
            SharedModelsLocalizableContent(
                language_code="language_code_example",
                content="content_example",
            )
        ],
    ) # BrandModelsWriteBrand | The brand to create.

    try:
        # Create a new brand
        api_response = api_instance.create_brand(brand)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BrandApi->create_brand: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://mgmtapi.geins.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BrandApi* | [**create_brand**](docs/apis/tags/BrandApi.md#create_brand) | **post** /API/Brand | Create a new brand
*BrandApi* | [**get_brand_by_id**](docs/apis/tags/BrandApi.md#get_brand_by_id) | **get** /API/Brand/{id} | Get a specific brand
*BrandApi* | [**query_brands**](docs/apis/tags/BrandApi.md#query_brands) | **post** /API/Brand/Query | Query brands
*BrandApi* | [**update_brand**](docs/apis/tags/BrandApi.md#update_brand) | **put** /API/Brand/{id} | Updates a brand
*CategoryApi* | [**create_category**](docs/apis/tags/CategoryApi.md#create_category) | **post** /API/Category | Create a new category
*CategoryApi* | [**get_category_by_id**](docs/apis/tags/CategoryApi.md#get_category_by_id) | **get** /API/Category/{id} | Get a specific category
*CategoryApi* | [**query_categories**](docs/apis/tags/CategoryApi.md#query_categories) | **post** /API/Category/Query | Query categories
*CategoryApi* | [**update_category**](docs/apis/tags/CategoryApi.md#update_category) | **put** /API/Category/{id} | Update a category
*MarketApi* | [**get_market_by_id**](docs/apis/tags/MarketApi.md#get_market_by_id) | **get** /API/Market/{marketId} | Get a specific market
*MarketApi* | [**list_markets**](docs/apis/tags/MarketApi.md#list_markets) | **get** /API/Market/List | Gets a list of all markets
*OrderApi* | [**add_comment_to_order**](docs/apis/tags/OrderApi.md#add_comment_to_order) | **post** /API/Order/{id}/Comment | Adds a comment to the order
*OrderApi* | [**create_order**](docs/apis/tags/OrderApi.md#create_order) | **post** /API/Order | Post a new order
*OrderApi* | [**create_order_id**](docs/apis/tags/OrderApi.md#create_order_id) | **post** /API/Order/Id | Create a new order id
*OrderApi* | [**delete_order**](docs/apis/tags/OrderApi.md#delete_order) | **delete** /API/Order/{id} | Deletes or deactivates an order
*OrderApi* | [**get_capture_by_id**](docs/apis/tags/OrderApi.md#get_capture_by_id) | **get** /API/Order/Capture/{captureId} | Get Capture by Id
*OrderApi* | [**get_order_by_id**](docs/apis/tags/OrderApi.md#get_order_by_id) | **get** /API/Order/{id}/{include} | Get an instance of a order
*OrderApi* | [**get_order_statuses**](docs/apis/tags/OrderApi.md#get_order_statuses) | **get** /API/Order/Statuses | Get a list of available order statuses
*OrderApi* | [**get_refund_by_id**](docs/apis/tags/OrderApi.md#get_refund_by_id) | **get** /API/Order/Refund/{refundId} | Get Refund by Id
*OrderApi* | [**partial_update_of_order**](docs/apis/tags/OrderApi.md#partial_update_of_order) | **patch** /API/Order/{id} | Partial update of an order
*OrderApi* | [**query_orders**](docs/apis/tags/OrderApi.md#query_orders) | **post** /API/Order/Query | Query the order repository
*OrderApi* | [**set_capture_as_processed**](docs/apis/tags/OrderApi.md#set_capture_as_processed) | **post** /API/Order/Capture/SetAsProcessed | Set a capture as processed (&#x3D; captured)
*OrderApi* | [**set_payment_as_payed**](docs/apis/tags/OrderApi.md#set_payment_as_payed) | **post** /API/Order/PaymentDetail/{paymentDetailId}/SetAsPayed | Set Payment Detail as payed
*OrderApi* | [**set_refund_as_processed**](docs/apis/tags/OrderApi.md#set_refund_as_processed) | **post** /API/Order/Refund/SetAsProcessed | Set a refund as processed (&#x3D; settled)
*OrderApi* | [**update_order_status**](docs/apis/tags/OrderApi.md#update_order_status) | **post** /API/Order/{id}/Status/{status}/{transactionId}/{secondaryTransactionId} | Update order status
*OrderApi* | [**update_transaction_data**](docs/apis/tags/OrderApi.md#update_transaction_data) | **post** /API/Order/{id}/TransactionData | Updates transaction data on an order
*OrderApi* | [**validate_order**](docs/apis/tags/OrderApi.md#validate_order) | **post** /API/Order/ValidateCreation | Validates order data for order creation.
*PageAreaApi* | [**create_or_update_a_page_area**](docs/apis/tags/PageAreaApi.md#create_or_update_a_page_area) | **post** /API/PageArea | Create or update a page area
*PageAreaApi* | [**create_or_update_page_area_family**](docs/apis/tags/PageAreaApi.md#create_or_update_page_area_family) | **post** /API/PageAreaFamily | Create or update a page area family
*PageAreaApi* | [**get_page_area**](docs/apis/tags/PageAreaApi.md#get_page_area) | **get** /API/PageArea/{name} | Get a specific page area
*PageAreaApi* | [**get_page_area_family**](docs/apis/tags/PageAreaApi.md#get_page_area_family) | **get** /API/PageAreaFamily/{familyId} | Get a specific page area family
*PageAreaApi* | [**list_page_area_families**](docs/apis/tags/PageAreaApi.md#list_page_area_families) | **get** /API/PageAreaFamily/List | Gets a list of all page area families, including nested data
*PaymentApi* | [**query_payment_options**](docs/apis/tags/PaymentApi.md#query_payment_options) | **post** /API/Payment/Query | Query payment options
*PriceListApi* | [**list_price_lists**](docs/apis/tags/PriceListApi.md#list_price_lists) | **get** /API/PriceList/List | Get all price list definitions
*PriceListApi* | [**update_pricelist_prices**](docs/apis/tags/PriceListApi.md#update_pricelist_prices) | **put** /API/PriceList/Price | Updates price list prices
*ProductApi* | [**add_availability_monitor**](docs/apis/tags/ProductApi.md#add_availability_monitor) | **post** /API/Product/MonitorAvailability | Add a product availability monitor
*ProductApi* | [**add_category_to_product**](docs/apis/tags/ProductApi.md#add_category_to_product) | **put** /API/Product/{productId}/Category | Adds a category relation to a product
*ProductApi* | [**add_image_to_product**](docs/apis/tags/ProductApi.md#add_image_to_product) | **put** /API/Product/{productId}/Image/{imageName} | Adds an image relation to a product
*ProductApi* | [**add_related_products_to_product**](docs/apis/tags/ProductApi.md#add_related_products_to_product) | **put** /API/Product/{productId}/Related | Add related products to a product
*ProductApi* | [**batch_update_product_items**](docs/apis/tags/ProductApi.md#batch_update_product_items) | **put** /API/Product/Items | Updates product items in batch
*ProductApi* | [**batch_update_stock_values**](docs/apis/tags/ProductApi.md#batch_update_stock_values) | **put** /API/Product/Stock | Update stock values for multiple product items
*ProductApi* | [**create_product**](docs/apis/tags/ProductApi.md#create_product) | **post** /API/Product | Create a new product
*ProductApi* | [**create_product_items**](docs/apis/tags/ProductApi.md#create_product_items) | **post** /API/Product/{productId}/Item | Create a new product item
*ProductApi* | [**get_product_by_id**](docs/apis/tags/ProductApi.md#get_product_by_id) | **get** /API/Product/{productId} | Get a specific product
*ProductApi* | [**get_product_item_by_id**](docs/apis/tags/ProductApi.md#get_product_item_by_id) | **get** /API/Product/Item/{itemId} | Get a specific product item
*ProductApi* | [**link_related_products_by_relation_id**](docs/apis/tags/ProductApi.md#link_related_products_by_relation_id) | **put** /API/Product/{productId}/Related/{relationTypeId} | Add related products to a product using a fixed relation type
*ProductApi* | [**list_all_product_items_paged**](docs/apis/tags/ProductApi.md#list_all_product_items_paged) | **get** /API/Product/Items/{page} | Get all product items with pagination
*ProductApi* | [**list_feeds**](docs/apis/tags/ProductApi.md#list_feeds) | **get** /API/Product/Feeds | Gets a list of all feeds
*ProductApi* | [**list_product_items**](docs/apis/tags/ProductApi.md#list_product_items) | **get** /API/Product/Items | Get all product items
*ProductApi* | [**list_product_relation_types**](docs/apis/tags/ProductApi.md#list_product_relation_types) | **get** /API/Product/RelationTypes | Gets a list of product relation types
*ProductApi* | [**query_products**](docs/apis/tags/ProductApi.md#query_products) | **post** /API/Product/Query | Query products
*ProductApi* | [**query_products_paged**](docs/apis/tags/ProductApi.md#query_products_paged) | **post** /API/Product/Query/{page} | Query products with pagination
*ProductApi* | [**query_stock**](docs/apis/tags/ProductApi.md#query_stock) | **post** /API/Product/Stock/Query | Query stock
*ProductApi* | [**update_product**](docs/apis/tags/ProductApi.md#update_product) | **put** /API/Product/{productId} | Updates a product
*ProductApi* | [**update_product_item**](docs/apis/tags/ProductApi.md#update_product_item) | **put** /API/Product/Item/{itemId} | Updates a product item
*ProductParameterApi* | [**batch_replace_product_parameter_values**](docs/apis/tags/ProductParameterApi.md#batch_replace_product_parameter_values) | **post** /API/ProductParameter/Values | Replace multiple product parameter values
*ProductParameterApi* | [**batch_update_product_parameter_values**](docs/apis/tags/ProductParameterApi.md#batch_update_product_parameter_values) | **put** /API/ProductParameter/Values | Update multiple product parameter values
*ProductParameterApi* | [**create_or_update_product_parameter_value**](docs/apis/tags/ProductParameterApi.md#create_or_update_product_parameter_value) | **post** /API/ProductParameter/Value | Create or update a new product parameter value
*ProductParameterApi* | [**create_product_parameter**](docs/apis/tags/ProductParameterApi.md#create_product_parameter) | **post** /API/ProductParameter | Create a new product parameter
*ProductParameterApi* | [**create_product_parameter_group**](docs/apis/tags/ProductParameterApi.md#create_product_parameter_group) | **post** /API/ProductParameter/Group | Create a new product parameter group
*ProductParameterApi* | [**create_product_parameter_predefined_value**](docs/apis/tags/ProductParameterApi.md#create_product_parameter_predefined_value) | **post** /API/ProductParameter/PredefinedValue | Create a new predefined value for a product parameter
*ProductParameterApi* | [**get_product_parameter_by_id**](docs/apis/tags/ProductParameterApi.md#get_product_parameter_by_id) | **get** /API/ProductParameter/{id} | Get a specific product parameter
*ProductParameterApi* | [**get_product_parameter_group_by_id**](docs/apis/tags/ProductParameterApi.md#get_product_parameter_group_by_id) | **get** /API/ProductParameter/Group/{id} | Get a specific product parameter group
*ProductParameterApi* | [**get_product_parameter_predefined_value**](docs/apis/tags/ProductParameterApi.md#get_product_parameter_predefined_value) | **get** /API/ProductParameter/PredefinedValue/{id} | Get a specific predefined value for a product parameter
*ProductParameterApi* | [**get_product_parameter_value**](docs/apis/tags/ProductParameterApi.md#get_product_parameter_value) | **get** /API/ProductParameter/Value/{id} | Get a specific product parameter value
*ProductParameterApi* | [**update_product_parameter**](docs/apis/tags/ProductParameterApi.md#update_product_parameter) | **put** /API/ProductParameter/{id} | Updates a product parameter
*ProductParameterApi* | [**update_product_parameter_group**](docs/apis/tags/ProductParameterApi.md#update_product_parameter_group) | **put** /API/ProductParameter/Group/{id} | Update a product parameter group
*ShippingApi* | [**create_parcel_group**](docs/apis/tags/ShippingApi.md#create_parcel_group) | **post** /API/Shipping/ParcelGroup | Create a new parcel group
*ShippingApi* | [**query_shipping_options**](docs/apis/tags/ShippingApi.md#query_shipping_options) | **post** /API/Shipping/Query | Query shipping options
*SupplierApi* | [**create_supplier**](docs/apis/tags/SupplierApi.md#create_supplier) | **post** /API/Supplier | Create a new supplier
*SupplierApi* | [**get_supplier_by_id**](docs/apis/tags/SupplierApi.md#get_supplier_by_id) | **get** /API/Supplier/{id} | Get a specific supplier
*SupplierApi* | [**query_suppliers**](docs/apis/tags/SupplierApi.md#query_suppliers) | **post** /API/Supplier/Query | Query suppliers
*SupplierApi* | [**update_supplier**](docs/apis/tags/SupplierApi.md#update_supplier) | **put** /API/Supplier/{id} | Updates a supplier
*UserApi* | [**create_user_profile**](docs/apis/tags/UserApi.md#create_user_profile) | **post** /API/User | Create user profile
*UserApi* | [**delete_user_profile**](docs/apis/tags/UserApi.md#delete_user_profile) | **delete** /API/User/email | Delete user profile
*UserApi* | [**get_user_profile**](docs/apis/tags/UserApi.md#get_user_profile) | **post** /API/User/Query | Get a specific user profile
*UserApi* | [**update_user_profile**](docs/apis/tags/UserApi.md#update_user_profile) | **put** /API/User | Update user profile
*VariantApi* | [**add_product_to_variant_group**](docs/apis/tags/VariantApi.md#add_product_to_variant_group) | **put** /API/VariantGroup/{groupId}/{productId} | Adds a product to an existing group
*VariantApi* | [**add_product_to_variant_group_by_product_id**](docs/apis/tags/VariantApi.md#add_product_to_variant_group_by_product_id) | **put** /API/Variant/{productId1}/{productId2} | Adds a product to an existing group
*VariantApi* | [**create_variant_group**](docs/apis/tags/VariantApi.md#create_variant_group) | **post** /API/VariantGroup | Create a new variant group
*VariantApi* | [**create_variant_group_with_product**](docs/apis/tags/VariantApi.md#create_variant_group_with_product) | **post** /API/Variant/{productId}/VariantGroup | Create a new group for the provided product id
*VariantApi* | [**delete_variant_group**](docs/apis/tags/VariantApi.md#delete_variant_group) | **delete** /API/VariantGroup/{groupId} | Delete an entire variant group
*VariantApi* | [**delete_variant_group_by_product_id**](docs/apis/tags/VariantApi.md#delete_variant_group_by_product_id) | **delete** /API/Variant/{productId}/VariantGroup | Delete an entire variant group
*VariantApi* | [**get_variant_group**](docs/apis/tags/VariantApi.md#get_variant_group) | **get** /API/VariantGroup/{groupId} | Get a specific variant group
*VariantApi* | [**get_variant_group_by_product_id**](docs/apis/tags/VariantApi.md#get_variant_group_by_product_id) | **get** /API/Variant/{productId}/VariantGroup | Get the variant group for the provided id
*VariantApi* | [**get_variant_labels**](docs/apis/tags/VariantApi.md#get_variant_labels) | **get** /API/Variant/Labels | Get all valid variant labels
*VariantApi* | [**remove_product_from_variant_group**](docs/apis/tags/VariantApi.md#remove_product_from_variant_group) | **delete** /API/Variant/{productId} | Remove a product from its variant group
*VariantApi* | [**update_variant**](docs/apis/tags/VariantApi.md#update_variant) | **put** /API/Variant/{productId} | Adds the variant details for the product with the provided ID
*VariantApi* | [**update_variant_group**](docs/apis/tags/VariantApi.md#update_variant_group) | **put** /API/VariantGroup/{groupId} | Updates the settings of a group

## Documentation For Models

 - [APIOrderOrderComment](docs/models/APIOrderOrderComment.md)
 - [APIOrderTransactionData](docs/models/APIOrderTransactionData.md)
 - [BrandModelsBrandQuery](docs/models/BrandModelsBrandQuery.md)
 - [BrandModelsReadBrand](docs/models/BrandModelsReadBrand.md)
 - [BrandModelsWriteBrand](docs/models/BrandModelsWriteBrand.md)
 - [CategoryModelsCategoryQuery](docs/models/CategoryModelsCategoryQuery.md)
 - [CategoryModelsReadCategory](docs/models/CategoryModelsReadCategory.md)
 - [CategoryModelsWriteCategory](docs/models/CategoryModelsWriteCategory.md)
 - [ContainerRestrictionSetupContainerRestrictionConfiguration](docs/models/ContainerRestrictionSetupContainerRestrictionConfiguration.md)
 - [Envelope](docs/models/Envelope.md)
 - [EnvelopeBrandModelsReadBrand](docs/models/EnvelopeBrandModelsReadBrand.md)
 - [EnvelopeCategoryModelsReadCategory](docs/models/EnvelopeCategoryModelsReadCategory.md)
 - [EnvelopeInt](docs/models/EnvelopeInt.md)
 - [EnvelopeListProductModelsReadFeed](docs/models/EnvelopeListProductModelsReadFeed.md)
 - [EnvelopeListProductModelsReadProduct](docs/models/EnvelopeListProductModelsReadProduct.md)
 - [EnvelopeListProductModelsReadProductItem](docs/models/EnvelopeListProductModelsReadProductItem.md)
 - [EnvelopeListProductModelsReadRelationType](docs/models/EnvelopeListProductModelsReadRelationType.md)
 - [EnvelopeMarketModelsMarket](docs/models/EnvelopeMarketModelsMarket.md)
 - [EnvelopePageAreaModelsReadPageArea](docs/models/EnvelopePageAreaModelsReadPageArea.md)
 - [EnvelopePageAreaModelsReadPageAreaFamily](docs/models/EnvelopePageAreaModelsReadPageAreaFamily.md)
 - [EnvelopeProductModelsReadProduct](docs/models/EnvelopeProductModelsReadProduct.md)
 - [EnvelopeProductModelsReadProductItem](docs/models/EnvelopeProductModelsReadProductItem.md)
 - [EnvelopeProductParameterModelsReadProductParameter](docs/models/EnvelopeProductParameterModelsReadProductParameter.md)
 - [EnvelopeProductParameterModelsReadProductParameterGroup](docs/models/EnvelopeProductParameterModelsReadProductParameterGroup.md)
 - [EnvelopeProductParameterModelsReadProductParameterPredefinedValue](docs/models/EnvelopeProductParameterModelsReadProductParameterPredefinedValue.md)
 - [EnvelopeProductParameterModelsReadProductParameterValue](docs/models/EnvelopeProductParameterModelsReadProductParameterValue.md)
 - [EnvelopeString](docs/models/EnvelopeString.md)
 - [EnvelopeSupplierModelsReadSupplier](docs/models/EnvelopeSupplierModelsReadSupplier.md)
 - [EnvelopeUserModelsReadUserProfile](docs/models/EnvelopeUserModelsReadUserProfile.md)
 - [EnvelopeVariantModelsReadVariant](docs/models/EnvelopeVariantModelsReadVariant.md)
 - [EnvelopeVariantModelsReadVariantGroup](docs/models/EnvelopeVariantModelsReadVariantGroup.md)
 - [MarketModelsMarket](docs/models/MarketModelsMarket.md)
 - [OrderCapture](docs/models/OrderCapture.md)
 - [OrderCaptureRow](docs/models/OrderCaptureRow.md)
 - [OrderCheckoutOrder](docs/models/OrderCheckoutOrder.md)
 - [OrderCheckoutOrderRow](docs/models/OrderCheckoutOrderRow.md)
 - [OrderFreightClass](docs/models/OrderFreightClass.md)
 - [OrderModelsAddress](docs/models/OrderModelsAddress.md)
 - [OrderModelsOrder](docs/models/OrderModelsOrder.md)
 - [OrderModelsOrderQuery](docs/models/OrderModelsOrderQuery.md)
 - [OrderModelsOrderRow](docs/models/OrderModelsOrderRow.md)
 - [OrderModelsOrderStatus](docs/models/OrderModelsOrderStatus.md)
 - [OrderModelsOrderUpdate](docs/models/OrderModelsOrderUpdate.md)
 - [OrderModelsPaymentDetail](docs/models/OrderModelsPaymentDetail.md)
 - [OrderModelsRefund](docs/models/OrderModelsRefund.md)
 - [OrderModelsShippingDetail](docs/models/OrderModelsShippingDetail.md)
 - [OrderProcessedCapture](docs/models/OrderProcessedCapture.md)
 - [OrderProcessedRefund](docs/models/OrderProcessedRefund.md)
 - [OrderRefund](docs/models/OrderRefund.md)
 - [OrderRefundRow](docs/models/OrderRefundRow.md)
 - [OrderValidateOrderCreationRequest](docs/models/OrderValidateOrderCreationRequest.md)
 - [OrderValidateOrderCreationRequestStockItem](docs/models/OrderValidateOrderCreationRequestStockItem.md)
 - [PageAreaModelsReadPageArea](docs/models/PageAreaModelsReadPageArea.md)
 - [PageAreaModelsReadPageAreaFamily](docs/models/PageAreaModelsReadPageAreaFamily.md)
 - [PageAreaModelsReadPageWidget](docs/models/PageAreaModelsReadPageWidget.md)
 - [PageAreaModelsReadPageWidgetContainer](docs/models/PageAreaModelsReadPageWidgetContainer.md)
 - [PageAreaModelsWritePageArea](docs/models/PageAreaModelsWritePageArea.md)
 - [PageAreaModelsWritePageAreaFamily](docs/models/PageAreaModelsWritePageAreaFamily.md)
 - [PageResult](docs/models/PageResult.md)
 - [PageWidgetLazyLoadSetupLazyLoadCollectionConfiguration](docs/models/PageWidgetLazyLoadSetupLazyLoadCollectionConfiguration.md)
 - [PageWidgetLazyLoadSetupLazyLoadConfiguration](docs/models/PageWidgetLazyLoadSetupLazyLoadConfiguration.md)
 - [PaymentModelsPaymentOption](docs/models/PaymentModelsPaymentOption.md)
 - [PaymentModelsPaymentOptionQuery](docs/models/PaymentModelsPaymentOptionQuery.md)
 - [PriceListModelsPriceList](docs/models/PriceListModelsPriceList.md)
 - [PriceListModelsPriceListPriceResponse](docs/models/PriceListModelsPriceListPriceResponse.md)
 - [PriceListModelsReadPriceListPrice](docs/models/PriceListModelsReadPriceListPrice.md)
 - [PriceListModelsWritePriceListPrice](docs/models/PriceListModelsWritePriceListPrice.md)
 - [ProductModelsMonitorSku](docs/models/ProductModelsMonitorSku.md)
 - [ProductModelsProductCategory](docs/models/ProductModelsProductCategory.md)
 - [ProductModelsProductQuery](docs/models/ProductModelsProductQuery.md)
 - [ProductModelsReadFeed](docs/models/ProductModelsReadFeed.md)
 - [ProductModelsReadFeedMembership](docs/models/ProductModelsReadFeedMembership.md)
 - [ProductModelsReadImage](docs/models/ProductModelsReadImage.md)
 - [ProductModelsReadProduct](docs/models/ProductModelsReadProduct.md)
 - [ProductModelsReadProductItem](docs/models/ProductModelsReadProductItem.md)
 - [ProductModelsReadProductItemStock](docs/models/ProductModelsReadProductItemStock.md)
 - [ProductModelsReadProductUrl](docs/models/ProductModelsReadProductUrl.md)
 - [ProductModelsReadRelatedProduct](docs/models/ProductModelsReadRelatedProduct.md)
 - [ProductModelsReadRelationType](docs/models/ProductModelsReadRelationType.md)
 - [ProductModelsReadShippingFee](docs/models/ProductModelsReadShippingFee.md)
 - [ProductModelsRelatedProductEnvelope](docs/models/ProductModelsRelatedProductEnvelope.md)
 - [ProductModelsStockEnvelope](docs/models/ProductModelsStockEnvelope.md)
 - [ProductModelsWriteProduct](docs/models/ProductModelsWriteProduct.md)
 - [ProductModelsWriteProductItem](docs/models/ProductModelsWriteProductItem.md)
 - [ProductModelsWriteProductItemStock](docs/models/ProductModelsWriteProductItemStock.md)
 - [ProductModelsWriteRelatedProduct](docs/models/ProductModelsWriteRelatedProduct.md)
 - [ProductParameterModelsReadProductParameter](docs/models/ProductParameterModelsReadProductParameter.md)
 - [ProductParameterModelsReadProductParameterGroup](docs/models/ProductParameterModelsReadProductParameterGroup.md)
 - [ProductParameterModelsReadProductParameterPredefinedValue](docs/models/ProductParameterModelsReadProductParameterPredefinedValue.md)
 - [ProductParameterModelsReadProductParameterValue](docs/models/ProductParameterModelsReadProductParameterValue.md)
 - [ProductParameterModelsWriteProductParameter](docs/models/ProductParameterModelsWriteProductParameter.md)
 - [ProductParameterModelsWriteProductParameterGroup](docs/models/ProductParameterModelsWriteProductParameterGroup.md)
 - [ProductParameterModelsWriteProductParameterPredefinedValue](docs/models/ProductParameterModelsWriteProductParameterPredefinedValue.md)
 - [ProductParameterModelsWriteProductParameterValue](docs/models/ProductParameterModelsWriteProductParameterValue.md)
 - [ProductParameterModelsWriteProductParameterValueBatch](docs/models/ProductParameterModelsWriteProductParameterValueBatch.md)
 - [ProductProductItemEnvelope](docs/models/ProductProductItemEnvelope.md)
 - [SharedModelsLocalizableContent](docs/models/SharedModelsLocalizableContent.md)
 - [ShippingModelsParcelGroupOptions](docs/models/ShippingModelsParcelGroupOptions.md)
 - [ShippingModelsShippingOption](docs/models/ShippingModelsShippingOption.md)
 - [ShippingModelsShippingQuery](docs/models/ShippingModelsShippingQuery.md)
 - [ShippingModelsShippingSubOption](docs/models/ShippingModelsShippingSubOption.md)
 - [SupplierModelsReadSupplier](docs/models/SupplierModelsReadSupplier.md)
 - [SupplierModelsSupplierQuery](docs/models/SupplierModelsSupplierQuery.md)
 - [SupplierModelsWriteSupplier](docs/models/SupplierModelsWriteSupplier.md)
 - [SystemNullableValidationConfiguration](docs/models/SystemNullableValidationConfiguration.md)
 - [UserModelsReadUserProfile](docs/models/UserModelsReadUserProfile.md)
 - [UserModelsUserProfileQuery](docs/models/UserModelsUserProfileQuery.md)
 - [UserModelsWriteUserProfile](docs/models/UserModelsWriteUserProfile.md)
 - [VariantModelsReadVariant](docs/models/VariantModelsReadVariant.md)
 - [VariantModelsReadVariantGroup](docs/models/VariantModelsReadVariantGroup.md)
 - [VariantModelsWriteVariant](docs/models/VariantModelsWriteVariant.md)
 - [VariantModelsWriteVariantGroup](docs/models/VariantModelsWriteVariantGroup.md)
 - [WidgetRestrictionSetupWidgetRestrictionConfiguration](docs/models/WidgetRestrictionSetupWidgetRestrictionConfiguration.md)

## Documentation For Authorization


## apiKey

- **Type**: API key
- **API key parameter name**: x-apikey
- **Location**: HTTP header

 Authentication schemes defined for the API:
## basicAuth

- **Type**: HTTP basic authentication


## Author















## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.apis.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```
