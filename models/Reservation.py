from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, Numeric
from .base import Base

class Reservation(Base):
    reservation_id: int
    trip_id: int
    passenger_id: int
    reservation_datetime: str
    status: str