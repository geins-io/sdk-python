# openapi_client.model.product_models_read_shipping_fee.ProductModelsReadShippingFee

A shipping fee for a product item.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A shipping fee for a product item. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Market** | decimal.Decimal, int,  | decimal.Decimal,  | The market that the shipping fee is applicable on. | [optional] value must be a 32 bit integer
**Country** | str,  | str,  | The country that the shipping fee is applicable in. | [optional] 
**Service** | str,  | str,  | The shipping service with the current fee. | [optional] 
**ServiceId** | decimal.Decimal, int,  | decimal.Decimal,  | The shipping service id with the current fee. | [optional] value must be a 32 bit integer
**Fee** | decimal.Decimal, int, float,  | decimal.Decimal,  | The shipping fee. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

