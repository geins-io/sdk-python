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


class ProductModelsReadShippingFee(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A shipping fee for a product item.
    """


    class MetaOapg:
        
        class properties:
            Market = schemas.Int32Schema
            Country = schemas.StrSchema
            Service = schemas.StrSchema
            ServiceId = schemas.Int32Schema
            Fee = schemas.Float64Schema
            __annotations__ = {
                "Market": Market,
                "Country": Country,
                "Service": Service,
                "ServiceId": ServiceId,
                "Fee": Fee,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Market"]) -> MetaOapg.properties.Market: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Country"]) -> MetaOapg.properties.Country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Service"]) -> MetaOapg.properties.Service: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ServiceId"]) -> MetaOapg.properties.ServiceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Fee"]) -> MetaOapg.properties.Fee: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Market", "Country", "Service", "ServiceId", "Fee", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Market"]) -> typing.Union[MetaOapg.properties.Market, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Country"]) -> typing.Union[MetaOapg.properties.Country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Service"]) -> typing.Union[MetaOapg.properties.Service, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ServiceId"]) -> typing.Union[MetaOapg.properties.ServiceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Fee"]) -> typing.Union[MetaOapg.properties.Fee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Market", "Country", "Service", "ServiceId", "Fee", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Market: typing.Union[MetaOapg.properties.Market, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Country: typing.Union[MetaOapg.properties.Country, str, schemas.Unset] = schemas.unset,
        Service: typing.Union[MetaOapg.properties.Service, str, schemas.Unset] = schemas.unset,
        ServiceId: typing.Union[MetaOapg.properties.ServiceId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Fee: typing.Union[MetaOapg.properties.Fee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProductModelsReadShippingFee':
        return super().__new__(
            cls,
            *_args,
            Market=Market,
            Country=Country,
            Service=Service,
            ServiceId=ServiceId,
            Fee=Fee,
            _configuration=_configuration,
            **kwargs,
        )
