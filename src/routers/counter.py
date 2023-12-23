from fastapi import APIRouter, Depends
from sqlmodel import Session
from src.db.db import get_session
from src.models.extra_hours import ExtraHours
from src.schemas.extra_hours import ExtraHours as ExtraHoursSchema
from uuid import uuid4
from datetime import timedelta

router = APIRouter()

router.post("/register-extra-hours")
def register_extra_hours(data: ExtraHoursSchema, db: Session = Depends(get_session)):
    standard_workday = timedelta(hours=8)
    total_worked = data.end_time - data.started_time
    effective_worked = total_worked - data.break_time
    extra_time = effective_worked - standard_workday

    if extra_time < timedelta(0):
        extra_time = timedelta(0)

    worked_hours = ExtraHours(
        id= uuid4(),
        started_time=data.started_time,
        break_time=data.break_time,
        end_time=data.end_time,
        extra_time=extra_time
    )
    db.add(worked_hours)
    db.commit()
    return extra_time