# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"type_": "type", "var_base": "varBase"})
class Link2(BaseModel):
    """Link2

    :param href: Supplies the URI to a remote resource (or resource fragment).
    :type href: str
    :param rel: The type or semantics of the relation.
    :type rel: str
    :param type_: A hint indicating what the media type of the result of dereferencing the link should be., defaults to None
    :type type_: str, optional
    :param templated: This flag set to true if the link is a URL template., defaults to None
    :type templated: bool, optional
    :param var_base: A base path to retrieve semantic information about the variables used in URL template., defaults to None
    :type var_base: str, optional
    :param hreflang: A hint indicating what the language of the result of dereferencing the link should be., defaults to None
    :type hreflang: str, optional
    :param title: Used to label the destination of a link such that it can be used as a human-readable identifier., defaults to None
    :type title: str, optional
    :param length: length, defaults to None
    :type length: int, optional
    """

    def __init__(
        self,
        href: str,
        rel: str,
        type_: str = None,
        templated: bool = None,
        var_base: str = None,
        hreflang: str = None,
        title: str = None,
        length: int = None,
    ):
        """Link2

        :param href: Supplies the URI to a remote resource (or resource fragment).
        :type href: str
        :param rel: The type or semantics of the relation.
        :type rel: str
        :param type_: A hint indicating what the media type of the result of dereferencing the link should be., defaults to None
        :type type_: str, optional
        :param templated: This flag set to true if the link is a URL template., defaults to None
        :type templated: bool, optional
        :param var_base: A base path to retrieve semantic information about the variables used in URL template., defaults to None
        :type var_base: str, optional
        :param hreflang: A hint indicating what the language of the result of dereferencing the link should be., defaults to None
        :type hreflang: str, optional
        :param title: Used to label the destination of a link such that it can be used as a human-readable identifier., defaults to None
        :type title: str, optional
        :param length: length, defaults to None
        :type length: int, optional
        """
        self.href = href
        self.rel = rel
        if type_ is not None:
            self.type_ = type_
        if templated is not None:
            self.templated = templated
        if var_base is not None:
            self.var_base = var_base
        if hreflang is not None:
            self.hreflang = hreflang
        if title is not None:
            self.title = title
        if length is not None:
            self.length = length
