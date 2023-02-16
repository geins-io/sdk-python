# openapi_client.model.price_list_models_price_list_price_response.PriceListModelsPriceListPriceResponse

The response of a PriceListPrice request.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The response of a PriceListPrice request. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  | Information about the outcome of the request. | [optional] 
**[Invalid](#Invalid)** | list, tuple,  | tuple,  | Supplied PriceList prices that failed validation. | [optional] 
**[NotFound](#NotFound)** | list, tuple,  | tuple,  | Supplied PriceList prices that were technically valid, but couldn&#x27;t be found. | [optional] 
**UpdateCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of price updates resulting from the request. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Invalid

Supplied PriceList prices that failed validation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Supplied PriceList prices that failed validation. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PriceListModelsWritePriceListPrice**](PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**](PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**](PriceListModelsWritePriceListPrice.md) |  | 

# NotFound

Supplied PriceList prices that were technically valid, but couldn't be found.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Supplied PriceList prices that were technically valid, but couldn&#x27;t be found. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PriceListModelsWritePriceListPrice**](PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**](PriceListModelsWritePriceListPrice.md) | [**PriceListModelsWritePriceListPrice**](PriceListModelsWritePriceListPrice.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

