# openapi_client.model.order_checkout_order.OrderCheckoutOrder

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**OrderId** | str,  | str,  |  | [optional] 
**ExternalOrderId** | str,  | str,  |  | [optional] 
**CartId** | str,  | str,  |  | [optional] 
**SessionId** | str,  | str,  |  | [optional] 
**SiteId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**Currency** | str,  | str,  |  | [optional] 
**Status** | str,  | str,  |  | [optional] 
**IpAddress** | str,  | str,  |  | [optional] 
**Message** | str,  | str,  |  | [optional] 
**InternalMessage** | str,  | str,  |  | [optional] 
**Locale** | str,  | str,  |  | [optional] 
**[Rows](#Rows)** | list, tuple,  | tuple,  |  | [optional] 
**CampaignId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**CampaignCode** | str,  | str,  |  | [optional] 
**CampaignName** | str,  | str,  |  | [optional] 
**[CampaignIds](#CampaignIds)** | list, tuple,  | tuple,  |  | [optional] 
**[CampaignNames](#CampaignNames)** | list, tuple,  | tuple,  |  | [optional] 
**CustomerId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**CustomerTypeId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**Gender** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [0, 1, 2, ] value must be a 32 bit integer
**DateOfBirth** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**PersonalId** | str,  | str,  |  | [optional] 
**UserAgent** | str,  | str,  |  | [optional] 
**[MetaData](#MetaData)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**PaymentId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**TransactionId** | str,  | str,  |  | [optional] 
**SecondaryTransactionId** | str,  | str,  |  | [optional] 
**Country** | str,  | str,  |  | [optional] 
**Company** | str,  | str,  |  | [optional] 
**OrganizationNumber** | str,  | str,  |  | [optional] 
**FirstName** | str,  | str,  |  | [optional] 
**LastName** | str,  | str,  |  | [optional] 
**Email** | str,  | str,  |  | [optional] 
**Address1** | str,  | str,  |  | [optional] 
**Address2** | str,  | str,  |  | [optional] 
**Zip** | str,  | str,  |  | [optional] 
**City** | str,  | str,  |  | [optional] 
**Region** | str,  | str,  |  | [optional] 
**Phone** | str,  | str,  |  | [optional] 
**MobilePhone** | str,  | str,  |  | [optional] 
**CareOf** | str,  | str,  |  | [optional] 
**ShippingId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**ShippingCountry** | str,  | str,  |  | [optional] 
**ShippingCompany** | str,  | str,  |  | [optional] 
**ShippingOrganizationNumber** | str,  | str,  |  | [optional] 
**ShippingFirstName** | str,  | str,  |  | [optional] 
**ShippingLastName** | str,  | str,  |  | [optional] 
**ShippingEmail** | str,  | str,  |  | [optional] 
**ShippingAddress1** | str,  | str,  |  | [optional] 
**ShippingAddress2** | str,  | str,  |  | [optional] 
**ShippingZip** | str,  | str,  |  | [optional] 
**ShippingCity** | str,  | str,  |  | [optional] 
**ShippingRegion** | str,  | str,  |  | [optional] 
**ShippingPhone** | str,  | str,  |  | [optional] 
**ShippingMobilePhone** | str,  | str,  |  | [optional] 
**ShippingCareOf** | str,  | str,  |  | [optional] 
**PickupPoint** | str,  | str,  |  | [optional] 
**DesiredDeliveryDate** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**FreightClass** | [**OrderFreightClass**](OrderFreightClass.md) | [**OrderFreightClass**](OrderFreightClass.md) |  | [optional] 
**Sum** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**ExpectedSum** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**OrderValueIncVat** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**OrderValueExVat** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**ItemValueIncVat** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**ItemValueExVat** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**DiscountIncVat** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**DiscountExVat** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**PercentDiscount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**Balance** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**ShippingFeeIncVat** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**ShippingFeeExVat** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**PaymentFeeIncVat** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**PaymentFeeExVat** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Rows

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OrderCheckoutOrderRow**](OrderCheckoutOrderRow.md) | [**OrderCheckoutOrderRow**](OrderCheckoutOrderRow.md) | [**OrderCheckoutOrderRow**](OrderCheckoutOrderRow.md) |  | 

# CampaignIds

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# CampaignNames

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# MetaData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

