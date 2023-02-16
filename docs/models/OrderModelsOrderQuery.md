# openapi_client.model.order_models_order_query.OrderModelsOrderQuery

Data carrying class for order queries

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data carrying class for order queries | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Updated** | str, datetime,  | str,  | Given a date, only orders updated after the provided date will be returned. | [optional] value must conform to RFC-3339 date-time
**StatusList** | str,  | str,  | Comma separated list of statuses to filter on. | [optional] 
**MarketId** | decimal.Decimal, int,  | decimal.Decimal,  | Id of a market. | [optional] value must be a 32 bit integer
**PaymentName** | str,  | str,  | Name of a payment method | [optional] 
**ParcelGroupId** | decimal.Decimal, int,  | decimal.Decimal,  | Id of a parcel group. | [optional] value must be a 32 bit integer
**CustomerId** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of a customer | [optional] value must be a 32 bit integer
**Email** | str,  | str,  | The email of a customer | [optional] 
**Include** | str,  | str,  | Comma separated list of child-collections to also include in the query result. | [optional] 
**ExternalOrderStatus** | decimal.Decimal, int,  | decimal.Decimal,  | This status can be used by external systems to change the status of an order. Such as failed or done. | [optional] value must be a 32 bit integer
**CombineProductContainerRows** | bool,  | BoolClass,  | If true, will combine all order rows that are part of a container into a single container row. | [optional] 
**PackingLocationId** | decimal.Decimal, int,  | decimal.Decimal,  | The packing place to get orders from. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

