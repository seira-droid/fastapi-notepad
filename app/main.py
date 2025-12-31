from fastapi import FastAPI
from app.database import Base, engine

app = FastAPI(title="FastAPI Notepad")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "FastAPI Notepad running"}
