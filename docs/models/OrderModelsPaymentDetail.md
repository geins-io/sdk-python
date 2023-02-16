# openapi_client.model.order_models_payment_detail.OrderModelsPaymentDetail

Data carrier for a payment detail

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data carrier for a payment detail | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Id** | decimal.Decimal, int,  | decimal.Decimal,  | Unique identifier for this payment detail. Exception: For some payment options this field can be 0. These orders only have one payment detail. | [optional] value must be a 32 bit integer
**PaymentId** | decimal.Decimal, int,  | decimal.Decimal,  | Payment method id | [optional] value must be a 32 bit integer
**Name** | str,  | str,  | The name of the payment method | [optional] 
**DisplayName** | str,  | str,  | The display name of the payment method | [optional] 
**TransactionId** | str,  | str,  | The transaction id (external reference). | [optional] 
**SecondaryTransactionId** | str,  | str,  | The secondary transaction id, if any (external reference). | [optional] 
**ReservationNumber** | str,  | str,  | The reservation number. This field is not available for all payment methods. | [optional] 
**ReservationDate** | str, datetime,  | str,  | Reservation date | [optional] value must conform to RFC-3339 date-time
**PaymentDate** | str, datetime,  | str,  | Payment date | [optional] value must conform to RFC-3339 date-time
**Total** | decimal.Decimal, int, float,  | decimal.Decimal,  | Total | [optional] value must be a 64 bit float
**Payed** | bool,  | BoolClass,  | Shows if the order is paid using this payment method | [optional] 
**PaymentFee** | decimal.Decimal, int, float,  | decimal.Decimal,  | The payment fee | [optional] value must be a 64 bit float
**ShippingFee** | decimal.Decimal, int, float,  | decimal.Decimal,  | The shipping fee | [optional] value must be a 64 bit float
**PaymentOption** | str,  | str,  | The name of the payment option, if any.  This doesn&#x27;t have to be the same as the payment name. Eg \&quot;Direct bank payment\&quot;, \&quot;Card\&quot;, \&quot;Invoice\&quot; etc. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

