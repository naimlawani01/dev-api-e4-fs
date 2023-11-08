from pydantic import BaseModel


class Location(BaseModel):
    latitude: float
    longitude: float

class Driver(BaseModel):
    id: str 
    first_name: str 
    last_name: str
    phone_number: str = "0000000000"
    email: str = "carpooling@gmail.com"
    profile_picture: str = "undifined"
    average_rating: float = 4.2
    current_location: str = "Paris"
    user_id: str = "ftpz"

class Driver_POST(BaseModel):
    first_name: str 
    last_name: str
    phone_number: str = "0000000000"
    email: str = "carpooling@gmail.com"
    profile_picture: str = "undifined"
    average_rating: float = 4.2
    current_location: str = "Paris"
    password: str

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
    passenger_id: str
    first_name: str
    last_name: str
    phone_number: str = "0000000000"
    email: str = "carpooling@gmail.com"
    profile_picture: str = "undifined"
    user_id: str = "ftpz"

class Passenger_POST(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    profile_picture: str
    user_id: str
    password: str

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

class User(BaseModel):
    email: str
    password: str  