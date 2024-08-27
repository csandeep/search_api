import httpx
from app.config import settings
from app.schemas.event import SearchResult
from app.schemas.error import Fault, SearchException, SearchRequestError

async def search_events(**kwargs) -> SearchResult:
    """
    Search Ticketmaster for events

    Keyword Args:
        size (int, optional): The number of results to return. Defaults to 10.
        page (int, optional): The page number to return. Defaults to 0.
        keyword (str, optional): The search keyword.
        startDate (str, optional): The start date for the search in YYYY-MM-DD format.
        endDate (str, optional): The end date for the search in YYYY-MM-DD format.
        city (str, optional): The city to search in.
        segment (str, optional): The event segment to search in.

    Returns:
        SearchResult: The search results.

    Raises:
        SearchException: If there is an error searching for events.
        ErrorResponseException: If there is an unknown error with the Ticketmaster API.
    """
    size = kwargs.get("size", 10)
    page = kwargs.get("page", 0)

    if settings.TICKETMASTER_API_KEY is None:
        f =  Fault(faultstring="Missing TICKETMASTER_API_KEY.")
        raise SearchException(fault = f)

    params = {
        "apikey": settings.TICKETMASTER_API_KEY,
        "size": size,
        "page": page
    }

    for key in ['keyword', 'startDate', 'endDate', 'city', 'segment']:
        val = kwargs.get(key, None)
        if val is not None:
            params[key] = kwargs[key]

    endPont = "https://app.ticketmaster.com/discovery/v2/events.json"

    r = httpx.get(endPont, params=params)
    data = r.json()

    if r.status_code != 200:
        sre = SearchRequestError(**data)
        raise SearchException(sre.fault)

    sr = SearchResult(**data)
    return sr