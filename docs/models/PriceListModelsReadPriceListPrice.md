# openapi_client.model.price_list_models_read_price_list_price.PriceListModelsReadPriceListPrice

A price for a product on a specific price list.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A price for a product on a specific price list. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ProductId** | decimal.Decimal, int,  | decimal.Decimal,  | The id of the product that this price applies to. | [optional] value must be a 32 bit integer
**PriceListId** | decimal.Decimal, int,  | decimal.Decimal,  | The id of the price list that this price is associated with. | [optional] value must be a 32 bit integer
**PriceListName** | str,  | str,  | The name of the price list that this price is associated with. | [optional] 
**PriceIncVat** | decimal.Decimal, int, float,  | decimal.Decimal,  | The price, inc VAT, in the currency of the associated price list. | [optional] value must be a 64 bit float
**PriceExVat** | decimal.Decimal, int, float,  | decimal.Decimal,  | The price, ex VAT, in the currency of the associated price list. | [optional] value must be a 64 bit float
**VatRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | The Vat Rate | [optional] value must be a 64 bit float
**Country** | str,  | str,  | The 2-letter ISO country code for this price. | [optional] 
**Currency** | str,  | str,  | The 3-letter ISO 4217 currency code for this price. | [optional] 
**StaggeredCount** | decimal.Decimal, int,  | decimal.Decimal,  | Staggered count for this price. Defaults to 1. | [optional] value must be a 32 bit integer
**ValidFrom** | str, datetime,  | str,  | The date the price is valid from. | [optional] value must conform to RFC-3339 date-time
**ValidTo** | str, datetime,  | str,  | The date the price is valid to. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

