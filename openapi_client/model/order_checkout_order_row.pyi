# coding: utf-8

"""
    Geins Management API

     Geins Management API is an RESTful api to power your applications who manages your geins services. Geins provides an easy-to-use and scalable solution for managing all aspects of an online store, from product listings and customer information to order processing and payment transactions.   :::tip With this API, you can build custom applications and integrate with third-party systems, dashboards and other bussiness logic apps. :::    ## Getting started Once you have created an account, you can start using the Management API by creating an `API key`. You can create as many API keys as you need. Each `API key` is connected to a specific account so you can keep track of operations and manage keys. You can find your `API key` in the `geins merchant center`.   ### Fast track Use one of our [SDKs](https://docs.geins.io/docs/sdk/introduction) to get started quickly. The SDKs are available for the most popular programming languages and frameworks.  Or, if you prefer to just take it for a test run:  [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/25895885-aaf6598f-1a7c-4949-85d7-ba846c42d553?action=collection%2Ffork&collection-url=entityId%3D25895885-aaf6598f-1a7c-4949-85d7-ba846c42d553%26entityType%3Dcollection%26workspaceId%3Da2a179ce-158e-46b0-8d06-e9640f45112c)  ### Authentication Two authentication methods are supported:   - `API Key`   - `Basic Auth`   # noqa: E501

    The version of the OpenAPI document: v1.7
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class OrderCheckoutOrderRow(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            Sku = schemas.StrSchema
            ProductId = schemas.Int32Schema
            ExternalId = schemas.StrSchema
            DiscountRate = schemas.Float64Schema
            CartRowId = schemas.Int32Schema
            ProductContainerBuildId = schemas.Int32Schema
            Message = schemas.StrSchema
            ArticleNumber = schemas.StrSchema
            Gtin = schemas.StrSchema
            Brand = schemas.StrSchema
            
            
            class Categories(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Categories':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            Name = schemas.StrSchema
            Variant = schemas.StrSchema
            Quantity = schemas.Int32Schema
            PriceIncVat = schemas.Float64Schema
            PriceExVat = schemas.Float64Schema
            ExpectedTotalPriceIncVat = schemas.Float64Schema
            DiscountIncVat = schemas.Float64Schema
            DiscountExVat = schemas.Float64Schema
            ExpectedTotalDiscountIncVat = schemas.Float64Schema
            ProductUrl = schemas.StrSchema
            ImageUrl = schemas.StrSchema
            Weight = schemas.Int32Schema
            Height = schemas.Int32Schema
            Width = schemas.Int32Schema
            Length = schemas.Int32Schema
            
            
            class CampaignIds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'CampaignIds':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            CampaignGroupData = schemas.StrSchema
            
            
            class CampaignNames(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'CampaignNames':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            ProductPriceCampaignId = schemas.Int32Schema
            ProductPriceListId = schemas.Int32Schema
            __annotations__ = {
                "Sku": Sku,
                "ProductId": ProductId,
                "ExternalId": ExternalId,
                "DiscountRate": DiscountRate,
                "CartRowId": CartRowId,
                "ProductContainerBuildId": ProductContainerBuildId,
                "Message": Message,
                "ArticleNumber": ArticleNumber,
                "Gtin": Gtin,
                "Brand": Brand,
                "Categories": Categories,
                "Name": Name,
                "Variant": Variant,
                "Quantity": Quantity,
                "PriceIncVat": PriceIncVat,
                "PriceExVat": PriceExVat,
                "ExpectedTotalPriceIncVat": ExpectedTotalPriceIncVat,
                "DiscountIncVat": DiscountIncVat,
                "DiscountExVat": DiscountExVat,
                "ExpectedTotalDiscountIncVat": ExpectedTotalDiscountIncVat,
                "ProductUrl": ProductUrl,
                "ImageUrl": ImageUrl,
                "Weight": Weight,
                "Height": Height,
                "Width": Width,
                "Length": Length,
                "CampaignIds": CampaignIds,
                "CampaignGroupData": CampaignGroupData,
                "CampaignNames": CampaignNames,
                "ProductPriceCampaignId": ProductPriceCampaignId,
                "ProductPriceListId": ProductPriceListId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Sku"]) -> MetaOapg.properties.Sku: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductId"]) -> MetaOapg.properties.ProductId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExternalId"]) -> MetaOapg.properties.ExternalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DiscountRate"]) -> MetaOapg.properties.DiscountRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CartRowId"]) -> MetaOapg.properties.CartRowId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductContainerBuildId"]) -> MetaOapg.properties.ProductContainerBuildId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Message"]) -> MetaOapg.properties.Message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ArticleNumber"]) -> MetaOapg.properties.ArticleNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Gtin"]) -> MetaOapg.properties.Gtin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Brand"]) -> MetaOapg.properties.Brand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Categories"]) -> MetaOapg.properties.Categories: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Variant"]) -> MetaOapg.properties.Variant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Quantity"]) -> MetaOapg.properties.Quantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PriceIncVat"]) -> MetaOapg.properties.PriceIncVat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PriceExVat"]) -> MetaOapg.properties.PriceExVat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExpectedTotalPriceIncVat"]) -> MetaOapg.properties.ExpectedTotalPriceIncVat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DiscountIncVat"]) -> MetaOapg.properties.DiscountIncVat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DiscountExVat"]) -> MetaOapg.properties.DiscountExVat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExpectedTotalDiscountIncVat"]) -> MetaOapg.properties.ExpectedTotalDiscountIncVat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductUrl"]) -> MetaOapg.properties.ProductUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ImageUrl"]) -> MetaOapg.properties.ImageUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Weight"]) -> MetaOapg.properties.Weight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Height"]) -> MetaOapg.properties.Height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Width"]) -> MetaOapg.properties.Width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Length"]) -> MetaOapg.properties.Length: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CampaignIds"]) -> MetaOapg.properties.CampaignIds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CampaignGroupData"]) -> MetaOapg.properties.CampaignGroupData: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CampaignNames"]) -> MetaOapg.properties.CampaignNames: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductPriceCampaignId"]) -> MetaOapg.properties.ProductPriceCampaignId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductPriceListId"]) -> MetaOapg.properties.ProductPriceListId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Sku", "ProductId", "ExternalId", "DiscountRate", "CartRowId", "ProductContainerBuildId", "Message", "ArticleNumber", "Gtin", "Brand", "Categories", "Name", "Variant", "Quantity", "PriceIncVat", "PriceExVat", "ExpectedTotalPriceIncVat", "DiscountIncVat", "DiscountExVat", "ExpectedTotalDiscountIncVat", "ProductUrl", "ImageUrl", "Weight", "Height", "Width", "Length", "CampaignIds", "CampaignGroupData", "CampaignNames", "ProductPriceCampaignId", "ProductPriceListId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Sku"]) -> typing.Union[MetaOapg.properties.Sku, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductId"]) -> typing.Union[MetaOapg.properties.ProductId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExternalId"]) -> typing.Union[MetaOapg.properties.ExternalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DiscountRate"]) -> typing.Union[MetaOapg.properties.DiscountRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CartRowId"]) -> typing.Union[MetaOapg.properties.CartRowId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductContainerBuildId"]) -> typing.Union[MetaOapg.properties.ProductContainerBuildId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Message"]) -> typing.Union[MetaOapg.properties.Message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ArticleNumber"]) -> typing.Union[MetaOapg.properties.ArticleNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Gtin"]) -> typing.Union[MetaOapg.properties.Gtin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Brand"]) -> typing.Union[MetaOapg.properties.Brand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Categories"]) -> typing.Union[MetaOapg.properties.Categories, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Variant"]) -> typing.Union[MetaOapg.properties.Variant, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Quantity"]) -> typing.Union[MetaOapg.properties.Quantity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PriceIncVat"]) -> typing.Union[MetaOapg.properties.PriceIncVat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PriceExVat"]) -> typing.Union[MetaOapg.properties.PriceExVat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExpectedTotalPriceIncVat"]) -> typing.Union[MetaOapg.properties.ExpectedTotalPriceIncVat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DiscountIncVat"]) -> typing.Union[MetaOapg.properties.DiscountIncVat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DiscountExVat"]) -> typing.Union[MetaOapg.properties.DiscountExVat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExpectedTotalDiscountIncVat"]) -> typing.Union[MetaOapg.properties.ExpectedTotalDiscountIncVat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductUrl"]) -> typing.Union[MetaOapg.properties.ProductUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ImageUrl"]) -> typing.Union[MetaOapg.properties.ImageUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Weight"]) -> typing.Union[MetaOapg.properties.Weight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Height"]) -> typing.Union[MetaOapg.properties.Height, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Width"]) -> typing.Union[MetaOapg.properties.Width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Length"]) -> typing.Union[MetaOapg.properties.Length, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CampaignIds"]) -> typing.Union[MetaOapg.properties.CampaignIds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CampaignGroupData"]) -> typing.Union[MetaOapg.properties.CampaignGroupData, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CampaignNames"]) -> typing.Union[MetaOapg.properties.CampaignNames, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductPriceCampaignId"]) -> typing.Union[MetaOapg.properties.ProductPriceCampaignId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductPriceListId"]) -> typing.Union[MetaOapg.properties.ProductPriceListId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Sku", "ProductId", "ExternalId", "DiscountRate", "CartRowId", "ProductContainerBuildId", "Message", "ArticleNumber", "Gtin", "Brand", "Categories", "Name", "Variant", "Quantity", "PriceIncVat", "PriceExVat", "ExpectedTotalPriceIncVat", "DiscountIncVat", "DiscountExVat", "ExpectedTotalDiscountIncVat", "ProductUrl", "ImageUrl", "Weight", "Height", "Width", "Length", "CampaignIds", "CampaignGroupData", "CampaignNames", "ProductPriceCampaignId", "ProductPriceListId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Sku: typing.Union[MetaOapg.properties.Sku, str, schemas.Unset] = schemas.unset,
        ProductId: typing.Union[MetaOapg.properties.ProductId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ExternalId: typing.Union[MetaOapg.properties.ExternalId, str, schemas.Unset] = schemas.unset,
        DiscountRate: typing.Union[MetaOapg.properties.DiscountRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        CartRowId: typing.Union[MetaOapg.properties.CartRowId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ProductContainerBuildId: typing.Union[MetaOapg.properties.ProductContainerBuildId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Message: typing.Union[MetaOapg.properties.Message, str, schemas.Unset] = schemas.unset,
        ArticleNumber: typing.Union[MetaOapg.properties.ArticleNumber, str, schemas.Unset] = schemas.unset,
        Gtin: typing.Union[MetaOapg.properties.Gtin, str, schemas.Unset] = schemas.unset,
        Brand: typing.Union[MetaOapg.properties.Brand, str, schemas.Unset] = schemas.unset,
        Categories: typing.Union[MetaOapg.properties.Categories, list, tuple, schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
        Variant: typing.Union[MetaOapg.properties.Variant, str, schemas.Unset] = schemas.unset,
        Quantity: typing.Union[MetaOapg.properties.Quantity, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        PriceIncVat: typing.Union[MetaOapg.properties.PriceIncVat, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        PriceExVat: typing.Union[MetaOapg.properties.PriceExVat, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ExpectedTotalPriceIncVat: typing.Union[MetaOapg.properties.ExpectedTotalPriceIncVat, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        DiscountIncVat: typing.Union[MetaOapg.properties.DiscountIncVat, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        DiscountExVat: typing.Union[MetaOapg.properties.DiscountExVat, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ExpectedTotalDiscountIncVat: typing.Union[MetaOapg.properties.ExpectedTotalDiscountIncVat, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        ProductUrl: typing.Union[MetaOapg.properties.ProductUrl, str, schemas.Unset] = schemas.unset,
        ImageUrl: typing.Union[MetaOapg.properties.ImageUrl, str, schemas.Unset] = schemas.unset,
        Weight: typing.Union[MetaOapg.properties.Weight, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Height: typing.Union[MetaOapg.properties.Height, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Width: typing.Union[MetaOapg.properties.Width, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Length: typing.Union[MetaOapg.properties.Length, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        CampaignIds: typing.Union[MetaOapg.properties.CampaignIds, list, tuple, schemas.Unset] = schemas.unset,
        CampaignGroupData: typing.Union[MetaOapg.properties.CampaignGroupData, str, schemas.Unset] = schemas.unset,
        CampaignNames: typing.Union[MetaOapg.properties.CampaignNames, list, tuple, schemas.Unset] = schemas.unset,
        ProductPriceCampaignId: typing.Union[MetaOapg.properties.ProductPriceCampaignId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ProductPriceListId: typing.Union[MetaOapg.properties.ProductPriceListId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrderCheckoutOrderRow':
        return super().__new__(
            cls,
            *_args,
            Sku=Sku,
            ProductId=ProductId,
            ExternalId=ExternalId,
            DiscountRate=DiscountRate,
            CartRowId=CartRowId,
            ProductContainerBuildId=ProductContainerBuildId,
            Message=Message,
            ArticleNumber=ArticleNumber,
            Gtin=Gtin,
            Brand=Brand,
            Categories=Categories,
            Name=Name,
            Variant=Variant,
            Quantity=Quantity,
            PriceIncVat=PriceIncVat,
            PriceExVat=PriceExVat,
            ExpectedTotalPriceIncVat=ExpectedTotalPriceIncVat,
            DiscountIncVat=DiscountIncVat,
            DiscountExVat=DiscountExVat,
            ExpectedTotalDiscountIncVat=ExpectedTotalDiscountIncVat,
            ProductUrl=ProductUrl,
            ImageUrl=ImageUrl,
            Weight=Weight,
            Height=Height,
            Width=Width,
            Length=Length,
            CampaignIds=CampaignIds,
            CampaignGroupData=CampaignGroupData,
            CampaignNames=CampaignNames,
            ProductPriceCampaignId=ProductPriceCampaignId,
            ProductPriceListId=ProductPriceListId,
            _configuration=_configuration,
            **kwargs,
        )