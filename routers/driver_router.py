from fastapi import APIRouter, Depends, HTTPException
from typing import List
import uuid
from firebase_admin import auth
from database.firebase import authSession
from routers.auth_router import get_current_user
# from models import Driver
from schemas.schemas_dto import Driver, Driver_POST, User

#Database
from database.firebase import db

router = APIRouter(
    prefix='/driver',
    tags=["Drivers"]
)
drivers  = [
    Driver(id= "1", first_name= "Nick", last_name= "Pizza", phone_number= "+33953532784", email= "test@gmail.com", profile_picture= "https://images.unsplash.com/photo-1511367461989-f85a21fda167?auto=format&fit=crop&q=80&w=1931&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", average_rating= 4.4),
    Driver(id= "2", first_name= "Zuma", last_name= "Dembe", phone_number= "+3395353278", email= "new@gmail.com", profile_picture= "https://images.unsplash.com/photo-1511367461989-f85a21fda167?auto=format&fit=crop&q=80&w=1931&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", average_rating= 4.4)
]
@router.get("/", response_model=List[Driver])
def get_drivers():
    """ List all the Sessions from a Training Center"""
    fireBaseobject = db.child("driver").get().val()
    resultArray = [value for value in fireBaseobject.values()]
    return resultArray

@router.get("/{driver_id}", response_model=Driver)
def get_driver_by_id(driver_id: str):
    # Logique pour obtenir un conducteur par ID
    fireBaseobject = db.child("driver").child(driver_id).get().val()
    # resultArray = [value for value in fireBaseobject.values()]
    return fireBaseobject

@router.post("/")
def create_driver(driver_data: Driver_POST):
    
    generated_id = uuid.uuid4()
    # user = User(email = driver_data.email, password = driver_data.password)
    # new_user_ref  = db.child("user").push(user.model_dump())
    try:
        user = auth.create_user(
            email = driver_data.email,
            password = driver_data.password
        )
        new_driver = Driver(id=str(generated_id), first_name=driver_data.first_name, last_name=driver_data.last_name, user_id= str(user.uid))
        db.child("driver").push(new_driver.model_dump())
        return {
        "message": f"Nouvel utilisateur créé avec id : {user.uid}"
        }
    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=409,
            detail=f"Un compte existe déjà pour : {driver_data.email}"
        )


@router.put("/{driver_id}", status_code=204)
def update_driver(driver_id: str, modifiedDriver: Driver_POST, userData: int = Depends(get_current_user)):
    fireBaseobject = db.child("driver").child(driver_id).get(userData['idToken']).val()
    if fireBaseobject is not None:
        if fireBaseobject['user_id'] == userData['user_id']:
            updatedDriver = Driver(id=driver_id, **modifiedDriver.model_dump())
            return db.child("driver").child(driver_id).update(updatedDriver.model_dump(), userData['idToken'] )
        return {
            "message": "Vous n'avez pas le droit de modifier ce driver"
        }
    raise HTTPException(status_code= 404, detail="Driver  not found")

@router.delete("/{driver_id}",  status_code=204)
def delete_driver(driver_id: str, userData: int = Depends(get_current_user)):
    try:
        fireBaseobject = db.child("driver").child(driver_id).get(userData['idToken']).val()
    except:
        raise HTTPException(
            status_code=403, detail="Accès interdit"
        )
    if fireBaseobject is not None:
        if fireBaseobject['user_id'] == userData['user_id']:
            return db.child("driver").child(driver_id).remove(userData['idToken'])
        return {
            "message": "Vous n'avez pas le droit de supprimer ce driver"
        }
    raise HTTPException(status_code= 404, detail="Driver not found")

