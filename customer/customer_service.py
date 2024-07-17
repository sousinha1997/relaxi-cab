from models.customer import Customer

class CustomerService:
    async def signup(self, name: str, email: str, phone_number: str, password: str) -> Customer:
        raise NotImplementedError

    async def login(self, login_id: str, password: str) -> Customer:
        raise NotImplementedError
    

