# openapi_client.model.product_models_read_feed.ProductModelsReadFeed

A product feed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A product feed. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**FeedId** | decimal.Decimal, int,  | decimal.Decimal,  | The feed id. | [optional] value must be a 32 bit integer
**Name** | str,  | str,  | The feed name. | [optional] 
**Url** | str,  | str,  | The url to the feed. | [optional] 
**Layout** | str,  | str,  | The name of the feed layout. | [optional] 
**Market** | decimal.Decimal, int,  | decimal.Decimal,  | The market of the feed. | [optional] value must be a 32 bit integer
**Language** | str,  | str,  | The language code of the feed. | [optional] 
**DefaultCurrency** | str,  | str,  | The default currency for the market | [optional] 
**DefaultCountry** | str,  | str,  | The default country for the market | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

