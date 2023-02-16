# openapi_client.model.page_area_models_write_page_area_family.PageAreaModelsWritePageAreaFamily

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**Name** | str,  | str,  |  | [optional] 
**[FilterableProperties](#FilterableProperties)** | list, tuple,  | tuple,  | This page area family has access to the following properties that can be used for filtering, when rendering itself.  &lt;para&gt;  The following properties are available:  SiteId,  LanguageId,  ProductId,  CategoryId,  BrandId,  InfoPageId,  DiscountCampaignNumber,  GenderId,  Sale,  UserTypeId  ActiveFrom,  ActiveTo  &lt;/para&gt; | [optional] 
**[Areas](#Areas)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# FilterableProperties

This page area family has access to the following properties that can be used for filtering, when rendering itself.  <para>  The following properties are available:  SiteId,  LanguageId,  ProductId,  CategoryId,  BrandId,  InfoPageId,  DiscountCampaignNumber,  GenderId,  Sale,  UserTypeId  ActiveFrom,  ActiveTo  </para>

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This page area family has access to the following properties that can be used for filtering, when rendering itself.  &lt;para&gt;  The following properties are available:  SiteId,  LanguageId,  ProductId,  CategoryId,  BrandId,  InfoPageId,  DiscountCampaignNumber,  GenderId,  Sale,  UserTypeId  ActiveFrom,  ActiveTo  &lt;/para&gt; | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# Areas

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PageAreaModelsWritePageArea**](PageAreaModelsWritePageArea.md) | [**PageAreaModelsWritePageArea**](PageAreaModelsWritePageArea.md) | [**PageAreaModelsWritePageArea**](PageAreaModelsWritePageArea.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

