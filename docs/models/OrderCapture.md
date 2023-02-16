# openapi_client.model.order_capture.OrderCapture

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**CaptureId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**OrderPaymentId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**OrderId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**ExternalOrderId** | str,  | str,  |  | [optional] 
**ExternalId** | str,  | str,  |  | [optional] 
**Reference** | str,  | str,  |  | [optional] 
**Description** | str,  | str,  |  | [optional] 
**ProcessedOn** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**CapturedItemTotal** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**CapturedShippingFee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**CapturedPaymentFee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**CapturedDiscount** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**CapturedBalance** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**VatRate** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**TrackingNumber** | str,  | str,  |  | [optional] 
**ShippingName** | str,  | str,  |  | [optional] 
**TrackingUri** | str,  | str,  |  | [optional] 
**ShippingMethod** | str,  | str,  |  | [optional] 
**PaymentName** | str,  | str,  |  | [optional] 
**Locale** | str,  | str,  |  | [optional] 
**[Rows](#Rows)** | list, tuple,  | tuple,  |  | [optional] 
**OrderTransactionId** | str,  | str,  |  | [optional] 
**SecondaryOrderTransactionId** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Rows

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrderCaptureRow**](OrderCaptureRow.md) | [**OrderCaptureRow**](OrderCaptureRow.md) | [**OrderCaptureRow**](OrderCaptureRow.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

