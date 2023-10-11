from fastapi import APIRouter, HTTPException
from typing import List
# from models import Passenger
from schemas.schemas_dto import Passenger

router = APIRouter(
    prefix='/passengers',
    tags=["Passengers"]
)

@router.get("/", response_model=List[Passenger])
def get_passengers():
    # Logique pour obtenir la liste des passagers
    pass

@router.get("/{passenger_id}", response_model=Passenger)
def get_passenger_by_id(passenger_id: int):
    # Logique pour obtenir un passager par ID
    pass

@router.post("/", response_model=Passenger)
def create_passenger(passenger: Passenger):
    # Logique pour créer un passager
    pass

@router.put("/{passenger_id}", response_model=Passenger)
def update_passenger(passenger_id: int, passenger: Passenger):
    # Logique pour mettre à jour un passager
    pass

@router.delete("/{passenger_id}", response_model=dict)
def delete_passenger(passenger_id: int):
    # Logique pour supprimer un passager
    pass
