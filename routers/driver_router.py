from fastapi import APIRouter, HTTPException
from typing import List
# from models import Driver
from schemas.schemas_dto import Driver

router = APIRouter(
    prefix='/driver',
    tags=["Drivers"]
)

@router.get("/", response_model=List[Driver])
def get_drivers():
    # Logique pour obtenir la liste des conducteurs
    pass

@router.get("/{driver_id}", response_model=Driver)
def get_driver_by_id(driver_id: int):
    # Logique pour obtenir un conducteur par ID
    pass

@router.post("/", response_model=Driver)
def create_driver(driver: Driver):
    # Logique pour créer un conducteur
    pass

@router.put("/{driver_id}", response_model=Driver)
def update_driver(driver_id: int, driver: Driver):
    # Logique pour mettre à jour un conducteur
    pass

@router.delete("/{driver_id}", response_model=dict)
def delete_driver(driver_id: int):
    # Logique pour supprimer un conducteur
    pass
