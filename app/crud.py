from sqlalchemy.orm import Session
from . import models, schemas


def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = models.Device(**device.model_dump())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device


def get_devices(db: Session):
    return db.query(models.Device).all()


def create_incident(db: Session, incident: schemas.IncidentCreate):
    db_incident = models.Incident(**incident.model_dump())
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident


def get_incidents(db: Session):
    return db.query(models.Incident).all()


def get_incidents_by_device(db: Session, device_id: int):
    return db.query(models.Incident).filter(models.Incident.device_id == device_id).all()