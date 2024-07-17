from dataStore import customerStore


class CustomerManager:
    CustomerManagerInst = None

    def __init__(self):
        self.customerStore = customerStore.customer_map

    @staticmethod
    def get_instance():
        if not CustomerManager.CustomerManagerInst:
            CustomerManager.CustomerManagerInst = CustomerManager()
        return CustomerManager.CustomerManagerInst

    def add_customer(self, phone_number, customer_object):
        self.customerStore[phone_number] = customer_object

    def get_customer(self, phone_number):
        if not self.customerStore.get(phone_number):
            return None
        return self.customerStore[phone_number]

    def get_customer_map(self):
        return self.customerStore