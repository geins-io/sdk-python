# openapi_client.model.product_models_write_product.ProductModelsWriteProduct

A product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A product. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ArticleNumber** | str,  | str,  | The article number of the product. | [optional] 
**[Names](#Names)** | list, tuple,  | tuple,  | The localized names of the product. | [optional] 
**Active** | bool,  | BoolClass,  | The current state of the product. | [optional] 
**PurchasePrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | The purchase price in the currency defined in {Product.Models.Write.Product.PurchasePriceCurrency}. | [optional] value must be a 64 bit float
**PurchasePriceCurrency** | str,  | str,  | The 3-letter ISO 4217 currency code for the amount given in {Product.Models.Write.Product.PurchasePrice}. | [optional] 
**[ShortTexts](#ShortTexts)** | list, tuple,  | tuple,  | Localized short texts for the product. | [optional] 
**[LongTexts](#LongTexts)** | list, tuple,  | tuple,  | Localized long texts for the product. | [optional] 
**[TechTexts](#TechTexts)** | list, tuple,  | tuple,  | Localized tech texts for the product. | [optional] 
**BrandId** | decimal.Decimal, int,  | decimal.Decimal,  | The brand of the product. | [optional] value must be a 32 bit integer
**SupplierId** | decimal.Decimal, int,  | decimal.Decimal,  | The supplier id of the product. | [optional] value must be a 32 bit integer
**[Items](#Items)** | list, tuple,  | tuple,  | The items belonging to the product. | [optional] 
**[CategoryIds](#CategoryIds)** | list, tuple,  | tuple,  | The category ids the product belongs to. | [optional] 
**[ParameterValues](#ParameterValues)** | list, tuple,  | tuple,  | The parameter values associated with the product. | [optional] 
**[Variants](#Variants)** | list, tuple,  | tuple,  | The variants for this product. | [optional] 
**[Markets](#Markets)** | list, tuple,  | tuple,  | The markets for this product | [optional] 
**FreightClassId** | decimal.Decimal, int,  | decimal.Decimal,  | ID of freight class | [optional] value must be a 32 bit integer
**IntrastatCode** | str,  | str,  | Intrastat code of the product | [optional] 
**CountryOfOrigin** | str,  | str,  | Country of orgin of product | [optional] 
**VariantGroupId** | decimal.Decimal, int,  | decimal.Decimal,  | ID of Variant Group to whom the product should be associated | [optional] value must be a 32 bit integer
**Vat** | decimal.Decimal, int,  | decimal.Decimal,  | ID or rate of VAT (On create and if no VAT is provided then default VAT will be used) | [optional] value must be a 32 bit integer
**VatType** | str,  | str,  | Defines how VAT parameter should be interpreted  Actual &#x3D; VAT parameter is interpreted as VAT rate  VatId &#x3D; VAT parameter is interpreted as VAT Id | [optional] 
**ExternalId** | str,  | str,  | External Id of the product. | [optional] 
**ActivationDate** | str, datetime,  | str,  | Activation date for the product. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Names

The localized names of the product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The localized names of the product. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) |  | 

# ShortTexts

Localized short texts for the product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Localized short texts for the product. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) |  | 

# LongTexts

Localized long texts for the product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Localized long texts for the product. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) |  | 

# TechTexts

Localized tech texts for the product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Localized tech texts for the product. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) | [**SharedModelsLocalizableContent**](SharedModelsLocalizableContent.md) |  | 

# Items

The items belonging to the product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The items belonging to the product. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsWriteProductItem**](ProductModelsWriteProductItem.md) | [**ProductModelsWriteProductItem**](ProductModelsWriteProductItem.md) | [**ProductModelsWriteProductItem**](ProductModelsWriteProductItem.md) |  | 

# CategoryIds

The category ids the product belongs to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The category ids the product belongs to. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# ParameterValues

The parameter values associated with the product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The parameter values associated with the product. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductParameterModelsWriteProductParameterValue**](ProductParameterModelsWriteProductParameterValue.md) | [**ProductParameterModelsWriteProductParameterValue**](ProductParameterModelsWriteProductParameterValue.md) | [**ProductParameterModelsWriteProductParameterValue**](ProductParameterModelsWriteProductParameterValue.md) |  | 

# Variants

The variants for this product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The variants for this product. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VariantModelsWriteVariant**](VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**](VariantModelsWriteVariant.md) | [**VariantModelsWriteVariant**](VariantModelsWriteVariant.md) |  | 

# Markets

The markets for this product

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The markets for this product | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MarketModelsMarket**](MarketModelsMarket.md) | [**MarketModelsMarket**](MarketModelsMarket.md) | [**MarketModelsMarket**](MarketModelsMarket.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

