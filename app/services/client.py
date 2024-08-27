import httpx
from app.config import settings
from app.schemas.event import SearchResult
from app.schemas.error import Fault, SearchException
import json

async def search_events(**kwargs) -> SearchResult:
    """
    Search Ticketmaster for events

    """
    keyword = kwargs.get("keyword", None)
    startDate = kwargs.get("startDate", None)
    endDate = kwargs.get("endDate", None)
    city = kwargs.get("city", None)
    segment = kwargs.get("segment", None)

    if settings.TICKETMASTER_API_KEY is None:
        f =  Fault(faultstring="Missing TICKETMASTER_API_KEY.")
        raise SearchException(fault = f)
    
    raise SearchException(fault = Fault(faultstring="Not Implementd"))

    return None