# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.databasewatcher import DatabaseWatcherMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-databasewatcher
# USAGE
    python targets_delete_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DatabaseWatcherMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    client.targets.delete(
        resource_group_name="apiTest-ddat4p",
        watcher_name="databasemo3ej9ih",
        target_name="monitoringh22eed",
    )


# x-ms-original-file: 2025-01-02/Targets_Delete_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
