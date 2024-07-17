from models.driver import Driver

class DriverService:
    async def signup(self, name: str, email: str, phone_number: str, password: str, kycID: str, service_type: str) -> Driver:
        raise NotImplementedError

    async def login(self, login_id: str, password: str) -> Driver:
        raise NotImplementedError
    

