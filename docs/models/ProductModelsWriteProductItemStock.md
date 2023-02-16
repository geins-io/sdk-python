# openapi_client.model.product_models_write_product_item_stock.ProductModelsWriteProductItemStock

A stock value for a product item

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A stock value for a product item | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Id** | str,  | str,  | A value to uniquely identity a single product item.  &lt;remarks&gt;This value can represent different fields, depending on configuration.&lt;/remarks&gt; | [optional] 
**Stock** | decimal.Decimal, int,  | decimal.Decimal,  | The stock value. | [optional] value must be a 32 bit integer
**StockSellable** | decimal.Decimal, int,  | decimal.Decimal,  | The sellable stock value.  &lt;remarks&gt;This value is read only.&lt;/remarks&gt; | [optional] value must be a 32 bit integer
**StockType** | decimal.Decimal, int,  | decimal.Decimal,  | The type of stock to be updated. See {Product.Models.ProductItemStockType} | [optional] must be one of [0, 1, 2, ] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

