from fastapi import APIRouter
from app.services.donations_service import create_donation, list_donations
from app.schemas.donations import DonationCreate, DonationOut
from typing import List


router = APIRouter()

@router.get('/get-donations', response_model=List[DonationOut])
def get_recent_donations():
    return list_donations()

@router.post('/create-donation', response_model=DonationOut)
def add_donation(payload: DonationCreate):
    return create_donation(payload.model_dump())