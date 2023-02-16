# openapi_client.model.product_models_product_query.ProductModelsProductQuery

A prroduct query.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A prroduct query. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**UpdatedAfter** | str, datetime,  | str,  | Limits query to products updated after the specified date. | [optional] value must conform to RFC-3339 date-time
**[ProductIds](#ProductIds)** | list, tuple,  | tuple,  | Limits query to only include the supplied product ids. | [optional] 
**[ArticleNumbers](#ArticleNumbers)** | list, tuple,  | tuple,  | Limits query to only include products with supplied article numbers. | [optional] 
**OnlySellable** | bool,  | BoolClass,  | Limits query to only include products that are available for purchase | [optional] 
**FeedId** | decimal.Decimal, int,  | decimal.Decimal,  | Limits query to only include products contained in the specified feed. | [optional] value must be a 32 bit integer
**BatchId** | str, uuid.UUID,  | str,  | Used to fetch products where the result set is split into batches | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ProductIds

Limits query to only include the supplied product ids.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Limits query to only include the supplied product ids. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# ArticleNumbers

Limits query to only include products with supplied article numbers.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Limits query to only include products with supplied article numbers. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

