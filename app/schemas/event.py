from typing import List, Optional
from pydantic import BaseModel, Field

class Link(BaseModel):
    href: str
    templated: Optional[bool] = None

class Links(BaseModel):
    self: Link
    next: Optional[Link] = None
    attractions: Optional[List[Link]] = None
    venues: Optional[List[Link]] = None

class Image(BaseModel):
    ratio: str
    url: str
    width: int
    height: int
    fallback: bool

class Sales(BaseModel):
    startDateTime: str
    startTBD: bool
    endDateTime: str

class PublicSales(BaseModel):
    public: Sales

class DateStart(BaseModel):
    localDate: str
    dateTBD: bool
    dateTBA: bool
    timeTBA: bool
    noSpecificTime: bool

class Status(BaseModel):
    code: str

class Dates(BaseModel):
    start: DateStart
    timezone: str
    status: Status

class Segment(BaseModel):
    id: str
    name: str

class Genre(BaseModel):
    id: str
    name: str

class SubGenre(BaseModel):
    id: str
    name: str

class Classification(BaseModel):
    primary: bool
    segment: Segment
    genre: Genre
    subGenre: SubGenre

class Promoter(BaseModel):
    id: str

class City(BaseModel):
    name: str

class State(BaseModel):
    name: str
    stateCode: str

class Country(BaseModel):
    name: str
    countryCode: str

class Address(BaseModel):
    line1: str

class Location(BaseModel):
    longitude: str
    latitude: str

class Market(BaseModel):
    id: str

class Venue(BaseModel):
    name: str
    type: str
    id: str
    test: bool
    locale: str
    postalCode: str
    timezone: str
    city: City
    state: State
    country: Country
    address: Address
    location: Location
    markets: List[Market]
    links: Links = Field(alias="_links")

class Attraction(BaseModel):
    name: str
    type: str
    id: str
    test: bool
    locale: str
    images: List[Image]
    classifications: List[Classification]
    links: Links = Field(alias="_links")

class EmbeddedEvent(BaseModel):
    venues: List[Venue]
    attractions: List[Attraction]

class Event(BaseModel):
    name: str
    type: str
    id: str
    test: bool
    url: str
    locale: str
    images: List[Image]
    sales: PublicSales
    dates: Dates
    classifications: List[Classification]
    promoter: Promoter
    links: Links = Field(alias="_links")
    embedded: EmbeddedEvent = Field(alias="_embedded")

    @property
    def get_venues(self) -> List[Venue]:
        return self.embedded.venues

    @property
    def get_attractions(self) -> List[Attraction]:
        return self.embedded.attractions


class Embedded(BaseModel):
    events: List[Event]

class Page(BaseModel):
    size: int
    totalElements: int
    totalPages: int
    number: int

class RootModel(BaseModel):
    links: Links = Field(alias="_links")
    embedded: Embedded = Field(alias="_embedded")
    page: Page

    @property
    def get_events(self) -> List[Event]:
        return self.embedded.events