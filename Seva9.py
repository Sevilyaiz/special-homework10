class Artist:
    def __init__(self, name, art, drawing, painting):
        self.name = name
        self.art = art
        self.drawing = drawing
        self.painting = painting

    def change_name(self, new_name):
        self.name = new_name

    def change_number(self, new_art):
        self.art = new_art

    def change_number(self, new_drawing):
        self.drawing = new_drawing

    def change_mail(self, new_painting):
        self.painting = new_painting

people = Artist('Sofa', 'Van Gog', 'pencil','paints')
print(people.name, people.art, people.drawing, people.painting)






class Person:
      def __init__(self,name, age):
          self.name = name
          self.age = age

people = Person('Sofa', '22')
print(people.name, people.age)

people = Person('Lara', '27')
print(people.name, people.age)

people = Person('Joni', '45')
print(people.name, people.age)

people = Person('Tom', '33')
print(people.name, people.age)



Дополнительные задания:

class Student:
    def __init__(self, name, age, groupNumber):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber


new_Student = Student('Jon', '18', '10A')
print(new_Student.name, new_Student.age, new_Student.groupNumber)

getStudent = Student('Lola', '20', '11Б')
print(getStudent.name, getStudent.age, getStudent.groupNumber)

setStudent = Student('Toni', '13', '8Б')
print(setStudent.name, setStudent.age, setStudent.groupNumber)

retStudent = Student('Flora', '12', '6A')
print(retStudent.name, retStudent.age, retStudent.groupNumber)

betStudent = Student('Ivan', '14', '9A')
print(betStudent.name, betStudent.age, betStudent.groupNumber)




class Math:
     def init_ (self, a, b):
          self.a = a
          self.b = b

     def addition(self):
          return self.a + self.b

     def multiplication (self):
          return self.a * self.b






class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year


    def start(self) :
          return "Автомобиль заведен"

    def stop(self):
          return 'Атомобиль заглушен'

qwe = Car(  "Malibu", 'blue', 2024)
print (qwe.start())
print(vars(qwe))