


from dataStore import driverStore


class DriverManager:
    DriverManagerInst = None

    def __init__(self):
        self.driverStore = driverStore.driver_map

    @staticmethod
    def get_instance():
        if not DriverManager.DriverManagerInst:
            DriverManager.DriverManagerInst = DriverManager()
        return DriverManager.DriverManagerInst

    def add_driver(self, driver_name, driver_object):
        self.driverStore[driver_name] = driver_object

    def get_driver(self, phone_number):
        if not self.driverStore.get(phone_number):
            return None
        return self.driverStore[phone_number]

    def get_driver_map(self):
        return self.driverStore