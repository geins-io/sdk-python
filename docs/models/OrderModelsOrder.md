# openapi_client.model.order_models_order.OrderModelsOrder

Data carrier for an order.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data carrier for an order. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier for this order. | [optional] value must be a 32 bit integer
**ExternalId** | str,  | str,  | The unique external identifier for this order. | [optional] 
**PersonalId** | str,  | str,  | The social security number, or organisational number of the customer. | [optional] 
**CustomerId** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier of the customer placing this order. | [optional] value must be a 32 bit integer
**CustomerTypeId** | decimal.Decimal, int,  | decimal.Decimal,  | Customer type. Usually 1 for private customers and 2 for companies. This field is customer specific | [optional] value must be a 32 bit integer
**CreatedAt** | str, datetime,  | str,  | Datetime when the order was created. | [optional] value must conform to RFC-3339 date-time
**UpdatedAt** | str, datetime,  | str,  | Datetime when the order was last updated. | [optional] value must conform to RFC-3339 date-time
**CompletedAt** | str, datetime,  | str,  | The DateTime when the order was completed (delivered, payed). | [optional] value must conform to RFC-3339 date-time
**Status** | str,  | str,  | The order status. Possbile values: cancelled, on-hold, inactive, refunded, partial,  pending-payment, out-of-stock, backorder, completed, pending. | [optional] 
**Currency** | str,  | str,  | ISO Currency code. | [optional] 
**CurrencyRate** | decimal.Decimal, int, float,  | decimal.Decimal,  | The Currency Rate to SEK. | [optional] value must be a 64 bit float
**MarketId** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier for the market this order originates from. | [optional] value must be a 32 bit integer
**MarketName** | str,  | str,  | The market name. Usually this is the equal to the site name. | [optional] 
**Language** | str,  | str,  | Two-letter Language code. | [optional] 
**OrderTotal** | decimal.Decimal, int, float,  | decimal.Decimal,  | Order total. | [optional] value must be a 64 bit float
**ExpectedSum** | decimal.Decimal, int, float,  | decimal.Decimal,  | Expected total sum to be paid after discount and balance.   &lt;para&gt;The value is usually taken directly from the payment provider and represents the actual reserved amount.&lt;/para&gt;&lt;para&gt;If this differs from OrderTotal, actions should be taken to ensure they match. This usually happens due to rounding.&lt;/para&gt; | [optional] value must be a 64 bit float
**VATTotal** | decimal.Decimal, int, float,  | decimal.Decimal,  | Order VAT total. | [optional] value must be a 64 bit float
**OrderValueIncVat** | decimal.Decimal, int, float,  | decimal.Decimal,  | Order value inc vat after discount but before balance | [optional] value must be a 64 bit float
**OrderValueExVat** | decimal.Decimal, int, float,  | decimal.Decimal,  | Order value ex vat after discount but before balance | [optional] value must be a 64 bit float
**ItemValueIncVat** | decimal.Decimal, int, float,  | decimal.Decimal,  | Item value inc vat excluding fees and discount | [optional] value must be a 64 bit float
**ItemValueExVat** | decimal.Decimal, int, float,  | decimal.Decimal,  | Item value ex vat excluding fees and discount | [optional] value must be a 64 bit float
**Discount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Total discount inc vat. | [optional] value must be a 64 bit float
**DiscountExVat** | decimal.Decimal, int, float,  | decimal.Decimal,  | Total discount ex vat. | [optional] value must be a 64 bit float
**FromBalance** | decimal.Decimal, int, float,  | decimal.Decimal,  | The amount which was withdrawn from the customers balance inc vat. | [optional] value must be a 64 bit float
**ShippingFee** | decimal.Decimal, int, float,  | decimal.Decimal,  | Shipping fee inc vat. | [optional] value must be a 64 bit float
**ShippingFeeExVat** | decimal.Decimal, int, float,  | decimal.Decimal,  | Shipping fee ex vat. | [optional] value must be a 64 bit float
**PaymentFee** | decimal.Decimal, int, float,  | decimal.Decimal,  | Payment fee inc vat. | [optional] value must be a 64 bit float
**PaymentFeeExVat** | decimal.Decimal, int, float,  | decimal.Decimal,  | Payment fee ex vat. | [optional] value must be a 64 bit float
**Message** | str,  | str,  | Order message. Can contain instructions from customer or added details about the order. | [optional] 
**[OrderMessages](#OrderMessages)** | list, tuple,  | tuple,  | Internal order messages. Can contain internal details about the order. | [optional] 
**[PaymentDetails](#PaymentDetails)** | list, tuple,  | tuple,  | List of payment details &lt;seealso cref&#x3D;\&quot;T:Order.Models.PaymentDetail\&quot; /&gt;. | [optional] 
**[ShippingDetails](#ShippingDetails)** | list, tuple,  | tuple,  | List of shipping details &lt;seealso cref&#x3D;\&quot;T:Order.Models.ShippingDetail\&quot; /&gt;. | [optional] 
**ShippingAddress** | [**OrderModelsAddress**](OrderModelsAddress.md) | [**OrderModelsAddress**](OrderModelsAddress.md) |  | [optional] 
**BillingAddress** | [**OrderModelsAddress**](OrderModelsAddress.md) | [**OrderModelsAddress**](OrderModelsAddress.md) |  | [optional] 
**[Rows](#Rows)** | list, tuple,  | tuple,  | List of order rows | [optional] 
**[Refunds](#Refunds)** | list, tuple,  | tuple,  | List of order refunds &lt;seealso cref&#x3D;\&quot;T:Order.Models.Refund\&quot; /&gt;. | [optional] 
**Ip** | str,  | str,  | Customer IP-number. | [optional] 
**UserAgent** | str,  | str,  | Customer User Agent. | [optional] 
**ServiceLocation** | str,  | str,  | Chosen service location. | [optional] 
**CampaignCode** | str,  | str,  | Campaign code applied to the order. | [optional] 
**CampaignCodeId** | decimal.Decimal, int,  | decimal.Decimal,  | The internal id of the applied campaign code. | [optional] value must be a 32 bit integer
**Percent** | decimal.Decimal, int,  | decimal.Decimal,  | General percent discount applied to the order. | [optional] value must be a 32 bit integer
**DesiredDeliveryDate** | str, datetime,  | str,  | The desired delivery date of the order. | [optional] value must conform to RFC-3339 date-time
**Gender** | bool,  | BoolClass,  | The gender of the customer. True &#x3D; male, False &#x3D; female, null &#x3D; unknown. | [optional] 
**CartId** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier for the cart from which this order originates. | [optional] value must be a 32 bit integer
**SessionId** | str,  | str,  | The session id for the from which this order originates. | [optional] 
**ExternalOrderStatus** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [0, 10, 20, 30, 40, ] value must be a 32 bit integer
**[CampaignIds](#CampaignIds)** | list, tuple,  | tuple,  | The ids for the campaigns applied to this order (not rows) | [optional] 
**[CampaignNames](#CampaignNames)** | list, tuple,  | tuple,  | The names for the campaigns applied to this order (not rows) | [optional] 
**[MetaData](#MetaData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | The order meta data to store additional information about the order. Eg. customer specific shipping data to include for nShift checkout (former UDC) shipments | [optional] 
**PublicId** | str, uuid.UUID,  | str,  | The public id of this order. | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# OrderMessages

Internal order messages. Can contain internal details about the order.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Internal order messages. Can contain internal details about the order. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# PaymentDetails

List of payment details <seealso cref=\"T:Order.Models.PaymentDetail\" />.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of payment details &lt;seealso cref&#x3D;\&quot;T:Order.Models.PaymentDetail\&quot; /&gt;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrderModelsPaymentDetail**](OrderModelsPaymentDetail.md) | [**OrderModelsPaymentDetail**](OrderModelsPaymentDetail.md) | [**OrderModelsPaymentDetail**](OrderModelsPaymentDetail.md) |  | 

# ShippingDetails

List of shipping details <seealso cref=\"T:Order.Models.ShippingDetail\" />.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of shipping details &lt;seealso cref&#x3D;\&quot;T:Order.Models.ShippingDetail\&quot; /&gt;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrderModelsShippingDetail**](OrderModelsShippingDetail.md) | [**OrderModelsShippingDetail**](OrderModelsShippingDetail.md) | [**OrderModelsShippingDetail**](OrderModelsShippingDetail.md) |  | 

# Rows

List of order rows

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of order rows | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrderModelsOrderRow**](OrderModelsOrderRow.md) | [**OrderModelsOrderRow**](OrderModelsOrderRow.md) | [**OrderModelsOrderRow**](OrderModelsOrderRow.md) |  | 

# Refunds

List of order refunds <seealso cref=\"T:Order.Models.Refund\" />.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of order refunds &lt;seealso cref&#x3D;\&quot;T:Order.Models.Refund\&quot; /&gt;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrderModelsRefund**](OrderModelsRefund.md) | [**OrderModelsRefund**](OrderModelsRefund.md) | [**OrderModelsRefund**](OrderModelsRefund.md) |  | 

# CampaignIds

The ids for the campaigns applied to this order (not rows)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The ids for the campaigns applied to this order (not rows) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# CampaignNames

The names for the campaigns applied to this order (not rows)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The names for the campaigns applied to this order (not rows) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# MetaData

The order meta data to store additional information about the order. Eg. customer specific shipping data to include for nShift checkout (former UDC) shipments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The order meta data to store additional information about the order. Eg. customer specific shipping data to include for nShift checkout (former UDC) shipments | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

