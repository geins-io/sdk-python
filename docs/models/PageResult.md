# openapi_client.model.page_result.PageResult

Contains pagination information for paged operations, i.e. PageSize and PageCount.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Contains pagination information for paged operations, i.e. PageSize and PageCount. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**BatchId** | str, uuid.UUID,  | str,  | The id of the batch operation. If this property has a value for the first fetched page it has to be passed as a parameter for all subsequent requests- | [optional] value must be a uuid
**Page** | decimal.Decimal, int,  | decimal.Decimal,  | The current page | [optional] value must be a 32 bit integer
**RowCount** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of rows | [optional] value must be a 32 bit integer
**PageCount** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of pages | [optional] value must be a 32 bit integer
**PageSize** | decimal.Decimal, int,  | decimal.Decimal,  | Page size | [optional] value must be a 32 bit integer
**HasMoreRows** | bool,  | BoolClass,  | True if there is more content to fetch. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

