# openapi_client.model.system_nullable_validation_configuration.SystemNullableValidationConfiguration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LazyLoadConfiguration** | [**PageWidgetLazyLoadSetupLazyLoadConfiguration**](PageWidgetLazyLoadSetupLazyLoadConfiguration.md) | [**PageWidgetLazyLoadSetupLazyLoadConfiguration**](PageWidgetLazyLoadSetupLazyLoadConfiguration.md) |  | [optional] 
**[LazyLoadCollectionConfigurations](#LazyLoadCollectionConfigurations)** | list, tuple,  | tuple,  |  | [optional] 
**[WidgetRestrictions](#WidgetRestrictions)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**ContainerRestrictions** | [**ContainerRestrictionSetupContainerRestrictionConfiguration**](ContainerRestrictionSetupContainerRestrictionConfiguration.md) | [**ContainerRestrictionSetupContainerRestrictionConfiguration**](ContainerRestrictionSetupContainerRestrictionConfiguration.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LazyLoadCollectionConfigurations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PageWidgetLazyLoadSetupLazyLoadCollectionConfiguration**](PageWidgetLazyLoadSetupLazyLoadCollectionConfiguration.md) | [**PageWidgetLazyLoadSetupLazyLoadCollectionConfiguration**](PageWidgetLazyLoadSetupLazyLoadCollectionConfiguration.md) | [**PageWidgetLazyLoadSetupLazyLoadCollectionConfiguration**](PageWidgetLazyLoadSetupLazyLoadCollectionConfiguration.md) |  | 

# WidgetRestrictions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**WidgetRestrictionSetupWidgetRestrictionConfiguration**](WidgetRestrictionSetupWidgetRestrictionConfiguration.md) | [**WidgetRestrictionSetupWidgetRestrictionConfiguration**](WidgetRestrictionSetupWidgetRestrictionConfiguration.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

