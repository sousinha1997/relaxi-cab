import datetime
from passlib.hash import bcrypt
from models.localtion import Location
from utils.common import Rating
from utils.utils import generate_user_ids
import datetime, time


class Cab:
    def __init__(self):
        self.serviceType = None

    @property
    def service_type(self):
        return self.serviceType

    @service_type.setter
    def service_type(self, service_type):
        self.serviceType = service_type


class Driver(Cab):

    def __init__(self, name: str,email: str,phone_number: str, password: str, kycID: str, service_type: str):
        self.__name = name
        self.__email = email
        self.__kycID = kycID
        self.__phone = phone_number
        self.__rating = Rating.UNASSIGNED
        self.__created_at = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.__last_login = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.__available = False
        self.__serviceType = service_type
        self.__driver_id = self._generate_username()
        self.__coordinates = Location(0,0)
        self.__trips = None
        self.__password = self._hash_password(password)

    @property
    def get_name(self):
        return self.__name

    @property
    def get_phone(self):
        return self.__phone
    
    @property
    def creationTime(self):
        return self.__created_at
    
    @property
    def loginTime(self):
        return self.__last_login

    @property
    def email(self):
        return self.__email
    
    @property
    def driver_id(self):
        return self.__driver_id

    @property
    def rating(self):
        return self.__rating

    @property
    def available(self):
        return self.__available
    
    @property
    def coordinates(self):
        return self.__coordinates
    
    @property
    def service_type(self):
        return self.__serviceType
    
    @property
    def get_trips(self):
        return self.__trips
    

    @rating.setter
    def rating(self, rating):
        self.__rating = (self.rating + rating) // 2   

    @available.setter
    def available(self, isavailable):
        self.__available = isavailable

    @email.setter
    def email(self, email):
        self.__email = email

    @coordinates.setter
    def coordinates(self, longitude, latitude):
        self.__coordinates.longitude = longitude
        self.__coordinates.latitude = latitude


    def _generate_username(self) -> str:
        return generate_user_ids()
    
    def _hash_password(self, password: str) -> str:
        return bcrypt.hash(password)

    def verify_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.__password)