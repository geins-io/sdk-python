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


class ProductParameterModelsReadProductParameterValue(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A parameter value for a product.
    """


    class MetaOapg:
        
        class properties:
            ParameterValueId = schemas.Int32Schema
            ProductId = schemas.Int32Schema
            ParameterId = schemas.Int32Schema
            ParameterName = schemas.StrSchema
            GroupId = schemas.Int32Schema
            GroupName = schemas.StrSchema
            
            
            class ParameterType(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
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
            Value = schemas.StrSchema
            Description = schemas.StrSchema
            
            
            class LocalizedDescriptions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SharedModelsLocalizableContent']:
                        return SharedModelsLocalizableContent
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SharedModelsLocalizableContent'], typing.List['SharedModelsLocalizableContent']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'LocalizedDescriptions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SharedModelsLocalizableContent':
                    return super().__getitem__(i)
            InternalIdentifier = schemas.StrSchema
            __annotations__ = {
                "ParameterValueId": ParameterValueId,
                "ProductId": ProductId,
                "ParameterId": ParameterId,
                "ParameterName": ParameterName,
                "GroupId": GroupId,
                "GroupName": GroupName,
                "ParameterType": ParameterType,
                "Value": Value,
                "Description": Description,
                "LocalizedDescriptions": LocalizedDescriptions,
                "InternalIdentifier": InternalIdentifier,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ParameterValueId"]) -> MetaOapg.properties.ParameterValueId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProductId"]) -> MetaOapg.properties.ProductId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ParameterId"]) -> MetaOapg.properties.ParameterId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ParameterName"]) -> MetaOapg.properties.ParameterName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["GroupId"]) -> MetaOapg.properties.GroupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["GroupName"]) -> MetaOapg.properties.GroupName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ParameterType"]) -> MetaOapg.properties.ParameterType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Value"]) -> MetaOapg.properties.Value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Description"]) -> MetaOapg.properties.Description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LocalizedDescriptions"]) -> MetaOapg.properties.LocalizedDescriptions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["InternalIdentifier"]) -> MetaOapg.properties.InternalIdentifier: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ParameterValueId", "ProductId", "ParameterId", "ParameterName", "GroupId", "GroupName", "ParameterType", "Value", "Description", "LocalizedDescriptions", "InternalIdentifier", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ParameterValueId"]) -> typing.Union[MetaOapg.properties.ParameterValueId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProductId"]) -> typing.Union[MetaOapg.properties.ProductId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ParameterId"]) -> typing.Union[MetaOapg.properties.ParameterId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ParameterName"]) -> typing.Union[MetaOapg.properties.ParameterName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["GroupId"]) -> typing.Union[MetaOapg.properties.GroupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["GroupName"]) -> typing.Union[MetaOapg.properties.GroupName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ParameterType"]) -> typing.Union[MetaOapg.properties.ParameterType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Value"]) -> typing.Union[MetaOapg.properties.Value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Description"]) -> typing.Union[MetaOapg.properties.Description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LocalizedDescriptions"]) -> typing.Union[MetaOapg.properties.LocalizedDescriptions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["InternalIdentifier"]) -> typing.Union[MetaOapg.properties.InternalIdentifier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ParameterValueId", "ProductId", "ParameterId", "ParameterName", "GroupId", "GroupName", "ParameterType", "Value", "Description", "LocalizedDescriptions", "InternalIdentifier", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ParameterValueId: typing.Union[MetaOapg.properties.ParameterValueId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ProductId: typing.Union[MetaOapg.properties.ProductId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ParameterId: typing.Union[MetaOapg.properties.ParameterId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ParameterName: typing.Union[MetaOapg.properties.ParameterName, str, schemas.Unset] = schemas.unset,
        GroupId: typing.Union[MetaOapg.properties.GroupId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        GroupName: typing.Union[MetaOapg.properties.GroupName, str, schemas.Unset] = schemas.unset,
        ParameterType: typing.Union[MetaOapg.properties.ParameterType, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Value: typing.Union[MetaOapg.properties.Value, str, schemas.Unset] = schemas.unset,
        Description: typing.Union[MetaOapg.properties.Description, str, schemas.Unset] = schemas.unset,
        LocalizedDescriptions: typing.Union[MetaOapg.properties.LocalizedDescriptions, list, tuple, schemas.Unset] = schemas.unset,
        InternalIdentifier: typing.Union[MetaOapg.properties.InternalIdentifier, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProductParameterModelsReadProductParameterValue':
        return super().__new__(
            cls,
            *_args,
            ParameterValueId=ParameterValueId,
            ProductId=ProductId,
            ParameterId=ParameterId,
            ParameterName=ParameterName,
            GroupId=GroupId,
            GroupName=GroupName,
            ParameterType=ParameterType,
            Value=Value,
            Description=Description,
            LocalizedDescriptions=LocalizedDescriptions,
            InternalIdentifier=InternalIdentifier,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.shared_models_localizable_content import SharedModelsLocalizableContent
