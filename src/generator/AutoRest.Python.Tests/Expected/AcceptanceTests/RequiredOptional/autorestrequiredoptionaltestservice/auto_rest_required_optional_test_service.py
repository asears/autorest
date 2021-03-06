# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.implicit_operations import ImplicitOperations
from .operations.explicit_operations import ExplicitOperations
from . import models


class AutoRestRequiredOptionalTestServiceConfiguration(Configuration):
    """Configuration for AutoRestRequiredOptionalTestService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param required_global_path: number of items to skip
    :type required_global_path: str
    :param required_global_query: number of items to skip
    :type required_global_query: str
    :param optional_global_query: number of items to skip
    :type optional_global_query: int
    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, required_global_path, required_global_query, optional_global_query=None, base_url=None, filepath=None):

        if required_global_path is None:
            raise ValueError("Parameter 'required_global_path' must not be None.")
        if not isinstance(required_global_path, str):
            raise TypeError("Parameter 'required_global_path' must be str.")
        if required_global_query is None:
            raise ValueError("Parameter 'required_global_query' must not be None.")
        if not isinstance(required_global_query, str):
            raise TypeError("Parameter 'required_global_query' must be str.")
        if not base_url:
            base_url = 'http://localhost'

        super(AutoRestRequiredOptionalTestServiceConfiguration, self).__init__(base_url, filepath)

        self.add_user_agent('autorestrequiredoptionaltestservice/{}'.format(VERSION))

        self.required_global_path = required_global_path
        self.required_global_query = required_global_query
        self.optional_global_query = optional_global_query


class AutoRestRequiredOptionalTestService(object):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestRequiredOptionalTestServiceConfiguration

    :ivar implicit: Implicit operations
    :vartype implicit: .operations.ImplicitOperations
    :ivar explicit: Explicit operations
    :vartype explicit: .operations.ExplicitOperations

    :param required_global_path: number of items to skip
    :type required_global_path: str
    :param required_global_query: number of items to skip
    :type required_global_query: str
    :param optional_global_query: number of items to skip
    :type optional_global_query: int
    :param str base_url: Service URL
    :param str filepath: Existing config
    """

    def __init__(
            self, required_global_path, required_global_query, optional_global_query=None, base_url=None, filepath=None):

        self.config = AutoRestRequiredOptionalTestServiceConfiguration(required_global_path, required_global_query, optional_global_query, base_url, filepath)
        self._client = ServiceClient(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.implicit = ImplicitOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.explicit = ExplicitOperations(
            self._client, self.config, self._serialize, self._deserialize)
