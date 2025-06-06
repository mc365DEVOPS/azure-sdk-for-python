# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.apimanagement.aio import ApiManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestApiManagementReportsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ApiManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_reports_list_by_api(self, resource_group):
        response = self.client.reports.list_by_api(
            resource_group_name=resource_group.name,
            service_name="str",
            filter="str",
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_reports_list_by_user(self, resource_group):
        response = self.client.reports.list_by_user(
            resource_group_name=resource_group.name,
            service_name="str",
            filter="str",
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_reports_list_by_operation(self, resource_group):
        response = self.client.reports.list_by_operation(
            resource_group_name=resource_group.name,
            service_name="str",
            filter="str",
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_reports_list_by_product(self, resource_group):
        response = self.client.reports.list_by_product(
            resource_group_name=resource_group.name,
            service_name="str",
            filter="str",
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_reports_list_by_geo(self, resource_group):
        response = self.client.reports.list_by_geo(
            resource_group_name=resource_group.name,
            service_name="str",
            filter="str",
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_reports_list_by_subscription(self, resource_group):
        response = self.client.reports.list_by_subscription(
            resource_group_name=resource_group.name,
            service_name="str",
            filter="str",
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_reports_list_by_time(self, resource_group):
        response = self.client.reports.list_by_time(
            resource_group_name=resource_group.name,
            service_name="str",
            filter="str",
            interval="1 day, 0:00:00",
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_reports_list_by_request(self, resource_group):
        response = self.client.reports.list_by_request(
            resource_group_name=resource_group.name,
            service_name="str",
            filter="str",
            api_version="2024-05-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
