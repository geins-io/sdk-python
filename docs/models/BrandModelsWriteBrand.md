# openapi_client.model.brand_models_write_brand.BrandModelsWriteBrand

A brand.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A brand. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Name** | str,  | str,  | The name of this brand. | [optional] 
**ExternalId** | str,  | str,  | External Id of the brand. | [optional] 
**[Descriptions](#Descriptions)** | list, tuple,  | tuple,  | The localized descriptions of the brand. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Descriptions

The localized descriptions of the brand.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The localized descriptions of the brand. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

