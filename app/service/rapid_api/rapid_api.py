import os

from app.service.service import ServiceRequestHandler
from app.config import settings


class ServiceRapidAPI(ServiceRequestHandler):
    _service = settings.RAPID_API_HOST
    _service_key = settings.RAPID_API_KEY
    _headers = {
        "x-rapidapi-key": _service_key,
    }
