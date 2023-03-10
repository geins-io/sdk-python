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


class PageWidgetLazyLoadSetupLazyLoadConfiguration(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            EnableLazyloadMobile = schemas.BoolSchema
            EagerLoadStepsMobile = schemas.Int32Schema
            EnableLazyloadDesktop = schemas.BoolSchema
            EagerLoadStepsDesktop = schemas.Int32Schema
            __annotations__ = {
                "EnableLazyloadMobile": EnableLazyloadMobile,
                "EagerLoadStepsMobile": EagerLoadStepsMobile,
                "EnableLazyloadDesktop": EnableLazyloadDesktop,
                "EagerLoadStepsDesktop": EagerLoadStepsDesktop,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EnableLazyloadMobile"]) -> MetaOapg.properties.EnableLazyloadMobile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EagerLoadStepsMobile"]) -> MetaOapg.properties.EagerLoadStepsMobile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EnableLazyloadDesktop"]) -> MetaOapg.properties.EnableLazyloadDesktop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EagerLoadStepsDesktop"]) -> MetaOapg.properties.EagerLoadStepsDesktop: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["EnableLazyloadMobile", "EagerLoadStepsMobile", "EnableLazyloadDesktop", "EagerLoadStepsDesktop", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EnableLazyloadMobile"]) -> typing.Union[MetaOapg.properties.EnableLazyloadMobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EagerLoadStepsMobile"]) -> typing.Union[MetaOapg.properties.EagerLoadStepsMobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EnableLazyloadDesktop"]) -> typing.Union[MetaOapg.properties.EnableLazyloadDesktop, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EagerLoadStepsDesktop"]) -> typing.Union[MetaOapg.properties.EagerLoadStepsDesktop, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["EnableLazyloadMobile", "EagerLoadStepsMobile", "EnableLazyloadDesktop", "EagerLoadStepsDesktop", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        EnableLazyloadMobile: typing.Union[MetaOapg.properties.EnableLazyloadMobile, bool, schemas.Unset] = schemas.unset,
        EagerLoadStepsMobile: typing.Union[MetaOapg.properties.EagerLoadStepsMobile, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        EnableLazyloadDesktop: typing.Union[MetaOapg.properties.EnableLazyloadDesktop, bool, schemas.Unset] = schemas.unset,
        EagerLoadStepsDesktop: typing.Union[MetaOapg.properties.EagerLoadStepsDesktop, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PageWidgetLazyLoadSetupLazyLoadConfiguration':
        return super().__new__(
            cls,
            *_args,
            EnableLazyloadMobile=EnableLazyloadMobile,
            EagerLoadStepsMobile=EagerLoadStepsMobile,
            EnableLazyloadDesktop=EnableLazyloadDesktop,
            EagerLoadStepsDesktop=EagerLoadStepsDesktop,
            _configuration=_configuration,
            **kwargs,
        )
