from fastapi import FastAPI
from fastapi import FastAPI, Body ,  HTTPException
from customer.customer_service_impl import CustomerServiceImpl
from driver.driver_service_impl import DriverServiceImpl

app = FastAPI()
customer_service = CustomerServiceImpl()
driver_service = DriverServiceImpl()

@app.post("/customer/signup")
async def signup(name: str = Body(...), email: str = Body(...), phone_number: str = Body(...), password: str = Body(...)):
    status = await customer_service.signup(name, email, phone_number, password)
    return status

@app.post("/customer/login")
async def login(login_id: str = Body(...), password: str = Body(...)):
    status = await customer_service.login(login_id, password)
    return status  

@app.post("/driver/signup")
async def signup(name: str = Body(...), email: str = Body(...), phone_number: str = Body(...), password: str = Body(...), kycID: str = Body(...), service_type: str = Body(...)):
    status = await driver_service.signup(name, email, phone_number, password, kycID, service_type)
    return status

@app.post("/driver/login")
async def login(login_id: str = Body(...), password: str = Body(...)):
    status = await driver_service.login(login_id, password)
    return status  

@app.get("/health-check")
async def health_check():

    state_healthy = True
    # ...
    if state_healthy: 
        return {"status": "no issues reported"}
    else:
        return {"status": "issues reported"}

@app.get("/")
async def root():
    return {"message": "Hello FastAPI from your Uber-like app!"}
