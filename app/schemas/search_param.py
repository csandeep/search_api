from typing import Optional
from pydantic import BaseModel, Field
import datetime
from fastapi import Query

class SearchParams(BaseModel):
    keyword: Optional[str] = Field(Query(
        default=None,
        description="The search keyword to filter events."
        ))
    startDate: Optional[datetime.date] = Field(Query(
        default=None,
        description="Filter with a start date after this date, in YYYY-MM-DD format."))
    endDate: Optional[datetime.date] = Field(Query(
        default=None,
        description="Filter with a start date before this date, in YYYY-MM-DD format."))
    city: Optional[str] = Field(Query(
        default=None,
        description="Filter by City"))
    segment: Optional[str] = Field(Query(
        default=None,
        description="Filter by segment name."))
    size: int = Field(Query(
        default=10,
        description="Page size of the response.",
        ge=1,
        le=100))
    page: int = Field(Query(
        default=0,
        description="The page number to return.",
        ge=0,
        le=100))
