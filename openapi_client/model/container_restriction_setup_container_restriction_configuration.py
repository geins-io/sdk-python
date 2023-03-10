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


class ContainerRestrictionSetupContainerRestrictionConfiguration(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class AllowedLayouts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.Int32Schema
                    ):
                    
                    
                        class MetaOapg:
                            format = 'int32'
                            enum_value_to_name = {
                                0: "POSITIVE_0",
                                1: "POSITIVE_1",
                                2: "POSITIVE_2",
                                3: "POSITIVE_3",
                                4: "POSITIVE_4",
                                5: "POSITIVE_5",
                                6: "POSITIVE_6",
                                7: "POSITIVE_7",
                                8: "POSITIVE_8",
                            }
                        
                        @schemas.classproperty
                        def POSITIVE_0(cls):
                            return cls(0)
                        
                        @schemas.classproperty
                        def POSITIVE_1(cls):
                            return cls(1)
                        
                        @schemas.classproperty
                        def POSITIVE_2(cls):
                            return cls(2)
                        
                        @schemas.classproperty
                        def POSITIVE_3(cls):
                            return cls(3)
                        
                        @schemas.classproperty
                        def POSITIVE_4(cls):
                            return cls(4)
                        
                        @schemas.classproperty
                        def POSITIVE_5(cls):
                            return cls(5)
                        
                        @schemas.classproperty
                        def POSITIVE_6(cls):
                            return cls(6)
                        
                        @schemas.classproperty
                        def POSITIVE_7(cls):
                            return cls(7)
                        
                        @schemas.classproperty
                        def POSITIVE_8(cls):
                            return cls(8)
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AllowedLayouts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class BannedWidgets(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.UUIDSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, uuid.UUID, ]], typing.List[typing.Union[MetaOapg.items, str, uuid.UUID, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'BannedWidgets':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "AllowedLayouts": AllowedLayouts,
                "BannedWidgets": BannedWidgets,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["AllowedLayouts"]) -> MetaOapg.properties.AllowedLayouts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["BannedWidgets"]) -> MetaOapg.properties.BannedWidgets: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["AllowedLayouts", "BannedWidgets", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["AllowedLayouts"]) -> typing.Union[MetaOapg.properties.AllowedLayouts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["BannedWidgets"]) -> typing.Union[MetaOapg.properties.BannedWidgets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["AllowedLayouts", "BannedWidgets", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        AllowedLayouts: typing.Union[MetaOapg.properties.AllowedLayouts, list, tuple, schemas.Unset] = schemas.unset,
        BannedWidgets: typing.Union[MetaOapg.properties.BannedWidgets, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContainerRestrictionSetupContainerRestrictionConfiguration':
        return super().__new__(
            cls,
            *_args,
            AllowedLayouts=AllowedLayouts,
            BannedWidgets=BannedWidgets,
            _configuration=_configuration,
            **kwargs,
        )
