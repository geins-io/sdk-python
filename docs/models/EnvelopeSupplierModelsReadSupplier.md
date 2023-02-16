# openapi_client.model.envelope_supplier_models_read_supplier.EnvelopeSupplierModelsReadSupplier

An envelope for the result of and action taken on a resource.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An envelope for the result of and action taken on a resource. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Message** | str,  | str,  | A status message for the action taken. | [optional] 
**[Details](#Details)** | list, tuple,  | tuple,  | Any validation messages for the data on the current action. | [optional] 
**Resource** | [**SupplierModelsReadSupplier**](SupplierModelsReadSupplier.md) | [**SupplierModelsReadSupplier**](SupplierModelsReadSupplier.md) |  | [optional] 
**PageResult** | [**PageResult**](PageResult.md) | [**PageResult**](PageResult.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Details

Any validation messages for the data on the current action.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Any validation messages for the data on the current action. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

