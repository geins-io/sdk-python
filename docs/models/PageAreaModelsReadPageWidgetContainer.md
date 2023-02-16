# openapi_client.model.page_area_models_read_page_widget_container.PageAreaModelsReadPageWidgetContainer

This class represents a collection of widgets, and defines how they should be layouted in the area they are rendered in.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This class represents a collection of widgets, and defines how they should be layouted in the area they are rendered in. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Id** | decimal.Decimal, int,  | decimal.Decimal,  | The primary ID of this container | [optional] value must be a 32 bit integer
**Name** | str,  | str,  | The descriptive user defined name of this container, which is used to distinguish this container in a container library | [optional] 
**[ClassNames](#ClassNames)** | list, tuple,  | tuple,  | The CSS class names this container should use. | [optional] 
**Active** | bool,  | BoolClass,  |  | [optional] 
**Layout** | str,  | str,  |  | [optional] 
**ResponsiveMode** | str,  | str,  |  | [optional] 
**Visibility** | str,  | str,  |  | [optional] 
**Design** | str,  | str,  |  | [optional] 
**[Widgets](#Widgets)** | list, tuple,  | tuple,  | The configured widgets held by this container | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ClassNames

The CSS class names this container should use.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The CSS class names this container should use. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Widgets

The configured widgets held by this container

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The configured widgets held by this container | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PageAreaModelsReadPageWidget**](PageAreaModelsReadPageWidget.md) | [**PageAreaModelsReadPageWidget**](PageAreaModelsReadPageWidget.md) | [**PageAreaModelsReadPageWidget**](PageAreaModelsReadPageWidget.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

