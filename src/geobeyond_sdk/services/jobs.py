# This file was generated by liblab | https://liblab.com/

from typing import Any
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models import GetLandingPageF


class JobsService(BaseService):

    @cast_models
    def get_jobs(self) -> Any:
        """Retrieve a list of jobs

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        serialized_request = (
            Serializer(f"{self.base_url}/jobs", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def get_job(self, job_id: str, f: GetLandingPageF = None) -> Any:
        """Retrieve job details

        :param job_id: job identifier
        :type job_id: str
        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(job_id)
        Validator(GetLandingPageF).is_optional().validate(f)

        serialized_request = (
            Serializer(f"{self.base_url}/jobs/{{jobId}}", self.get_default_headers())
            .add_path("jobId", job_id)
            .add_query("f", f, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def delete_job(self, job_id: str) -> Any:
        """Cancel / delete job

        :param job_id: job identifier
        :type job_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(job_id)

        serialized_request = (
            Serializer(f"{self.base_url}/jobs/{{jobId}}", self.get_default_headers())
            .add_path("jobId", job_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)
        return response

    @cast_models
    def get_job_results(self, job_id: str, f: GetLandingPageF = None) -> Any:
        """Retrieve job results

        :param job_id: job identifier
        :type job_id: str
        :param f: The optional f parameter indicates the output format which the server shall provide as part of the response document.  The default format is GeoJSON., defaults to None
        :type f: GetLandingPageF, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(job_id)
        Validator(GetLandingPageF).is_optional().validate(f)

        serialized_request = (
            Serializer(
                f"{self.base_url}/jobs/{{jobId}}/results", self.get_default_headers()
            )
            .add_path("jobId", job_id)
            .add_query("f", f, explode=False)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)
        return response