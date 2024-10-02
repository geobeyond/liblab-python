# This file was generated by liblab | https://liblab.com/

from typing import Any
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class StacService(BaseService):

    @cast_models
    def get_stac_catalog(self) -> Any:
        """SpatioTemporal Asset Catalog

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        serialized_request = (
            Serializer(f"{self.base_url}/stac", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return response