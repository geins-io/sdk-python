# openapi_client.model.page_area_models_read_page_widget.PageAreaModelsReadPageWidget

The API-representation of page widgets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The API-representation of page widgets | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Id** | str, uuid.UUID,  | str,  | The IDs of widgets are immutable (determined by each view model implementation, in the namespace Carismar.Core) | [optional] value must be a uuid
**Name** | str,  | str,  | The static name of this widget. Used to translate into icons, or to append to css-classes. | [optional] 
**Type** | str,  | str,  | The name of the widget-type | [optional] 
**Active** | bool,  | BoolClass,  | Decides if this {PageArea.Models.Read.PageWidget} is active or not | [optional] 
**[ClassNames](#ClassNames)** | list, tuple,  | tuple,  | Holds all CSS Class names that this widget should render | [optional] 
**Size** | str,  | str,  | The fractional size for this widget in it&#x27;s container. | [optional] 
**Configuration** | str,  | str,  | The configuration for this {PageArea.Models.Read.PageWidget} | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ClassNames

Holds all CSS Class names that this widget should render

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Holds all CSS Class names that this widget should render | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

