# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.api_variant_product_id1_product_id2 import put  # noqa: E501
from openapi_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestAPIVariantProductId1ProductId2(ApiTestMixin, unittest.TestCase):
    """
    APIVariantProductId1ProductId2 unit test stubs
        Adds a product to an existing group  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = put.ApiForput(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200










if __name__ == '__main__':
    unittest.main()