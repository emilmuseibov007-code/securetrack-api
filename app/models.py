from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String, nullable=False)
    ip_address = Column(String, unique=True, nullable=False)
    os = Column(String, nullable=False)
    location = Column(String, nullable=True)
    owner = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    incidents = relationship("Incident", back_populates="device", cascade="all, delete")


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    severity = Column(String, nullable=False)
    status = Column(String, nullable=False, default="open")
    discovered_at = Column(DateTime, default=datetime.utcnow)

    device_id = Column(Integer, ForeignKey("devices.id"), nullable=False)
    device = relationship("Device", back_populates="incidents")