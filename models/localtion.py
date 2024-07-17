
class Location:

    def __init__(self,longitude,latitude):
        self.__longitude = longitude
        self.__latitude = latitude

    @property
    def longitude(self):
        return self.__longitude
    @property
    def latitude(self):
        return self.__latitude
