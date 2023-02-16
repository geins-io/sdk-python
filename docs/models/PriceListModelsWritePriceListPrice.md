# openapi_client.model.price_list_models_write_price_list_price.PriceListModelsWritePriceListPrice

A price for a product on a specific price list.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A price for a product on a specific price list. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**PriceListId** | decimal.Decimal, int,  | decimal.Decimal,  | The price list id. | [optional] value must be a 32 bit integer
**Price** | decimal.Decimal, int, float,  | decimal.Decimal,  | The price in the currency of the associated price list. | [optional] value must be a 64 bit float
**ProductId** | str,  | str,  | The id of the product that this price applies to. | [optional] 
**Currency** | str,  | str,  | The 3-letter ISO 4217 currency code for this price. If ommitted the price will be updated on the default market. | [optional] 
**StaggeredCount** | decimal.Decimal, int,  | decimal.Decimal,  | Staggered count for this price. Defaults to 1. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

