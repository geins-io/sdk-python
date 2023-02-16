# openapi_client.model.shipping_models_shipping_query.ShippingModelsShippingQuery

A query to filter shipping options by.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A query to filter shipping options by. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**SiteId** | decimal.Decimal, int,  | decimal.Decimal,  | The site ID the delivery options belong to. Required. | [optional] value must be a 32 bit integer
**CountryId** | decimal.Decimal, int,  | decimal.Decimal,  | The country ID where the order should be shipped to. | [optional] value must be a 32 bit integer
**ShippingId** | decimal.Decimal, int,  | decimal.Decimal,  | Carismar Shipping Option ID | [optional] value must be a 32 bit integer
**DeliveryOptionId** | str, uuid.UUID,  | str,  | Unifaun Delivery Option ID | [optional] value must be a uuid
**Order** | [**OrderCheckoutOrder**](OrderCheckoutOrder.md) | [**OrderCheckoutOrder**](OrderCheckoutOrder.md) |  | [optional] 
**MinimumFreeShippingLimit** | decimal.Decimal, int, float,  | decimal.Decimal,  | The cart sum limit for free shipping - to be used for conditions in the delivery checkout portal | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

