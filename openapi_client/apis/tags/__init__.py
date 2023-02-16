# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    BRAND = "Brand"
    CATEGORY = "Category"
    MARKET = "Market"
    ORDER = "Order"
    PAGE_AREA = "PageArea"
    PAYMENT = "Payment"
    PRICE_LIST = "PriceList"
    PRODUCT = "Product"
    PRODUCT_PARAMETER = "ProductParameter"
    SHIPPING = "Shipping"
    SUPPLIER = "Supplier"
    USER = "User"
    VARIANT = "Variant"
