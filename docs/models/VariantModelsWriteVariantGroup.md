# openapi_client.model.variant_models_write_variant_group.VariantModelsWriteVariantGroup

A variant group for a collection of related variants.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A variant group for a collection of related variants. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Name** | str,  | str,  | The optional internal name of the variant group. | [optional] 
**CollapseInLists** | bool,  | BoolClass,  | A setting to control the display behaviour in product listings of variants belonging to this group. | [optional] 
**[VariantLabels](#VariantLabels)** | list, tuple,  | tuple,  | The labels of the variant data that this group keeps track of | [optional] 
**[Products](#Products)** | list, tuple,  | tuple,  | Products to be created and connected to the group. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# VariantLabels

The labels of the variant data that this group keeps track of

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The labels of the variant data that this group keeps track of | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Products

Products to be created and connected to the group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Products to be created and connected to the group. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteProduct**](ProductModelsWriteProduct.md) | [**ProductModelsWriteProduct**](ProductModelsWriteProduct.md) | [**ProductModelsWriteProduct**](ProductModelsWriteProduct.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

