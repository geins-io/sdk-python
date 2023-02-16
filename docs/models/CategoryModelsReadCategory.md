# openapi_client.model.category_models_read_category.CategoryModelsReadCategory

An existing category.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An existing category. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**CategoryId** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier for the category. | [optional] value must be a 32 bit integer
**ParentCategoryId** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier for the parent category. | [optional] value must be a 32 bit integer
**[Names](#Names)** | list, tuple,  | tuple,  | The localizable names of the category. | [optional] 
**[Descriptions](#Descriptions)** | list, tuple,  | tuple,  | The localized descriptions of the category. | [optional] 
**GoogleCategoryPath** | str,  | str,  | The Google Taxonomy category path for the category, if any. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Names

The localizable names of the category.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The localizable names of the category. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) |  | 

# Descriptions

The localized descriptions of the category.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The localized descriptions of the category. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

