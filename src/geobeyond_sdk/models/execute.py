# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .subscriber import Subscriber


class Response(Enum):
    """An enumeration representing different categories.

    :cvar RAW: "raw"
    :vartype RAW: str
    :cvar DOCUMENT: "document"
    :vartype DOCUMENT: str
    """

    RAW = "raw"
    DOCUMENT = "document"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Response._member_map_.values()))


@JsonMap({})
class Execute(BaseModel):
    """Execute

    :param inputs: inputs, defaults to None
    :type inputs: any, optional
    :param outputs: outputs, defaults to None
    :type outputs: any, optional
    :param response: response, defaults to None
    :type response: Response, optional
    :param subscriber: Optional URIs for callbacks for this job. Support for this parameter is not required and the parameter may be removed from the API definition, if conformance class **'callback'** is not listed in the conformance declaration under `/conformance`., defaults to None
    :type subscriber: Subscriber, optional
    """

    def __init__(
        self,
        inputs: any = None,
        outputs: any = None,
        response: Response = None,
        subscriber: Subscriber = None,
    ):
        """Execute

        :param inputs: inputs, defaults to None
        :type inputs: any, optional
        :param outputs: outputs, defaults to None
        :type outputs: any, optional
        :param response: response, defaults to None
        :type response: Response, optional
        :param subscriber: Optional URIs for callbacks for this job. Support for this parameter is not required and the parameter may be removed from the API definition, if conformance class **'callback'** is not listed in the conformance declaration under `/conformance`., defaults to None
        :type subscriber: Subscriber, optional
        """
        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs
        if response is not None:
            self.response = self._enum_matching(response, Response.list(), "response")
        if subscriber is not None:
            self.subscriber = self._define_object(subscriber, Subscriber)
