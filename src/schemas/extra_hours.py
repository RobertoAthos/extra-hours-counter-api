from pydantic import BaseModel


class ExtraHours(BaseModel):
    id: int
    started_time: str
    break_time: str
    end_time: str
    extra_time: str