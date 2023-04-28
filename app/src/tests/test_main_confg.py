import pytest
import requests


def test_server_is_on():
    response = requests.get("http://localhost:8000")
    assert response.status_code == 200
