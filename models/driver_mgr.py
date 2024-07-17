

class DriverManager:
    DriverManagerInst = None

    def __init__(self):
        self.__driverStore = {}

    @staticmethod
    def get_instance():
        if not DriverManager.DriverManagerInst:
            DriverManager.DriverManagerInst = DriverManager()
        return DriverManager.DriverManagerInst

    def add_driver(self, driver_name, driver_object):
        self.__driverStore[driver_name] = driver_object

    def get_driver(self, phone_number):
        if not self.__driverStore.get(phone_number):
            return None
        return self.__driverStore[phone_number]

    def get_driver_map(self):
        return self.__driverStore