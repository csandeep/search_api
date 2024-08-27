from typing import Annotated

from fastapi import FastAPI, Header, HTTPException, Depends

from .services.client import search_events
from .schemas.event import SearchResult

app = FastAPI()


@app.get("/search_events", response_model=SearchResult)
async def serach_events():
    res = await search_events()
    return res