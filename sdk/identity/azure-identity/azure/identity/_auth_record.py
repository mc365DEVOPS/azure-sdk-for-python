# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import json


SUPPORTED_VERSIONS = {"1.0"}


class AuthenticationRecord:
    """Non-secret account information for an authenticated user

    This class enables :class:`DeviceCodeCredential` and :class:`InteractiveBrowserCredential` to access
    previously cached authentication data. Applications shouldn't construct instances of this class. They should
    instead acquire one from a credential's **authenticate** method, such as
    :func:`InteractiveBrowserCredential.authenticate`. See the user_authentication sample for more details.

    :param str tenant_id: The tenant the account should authenticate in.
    :param str client_id: The client ID of the application which performed the original authentication.
    :param str authority: The authority host used to authenticate the account.
    :param str home_account_id: A unique identifier of the account.
    :param str username: The user principal or service principal name of the account.
    """

    def __init__(self, tenant_id: str, client_id: str, authority: str, home_account_id: str, username: str) -> None:
        self._authority = authority
        self._client_id = client_id
        self._home_account_id = home_account_id
        self._tenant_id = tenant_id
        self._username = username

    @property
    def authority(self) -> str:
        """The authority host used to authenticate the account.

        :return: The authority host used to authenticate the account.
        :rtype: str
        """
        return self._authority

    @property
    def client_id(self) -> str:
        """The client ID of the application which performed the original authentication.

        :return: The client ID of the application which performed the original authentication.
        :rtype: str
        """
        return self._client_id

    @property
    def home_account_id(self) -> str:
        """A unique identifier of the account.

        :return: A unique identifier of the account.
        :rtype: str
        """
        return self._home_account_id

    @property
    def tenant_id(self) -> str:
        """The tenant the account should authenticate in.

        :return: The tenant the account should authenticate in.
        :rtype: str
        """
        return self._tenant_id

    @property
    def username(self) -> str:
        """The user principal or service principal name of the account.

        :return: The user principal or service principal name of the account.
        :rtype: str
        """
        return self._username

    @classmethod
    def deserialize(cls, data: str) -> "AuthenticationRecord":
        """Deserialize a record.

        :param str data: A serialized record.
        :return: The deserialized record.
        :rtype: ~azure.identity.AuthenticationRecord
        """

        deserialized = json.loads(data)

        version = deserialized.get("version")
        if version not in SUPPORTED_VERSIONS:
            raise ValueError(
                'Unexpected version "{}". This package supports these versions: {}'.format(version, SUPPORTED_VERSIONS)
            )

        return cls(
            authority=deserialized["authority"],
            client_id=deserialized["clientId"],
            home_account_id=deserialized["homeAccountId"],
            tenant_id=deserialized["tenantId"],
            username=deserialized["username"],
        )

    def serialize(self) -> str:
        """Serialize the record.

        :return: The serialized record.
        :rtype: str
        """

        record = {
            "authority": self._authority,
            "clientId": self._client_id,
            "homeAccountId": self._home_account_id,
            "tenantId": self._tenant_id,
            "username": self._username,
            "version": "1.0",
        }

        return json.dumps(record)
