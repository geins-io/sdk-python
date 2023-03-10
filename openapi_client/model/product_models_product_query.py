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


class ProductModelsProductQuery(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A prroduct query.
    """


    class MetaOapg:
        
        class properties:
            UpdatedAfter = schemas.DateTimeSchema
            
            
            class ProductIds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.Int32Schema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ProductIds':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class ArticleNumbers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ArticleNumbers':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            OnlySellable = schemas.BoolSchema
            FeedId = schemas.Int32Schema
            BatchId = schemas.UUIDSchema
            __annotations__ = {
                "UpdatedAfter": UpdatedAfter,
                "ProductIds": ProductIds,
                "ArticleNumbers": ArticleNumbers,
                "OnlySellable": OnlySellable,
                "FeedId": FeedId,
                "BatchId": BatchId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UpdatedAfter"]) -> MetaOapg.properties.UpdatedAfter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductIds"]) -> MetaOapg.properties.ProductIds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ArticleNumbers"]) -> MetaOapg.properties.ArticleNumbers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OnlySellable"]) -> MetaOapg.properties.OnlySellable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FeedId"]) -> MetaOapg.properties.FeedId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BatchId"]) -> MetaOapg.properties.BatchId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["UpdatedAfter", "ProductIds", "ArticleNumbers", "OnlySellable", "FeedId", "BatchId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UpdatedAfter"]) -> typing.Union[MetaOapg.properties.UpdatedAfter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductIds"]) -> typing.Union[MetaOapg.properties.ProductIds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ArticleNumbers"]) -> typing.Union[MetaOapg.properties.ArticleNumbers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OnlySellable"]) -> typing.Union[MetaOapg.properties.OnlySellable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FeedId"]) -> typing.Union[MetaOapg.properties.FeedId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BatchId"]) -> typing.Union[MetaOapg.properties.BatchId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["UpdatedAfter", "ProductIds", "ArticleNumbers", "OnlySellable", "FeedId", "BatchId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        UpdatedAfter: typing.Union[MetaOapg.properties.UpdatedAfter, str, datetime, schemas.Unset] = schemas.unset,
        ProductIds: typing.Union[MetaOapg.properties.ProductIds, list, tuple, schemas.Unset] = schemas.unset,
        ArticleNumbers: typing.Union[MetaOapg.properties.ArticleNumbers, list, tuple, schemas.Unset] = schemas.unset,
        OnlySellable: typing.Union[MetaOapg.properties.OnlySellable, bool, schemas.Unset] = schemas.unset,
        FeedId: typing.Union[MetaOapg.properties.FeedId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        BatchId: typing.Union[MetaOapg.properties.BatchId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProductModelsProductQuery':
        return super().__new__(
            cls,
            *_args,
            UpdatedAfter=UpdatedAfter,
            ProductIds=ProductIds,
            ArticleNumbers=ArticleNumbers,
            OnlySellable=OnlySellable,
            FeedId=FeedId,
            BatchId=BatchId,
            _configuration=_configuration,
            **kwargs,
        )
