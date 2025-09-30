from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health, donations, auth as auth_router


app = FastAPI(title="Donation Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(donations.router, prefix="/donations", tags=["donations"])

# include only if you implement server driven OAuth callbacks
# app.include_router(auth_router.router, prefix="/auth", tags=["auth"])

