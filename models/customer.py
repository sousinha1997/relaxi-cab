import datetime, time
from typing import Optional
from passlib.hash import bcrypt
from models.localtion import Location
from utils.common import Rating
from utils.utils import generate_user_ids


class Customer:
    def __init__(self,  name: str, password: str, phone_number: str, email: str):
        self.__name = name
        self.__email = email
        self.__phone_number = phone_number
        self.__rating = Rating.UNASSIGNED
        self.__created_at = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.__last_login = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.__customer_id = self._generate_username()
        self.__coordinates = Location(0,0)
        self.__trips = None 
        self.__password = self._hash_password(password)
    
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_phone(self):
        return self.__phone_number

    @property
    def customer_id(self):
        return self.__customer_id
    
    @property
    def trips(self):
        return self.__trips

    @property
    def rating(self):
        return self.__rating

    @property
    def email(self):
        return self.__email
    
    @property
    def coordinates(self):
        return self.__coordinates
    
    @property
    def creationTime(self):
        return self.__created_at
    
    @property
    def loginTime(self):
        return self.__last_login
    

    @rating.setter
    def rating(self, rating):
        self.rating = (self.rating + rating) 

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
    


