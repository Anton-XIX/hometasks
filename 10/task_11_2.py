class Car():
    def __init__(self, model: str, year_of_release: int,  speed: int = 0):
        self.__model = model
        self.__speed = speed
        self.__year_of_release = year_of_release

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def year_of_release(self):
        return self.__year_of_release

    @year_of_release.setter
    def year_of_release(self, year_of_release: int):
        self.__year_of_release = year_of_release

    def increase_speed(self):
        self.__speed += 5

    def decrease_speed(self):
        self.__speed -= 5

    def stop_moving(self):
        self.__speed = 0

    def change_direction(self):
        self.__speed *= -1