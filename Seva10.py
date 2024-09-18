class Animal:
    def make_sound(self,):
       print('Животные')

class Dog(Animal):
   def sobaka(self,):
       print('Gafff')

class Cat(Animal):
    def koshka(self,):
        print('Myuu')


class Cow(Animal):
    def korova(self,):
        print('Muuuuuu')




class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Mapкa: {self.brand}, Год выпуска: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, four_koleso):
        super().__init__(brand, year)
        self.four_koleso = four_koleso

    def display_info(self):
        super().display_info()
        print(f'Четыре колеса: {self.four_koleso}')


class Motorcycle(Vehicle):
    def __init__(self, brand, year, two_koleso):
        super().__init__(brand, year)
        self.two_koleso = two_koleso

    def display_info(self):
        super().display_info()
        print(f'Два колеса: {self.two_koleso}')


car1 = Car("Mersedes", 2025, 4)
motorcycle1 = Motorcycle("Honda", 2012, 2)

car1.display_info()
print()
motorcycle1.display_info()