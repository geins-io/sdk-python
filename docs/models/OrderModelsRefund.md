# openapi_client.model.order_models_refund.OrderModelsRefund

Data carrier for a refund

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data carrier for a refund | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Id** | decimal.Decimal, int,  | decimal.Decimal,  | Unique identifier for this refund | [optional] value must be a 32 bit integer
**OrderRowId** | decimal.Decimal, int,  | decimal.Decimal,  | Reference to the order row that has been refunded | [optional] value must be a 32 bit integer
**PaymentDetailId** | decimal.Decimal, int,  | decimal.Decimal,  | Reference to the payment detail that has been refunded | [optional] value must be a 32 bit integer
**ReturnId** | decimal.Decimal, int,  | decimal.Decimal,  | Id number of the return. Can be used to group refunds. | [optional] value must be a 32 bit integer
**ArticleNumber** | str,  | str,  | Article number. If the refund is not bound to an order row this field contains an optional refund article number. | [optional] 
**CreatedAt** | str, datetime,  | str,  | Datetime when the refund was created | [optional] value must conform to RFC-3339 date-time
**Total** | decimal.Decimal, int, float,  | decimal.Decimal,  | Total amount refunded | [optional] value must be a 64 bit float
**ReasonCode** | decimal.Decimal, int,  | decimal.Decimal,  | Reason code for the refund | [optional] value must be a 32 bit integer
**Reason** | str,  | str,  | Reason for refund | [optional] 
**ToBalance** | bool,  | BoolClass,  | Shows if the refund was deposited to the customers balance | [optional] 
**Vat** | decimal.Decimal, int, float,  | decimal.Decimal,  | Vat percent in decimals for the refunded amount | [optional] value must be a 64 bit float
**ItemId** | decimal.Decimal, int,  | decimal.Decimal,  | Item ID (SKU). | [optional] value must be a 32 bit integer
**RefundType** | str,  | str,  | Refund Type | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

