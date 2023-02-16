# openapi_client.model.product_parameter_models_write_product_parameter_value.ProductParameterModelsWriteProductParameterValue

A parameter value for a product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A parameter value for a product. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ProductId** | decimal.Decimal, int,  | decimal.Decimal,  | The product id of the parameter. | [optional] value must be a 32 bit integer
**ParameterId** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier of the parameter that this value belongs to. | [optional] value must be a 32 bit integer
**Value** | str,  | str,  | The identifying value of the parameter. | [optional] 
**[LocalizedDescriptions](#LocalizedDescriptions)** | list, tuple,  | tuple,  | The localized descriptions of the parameter. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# LocalizedDescriptions

The localized descriptions of the parameter.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The localized descriptions of the parameter. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

