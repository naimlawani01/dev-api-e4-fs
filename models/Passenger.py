from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, Numeric
from .base import Base


class Passenger(Base):
    passenger_id: int
    first_name: str
    last_name: str
    phone_number: str
    email: str
    profile_picture: str