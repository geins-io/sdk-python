# openapi_client.model.product_models_read_product.ProductModelsReadProduct

A product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A product. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ProductId** | decimal.Decimal, int,  | decimal.Decimal,  | The unique identifier for the product. | [optional] value must be a 32 bit integer
**ArticleNumber** | str,  | str,  | The article number of the product. | [optional] 
**[Names](#Names)** | list, tuple,  | tuple,  | The localized names of the product. | [optional] 
**DateCreated** | str, datetime,  | str,  | The date the product was created. | [optional] value must conform to RFC-3339 date-time
**DateUpdated** | str, datetime,  | str,  | The date the product was last updated. | [optional] value must conform to RFC-3339 date-time
**Active** | bool,  | BoolClass,  | The current state of the product. | [optional] 
**PurchasePrice** | decimal.Decimal, int, float,  | decimal.Decimal,  | The purchase price in the currency defined in {Product.Models.Read.Product.PurchasePriceCurrency}. | [optional] value must be a 64 bit float
**PurchasePriceCurrency** | str,  | str,  | The 3-letter ISO 4217 currency code for the amount given in {Product.Models.Read.Product.PurchasePrice}. | [optional] 
**[ShortTexts](#ShortTexts)** | list, tuple,  | tuple,  | Localized short texts for the product. | [optional] 
**[LongTexts](#LongTexts)** | list, tuple,  | tuple,  | Localized long texts for the product. | [optional] 
**[TechTexts](#TechTexts)** | list, tuple,  | tuple,  | Localized tech texts for the product. | [optional] 
**[Items](#Items)** | list, tuple,  | tuple,  | The items belonging to the product. | [optional] 
**[Prices](#Prices)** | list, tuple,  | tuple,  | The current prices of the product. | [optional] 
**[Categories](#Categories)** | list, tuple,  | tuple,  | The categories the product belongs to. | [optional] 
**[Images](#Images)** | list, tuple,  | tuple,  | The images for the product | [optional] 
**BrandId** | decimal.Decimal, int,  | decimal.Decimal,  | The brand id of the product. | [optional] value must be a 32 bit integer
**BrandName** | str,  | str,  | The brand name of the product. | [optional] 
**SupplierId** | decimal.Decimal, int,  | decimal.Decimal,  | The supplier id of the product. | [optional] value must be a 32 bit integer
**SupplierName** | str,  | str,  | The supplier name of the product. | [optional] 
**[ParameterValues](#ParameterValues)** | list, tuple,  | tuple,  | The parameter values associated with the product. | [optional] 
**[Variants](#Variants)** | list, tuple,  | tuple,  | The variants for this product. | [optional] 
**[Markets](#Markets)** | list, tuple,  | tuple,  | The markets for this product | [optional] 
**Vat** | decimal.Decimal, int, float,  | decimal.Decimal,  | The vat percent for this product. Eg) 0.25 meaning 25% VAT. | [optional] value must be a 64 bit float
**PrimaryImage** | str,  | str,  | The filename of this products primary image. | [optional] 
**FreightClassId** | decimal.Decimal, int,  | decimal.Decimal,  | ID of freight class | [optional] value must be a 32 bit integer
**IntrastatCode** | str,  | str,  | Intrastat code of the product | [optional] 
**CountryOfOrigin** | str,  | str,  | Country of orgin of product | [optional] 
**VariantGroupId** | decimal.Decimal, int,  | decimal.Decimal,  | ID of Variant Group to which the product is associated | [optional] value must be a 32 bit integer
**VatId** | decimal.Decimal, int,  | decimal.Decimal,  | ID of Vat | [optional] value must be a 32 bit integer
**ExternalId** | str,  | str,  | External Id of the product. | [optional] 
**ActivationDate** | str, datetime,  | str,  | Activation date for the product. | [optional] value must conform to RFC-3339 date-time
**[Feeds](#Feeds)** | list, tuple,  | tuple,  | The feeds the product is a member of | [optional] 
**[Urls](#Urls)** | list, tuple,  | tuple,  | All canonical urls for the product | [optional] 
**MainCategoryId** | decimal.Decimal, int,  | decimal.Decimal,  | The main category id for the product. | [optional] value must be a 32 bit integer
**[RelatedProducts](#RelatedProducts)** | list, tuple,  | tuple,  | The related products for the product. | [optional] 
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
[**ProductModelsReadProductItem**](ProductModelsReadProductItem.md) | [**ProductModelsReadProductItem**](ProductModelsReadProductItem.md) | [**ProductModelsReadProductItem**](ProductModelsReadProductItem.md) |  | 

# Prices

The current prices of the product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The current prices of the product. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PriceListModelsReadPriceListPrice**](PriceListModelsReadPriceListPrice.md) | [**PriceListModelsReadPriceListPrice**](PriceListModelsReadPriceListPrice.md) | [**PriceListModelsReadPriceListPrice**](PriceListModelsReadPriceListPrice.md) |  | 

# Categories

The categories the product belongs to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The categories the product belongs to. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CategoryModelsReadCategory**](CategoryModelsReadCategory.md) | [**CategoryModelsReadCategory**](CategoryModelsReadCategory.md) | [**CategoryModelsReadCategory**](CategoryModelsReadCategory.md) |  | 

# Images

The images for the product

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The images for the product | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsReadImage**](ProductModelsReadImage.md) | [**ProductModelsReadImage**](ProductModelsReadImage.md) | [**ProductModelsReadImage**](ProductModelsReadImage.md) |  | 

# ParameterValues

The parameter values associated with the product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The parameter values associated with the product. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductParameterModelsReadProductParameterValue**](ProductParameterModelsReadProductParameterValue.md) | [**ProductParameterModelsReadProductParameterValue**](ProductParameterModelsReadProductParameterValue.md) | [**ProductParameterModelsReadProductParameterValue**](ProductParameterModelsReadProductParameterValue.md) |  | 

# Variants

The variants for this product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The variants for this product. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**VariantModelsReadVariant**](VariantModelsReadVariant.md) | [**VariantModelsReadVariant**](VariantModelsReadVariant.md) | [**VariantModelsReadVariant**](VariantModelsReadVariant.md) |  | 

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

# Feeds

The feeds the product is a member of

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The feeds the product is a member of | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsReadFeedMembership**](ProductModelsReadFeedMembership.md) | [**ProductModelsReadFeedMembership**](ProductModelsReadFeedMembership.md) | [**ProductModelsReadFeedMembership**](ProductModelsReadFeedMembership.md) |  | 

# Urls

All canonical urls for the product

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | All canonical urls for the product | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsReadProductUrl**](ProductModelsReadProductUrl.md) | [**ProductModelsReadProductUrl**](ProductModelsReadProductUrl.md) | [**ProductModelsReadProductUrl**](ProductModelsReadProductUrl.md) |  | 

# RelatedProducts

The related products for the product.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The related products for the product. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProductModelsReadRelatedProduct**](ProductModelsReadRelatedProduct.md) | [**ProductModelsReadRelatedProduct**](ProductModelsReadRelatedProduct.md) | [**ProductModelsReadRelatedProduct**](ProductModelsReadRelatedProduct.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

