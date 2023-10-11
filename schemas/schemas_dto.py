from pydantic import BaseModel


class Location(BaseModel):
    latitude: float
    longitude: float

class Driver(BaseModel):
    driver_id: int
    first_name: str
    last_name: str
    phone_number: str
    email: str
    profile_picture: str
    average_rating: float
    current_location: Location

class Trip(BaseModel):
    trip_id: int
    driver_id: int
    start_location: Location
    end_location: Location
    departure_datetime: str
    available_seats: int
    seat_price: float
    status: str
    current_location: Location

class Passenger(BaseModel):
    passenger_id: int
    first_name: str
    last_name: str
    phone_number: str
    email: str
    profile_picture: str

class Reservation(BaseModel):
    reservation_id: int
    trip_id: int
    passenger_id: int
    reservation_datetime: str
    status: str

class Payment(BaseModel):
    payment_id: int
    reservation_id: int
    amount: float
    payment_datetime: str
    payment_method: str
