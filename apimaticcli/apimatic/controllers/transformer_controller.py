# -*- coding: utf-8 -*-

"""
    apimatic.controllers.transformer_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.custom_header_auth import CustomHeaderAuth

class TransformerController(BaseController):

    """A Controller to access Endpoints in the apimatic API."""


    def transform_from_file(self,
                            file,
                            format):
        """Does a POST request to /transform.

        Transform an API description from a file.

        Args:
            file (string): TODO: type description here. Example: 
            format (string): TODO: type description here. Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/transform'
        _query_parameters = {
            'format': format
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare files
        _files = {
            'file': file
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, files=_files)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def transform_from_url(self,
                           description_url,
                           format):
        """Does a GET request to /transform.

        Transform an API description from a URL.

        Args:
            description_url (string): TODO: type description here. Example: 
            format (string): TODO: type description here. Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/transform'
        _query_parameters = {
            'descriptionUrl': description_url,
            'format': format
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def transform_from_key(self,
                           api_key,
                           format):
        """Does a GET request to /transform.

        Transform an API description from an API key.

        Args:
            api_key (string): TODO: type description here. Example: 
            format (string): TODO: type description here. Example: 

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/transform'
        _query_parameters = {
            'apiKey': api_key,
            'format': format
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body