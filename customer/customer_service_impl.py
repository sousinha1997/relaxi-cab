from fastapi import HTTPException
from models.customer import Customer
from models.customer_mgr import CustomerManager

class CustomerServiceImpl:

    async def signup(self, name: str, email: str, phone_number: str, password: str) -> Customer:
        cusMgrsInst = CustomerManager.get_instance()
        customer = cusMgrsInst.get_customer(phone_number)

        if not customer:
            customer = Customer(name, password, phone_number, email)
            cusMgrsInst.add_customer(phone_number, customer)
            return {"status_code": 200, "userID": str(customer.customer_id), "UserCreatedAt": str(customer.creationTime)}
        else:
            raise HTTPException(status_code=409, detail="User with phone already exists")

    async def login(self, login_id: str, password: str) -> Customer:
        cusMgrsInst = CustomerManager.get_instance()
        customersMap = cusMgrsInst.get_customer_map()

        if login_id not in customersMap:
            return {"error": "User not found"}

        customerObj = customersMap[login_id]

        if not customerObj.verify_password(password):
            return {"error": "Incorrect password"}

        return {"status_code": 200, "userID": str(customerObj.customer_id), "UserLoginAt": str(customerObj.loginTime)}
