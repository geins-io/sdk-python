# openapi_client.model.variant_models_read_variant.VariantModelsReadVariant

A variant of a product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A variant of a product. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ProductId** | decimal.Decimal, int,  | decimal.Decimal,  | The id of the product this variant information belongs to | [optional] value must be a 32 bit integer
**GroupId** | decimal.Decimal, int,  | decimal.Decimal,  | The id of the group this variant belongs to. | [optional] value must be a 32 bit integer
**Label** | str,  | str,  | The name of the variant information, eg \&quot;Weight\&quot;, \&quot;Length\&quot; etc | [optional] 
**Value** | str,  | str,  | The value of the variant information, eg \&quot;250g\&quot;, \&quot;89cm\&quot; etc | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

