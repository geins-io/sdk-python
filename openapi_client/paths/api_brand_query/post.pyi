# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from openapi_client import api_client, exceptions
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

from openapi_client.model.brand_models_read_brand import BrandModelsReadBrand
from openapi_client.model.brand_models_brand_query import BrandModelsBrandQuery

# body param
SchemaForRequestBodyApplicationJson = BrandModelsBrandQuery
SchemaForRequestBodyTextJson = BrandModelsBrandQuery
SchemaForRequestBodyApplicationXml = BrandModelsBrandQuery
SchemaForRequestBodyTextXml = BrandModelsBrandQuery
SchemaForRequestBodyApplicationXWwwFormUrlencoded = BrandModelsBrandQuery


request_body_query = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaForRequestBodyTextJson),
        'application/xml': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXml),
        'text/xml': api_client.MediaType(
            schema=SchemaForRequestBodyTextXml),
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
    required=True,
)


class SchemaFor200ResponseBodyApplicationJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['BrandModelsReadBrand']:
            return BrandModelsReadBrand

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['BrandModelsReadBrand'], typing.List['BrandModelsReadBrand']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'BrandModelsReadBrand':
        return super().__getitem__(i)


class SchemaFor200ResponseBodyTextJson(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['BrandModelsReadBrand']:
            return BrandModelsReadBrand

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['BrandModelsReadBrand'], typing.List['BrandModelsReadBrand']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaFor200ResponseBodyTextJson':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'BrandModelsReadBrand':
        return super().__getitem__(i)


class SchemaFor200ResponseBodyApplicationXml(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['BrandModelsReadBrand']:
            return BrandModelsReadBrand

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['BrandModelsReadBrand'], typing.List['BrandModelsReadBrand']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaFor200ResponseBodyApplicationXml':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'BrandModelsReadBrand':
        return super().__getitem__(i)


class SchemaFor200ResponseBodyTextXml(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['BrandModelsReadBrand']:
            return BrandModelsReadBrand

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['BrandModelsReadBrand'], typing.List['BrandModelsReadBrand']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SchemaFor200ResponseBodyTextXml':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'BrandModelsReadBrand':
        return super().__getitem__(i)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
        SchemaFor200ResponseBodyTextJson,
        SchemaFor200ResponseBodyApplicationXml,
        SchemaFor200ResponseBodyTextXml,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJson),
        'application/xml': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationXml),
        'text/xml': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextXml),
    },
)
_all_accept_content_types = (
    'application/json',
    'text/json',
    'application/xml',
    'text/xml',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _query_brands_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _query_brands_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyTextJson,],
        content_type: typing_extensions.Literal["text/json"],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _query_brands_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationXml,],
        content_type: typing_extensions.Literal["application/xml"],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _query_brands_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyTextXml,],
        content_type: typing_extensions.Literal["text/xml"],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _query_brands_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _query_brands_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationXml,SchemaForRequestBodyTextXml,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def _query_brands_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationXml,SchemaForRequestBodyTextXml,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _query_brands_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationXml,SchemaForRequestBodyTextXml,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _query_brands_oapg(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationXml,SchemaForRequestBodyTextXml,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Query brands
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_query.serialize(body, content_type)
        _headers.add('Content-Type', content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class QueryBrands(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def query_brands(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def query_brands(
        self,
        body: typing.Union[SchemaForRequestBodyTextJson,],
        content_type: typing_extensions.Literal["text/json"],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def query_brands(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationXml,],
        content_type: typing_extensions.Literal["application/xml"],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def query_brands(
        self,
        body: typing.Union[SchemaForRequestBodyTextXml,],
        content_type: typing_extensions.Literal["text/xml"],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def query_brands(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def query_brands(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationXml,SchemaForRequestBodyTextXml,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def query_brands(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationXml,SchemaForRequestBodyTextXml,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def query_brands(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationXml,SchemaForRequestBodyTextXml,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def query_brands(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationXml,SchemaForRequestBodyTextXml,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._query_brands_oapg(
            body=body,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyTextJson,],
        content_type: typing_extensions.Literal["text/json"],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationXml,],
        content_type: typing_extensions.Literal["application/xml"],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyTextXml,],
        content_type: typing_extensions.Literal["text/xml"],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: typing_extensions.Literal["application/x-www-form-urlencoded"],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationXml,SchemaForRequestBodyTextXml,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationXml,SchemaForRequestBodyTextXml,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationXml,SchemaForRequestBodyTextXml,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,SchemaForRequestBodyTextJson,SchemaForRequestBodyApplicationXml,SchemaForRequestBodyTextXml,SchemaForRequestBodyApplicationXWwwFormUrlencoded,],
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._query_brands_oapg(
            body=body,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


