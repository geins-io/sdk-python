# openapi_client.model.product_models_read_product_item_stock.ProductModelsReadProductItemStock

A stock value for a product item

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A stock value for a product item | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ItemId** | decimal.Decimal, int,  | decimal.Decimal,  | A value to uniquely identity a single product item. | [optional] value must be a 32 bit integer
**Stock** | decimal.Decimal, int,  | decimal.Decimal,  | The physical stock value. | [optional] value must be a 32 bit integer
**StockOversellable** | decimal.Decimal, int,  | decimal.Decimal,  | The oversellable stock value. | [optional] value must be a 32 bit integer
**StockStatic** | decimal.Decimal, int,  | decimal.Decimal,  | The static stock value. | [optional] value must be a 32 bit integer
**StockSellable** | decimal.Decimal, int,  | decimal.Decimal,  | The sellable stock value. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

