from locale import currency
from pydantic import BaseModel, condecimal
from typing import Optional 

#what client sends to db whne creating a donation
class DonationCreate(BaseModel):
    amount: condecimal(max_digits=10, decimal_places=2)
    currency: str = 'USD'
    donor_name: Optional[str] = None
    cause: Optional[str] = None

#what backend returns when client inserts or fetches from db
class DonationOut(BaseModel):
    id: int
    amount: condecimal(max_digits=10, decimal_places=2)
    currency: str = 'USD'
    donor_name: Optional[str] = None
    cause: Optional[str] = None



