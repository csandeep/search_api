from pydantic import BaseModel


class Detail(BaseModel):
    errorcode: str

class Fault(BaseModel):
    faultstring: str
    detail: Detail

class TicketMasterError(BaseModel):
    fault: Fault