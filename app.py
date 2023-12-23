from sqlmodel import SQLModel
import uvicorn
from fastapi import FastAPI
from src.routers  import counter
from src.db.db import engine

app = FastAPI()

app.include_router(counter.router)

def create_db_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    create_db_tables()

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
