import time
import functools
from datetime import datetime

# task 1

# def hello_function(fn):
#     def wrapper():
#         if 9 <= datetime.now().hour < 21:
#             fn()
#         else:
#             print('Уже поздно')
#     return wrapper


# @hello_function
# def say_whee():
#     print('Whee!')
# say_whee()


## task 2

# def timer(func):
#     def tm(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         print('Время выполнения функции:', time.time() - start_time)
#         return res

#     return tm

# @timer
# def function(x, y):
#     return x + y

# function(123, 2121)


# task 3

# def repeat(num):
#     def wrapper(func):
#         def wrapper_repeat(*args, **kwargs):
#             for i in range(num):
#                 func(*args, **kwargs)
#         return wrapper_repeat
#     return wrapper

# @repeat(num=4)
# def function(name):
#     print(f"{name}")

# function('Python')


# task 4

# users = {'user1': 123, 'user2': 456, 'user3': 678}

# def check_user(func):
#     def wrapper(username, password):
#         global users
#         if username in users.keys() :
#                 if password in users.values():
#                         func(username, password)
#                 else :
#                         raise Exception ('Password is invalid')
#         elif username not in users.keys() :
#                 if password in users.values() :
#                         raise Exception ('Username is not defined!') 
#                 else :
#                         raise Exception ('Username and password are incorrect!')  
#     return wrapper

# @check_user
# def login(username, password):
#     print(f'Welcome, {username}!')

# login('user1', 123)


# task 5

# def myDecorator(func):
#     def wrapper(a, b=1, *args, **kwargs):
#         print('Calling testFunc',((a, b, *args), kwargs))
#         print('argument a:', a)
#         print('argument b:', b)
#         print('argument args:', args)
#         print('argument kwargs:', kwargs)
#         print('Finished testFunc', func(a, b, *args, **kwargs))
#     return wrapper

# @myDecorator
# def testFunc(a, b=1, *args, **kwargs):
#     return a + b
# testFunc(2, 3, 4, 5, c=6, d=7)
# print()
# testFunc(2, c=5, d=6)
# print()
# testFunc(10)









