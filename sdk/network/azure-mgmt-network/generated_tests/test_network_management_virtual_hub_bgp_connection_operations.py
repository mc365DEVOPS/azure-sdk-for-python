# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.network import NetworkManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkManagementVirtualHubBgpConnectionOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_hub_bgp_connection_get(self, resource_group):
        response = self.client.virtual_hub_bgp_connection.get(
            resource_group_name=resource_group.name,
            virtual_hub_name="str",
            connection_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_hub_bgp_connection_begin_create_or_update(self, resource_group):
        response = self.client.virtual_hub_bgp_connection.begin_create_or_update(
            resource_group_name=resource_group.name,
            virtual_hub_name="str",
            connection_name="str",
            parameters={
                "connectionState": "str",
                "etag": "str",
                "hubVirtualNetworkConnection": {"id": "str"},
                "id": "str",
                "name": "str",
                "peerAsn": 0,
                "peerIp": "str",
                "provisioningState": "str",
                "type": "str",
            },
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_hub_bgp_connection_begin_delete(self, resource_group):
        response = self.client.virtual_hub_bgp_connection.begin_delete(
            resource_group_name=resource_group.name,
            virtual_hub_name="str",
            connection_name="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
