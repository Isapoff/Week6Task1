# task 1

# class Student:
#     def __init__(self, name, lastname, department, year_of_entrance):
#         self.name = name
#         self.lastname = lastname
#         self.department = department
#         self.year_of_entrance = year_of_entrance

#     def get_student_info(self):
#         print(f'{self.name.title()} {self.lastname.title()} поступил в {self.year_of_entrance} на факультет: {self.department}')

# stud = Student(name = 'Вася', lastname = 'Иванов', department = 'Програмирование', year_of_entrance = '2017 г.')
# stud.get_student_info()


# task 2

# class BankAccount:
#     def __init__(self, balance):
#         self.bal = balance
#     def withdraw(self, amount):
#         self.bal -= amount
#     def deposit(self, amount):
#         self.bal += amount
# my_acc = BankAccount(150)
# my_acc.withdraw(50)
# my_acc.deposit(70)
# print(my_acc.bal)

    
# task 3

# class Airplane:
#     def __init__(self, make, model, year, max_speed):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = 0
#         self.is_flying = False

#     def take_off(self):
#         self.is_flying = True
#         print(f'{self.make} {self.model} was take off')

#     def fly(self):
#         self.odometer = 500
#         print(f'{self.make} {self.model} is flying now {self.max_speed} km/h')
#     def land(self):
#         self.is_flying = False
#         print(f'{self.make} {self.model} landed, he has {self.odometer} km on it')

# plane = Airplane('Boeing', '747', '2017', 910)
# print(plane.take_off())
# print(plane.fly())
# print(plane.land())


