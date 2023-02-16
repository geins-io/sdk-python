# openapi_client.model.order_models_order_update.OrderModelsOrderUpdate

Data carrier for update operation on an order.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data carrier for update operation on an order. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ExternalId** | str,  | str,  | The unique external identifier for this order. | [optional] 
**ParcelNumber** | str,  | str,  | Parcel number (tracking number) | [optional] 
**ExternalOrderStatus** | decimal.Decimal, int,  | decimal.Decimal,  | The external order status | [optional] must be one of [0, 10, 20, 30, 40, ] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

