from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, get_db
from . import models, schemas
from sqlalchemy import text

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/data")
def get_data(table_name: str, start_date: str, end_date: str, db: Session = Depends(get_db)):
    query = text(f"SELECT * FROM {table_name} WHERE \"dateCourse\" BETWEEN '{start_date}' AND '{end_date}'")
    result = db.execute(query, {"start_date": start_date, "end_date": end_date}).fetchall()
    data = [dict(row._mapping) for row in result]
    return {"data": data}