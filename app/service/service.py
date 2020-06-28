from os import environ

from abc import ABC, abstractmethod

from requests import Session, Request


class ServiceRequestHandler(ABC):
    def __init__(
        self,
        request_url: str,
        method: str,
        service: str = None,
        service_key: str = None,
        headers: str = None,
    ):
        self._request_url = request_url
        self._method = method.upper()
        self._service = service or self._service
        self._service_key = service_key or self._service_key
        self._headers = headers or self._headers

    def execute(self):
        self._set_url()

        self._set_session()

        self._prepare_request()

        request = self._send_request()

        return request

    def _set_url(self):
        self._url = f"{self._service}/{self._request_url}"

    def _set_session(self) -> None:
        self._session = Session()

    def _prepare_request(self) -> None:
        self._request = Request(
            url=self._url,
            method=self._method,
            headers=self._headers
        ).prepare()

    def _send_request(self) -> Request:
        request = self._session.send(self._request)
        return request
