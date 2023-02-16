# openapi_client.model.order_refund.OrderRefund

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**RefundId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**RefundInstanceId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**OrderId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**ExternalOrderId** | str,  | str,  |  | [optional] 
**ExternalId** | str,  | str,  |  | [optional] 
**Reference** | str,  | str,  |  | [optional] 
**Description** | str,  | str,  |  | [optional] 
**ProcessedOn** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**RefundedItemTotal** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**RefundedShippingFee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**RefundedPaymentFee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**RefundedDiscount** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**RefundedBalance** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**VatRate** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
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
[**OrderRefundRow**](OrderRefundRow.md) | [**OrderRefundRow**](OrderRefundRow.md) | [**OrderRefundRow**](OrderRefundRow.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

