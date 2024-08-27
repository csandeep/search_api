from typing import Optional
from pydantic import BaseModel


class Detail(BaseModel):
    errorcode: str

class Fault(BaseModel):
    faultstring: str
    detail: Optional[Detail] = None

class SearchRequestError(BaseModel):
    fault: Fault

class SearchException(Exception):
    def __init__(self, fault: Fault):
        self.fault = fault
        super().__init__(str(fault))