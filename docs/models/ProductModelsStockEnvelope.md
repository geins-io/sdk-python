# openapi_client.model.product_models_stock_envelope.ProductModelsStockEnvelope

The response of a Stock request.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The response of a Stock request. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  | Information about the outcome of the request. | [optional] 
**[Invalid](#Invalid)** | list, tuple,  | tuple,  | Supplied productItemStocks that failed validation. | [optional] 
**[NotFound](#NotFound)** | list, tuple,  | tuple,  | Supplied productItemStocks that were technically valid, but couldn&#x27;t be found. | [optional] 
**UpdateCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of stock updates resulting from the request. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Invalid

Supplied productItemStocks that failed validation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Supplied productItemStocks that failed validation. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteProductItemStock**](ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**](ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**](ProductModelsWriteProductItemStock.md) |  | 

# NotFound

Supplied productItemStocks that were technically valid, but couldn't be found.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Supplied productItemStocks that were technically valid, but couldn&#x27;t be found. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteProductItemStock**](ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**](ProductModelsWriteProductItemStock.md) | [**ProductModelsWriteProductItemStock**](ProductModelsWriteProductItemStock.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

