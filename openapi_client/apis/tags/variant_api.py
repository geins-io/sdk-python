# coding: utf-8

"""
    Geins Management API

     Geins Management API is an RESTful api to power your applications who manages your geins services. Geins provides an easy-to-use and scalable solution for managing all aspects of an online store, from product listings and customer information to order processing and payment transactions.   :::tip With this API, you can build custom applications and integrate with third-party systems, dashboards and other bussiness logic apps. :::    ## Getting started Once you have created an account, you can start using the Management API by creating an `API key`. You can create as many API keys as you need. Each `API key` is connected to a specific account so you can keep track of operations and manage keys. You can find your `API key` in the `geins merchant center`.   ### Fast track Use one of our [SDKs](https://docs.geins.io/docs/sdk/introduction) to get started quickly. The SDKs are available for the most popular programming languages and frameworks.  Or, if you prefer to just take it for a test run:  [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/25895885-aaf6598f-1a7c-4949-85d7-ba846c42d553?action=collection%2Ffork&collection-url=entityId%3D25895885-aaf6598f-1a7c-4949-85d7-ba846c42d553%26entityType%3Dcollection%26workspaceId%3Da2a179ce-158e-46b0-8d06-e9640f45112c)  ### Authentication Two authentication methods are supported:   - `API Key`   - `Basic Auth`   # noqa: E501

    The version of the OpenAPI document: v1.7
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api_variant_group_group_id_product_id.put import AddProductToVariantGroup
from openapi_client.paths.api_variant_product_id1_product_id2.put import AddProductToVariantGroupByProductId
from openapi_client.paths.api_variant_group.post import CreateVariantGroup
from openapi_client.paths.api_variant_product_id_variant_group.post import CreateVariantGroupWithProduct
from openapi_client.paths.api_variant_group_group_id.delete import DeleteVariantGroup
from openapi_client.paths.api_variant_product_id_variant_group.delete import DeleteVariantGroupByProductId
from openapi_client.paths.api_variant_group_group_id.get import GetVariantGroup
from openapi_client.paths.api_variant_product_id_variant_group.get import GetVariantGroupByProductId
from openapi_client.paths.api_variant_labels.get import GetVariantLabels
from openapi_client.paths.api_variant_product_id.delete import RemoveProductFromVariantGroup
from openapi_client.paths.api_variant_product_id.put import UpdateVariant
from openapi_client.paths.api_variant_group_group_id.put import UpdateVariantGroup


class VariantApi(
    AddProductToVariantGroup,
    AddProductToVariantGroupByProductId,
    CreateVariantGroup,
    CreateVariantGroupWithProduct,
    DeleteVariantGroup,
    DeleteVariantGroupByProductId,
    GetVariantGroup,
    GetVariantGroupByProductId,
    GetVariantLabels,
    RemoveProductFromVariantGroup,
    UpdateVariant,
    UpdateVariantGroup,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass