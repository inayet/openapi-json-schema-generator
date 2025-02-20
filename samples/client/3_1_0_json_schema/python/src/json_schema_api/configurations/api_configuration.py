# coding: utf-8

"""
    Example
    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import copy
from http import client as http_client
import logging
import multiprocessing
import sys
import typing
import typing_extensions

import urllib3

from json_schema_api import exceptions
from json_schema_api.servers import server_0

# the server to use at each openapi document json path
ServerInfo = typing.TypedDict(
    'ServerInfo',
    {
        'servers/0': server_0.Server0,
    },
    total=False
)


class ServerIndexInfoRequired(typing.TypedDict):
    servers: typing.Literal[0]

ServerIndexInfoOptional = typing.TypedDict(
    'ServerIndexInfoOptional',
    {
    },
    total=False
)


class ServerIndexInfo(ServerIndexInfoRequired, ServerIndexInfoOptional):
    """
    the default server_index to use at each openapi document json path
    the fallback value is stored in the 'servers' key
    """


class ApiConfiguration(object):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator

    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    Do not edit the class manually.

    :param server_info: the servers that can be used to make endpoint calls
    :param server_index_info: index to servers configuration
    """

    def __init__(
        self,
        server_info: typing.Optional[ServerInfo] = None,
        server_index_info: typing.Optional[ServerIndexInfo] = None,
    ):
        """Constructor
        """
        # Authentication Settings
        self.security_scheme_info: typing.Dict[str, typing.Any] = {}
        self.security_index_info = {'security': 0}
        # Server Info
        self.server_info: ServerInfo = server_info or {
            'servers/0': server_0.Server0(),
        }
        self.server_index_info: ServerIndexInfo = server_index_info or {'servers': 0}
        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("json_schema_api")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        self.debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = None
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        """urllib3 connection pool's maximum number of connections saved
           per pool. urllib3 uses 1 connection as default value, but this is
           not the best value when you are making a lot of possibly parallel
           requests to the same host, which is often the case here.
           cpu_count * 5 is used as default value to increase performance.
        """

        self.proxy = None
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = None
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        # Options to pass down to the underlying urllib3 socket
        self.socket_options = None

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on http_client debug
            http_client.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off http_client debug
            http_client.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 1.0.0\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)

    def get_server_url(
        self,
        key_prefix: typing.Literal[
            "servers",
        ],
        index: typing.Optional[int],
    ) -> str:
        """Gets host URL based on the index
        :param index: array index of the host settings
        :return: URL based on host settings
        """
        if index:
            used_index = index
        else:
            try:
                used_index = self.server_index_info[key_prefix]
            except KeyError:
                # fallback and use the default index
                used_index = self.server_index_info.get("servers", 0)
        server_info_key = typing.cast(
            typing.Literal[
                "servers/0",
            ],
            f"{key_prefix}/{used_index}"
        )
        try:
            server = self.server_info[server_info_key]
        except KeyError as ex:
            raise ex
        return server.url
