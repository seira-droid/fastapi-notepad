from fastapi import FastAPI
from app.database import Base, engine
from app import models  # NEW: import models to create tables

app = FastAPI(title="FastAPI Notepad")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "FastAPI Notepad running"}
