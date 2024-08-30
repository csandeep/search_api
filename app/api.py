from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse

from .services.client import search_events
from .schemas.event import SearchResult, SearchResponse
from .schemas.error import SearchException
from .schemas.search_param import SearchParams

description = """
Discovery API helps you search Ticket Master Events. 🚀


## Discovery

You will be able to:

* **Search Events**
"""

app = FastAPI(title="Discovery API", description=description, version="0.0.1")

@app.exception_handler(SearchException)
async def search_exception_handler(request: Request, exc: SearchException):
    return JSONResponse(
        status_code=400,
        content={"message": f"Oops! {exc.fault.faultstring}"},
    )

@app.get("/search_events", response_model=SearchResponse)
async def search_events_handler(params: SearchParams = Depends()):

    res = await search_events(**params.model_dump())
    return SearchResponse(events=res.events if res.embedded else [], page=res.page)