# This file was generated by liblab | https://liblab.com/

from typing import Any
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import GetLandingPageF, LandingPage, Lang, ProcessList, Ui


class ServerService(BaseService):

    @cast_models
    def get_landing_page(
        self, f: GetLandingPageF = None, lang: Lang = None
    ) -> LandingPage:
        """Landing page

        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        :param lang: The optional lang parameter instructs the server return a response in a certain language, if supported.  If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language.  Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion., defaults to None
        :type lang: Lang, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The landing page provides links to the API definition
        (link relations `service-desc` and `service-doc`),
        the Conformance declaration (path `/conformance`,
        link relation `conformance`), and the Feature
        Collections (path `/collections`, link relation
        `data`).
        :rtype: LandingPage
        """

        Validator(GetLandingPageF).is_optional().validate(f)
        Validator(Lang).is_optional().validate(lang)

        serialized_request = (
            Serializer(f"{self.base_url}/", self.get_default_headers())
            .add_query("f", f, explode=False)
            .add_query("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return LandingPage._unmap(response)

    @cast_models
    def get_collections(
        self, f: GetLandingPageF = None, lang: Lang = None
    ) -> LandingPage:
        """Collections

        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        :param lang: The optional lang parameter instructs the server return a response in a certain language, if supported.  If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language.  Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion., defaults to None
        :type lang: Lang, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The landing page provides links to the API definition
        (link relations `service-desc` and `service-doc`),
        the Conformance declaration (path `/conformance`,
        link relation `conformance`), and the Feature
        Collections (path `/collections`, link relation
        `data`).
        :rtype: LandingPage
        """

        Validator(GetLandingPageF).is_optional().validate(f)
        Validator(Lang).is_optional().validate(lang)

        serialized_request = (
            Serializer(f"{self.base_url}/collections", self.get_default_headers())
            .add_query("f", f, explode=False)
            .add_query("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return LandingPage._unmap(response)

    @cast_models
    def get_conformance_declaration(
        self, f: GetLandingPageF = None, lang: Lang = None
    ) -> LandingPage:
        """API conformance definition

        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        :param lang: The optional lang parameter instructs the server return a response in a certain language, if supported.  If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language.  Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion., defaults to None
        :type lang: Lang, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The landing page provides links to the API definition
        (link relations `service-desc` and `service-doc`),
        the Conformance declaration (path `/conformance`,
        link relation `conformance`), and the Feature
        Collections (path `/collections`, link relation
        `data`).
        :rtype: LandingPage
        """

        Validator(GetLandingPageF).is_optional().validate(f)
        Validator(Lang).is_optional().validate(lang)

        serialized_request = (
            Serializer(f"{self.base_url}/conformance", self.get_default_headers())
            .add_query("f", f, explode=False)
            .add_query("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return LandingPage._unmap(response)

    @cast_models
    def get_openapi(
        self, f: GetLandingPageF = None, lang: Lang = None, ui: Ui = None
    ) -> Any:
        """This document

        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        :param lang: The optional lang parameter instructs the server return a response in a certain language, if supported.  If the language is not among the available values, the Accept-Language header language will be used if it is supported. If the header is missing, the default server language is used. Note that providers may only support a single language (or often no language at all), that can be different from the server language.  Language strings can be written in a complex (e.g. "fr-CA,fr;q=0.9,en-US;q=0.8,en;q=0.7"), simple (e.g. "de") or locale-like (e.g. "de-CH" or "fr_BE") fashion., defaults to None
        :type lang: Lang, optional
        :param ui: UI to render the OpenAPI document, defaults to None
        :type ui: Ui, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(GetLandingPageF).is_optional().validate(f)
        Validator(Lang).is_optional().validate(lang)
        Validator(Ui).is_optional().validate(ui)

        serialized_request = (
            Serializer(f"{self.base_url}/openapi", self.get_default_headers())
            .add_query("f", f, explode=False)
            .add_query("lang", lang)
            .add_query("ui", ui, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def get_processes(self, f: GetLandingPageF = None) -> ProcessList:
        """Processes

        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Information about the available processes
        :rtype: ProcessList
        """

        Validator(GetLandingPageF).is_optional().validate(f)

        serialized_request = (
            Serializer(f"{self.base_url}/processes", self.get_default_headers())
            .add_query("f", f, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return ProcessList._unmap(response)