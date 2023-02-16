# coding: utf-8

"""
    Geins Management API

     Geins Management API is an RESTful api to power your applications who manages your geins services. Geins provides an easy-to-use and scalable solution for managing all aspects of an online store, from product listings and customer information to order processing and payment transactions.   :::tip With this API, you can build custom applications and integrate with third-party systems, dashboards and other bussiness logic apps. :::    ## Getting started Once you have created an account, you can start using the Management API by creating an `API key`. You can create as many API keys as you need. Each `API key` is connected to a specific account so you can keep track of operations and manage keys. You can find your `API key` in the `geins merchant center`.   ### Fast track Use one of our [SDKs](https://docs.geins.io/docs/sdk/introduction) to get started quickly. The SDKs are available for the most popular programming languages and frameworks.  Or, if you prefer to just take it for a test run:  [![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/25895885-aaf6598f-1a7c-4949-85d7-ba846c42d553?action=collection%2Ffork&collection-url=entityId%3D25895885-aaf6598f-1a7c-4949-85d7-ba846c42d553%26entityType%3Dcollection%26workspaceId%3Da2a179ce-158e-46b0-8d06-e9640f45112c)  ### Authentication Two authentication methods are supported:   - `API Key`   - `Basic Auth`   # noqa: E501

    The version of the OpenAPI document: v1.7
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api_product_monitor_availability.post import AddAvailabilityMonitor
from openapi_client.paths.api_product_product_id_category.put import AddCategoryToProduct
from openapi_client.paths.api_product_product_id_image_image_name.put import AddImageToProduct
from openapi_client.paths.api_product_product_id_related.put import AddRelatedProductsToProduct
from openapi_client.paths.api_product_items.put import BatchUpdateProductItems
from openapi_client.paths.api_product_stock.put import BatchUpdateStockValues
from openapi_client.paths.api_product.post import CreateProduct
from openapi_client.paths.api_product_product_id_item.post import CreateProductItems
from openapi_client.paths.api_product_product_id.get import GetProductById
from openapi_client.paths.api_product_item_item_id.get import GetProductItemById
from openapi_client.paths.api_product_product_id_related_relation_type_id.put import LinkRelatedProductsByRelationId
from openapi_client.paths.api_product_items_page.get import ListAllProductItemsPaged
from openapi_client.paths.api_product_feeds.get import ListFeeds
from openapi_client.paths.api_product_items.get import ListProductItems
from openapi_client.paths.api_product_relation_types.get import ListProductRelationTypes
from openapi_client.paths.api_product_query.post import QueryProducts
from openapi_client.paths.api_product_query_page.post import QueryProductsPaged
from openapi_client.paths.api_product_stock_query.post import QueryStock
from openapi_client.paths.api_product_product_id.put import UpdateProduct
from openapi_client.paths.api_product_item_item_id.put import UpdateProductItem


class ProductApi(
    AddAvailabilityMonitor,
    AddCategoryToProduct,
    AddImageToProduct,
    AddRelatedProductsToProduct,
    BatchUpdateProductItems,
    BatchUpdateStockValues,
    CreateProduct,
    CreateProductItems,
    GetProductById,
    GetProductItemById,
    LinkRelatedProductsByRelationId,
    ListAllProductItemsPaged,
    ListFeeds,
    ListProductItems,
    ListProductRelationTypes,
    QueryProducts,
    QueryProductsPaged,
    QueryStock,
    UpdateProduct,
    UpdateProductItem,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass