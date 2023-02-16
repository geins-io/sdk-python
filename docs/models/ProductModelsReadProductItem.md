# openapi_client.model.product_models_read_product_item.ProductModelsReadProductItem

A product item belonging to a product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A product item belonging to a product. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ItemId** | decimal.Decimal, int,  | decimal.Decimal,  | The product item id. | [optional] value must be a 32 bit integer
**ArticleNumber** | str,  | str,  | The article number for the product item. | [optional] 
**ProductId** | decimal.Decimal, int,  | decimal.Decimal,  | The id of the product that the item belongs to. | [optional] value must be a 32 bit integer
**Name** | str,  | str,  | The name of the product item. | [optional] 
**Shelf** | str,  | str,  | The shelf name where the product item can be found. | [optional] 
**Weight** | decimal.Decimal, int,  | decimal.Decimal,  | The weight of the item in grams (g). | [optional] value must be a 32 bit integer
**Length** | decimal.Decimal, int,  | decimal.Decimal,  | The length of the item in millimeters (mm). | [optional] value must be a 32 bit integer
**Width** | decimal.Decimal, int,  | decimal.Decimal,  | The width of the item in millimeters (mm). | [optional] value must be a 32 bit integer
**Height** | decimal.Decimal, int,  | decimal.Decimal,  | The height of the item in millimeters (mm). | [optional] value must be a 32 bit integer
**Gtin** | str,  | str,  | The GTIN number for the item. | [optional] 
**DateCreated** | str, datetime,  | str,  | The date the item was created. | [optional] value must conform to RFC-3339 date-time
**DateUpdated** | str, datetime,  | str,  | The date the item was last updated. | [optional] value must conform to RFC-3339 date-time
**Active** | bool,  | BoolClass,  | The current state of the item. | [optional] 
**ExternalId** | str,  | str,  | External Id of the product item. | [optional] 
**Stock** | [**ProductModelsReadProductItemStock**](ProductModelsReadProductItemStock.md) | [**ProductModelsReadProductItemStock**](ProductModelsReadProductItemStock.md) |  | [optional] 
**[ShippingFees](#ShippingFees)** | list, tuple,  | tuple,  | The lowest shipping fees for each market and country for the product item. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ShippingFees

The lowest shipping fees for each market and country for the product item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The lowest shipping fees for each market and country for the product item. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsReadShippingFee**](ProductModelsReadShippingFee.md) | [**ProductModelsReadShippingFee**](ProductModelsReadShippingFee.md) | [**ProductModelsReadShippingFee**](ProductModelsReadShippingFee.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

