from fastapi import FastAPI
# Documentation
from docs.description import api_description
from docs.tags import tags_metadata
#Routers
import routers.driver_router
import routers.passenger_router
import routers.reservation_router
import routers.trip_router

app = FastAPI(
    title="Carpooling API",
    description= api_description,
    openapi_tags= tags_metadata
)



# Montez les routeurs sur l'application
app.include_router(routers.driver_router.router)
app.include_router(routers.passenger_router.router, prefix="/api")
app.include_router(routers.reservation_router.router, prefix="/api")
app.include_router(routers.trip_router.router, prefix="/api")
# app.include_router(routers.payment_router, prefix="/api")

