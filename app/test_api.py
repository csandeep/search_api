import pytest

from fastapi.testclient import TestClient
from httpx import AsyncClient

from .api import app


client = TestClient(app)


def test_search_events():
    response = client.get("/search_events")
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "title": "Foo",
        "description": "There goes my hero",
    }