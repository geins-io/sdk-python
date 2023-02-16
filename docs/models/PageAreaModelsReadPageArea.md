# openapi_client.model.page_area_models_read_page_area.PageAreaModelsReadPageArea

The API-version of the PageArea class

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The API-version of the PageArea class | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Index** | decimal.Decimal, int,  | decimal.Decimal,  | The primary id of this page are family collection | [optional] value must be a 32 bit integer
**Name** | str,  | str,  | A descriptive, user-defined name for this page area family collection | [optional] 
**FamilyId** | decimal.Decimal, int,  | decimal.Decimal,  | The family this area belongs to. | [optional] value must be a 32 bit integer
**Settings** | str,  | str,  | The settings that determine how containers can be added to this area. | [optional] 
**[Containers](#Containers)** | list, tuple,  | tuple,  | The containers in this area | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Containers

The containers in this area

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The containers in this area | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PageAreaModelsReadPageWidgetContainer**](PageAreaModelsReadPageWidgetContainer.md) | [**PageAreaModelsReadPageWidgetContainer**](PageAreaModelsReadPageWidgetContainer.md) | [**PageAreaModelsReadPageWidgetContainer**](PageAreaModelsReadPageWidgetContainer.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

