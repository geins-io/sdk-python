# openapi_client.model.product_parameter_models_read_product_parameter.ProductParameterModelsReadProductParameter

An existing product parameter.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An existing product parameter. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ParameterId** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier for the parameter. | [optional] value must be a 32 bit integer
**GroupId** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier of the group that this parameter belongs to. | [optional] value must be a 32 bit integer
**GroupName** | str,  | str,  | The name of the group that this parameter belongs to. | [optional] 
**ParameterType** | decimal.Decimal, int,  | decimal.Decimal,  | The type of parameter. | [optional] must be one of [1, 2, 3, 4, 5, 6, 7, ] value must be a 32 bit integer
**Name** | str,  | str,  | The non-localized name of the parameter. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

