# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.recoveryservicessiterecovery import SiteRecoveryManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSiteRecoveryManagementReplicationProtectableItemsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(SiteRecoveryManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_replication_protectable_items_list_by_replication_protection_containers(self, resource_group):
        response = self.client.replication_protectable_items.list_by_replication_protection_containers(
            fabric_name="str",
            protection_container_name="str",
            api_version="2025-01-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_replication_protectable_items_get(self, resource_group):
        response = self.client.replication_protectable_items.get(
            fabric_name="str",
            protection_container_name="str",
            protectable_item_name="str",
            api_version="2025-01-01",
        )

        # please add some check logic here by yourself
        # ...
