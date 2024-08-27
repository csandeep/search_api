from typing import Annotated
import traceback

from fastapi import FastAPI, Header, HTTPException, Depends, Request, Response
from fastapi.responses import JSONResponse

from .services.client import search_events
from .schemas.event import SearchResult
from .schemas.error import SearchException

app = FastAPI()

@app.exception_handler(SearchException)
async def search_exception_handler(request: Request, exc: SearchException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.fault.faultstring}"},
    )

@app.get("/search_events", response_model=SearchResult)
async def serach_events():
    res = await search_events()
    return res