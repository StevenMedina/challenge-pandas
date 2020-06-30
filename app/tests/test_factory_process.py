from unittest.mock import MagicMock, patch

import pytest

from app.runner import FactoryProcess


class TestThirdPartyService:

    @patch('app.runner.FactoryProcess._call_rapid_api')
    def test_call_rapid_api(self, mock_call_rapid_api):
        mock_call_rapid_api.return_value = [
            {"region": "Asia"}, {"region": "Americas"},
        ]
        response = FactoryProcess._call_rapid_api()

        assert "Asia" == response[0]["region"]
        assert "Americas" in response[1]["region"]

    @patch('app.runner.FactoryProcess._call_rest_countries_api')
    def test_call_rest_countries_api(self, mock_call_rest_countries_api):
        mock_call_rest_countries_api.return_value = [
            {
                "name": "Afghanistan",
                "capital": "Kabul",
                "region": "Asia",
                "subregion": "Southern Asia",
                "population": 27657145,
            },
            {
                "name": "Colombia",
                "capital": "Bogotá",
                "region": "Americas",
                "subregion": "South America",
                "population": 48759958,
            },
        ]
        response = FactoryProcess._call_rest_countries_api(region="Americas")

        assert "Afghanistan" == response[0]["name"]
        assert "Colombia" in response[1]["name"]
