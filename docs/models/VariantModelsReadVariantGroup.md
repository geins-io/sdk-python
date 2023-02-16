# openapi_client.model.variant_models_read_variant_group.VariantModelsReadVariantGroup

A variant group for a collection of related variants.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A variant group for a collection of related variants. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**GroupId** | decimal.Decimal, int,  | decimal.Decimal,  | The id of variant goup. | [optional] value must be a 32 bit integer
**Name** | str,  | str,  | The optional internal name of the variant group. | [optional] 
**CollapseInLists** | bool,  | BoolClass,  | Determine visibility of non-main products of this group in lists. | [optional] 
**MainProductId** | decimal.Decimal, int,  | decimal.Decimal,  | The main product of this group. If the group is collapsed in lists, this will be the only visible product. | [optional] value must be a 32 bit integer
**[ProductIds](#ProductIds)** | list, tuple,  | tuple,  | The product ids of the variants that belong to this group. | [optional] 
**[Products](#Products)** | list, tuple,  | tuple,  | Products belonging to the Variant group. Only included when parameter \&quot;include\&quot; is supplied in the query string | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# ProductIds

The product ids of the variants that belong to this group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The product ids of the variants that belong to this group. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# Products

Products belonging to the Variant group. Only included when parameter \"include\" is supplied in the query string

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Products belonging to the Variant group. Only included when parameter \&quot;include\&quot; is supplied in the query string | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsReadProduct**](ProductModelsReadProduct.md) | [**ProductModelsReadProduct**](ProductModelsReadProduct.md) | [**ProductModelsReadProduct**](ProductModelsReadProduct.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

