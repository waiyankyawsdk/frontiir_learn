from email.policy import default
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Customer(BaseModel):
    customer_id: str
    cid : Optional[str]
    group_id : Optional[str] = None
    nrc_number : Optional[str] = None
    nrc_front : Optional[str] = None
    nrc_back : Optional[str] = None
    passport : Optional[str] = None
    plan_status : Optional[str] = None
    package_type : Optional[str] = None

data = {
    'customer_id': '2',
    'cid': '2',
    'group_id': '3',
    'nrc_number': '4',
    'nrc_front': '5',
    'nrc_back': '6',
    'passport': 'MJ',
    'plan_status': 'true',
    'package_type': 'Myanmarnet+',
    
}
customer = Customer(**data)
app = FastAPI()

@app.get("/customers/{customer_id}",response_model=Customer)
async def get_customer_info(customer_id : str):
    if customer_id == customer.customer_id:
        return customer.dict()

@app.put("/customers/{customer_id}")
async def create_nrc(customer_id: int, customer: Customer):
    return {"customer_id": customer_id, **customer.dict()}

