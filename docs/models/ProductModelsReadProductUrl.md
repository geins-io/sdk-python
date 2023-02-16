# openapi_client.model.product_models_read_product_url.ProductModelsReadProductUrl

A canonical product url for a specific market and language.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A canonical product url for a specific market and language. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Url** | str,  | str,  | The canonical url to the product. | [optional] 
**Market** | decimal.Decimal, int,  | decimal.Decimal,  | The market of the url. | [optional] value must be a 32 bit integer
**Language** | str,  | str,  | The language code of the url. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

