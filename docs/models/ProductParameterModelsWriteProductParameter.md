# openapi_client.model.product_parameter_models_write_product_parameter.ProductParameterModelsWriteProductParameter

A product parameter to create or update.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A product parameter to create or update. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ParameterId** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier for the parameter. | [optional] value must be a 32 bit integer
**GroupId** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier of the group that this parameter belongs to. | [optional] value must be a 32 bit integer
**ParameterType** | decimal.Decimal, int,  | decimal.Decimal,  | The type of parameter. | [optional] must be one of [1, 2, 3, 4, 5, 6, 7, ] value must be a 32 bit integer
**Name** | str,  | str,  | The non-localized name of the parameter. | [optional] 
**[LocalizedNames](#LocalizedNames)** | list, tuple,  | tuple,  | The localized names of the parameter. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LocalizedNames

The localized names of the parameter.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The localized names of the parameter. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

