class Phone:
    def __init__(self, model: str, cost: int, year_of_release: int):
        self.__model = model
        self.__cost = cost
        self.__ = year_of_release

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost

    @property
    def year_of_release(self):
        return self.__year_of_release

    @year_of_release.setter
    def year_of_release(self, year_of_release: int):
        self.__year_of_release = year_of_release

    def get_data(self):
        return f'{self.__model}costs{self.__cost}and release year is{self.__year_of_release}'

    def get_usd_cost(self):
        return self.__cost / 2.62


class Gun:
    def __init__(self, model: str, cost: int, caliber: float):
        self.__model = model
        self.__cost = cost
        self.__caliber = caliber

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: int):
        self.__model = model

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost

    @property
    def caliber(self):
        return self.__caliber

    @caliber.setter
    def caliber(self, caliber: int):
        self.__caliber = caliber

    def get_data(self):
        return f'{self.__model}costs{self.__cost}and its caliber  is{self.__caliber}'

    def get_caliber_type(self):
        if self.__caliber > 18.2:
            return 'large-caliber'
        elif self.__caliber > 14.7:
            return 'middle-caliber'
        elif self.__caliber > 8.7:
            return 'Normal-caliber'
        else:
            return 'small-bored'


class Character:
    def __init__(self, name: str, age: int, gender: str):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    def get_person_info(self):
        return f'{self.__name}is{self.__age}years old'

    def is_adult(self):
        if self.__age >= 18:
            return True
        else:
            return False


class Triangle:
    def __init__(self, length_a: int, length_b: int, length_c: int):
        self.__length_a = length_a
        self.__length_b = length_b
        self.__length_c = length_c

    @property
    def length_a(self):
        return self.__length_a

    @length_a.setter
    def length_a(self, length_a: str):
        self.__length_a = length_a

    @property
    def length_b(self):
        return self.__length_b

    @length_b.setter
    def length_b(self, length_b: str):
        self.__length_b = length_b

    @property
    def length_c(self):
        return self.__length_c

    @length_c.setter
    def length_c(self, length_c: str):
        self.__length_c = length_c

    def get_perimetr(self):
        return (self.__length_a + self.__length_b + self.__length_c) / 2

    def is_equilateral_triangle(self):
        if self.__length_a == self.__length_b:
            return True
        elif self.__length_a == self.__length_c:
            return True
        elif self.__length_b == self.__length_c:
            return True
        else:
            return False


class Cat:
    def __init__(self, name: str, weight: int, age: int):
        self.__name = name
        self.weight = weight
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    def meow(self):
        print('Meow')

    def weight_status(self):
        if self.__weight > 6:
            print('Cat is too fat')
        else:
            print('Weight is normal')
