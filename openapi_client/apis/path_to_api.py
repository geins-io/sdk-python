import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.api_brand_id import APIBrandId
from openapi_client.apis.paths.api_brand_query import APIBrandQuery
from openapi_client.apis.paths.api_brand import APIBrand
from openapi_client.apis.paths.api_category_id import APICategoryId
from openapi_client.apis.paths.api_category_query import APICategoryQuery
from openapi_client.apis.paths.api_category import APICategory
from openapi_client.apis.paths.api_market_list import APIMarketList
from openapi_client.apis.paths.api_market_market_id import APIMarketMarketId
from openapi_client.apis.paths.api_order_query import APIOrderQuery
from openapi_client.apis.paths.api_order_id import APIOrderId
from openapi_client.apis.paths.api_order import APIOrder
from openapi_client.apis.paths.api_order_id_include import APIOrderIdInclude
from openapi_client.apis.paths.api_order_statuses import APIOrderStatuses
from openapi_client.apis.paths.api_order_id_status_status_transaction_id_secondary_transaction_id import APIOrderIdStatusStatusTransactionIdSecondaryTransactionId
from openapi_client.apis.paths.api_order_payment_detail_payment_detail_id_set_as_payed import APIOrderPaymentDetailPaymentDetailIdSetAsPayed
from openapi_client.apis.paths.api_order_capture_capture_id import APIOrderCaptureCaptureId
from openapi_client.apis.paths.api_order_capture_set_as_processed import APIOrderCaptureSetAsProcessed
from openapi_client.apis.paths.api_order_validate_creation import APIOrderValidateCreation
from openapi_client.apis.paths.api_order_refund_refund_id import APIOrderRefundRefundId
from openapi_client.apis.paths.api_order_refund_set_as_processed import APIOrderRefundSetAsProcessed
from openapi_client.apis.paths.api_order_id_comment import APIOrderIdComment
from openapi_client.apis.paths.api_order_id_transaction_data import APIOrderIdTransactionData
from openapi_client.apis.paths.api_page_area_family_list import APIPageAreaFamilyList
from openapi_client.apis.paths.api_page_area_family_family_id import APIPageAreaFamilyFamilyId
from openapi_client.apis.paths.api_page_area_name import APIPageAreaName
from openapi_client.apis.paths.api_page_area_family import APIPageAreaFamily
from openapi_client.apis.paths.api_page_area import APIPageArea
from openapi_client.apis.paths.api_payment_query import APIPaymentQuery
from openapi_client.apis.paths.api_price_list_list import APIPriceListList
from openapi_client.apis.paths.api_price_list_price import APIPriceListPrice
from openapi_client.apis.paths.api_product_product_id import APIProductProductId
from openapi_client.apis.paths.api_product_query import APIProductQuery
from openapi_client.apis.paths.api_product_query_page import APIProductQueryPage
from openapi_client.apis.paths.api_product import APIProduct
from openapi_client.apis.paths.api_product_product_id_category import APIProductProductIdCategory
from openapi_client.apis.paths.api_product_monitor_availability import APIProductMonitorAvailability
from openapi_client.apis.paths.api_product_item_item_id import APIProductItemItemId
from openapi_client.apis.paths.api_product_items import APIProductItems
from openapi_client.apis.paths.api_product_items_page import APIProductItemsPage
from openapi_client.apis.paths.api_product_product_id_item import APIProductProductIdItem
from openapi_client.apis.paths.api_product_stock import APIProductStock
from openapi_client.apis.paths.api_product_stock_query import APIProductStockQuery
from openapi_client.apis.paths.api_product_product_id_image_image_name import APIProductProductIdImageImageName
from openapi_client.apis.paths.api_product_feeds import APIProductFeeds
from openapi_client.apis.paths.api_product_relation_types import APIProductRelationTypes
from openapi_client.apis.paths.api_product_product_id_related_relation_type_id import APIProductProductIdRelatedRelationTypeId
from openapi_client.apis.paths.api_product_product_id_related import APIProductProductIdRelated
from openapi_client.apis.paths.api_product_parameter_id import APIProductParameterId
from openapi_client.apis.paths.api_product_parameter import APIProductParameter
from openapi_client.apis.paths.api_product_parameter_group_id import APIProductParameterGroupId
from openapi_client.apis.paths.api_product_parameter_group import APIProductParameterGroup
from openapi_client.apis.paths.api_product_parameter_value_id import APIProductParameterValueId
from openapi_client.apis.paths.api_product_parameter_value import APIProductParameterValue
from openapi_client.apis.paths.api_product_parameter_values import APIProductParameterValues
from openapi_client.apis.paths.api_product_parameter_predefined_value_id import APIProductParameterPredefinedValueId
from openapi_client.apis.paths.api_product_parameter_predefined_value import APIProductParameterPredefinedValue
from openapi_client.apis.paths.api_shipping_query import APIShippingQuery
from openapi_client.apis.paths.api_shipping_parcel_group import APIShippingParcelGroup
from openapi_client.apis.paths.api_supplier_id import APISupplierId
from openapi_client.apis.paths.api_supplier_query import APISupplierQuery
from openapi_client.apis.paths.api_supplier import APISupplier
from openapi_client.apis.paths.api_user_query import APIUserQuery
from openapi_client.apis.paths.api_user import APIUser
from openapi_client.apis.paths.api_user_email import APIUserEmail
from openapi_client.apis.paths.api_variant_labels import APIVariantLabels
from openapi_client.apis.paths.api_variant_product_id_variant_group import APIVariantProductIdVariantGroup
from openapi_client.apis.paths.api_variant_product_id1_product_id2 import APIVariantProductId1ProductId2
from openapi_client.apis.paths.api_variant_product_id import APIVariantProductId
from openapi_client.apis.paths.api_variant_group_group_id import APIVariantGroupGroupId
from openapi_client.apis.paths.api_variant_group import APIVariantGroup
from openapi_client.apis.paths.api_variant_group_group_id_product_id import APIVariantGroupGroupIdProductId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_BRAND_ID: APIBrandId,
        PathValues.API_BRAND_QUERY: APIBrandQuery,
        PathValues.API_BRAND: APIBrand,
        PathValues.API_CATEGORY_ID: APICategoryId,
        PathValues.API_CATEGORY_QUERY: APICategoryQuery,
        PathValues.API_CATEGORY: APICategory,
        PathValues.API_MARKET_LIST: APIMarketList,
        PathValues.API_MARKET_MARKET_ID: APIMarketMarketId,
        PathValues.API_ORDER_QUERY: APIOrderQuery,
        PathValues.API_ORDER_ID: APIOrderId,
        PathValues.API_ORDER: APIOrder,
        PathValues.API_ORDER_ID_INCLUDE: APIOrderIdInclude,
        PathValues.API_ORDER_STATUSES: APIOrderStatuses,
        PathValues.API_ORDER_ID_STATUS_STATUS_TRANSACTION_ID_SECONDARY_TRANSACTION_ID: APIOrderIdStatusStatusTransactionIdSecondaryTransactionId,
        PathValues.API_ORDER_PAYMENT_DETAIL_PAYMENT_DETAIL_ID_SET_AS_PAYED: APIOrderPaymentDetailPaymentDetailIdSetAsPayed,
        PathValues.API_ORDER_CAPTURE_CAPTURE_ID: APIOrderCaptureCaptureId,
        PathValues.API_ORDER_CAPTURE_SET_AS_PROCESSED: APIOrderCaptureSetAsProcessed,
        PathValues.API_ORDER_VALIDATE_CREATION: APIOrderValidateCreation,
        PathValues.API_ORDER_REFUND_REFUND_ID: APIOrderRefundRefundId,
        PathValues.API_ORDER_REFUND_SET_AS_PROCESSED: APIOrderRefundSetAsProcessed,
        PathValues.API_ORDER_ID_COMMENT: APIOrderIdComment,
        PathValues.API_ORDER_ID_TRANSACTION_DATA: APIOrderIdTransactionData,
        PathValues.API_PAGE_AREA_FAMILY_LIST: APIPageAreaFamilyList,
        PathValues.API_PAGE_AREA_FAMILY_FAMILY_ID: APIPageAreaFamilyFamilyId,
        PathValues.API_PAGE_AREA_NAME: APIPageAreaName,
        PathValues.API_PAGE_AREA_FAMILY: APIPageAreaFamily,
        PathValues.API_PAGE_AREA: APIPageArea,
        PathValues.API_PAYMENT_QUERY: APIPaymentQuery,
        PathValues.API_PRICE_LIST_LIST: APIPriceListList,
        PathValues.API_PRICE_LIST_PRICE: APIPriceListPrice,
        PathValues.API_PRODUCT_PRODUCT_ID: APIProductProductId,
        PathValues.API_PRODUCT_QUERY: APIProductQuery,
        PathValues.API_PRODUCT_QUERY_PAGE: APIProductQueryPage,
        PathValues.API_PRODUCT: APIProduct,
        PathValues.API_PRODUCT_PRODUCT_ID_CATEGORY: APIProductProductIdCategory,
        PathValues.API_PRODUCT_MONITOR_AVAILABILITY: APIProductMonitorAvailability,
        PathValues.API_PRODUCT_ITEM_ITEM_ID: APIProductItemItemId,
        PathValues.API_PRODUCT_ITEMS: APIProductItems,
        PathValues.API_PRODUCT_ITEMS_PAGE: APIProductItemsPage,
        PathValues.API_PRODUCT_PRODUCT_ID_ITEM: APIProductProductIdItem,
        PathValues.API_PRODUCT_STOCK: APIProductStock,
        PathValues.API_PRODUCT_STOCK_QUERY: APIProductStockQuery,
        PathValues.API_PRODUCT_PRODUCT_ID_IMAGE_IMAGE_NAME: APIProductProductIdImageImageName,
        PathValues.API_PRODUCT_FEEDS: APIProductFeeds,
        PathValues.API_PRODUCT_RELATION_TYPES: APIProductRelationTypes,
        PathValues.API_PRODUCT_PRODUCT_ID_RELATED_RELATION_TYPE_ID: APIProductProductIdRelatedRelationTypeId,
        PathValues.API_PRODUCT_PRODUCT_ID_RELATED: APIProductProductIdRelated,
        PathValues.API_PRODUCT_PARAMETER_ID: APIProductParameterId,
        PathValues.API_PRODUCT_PARAMETER: APIProductParameter,
        PathValues.API_PRODUCT_PARAMETER_GROUP_ID: APIProductParameterGroupId,
        PathValues.API_PRODUCT_PARAMETER_GROUP: APIProductParameterGroup,
        PathValues.API_PRODUCT_PARAMETER_VALUE_ID: APIProductParameterValueId,
        PathValues.API_PRODUCT_PARAMETER_VALUE: APIProductParameterValue,
        PathValues.API_PRODUCT_PARAMETER_VALUES: APIProductParameterValues,
        PathValues.API_PRODUCT_PARAMETER_PREDEFINED_VALUE_ID: APIProductParameterPredefinedValueId,
        PathValues.API_PRODUCT_PARAMETER_PREDEFINED_VALUE: APIProductParameterPredefinedValue,
        PathValues.API_SHIPPING_QUERY: APIShippingQuery,
        PathValues.API_SHIPPING_PARCEL_GROUP: APIShippingParcelGroup,
        PathValues.API_SUPPLIER_ID: APISupplierId,
        PathValues.API_SUPPLIER_QUERY: APISupplierQuery,
        PathValues.API_SUPPLIER: APISupplier,
        PathValues.API_USER_QUERY: APIUserQuery,
        PathValues.API_USER: APIUser,
        PathValues.API_USER_EMAIL: APIUserEmail,
        PathValues.API_VARIANT_LABELS: APIVariantLabels,
        PathValues.API_VARIANT_PRODUCT_ID_VARIANT_GROUP: APIVariantProductIdVariantGroup,
        PathValues.API_VARIANT_PRODUCT_ID1_PRODUCT_ID2: APIVariantProductId1ProductId2,
        PathValues.API_VARIANT_PRODUCT_ID: APIVariantProductId,
        PathValues.API_VARIANT_GROUP_GROUP_ID: APIVariantGroupGroupId,
        PathValues.API_VARIANT_GROUP: APIVariantGroup,
        PathValues.API_VARIANT_GROUP_GROUP_ID_PRODUCT_ID: APIVariantGroupGroupIdProductId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_BRAND_ID: APIBrandId,
        PathValues.API_BRAND_QUERY: APIBrandQuery,
        PathValues.API_BRAND: APIBrand,
        PathValues.API_CATEGORY_ID: APICategoryId,
        PathValues.API_CATEGORY_QUERY: APICategoryQuery,
        PathValues.API_CATEGORY: APICategory,
        PathValues.API_MARKET_LIST: APIMarketList,
        PathValues.API_MARKET_MARKET_ID: APIMarketMarketId,
        PathValues.API_ORDER_QUERY: APIOrderQuery,
        PathValues.API_ORDER_ID: APIOrderId,
        PathValues.API_ORDER: APIOrder,
        PathValues.API_ORDER_ID_INCLUDE: APIOrderIdInclude,
        PathValues.API_ORDER_STATUSES: APIOrderStatuses,
        PathValues.API_ORDER_ID_STATUS_STATUS_TRANSACTION_ID_SECONDARY_TRANSACTION_ID: APIOrderIdStatusStatusTransactionIdSecondaryTransactionId,
        PathValues.API_ORDER_PAYMENT_DETAIL_PAYMENT_DETAIL_ID_SET_AS_PAYED: APIOrderPaymentDetailPaymentDetailIdSetAsPayed,
        PathValues.API_ORDER_CAPTURE_CAPTURE_ID: APIOrderCaptureCaptureId,
        PathValues.API_ORDER_CAPTURE_SET_AS_PROCESSED: APIOrderCaptureSetAsProcessed,
        PathValues.API_ORDER_VALIDATE_CREATION: APIOrderValidateCreation,
        PathValues.API_ORDER_REFUND_REFUND_ID: APIOrderRefundRefundId,
        PathValues.API_ORDER_REFUND_SET_AS_PROCESSED: APIOrderRefundSetAsProcessed,
        PathValues.API_ORDER_ID_COMMENT: APIOrderIdComment,
        PathValues.API_ORDER_ID_TRANSACTION_DATA: APIOrderIdTransactionData,
        PathValues.API_PAGE_AREA_FAMILY_LIST: APIPageAreaFamilyList,
        PathValues.API_PAGE_AREA_FAMILY_FAMILY_ID: APIPageAreaFamilyFamilyId,
        PathValues.API_PAGE_AREA_NAME: APIPageAreaName,
        PathValues.API_PAGE_AREA_FAMILY: APIPageAreaFamily,
        PathValues.API_PAGE_AREA: APIPageArea,
        PathValues.API_PAYMENT_QUERY: APIPaymentQuery,
        PathValues.API_PRICE_LIST_LIST: APIPriceListList,
        PathValues.API_PRICE_LIST_PRICE: APIPriceListPrice,
        PathValues.API_PRODUCT_PRODUCT_ID: APIProductProductId,
        PathValues.API_PRODUCT_QUERY: APIProductQuery,
        PathValues.API_PRODUCT_QUERY_PAGE: APIProductQueryPage,
        PathValues.API_PRODUCT: APIProduct,
        PathValues.API_PRODUCT_PRODUCT_ID_CATEGORY: APIProductProductIdCategory,
        PathValues.API_PRODUCT_MONITOR_AVAILABILITY: APIProductMonitorAvailability,
        PathValues.API_PRODUCT_ITEM_ITEM_ID: APIProductItemItemId,
        PathValues.API_PRODUCT_ITEMS: APIProductItems,
        PathValues.API_PRODUCT_ITEMS_PAGE: APIProductItemsPage,
        PathValues.API_PRODUCT_PRODUCT_ID_ITEM: APIProductProductIdItem,
        PathValues.API_PRODUCT_STOCK: APIProductStock,
        PathValues.API_PRODUCT_STOCK_QUERY: APIProductStockQuery,
        PathValues.API_PRODUCT_PRODUCT_ID_IMAGE_IMAGE_NAME: APIProductProductIdImageImageName,
        PathValues.API_PRODUCT_FEEDS: APIProductFeeds,
        PathValues.API_PRODUCT_RELATION_TYPES: APIProductRelationTypes,
        PathValues.API_PRODUCT_PRODUCT_ID_RELATED_RELATION_TYPE_ID: APIProductProductIdRelatedRelationTypeId,
        PathValues.API_PRODUCT_PRODUCT_ID_RELATED: APIProductProductIdRelated,
        PathValues.API_PRODUCT_PARAMETER_ID: APIProductParameterId,
        PathValues.API_PRODUCT_PARAMETER: APIProductParameter,
        PathValues.API_PRODUCT_PARAMETER_GROUP_ID: APIProductParameterGroupId,
        PathValues.API_PRODUCT_PARAMETER_GROUP: APIProductParameterGroup,
        PathValues.API_PRODUCT_PARAMETER_VALUE_ID: APIProductParameterValueId,
        PathValues.API_PRODUCT_PARAMETER_VALUE: APIProductParameterValue,
        PathValues.API_PRODUCT_PARAMETER_VALUES: APIProductParameterValues,
        PathValues.API_PRODUCT_PARAMETER_PREDEFINED_VALUE_ID: APIProductParameterPredefinedValueId,
        PathValues.API_PRODUCT_PARAMETER_PREDEFINED_VALUE: APIProductParameterPredefinedValue,
        PathValues.API_SHIPPING_QUERY: APIShippingQuery,
        PathValues.API_SHIPPING_PARCEL_GROUP: APIShippingParcelGroup,
        PathValues.API_SUPPLIER_ID: APISupplierId,
        PathValues.API_SUPPLIER_QUERY: APISupplierQuery,
        PathValues.API_SUPPLIER: APISupplier,
        PathValues.API_USER_QUERY: APIUserQuery,
        PathValues.API_USER: APIUser,
        PathValues.API_USER_EMAIL: APIUserEmail,
        PathValues.API_VARIANT_LABELS: APIVariantLabels,
        PathValues.API_VARIANT_PRODUCT_ID_VARIANT_GROUP: APIVariantProductIdVariantGroup,
        PathValues.API_VARIANT_PRODUCT_ID1_PRODUCT_ID2: APIVariantProductId1ProductId2,
        PathValues.API_VARIANT_PRODUCT_ID: APIVariantProductId,
        PathValues.API_VARIANT_GROUP_GROUP_ID: APIVariantGroupGroupId,
        PathValues.API_VARIANT_GROUP: APIVariantGroup,
        PathValues.API_VARIANT_GROUP_GROUP_ID_PRODUCT_ID: APIVariantGroupGroupIdProductId,
    }
)
