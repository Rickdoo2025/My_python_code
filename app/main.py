# app/main.py

from fastapi import FastAPI
from app.api.user_routes import router as user_router 

app = FastAPI(
    title="MySQL Backend Service",
    description="Exposes data from MySQL using FastAPI",
    version="1.0.0"
)

# Register your user API routes
app.include_router(user_router)
