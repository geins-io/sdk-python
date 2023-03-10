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


class SupplierModelsReadSupplier(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A product supplier.
    """


    class MetaOapg:
        
        class properties:
            SupplierId = schemas.Int32Schema
            Name = schemas.StrSchema
            Address1 = schemas.StrSchema
            Address2 = schemas.StrSchema
            Address3 = schemas.StrSchema
            ZipCode = schemas.StrSchema
            Country = schemas.StrSchema
            ContactPerson = schemas.StrSchema
            Phone1 = schemas.StrSchema
            Phone2 = schemas.StrSchema
            Email = schemas.StrSchema
            ExternalId = schemas.StrSchema
            __annotations__ = {
                "SupplierId": SupplierId,
                "Name": Name,
                "Address1": Address1,
                "Address2": Address2,
                "Address3": Address3,
                "ZipCode": ZipCode,
                "Country": Country,
                "ContactPerson": ContactPerson,
                "Phone1": Phone1,
                "Phone2": Phone2,
                "Email": Email,
                "ExternalId": ExternalId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SupplierId"]) -> MetaOapg.properties.SupplierId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Name"]) -> MetaOapg.properties.Name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Address1"]) -> MetaOapg.properties.Address1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Address2"]) -> MetaOapg.properties.Address2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Address3"]) -> MetaOapg.properties.Address3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ZipCode"]) -> MetaOapg.properties.ZipCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Country"]) -> MetaOapg.properties.Country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ContactPerson"]) -> MetaOapg.properties.ContactPerson: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Phone1"]) -> MetaOapg.properties.Phone1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Phone2"]) -> MetaOapg.properties.Phone2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Email"]) -> MetaOapg.properties.Email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ExternalId"]) -> MetaOapg.properties.ExternalId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["SupplierId", "Name", "Address1", "Address2", "Address3", "ZipCode", "Country", "ContactPerson", "Phone1", "Phone2", "Email", "ExternalId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SupplierId"]) -> typing.Union[MetaOapg.properties.SupplierId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Name"]) -> typing.Union[MetaOapg.properties.Name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Address1"]) -> typing.Union[MetaOapg.properties.Address1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Address2"]) -> typing.Union[MetaOapg.properties.Address2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Address3"]) -> typing.Union[MetaOapg.properties.Address3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ZipCode"]) -> typing.Union[MetaOapg.properties.ZipCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Country"]) -> typing.Union[MetaOapg.properties.Country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ContactPerson"]) -> typing.Union[MetaOapg.properties.ContactPerson, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Phone1"]) -> typing.Union[MetaOapg.properties.Phone1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Phone2"]) -> typing.Union[MetaOapg.properties.Phone2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Email"]) -> typing.Union[MetaOapg.properties.Email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ExternalId"]) -> typing.Union[MetaOapg.properties.ExternalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["SupplierId", "Name", "Address1", "Address2", "Address3", "ZipCode", "Country", "ContactPerson", "Phone1", "Phone2", "Email", "ExternalId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        SupplierId: typing.Union[MetaOapg.properties.SupplierId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Name: typing.Union[MetaOapg.properties.Name, str, schemas.Unset] = schemas.unset,
        Address1: typing.Union[MetaOapg.properties.Address1, str, schemas.Unset] = schemas.unset,
        Address2: typing.Union[MetaOapg.properties.Address2, str, schemas.Unset] = schemas.unset,
        Address3: typing.Union[MetaOapg.properties.Address3, str, schemas.Unset] = schemas.unset,
        ZipCode: typing.Union[MetaOapg.properties.ZipCode, str, schemas.Unset] = schemas.unset,
        Country: typing.Union[MetaOapg.properties.Country, str, schemas.Unset] = schemas.unset,
        ContactPerson: typing.Union[MetaOapg.properties.ContactPerson, str, schemas.Unset] = schemas.unset,
        Phone1: typing.Union[MetaOapg.properties.Phone1, str, schemas.Unset] = schemas.unset,
        Phone2: typing.Union[MetaOapg.properties.Phone2, str, schemas.Unset] = schemas.unset,
        Email: typing.Union[MetaOapg.properties.Email, str, schemas.Unset] = schemas.unset,
        ExternalId: typing.Union[MetaOapg.properties.ExternalId, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SupplierModelsReadSupplier':
        return super().__new__(
            cls,
            *_args,
            SupplierId=SupplierId,
            Name=Name,
            Address1=Address1,
            Address2=Address2,
            Address3=Address3,
            ZipCode=ZipCode,
            Country=Country,
            ContactPerson=ContactPerson,
            Phone1=Phone1,
            Phone2=Phone2,
            Email=Email,
            ExternalId=ExternalId,
            _configuration=_configuration,
            **kwargs,
        )
