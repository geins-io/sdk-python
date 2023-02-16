import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.brand_api import BrandApi
from openapi_client.apis.tags.category_api import CategoryApi
from openapi_client.apis.tags.market_api import MarketApi
from openapi_client.apis.tags.order_api import OrderApi
from openapi_client.apis.tags.page_area_api import PageAreaApi
from openapi_client.apis.tags.payment_api import PaymentApi
from openapi_client.apis.tags.price_list_api import PriceListApi
from openapi_client.apis.tags.product_api import ProductApi
from openapi_client.apis.tags.product_parameter_api import ProductParameterApi
from openapi_client.apis.tags.shipping_api import ShippingApi
from openapi_client.apis.tags.supplier_api import SupplierApi
from openapi_client.apis.tags.user_api import UserApi
from openapi_client.apis.tags.variant_api import VariantApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BRAND: BrandApi,
        TagValues.CATEGORY: CategoryApi,
        TagValues.MARKET: MarketApi,
        TagValues.ORDER: OrderApi,
        TagValues.PAGE_AREA: PageAreaApi,
        TagValues.PAYMENT: PaymentApi,
        TagValues.PRICE_LIST: PriceListApi,
        TagValues.PRODUCT: ProductApi,
        TagValues.PRODUCT_PARAMETER: ProductParameterApi,
        TagValues.SHIPPING: ShippingApi,
        TagValues.SUPPLIER: SupplierApi,
        TagValues.USER: UserApi,
        TagValues.VARIANT: VariantApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BRAND: BrandApi,
        TagValues.CATEGORY: CategoryApi,
        TagValues.MARKET: MarketApi,
        TagValues.ORDER: OrderApi,
        TagValues.PAGE_AREA: PageAreaApi,
        TagValues.PAYMENT: PaymentApi,
        TagValues.PRICE_LIST: PriceListApi,
        TagValues.PRODUCT: ProductApi,
        TagValues.PRODUCT_PARAMETER: ProductParameterApi,
        TagValues.SHIPPING: ShippingApi,
        TagValues.SUPPLIER: SupplierApi,
        TagValues.USER: UserApi,
        TagValues.VARIANT: VariantApi,
    }
)
