import pytest
from fastapi.testclient import TestClient
from .api import app

from .schemas.event import SearchResult
from .schemas.error import SearchRequestError, ErrorResponseException
from .services.client import search_events

client = TestClient(app)

@pytest.mark.anyio
async def test_search_events():
    response = await search_events(startDate="2024-10-01")
    assert type(response) is SearchResult
    assert len(response.events) == 10

@pytest.mark.anyio
async def test_search_invalid_event():
    response = await search_events(city="unknown")
    assert type(response) is SearchResult
    assert response.embedded is None