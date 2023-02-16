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


class UserModelsWriteUserProfile(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            UserId = schemas.Int32Schema
            SiteId = schemas.Int32Schema
            Email = schemas.StrSchema
            Password = schemas.StrSchema
            FirstName = schemas.StrSchema
            LastName = schemas.StrSchema
            PhoneNr = schemas.StrSchema
            MobilePhoneNr = schemas.StrSchema
            Company = schemas.StrSchema
            UserTypeId = schemas.Int32Schema
            Address = schemas.StrSchema
            Address2 = schemas.StrSchema
            Address3 = schemas.StrSchema
            DoorCode = schemas.StrSchema
            PersonalId = schemas.StrSchema
            Birthyear = schemas.StrSchema
            Zip = schemas.StrSchema
            City = schemas.StrSchema
            CareOf = schemas.StrSchema
            Country = schemas.StrSchema
            CountryId = schemas.Int32Schema
            Gender = schemas.BoolSchema
            Newsletter = schemas.BoolSchema
            HasExternalAuth = schemas.BoolSchema
            __annotations__ = {
                "UserId": UserId,
                "SiteId": SiteId,
                "Email": Email,
                "Password": Password,
                "FirstName": FirstName,
                "LastName": LastName,
                "PhoneNr": PhoneNr,
                "MobilePhoneNr": MobilePhoneNr,
                "Company": Company,
                "UserTypeId": UserTypeId,
                "Address": Address,
                "Address2": Address2,
                "Address3": Address3,
                "DoorCode": DoorCode,
                "PersonalId": PersonalId,
                "Birthyear": Birthyear,
                "Zip": Zip,
                "City": City,
                "CareOf": CareOf,
                "Country": Country,
                "CountryId": CountryId,
                "Gender": Gender,
                "Newsletter": Newsletter,
                "HasExternalAuth": HasExternalAuth,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UserId"]) -> MetaOapg.properties.UserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SiteId"]) -> MetaOapg.properties.SiteId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Email"]) -> MetaOapg.properties.Email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Password"]) -> MetaOapg.properties.Password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["FirstName"]) -> MetaOapg.properties.FirstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["LastName"]) -> MetaOapg.properties.LastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PhoneNr"]) -> MetaOapg.properties.PhoneNr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["MobilePhoneNr"]) -> MetaOapg.properties.MobilePhoneNr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Company"]) -> MetaOapg.properties.Company: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["UserTypeId"]) -> MetaOapg.properties.UserTypeId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Address"]) -> MetaOapg.properties.Address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Address2"]) -> MetaOapg.properties.Address2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Address3"]) -> MetaOapg.properties.Address3: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["DoorCode"]) -> MetaOapg.properties.DoorCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PersonalId"]) -> MetaOapg.properties.PersonalId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Birthyear"]) -> MetaOapg.properties.Birthyear: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Zip"]) -> MetaOapg.properties.Zip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["City"]) -> MetaOapg.properties.City: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CareOf"]) -> MetaOapg.properties.CareOf: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Country"]) -> MetaOapg.properties.Country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CountryId"]) -> MetaOapg.properties.CountryId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Gender"]) -> MetaOapg.properties.Gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Newsletter"]) -> MetaOapg.properties.Newsletter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["HasExternalAuth"]) -> MetaOapg.properties.HasExternalAuth: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["UserId", "SiteId", "Email", "Password", "FirstName", "LastName", "PhoneNr", "MobilePhoneNr", "Company", "UserTypeId", "Address", "Address2", "Address3", "DoorCode", "PersonalId", "Birthyear", "Zip", "City", "CareOf", "Country", "CountryId", "Gender", "Newsletter", "HasExternalAuth", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UserId"]) -> typing.Union[MetaOapg.properties.UserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SiteId"]) -> typing.Union[MetaOapg.properties.SiteId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Email"]) -> typing.Union[MetaOapg.properties.Email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Password"]) -> typing.Union[MetaOapg.properties.Password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["FirstName"]) -> typing.Union[MetaOapg.properties.FirstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["LastName"]) -> typing.Union[MetaOapg.properties.LastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PhoneNr"]) -> typing.Union[MetaOapg.properties.PhoneNr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["MobilePhoneNr"]) -> typing.Union[MetaOapg.properties.MobilePhoneNr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Company"]) -> typing.Union[MetaOapg.properties.Company, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["UserTypeId"]) -> typing.Union[MetaOapg.properties.UserTypeId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Address"]) -> typing.Union[MetaOapg.properties.Address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Address2"]) -> typing.Union[MetaOapg.properties.Address2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Address3"]) -> typing.Union[MetaOapg.properties.Address3, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["DoorCode"]) -> typing.Union[MetaOapg.properties.DoorCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PersonalId"]) -> typing.Union[MetaOapg.properties.PersonalId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Birthyear"]) -> typing.Union[MetaOapg.properties.Birthyear, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Zip"]) -> typing.Union[MetaOapg.properties.Zip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["City"]) -> typing.Union[MetaOapg.properties.City, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CareOf"]) -> typing.Union[MetaOapg.properties.CareOf, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Country"]) -> typing.Union[MetaOapg.properties.Country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CountryId"]) -> typing.Union[MetaOapg.properties.CountryId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Gender"]) -> typing.Union[MetaOapg.properties.Gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Newsletter"]) -> typing.Union[MetaOapg.properties.Newsletter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["HasExternalAuth"]) -> typing.Union[MetaOapg.properties.HasExternalAuth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["UserId", "SiteId", "Email", "Password", "FirstName", "LastName", "PhoneNr", "MobilePhoneNr", "Company", "UserTypeId", "Address", "Address2", "Address3", "DoorCode", "PersonalId", "Birthyear", "Zip", "City", "CareOf", "Country", "CountryId", "Gender", "Newsletter", "HasExternalAuth", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        UserId: typing.Union[MetaOapg.properties.UserId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        SiteId: typing.Union[MetaOapg.properties.SiteId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Email: typing.Union[MetaOapg.properties.Email, str, schemas.Unset] = schemas.unset,
        Password: typing.Union[MetaOapg.properties.Password, str, schemas.Unset] = schemas.unset,
        FirstName: typing.Union[MetaOapg.properties.FirstName, str, schemas.Unset] = schemas.unset,
        LastName: typing.Union[MetaOapg.properties.LastName, str, schemas.Unset] = schemas.unset,
        PhoneNr: typing.Union[MetaOapg.properties.PhoneNr, str, schemas.Unset] = schemas.unset,
        MobilePhoneNr: typing.Union[MetaOapg.properties.MobilePhoneNr, str, schemas.Unset] = schemas.unset,
        Company: typing.Union[MetaOapg.properties.Company, str, schemas.Unset] = schemas.unset,
        UserTypeId: typing.Union[MetaOapg.properties.UserTypeId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Address: typing.Union[MetaOapg.properties.Address, str, schemas.Unset] = schemas.unset,
        Address2: typing.Union[MetaOapg.properties.Address2, str, schemas.Unset] = schemas.unset,
        Address3: typing.Union[MetaOapg.properties.Address3, str, schemas.Unset] = schemas.unset,
        DoorCode: typing.Union[MetaOapg.properties.DoorCode, str, schemas.Unset] = schemas.unset,
        PersonalId: typing.Union[MetaOapg.properties.PersonalId, str, schemas.Unset] = schemas.unset,
        Birthyear: typing.Union[MetaOapg.properties.Birthyear, str, schemas.Unset] = schemas.unset,
        Zip: typing.Union[MetaOapg.properties.Zip, str, schemas.Unset] = schemas.unset,
        City: typing.Union[MetaOapg.properties.City, str, schemas.Unset] = schemas.unset,
        CareOf: typing.Union[MetaOapg.properties.CareOf, str, schemas.Unset] = schemas.unset,
        Country: typing.Union[MetaOapg.properties.Country, str, schemas.Unset] = schemas.unset,
        CountryId: typing.Union[MetaOapg.properties.CountryId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        Gender: typing.Union[MetaOapg.properties.Gender, bool, schemas.Unset] = schemas.unset,
        Newsletter: typing.Union[MetaOapg.properties.Newsletter, bool, schemas.Unset] = schemas.unset,
        HasExternalAuth: typing.Union[MetaOapg.properties.HasExternalAuth, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserModelsWriteUserProfile':
        return super().__new__(
            cls,
            *_args,
            UserId=UserId,
            SiteId=SiteId,
            Email=Email,
            Password=Password,
            FirstName=FirstName,
            LastName=LastName,
            PhoneNr=PhoneNr,
            MobilePhoneNr=MobilePhoneNr,
            Company=Company,
            UserTypeId=UserTypeId,
            Address=Address,
            Address2=Address2,
            Address3=Address3,
            DoorCode=DoorCode,
            PersonalId=PersonalId,
            Birthyear=Birthyear,
            Zip=Zip,
            City=City,
            CareOf=CareOf,
            Country=Country,
            CountryId=CountryId,
            Gender=Gender,
            Newsletter=Newsletter,
            HasExternalAuth=HasExternalAuth,
            _configuration=_configuration,
            **kwargs,
        )
