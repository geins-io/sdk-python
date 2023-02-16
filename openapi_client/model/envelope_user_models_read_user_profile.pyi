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


class EnvelopeUserModelsReadUserProfile(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An envelope for the result of and action taken on a resource.
    """


    class MetaOapg:
        
        class properties:
            Message = schemas.StrSchema
            
            
            class Details(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'Details':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def Resource() -> typing.Type['UserModelsReadUserProfile']:
                return UserModelsReadUserProfile
        
            @staticmethod
            def PageResult() -> typing.Type['PageResult']:
                return PageResult
            __annotations__ = {
                "Message": Message,
                "Details": Details,
                "Resource": Resource,
                "PageResult": PageResult,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Message"]) -> MetaOapg.properties.Message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Details"]) -> MetaOapg.properties.Details: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Resource"]) -> 'UserModelsReadUserProfile': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PageResult"]) -> 'PageResult': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Message", "Details", "Resource", "PageResult", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Message"]) -> typing.Union[MetaOapg.properties.Message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Details"]) -> typing.Union[MetaOapg.properties.Details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Resource"]) -> typing.Union['UserModelsReadUserProfile', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PageResult"]) -> typing.Union['PageResult', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Message", "Details", "Resource", "PageResult", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Message: typing.Union[MetaOapg.properties.Message, str, schemas.Unset] = schemas.unset,
        Details: typing.Union[MetaOapg.properties.Details, list, tuple, schemas.Unset] = schemas.unset,
        Resource: typing.Union['UserModelsReadUserProfile', schemas.Unset] = schemas.unset,
        PageResult: typing.Union['PageResult', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EnvelopeUserModelsReadUserProfile':
        return super().__new__(
            cls,
            *_args,
            Message=Message,
            Details=Details,
            Resource=Resource,
            PageResult=PageResult,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.page_result import PageResult
from openapi_client.model.user_models_read_user_profile import UserModelsReadUserProfile
