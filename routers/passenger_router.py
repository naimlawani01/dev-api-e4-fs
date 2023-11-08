from fastapi import APIRouter, Depends, HTTPException
from typing import List
import uuid
from firebase_admin import auth
from database.firebase import authSession
from routers.auth_router import get_current_user
# from models import Passenger
from schemas.schemas_dto import Passenger, Passenger_POST

#Database
from database.firebase import db

router = APIRouter(
    prefix='/passengers',
    tags=["Passengers"]
)

@router.get("/", response_model=List[Passenger])
def get_passengers():
    # Logique pour obtenir la liste des passagers
    pass

@router.get("/{passenger_id}", status_code=200)
def get_passenger_by_id(passenger_id: int):
    # Logique pour obtenir un conducteur par ID
    fireBaseobject = db.child("passenger").child(passenger_id).get().val()
    # resultArray = [value for value in fireBaseobject.values()]
    return fireBaseobject

@router.post("/", status_code=201)
def create_passenger(passenger_data: Passenger_POST):
    
    generated_id = uuid.uuid4()
    try:
        user = auth.create_user(
            email = passenger_data.email,
            password = passenger_data.password
        )
        new_passager = Passenger(passenger_id=str(generated_id), first_name=passenger_data.first_name, last_name=passenger_data.last_name, user_id= str(user.uid))
        db.child("passenger").push(new_passager.model_dump())
        return {
        "message": f"Nouvel utilisateur créé avec id : {user.uid}"
        }
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=409,
            detail=f"Un compte existe déjà pour : {passenger_data.email}"
        )

@router.put("/{passenger_id}", response_model=Passenger)
def update_passenger(passenger_id: int, passenger: Passenger):
    # Logique pour mettre à jour un passager
    pass

@router.delete("/{passenger_id}", status_code=204)
def delete_passenger(passenger_id: str, userData: int = Depends(get_current_user)):
    try:
        fireBaseobject = db.child("passenger").child(passenger_id).get(userData['idToken']).val()
    except:
        raise HTTPException(
            status_code=403, detail="Accès interdit"
        )
    if fireBaseobject is not None:
        if fireBaseobject['user_id'] == userData['user_id']:
            return db.child("passenger").child(passenger_id).remove(userData['idToken'])
        return {
            "message": "Vous n'avez pas le droit de supprimer ce passager"
        }
    raise HTTPException(status_code= 404, detail="Passenger not found")