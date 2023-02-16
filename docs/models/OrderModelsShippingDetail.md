# openapi_client.model.order_models_shipping_detail.OrderModelsShippingDetail

Data carrier for a shipping detail

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data carrier for a shipping detail | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Id** | decimal.Decimal, int,  | decimal.Decimal,  | Unique identifier for this shipping detail | [optional] value must be a 32 bit integer
**ShippingId** | decimal.Decimal, int,  | decimal.Decimal,  | Id of the sipping method | [optional] value must be a 32 bit integer
**Name** | str,  | str,  | Name of the shipping method | [optional] 
**ParcelNumber** | str,  | str,  | Parcel number (tracking number) | [optional] 
**ShippingDate** | str, datetime,  | str,  | Shipping date | [optional] value must conform to RFC-3339 date-time
**TrackingUrl** | str,  | str,  | Tracking URL | [optional] 
**ExternalDeliveryOptionId** | str,  | str,  | Delivery option id of the external shipping provider | [optional] 
**ExternalServiceId** | str,  | str,  | Service id of the external shipping provider | [optional] 
**ExternalCarrierId** | str,  | str,  | Carrier id of the external shipping provider | [optional] 
**PickupPoint** | str,  | str,  | Pickup point | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

