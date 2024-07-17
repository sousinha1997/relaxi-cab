from fastapi import HTTPException
from models.driver import Driver
from models.driver_mgr import DriverManager

class DriverServiceImpl:

    async def signup(self, name: str, email: str, phone_number: str, password: str, kycID, service_type: str) -> Driver:
        driMgrsInst = DriverManager.get_instance()
        driver = driMgrsInst.get_driver(phone_number)

        if not driver:
            driver = Driver(name, email, phone_number, password, kycID, service_type)
            driMgrsInst.add_driver(phone_number, driver)
            return {"status_code": 200, "userID": str(driver.driver_id), "UserCreatedAt": str(driver.creationTime)}
        else:
            raise HTTPException(status_code=409, detail="User with phone already exists")

    async def login(self, login_id: str, password: str) -> Driver:
        driMgrsInst = DriverManager.get_instance()
        driversMap = driMgrsInst.get_driver_map()

        if login_id not in driversMap:
            return {"error": "User not found"}

        driverObj = driversMap[login_id]

        if not driverObj.verify_password(password):
            return {"error": "Incorrect password"}

        return {"status_code": 200, "userID": str(driverObj.driver_id), "UserLoginAt": str(driverObj.loginTime)}
