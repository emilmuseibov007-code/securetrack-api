from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class DeviceCreate(BaseModel):
    hostname: str
    ip_address: str
    os: str
    location: Optional[str] = None
    owner: Optional[str] = None


class DeviceResponse(BaseModel):
    id: int
    hostname: str
    ip_address: str
    os: str
    location: Optional[str]
    owner: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class IncidentCreate(BaseModel):
    title: str
    description: Optional[str] = None
    severity: str
    status: str = "open"
    device_id: int


class IncidentResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    severity: str
    status: str
    discovered_at: datetime
    device_id: int

    class Config:
        from_attributes = True