from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SecureTrack API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "SecureTrack API is running"}


@app.post("/devices", response_model=schemas.DeviceResponse)
def create_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    return crud.create_device(db, device)


@app.get("/devices", response_model=list[schemas.DeviceResponse])
def read_devices(db: Session = Depends(get_db)):
    return crud.get_devices(db)


@app.post("/incidents", response_model=schemas.IncidentResponse)
def create_incident(incident: schemas.IncidentCreate, db: Session = Depends(get_db)):
    return crud.create_incident(db, incident)


@app.get("/incidents", response_model=list[schemas.IncidentResponse])
def read_incidents(db: Session = Depends(get_db)):
    return crud.get_incidents(db)


@app.get("/devices/{device_id}/incidents", response_model=list[schemas.IncidentResponse])
def read_device_incidents(device_id: int, db: Session = Depends(get_db)):
    return crud.get_incidents_by_device(db, device_id)