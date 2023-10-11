from fastapi import APIRouter, HTTPException
from typing import List
# from models import Reservation
from schemas.schemas_dto import Reservation

router = APIRouter(
    prefix='/reservations',
    tags=["Reservations"]
)

@router.get("/", response_model=List[Reservation])
def get_reservations():
    # Logique pour obtenir la liste des réservations
    pass

@router.get("/{reservation_id}", response_model=Reservation)
def get_reservation_by_id(reservation_id: int):
    # Logique pour obtenir une réservation par ID
    pass

@router.post("/", response_model=Reservation)
def create_reservation(reservation: Reservation):
    # Logique pour créer une réservation
    pass

@router.put("/{reservation_id}", response_model=Reservation)
def update_reservation(reservation_id: int, reservation: Reservation):
    # Logique pour mettre à jour une réservation
    pass

@router.delete("/{reservation_id}", response_model=dict)
def delete_reservation(reservation_id: int):
    # Logique pour supprimer une réservation
    pass
