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


class OrderCaptureRow(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            OrderRowId = schemas.Int32Schema
            ItemId = schemas.Int32Schema
            ProductId = schemas.Int32Schema
            Price = schemas.Float64Schema
            PriceExVat = schemas.Float64Schema
            Name = schemas.StrSchema
            ProductName = schemas.StrSchema
            Variant = schemas.StrSchema
            Brand = schemas.StrSchema
            __annotations__ = {
                "OrderRowId": OrderRowId,
                "ItemId": ItemId,
                "ProductId": ProductId,
                "Price": Price,
                "PriceExVat": PriceExVat,
                "Name": Name,
                "ProductName": ProductName,
                "Variant": Variant,
                "Brand": Brand,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OrderRowId"]) -> MetaOapg.properties.OrderRowId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ItemId"]) -> MetaOapg.properties.ItemId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductId"]) -> MetaOapg.properties.ProductId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Price"]) -> MetaOapg.properties.Price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PriceExVat"]) -> MetaOapg.properties.PriceExVat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductName"]) -> MetaOapg.properties.ProductName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Variant"]) -> MetaOapg.properties.Variant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Brand"]) -> MetaOapg.properties.Brand: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["OrderRowId", "ItemId", "ProductId", "Price", "PriceExVat", "Name", "ProductName", "Variant", "Brand", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OrderRowId"]) -> typing.Union[MetaOapg.properties.OrderRowId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ItemId"]) -> typing.Union[MetaOapg.properties.ItemId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductId"]) -> typing.Union[MetaOapg.properties.ProductId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Price"]) -> typing.Union[MetaOapg.properties.Price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PriceExVat"]) -> typing.Union[MetaOapg.properties.PriceExVat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductName"]) -> typing.Union[MetaOapg.properties.ProductName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Variant"]) -> typing.Union[MetaOapg.properties.Variant, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Brand"]) -> typing.Union[MetaOapg.properties.Brand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["OrderRowId", "ItemId", "ProductId", "Price", "PriceExVat", "Name", "ProductName", "Variant", "Brand", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        OrderRowId: typing.Union[MetaOapg.properties.OrderRowId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ItemId: typing.Union[MetaOapg.properties.ItemId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ProductId: typing.Union[MetaOapg.properties.ProductId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Price: typing.Union[MetaOapg.properties.Price, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        PriceExVat: typing.Union[MetaOapg.properties.PriceExVat, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
        ProductName: typing.Union[MetaOapg.properties.ProductName, str, schemas.Unset] = schemas.unset,
        Variant: typing.Union[MetaOapg.properties.Variant, str, schemas.Unset] = schemas.unset,
        Brand: typing.Union[MetaOapg.properties.Brand, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrderCaptureRow':
        return super().__new__(
            cls,
            *_args,
            OrderRowId=OrderRowId,
            ItemId=ItemId,
            ProductId=ProductId,
            Price=Price,
            PriceExVat=PriceExVat,
            Name=Name,
            ProductName=ProductName,
            Variant=Variant,
            Brand=Brand,
            _configuration=_configuration,
            **kwargs,
        )
