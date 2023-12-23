from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class ExtraHours(SQLModel, table=True):
    id: int = Field(primary_key=True)
    started_time: str
    break_time: str
    end_time: str
    extra_time: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
