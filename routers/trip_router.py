from fastapi import APIRouter, HTTPException
from typing import List
# from models import Trip

from schemas.schemas_dto import Trip

router = APIRouter(
    prefix='/trips',
    tags=["Trips"]
)

@router.get("/", response_model=List[Trip])
def get_trips():
    # Logique pour obtenir la liste des trajets
    pass

@router.get("/{trip_id}", response_model=Trip)
def get_trip_by_id(trip_id: int):
    # Logique pour obtenir un trajet par ID
    pass

@router.post("/", response_model=Trip)
def create_trip(trip: Trip):
    # Logique pour créer un trajet
    pass

@router.put("/{trip_id}", response_model=Trip)
def update_trip(trip_id: int, trip: Trip):
    # Logique pour mettre à jour un trajet
    pass

@router.delete("/{trip_id}", response_model=dict)
def delete_trip(trip_id: int):
    # Logique pour supprimer un trajet
    pass
