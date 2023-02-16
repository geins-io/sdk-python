# openapi_client.model.product_parameter_models_read_product_parameter_group.ProductParameterModelsReadProductParameterGroup

An existing product parameter group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An existing product parameter group. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**GroupId** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier for the groups. | [optional] value must be a 32 bit integer
**Name** | str,  | str,  | The non-localized name of the group. | [optional] 
**[LocalizedNames](#LocalizedNames)** | list, tuple,  | tuple,  | The localized names of the group. | [optional] 
**[ParameterIds](#ParameterIds)** | list, tuple,  | tuple,  | The ids of the parameters belonging to this group. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LocalizedNames

The localized names of the group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The localized names of the group. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) |  | 

# ParameterIds

The ids of the parameters belonging to this group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The ids of the parameters belonging to this group. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

