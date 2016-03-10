# def foo(bar):
#     return bar + 1
#
# print(type(foo))
#
#
# def call_foo_with_arg(foo, arg):
#     return foo(arg)
#
# print(call_foo_with_arg(foo, 3))


# def parent():
#     print("Printing from the parent() function.")
#
#     def first_child():
#         return "Printing from the first_child() function."
#
#     def second_child():
#         return "Printing from the second_child() function."
#
#     print(first_child())
#     print(second_child())
#
# parent()

# def parent(num):
#     def first_child():
#         return "Printing from the first_child() function."
#
#     def second_child():
#         return "Printing from the second_child() function."
#
#     try:
#         assert num == 10
#         return first_child
#     except AssertionError:
#         return second_child
#
# foo = parent(10)
# bar = parent(11)
#
# print(foo)
# print(bar)
#
# print(foo())
# print(bar())

# def my_decorator(some_function):
#     def wrapper():
#         print("Something is happening before some_function() is called.")
#         some_function()
#         print("Something is happening after some_function() is called.")
#     return wrapper
#
#
# def just_some_function():
#     print("Wheee!")
#
# just_some_function = my_decorator(just_some_function)
# just_some_function()

# def my_decorator(some_function):
#     def wrapper():
#         num = 10
#         if num == 10:
#             print("Yes!")
#         else:
#             print("No!")
#         some_function()
#         print("Something is happening after some_function() is called.")
#     return wrapper


# def just_some_function():
#     print("Wheee!")
#
# just_some_function = my_decorator(just_some_function)
# just_some_function()

# @my_decorator
# def just_some_function():
#     print("Wheee!")
#
# just_some_function()

# import time
#
#
# def timing_function(some_function):
#     """
#     Outputs the time a function takes
#     to execute.
#     """
#     def wrapper():
#         t1 = time.time()
#         some_function()
#         t2 = time.time()
#         return "Time it took to run the function: " + str((t2 - t1)) + "\n"
#     return wrapper
#
#
# @timing_function
# def my_function():
#     num_list = []
#     for num in (range(0, 10000)):
#         num_list.append(num)
#     print("\nSum of all the numbers: " + str((sum(num_list))))
#
#
# print(my_function())

# from time import sleep
#
#
# def sleep_decorator(some_function):
#
#     """
#     Limits how fast the function is
#     called.
#     """
#
#     def wrapper(*args, **kwargs):
#         sleep(2)
#         return some_function(*args, **kwargs)
#     return wrapper
#
#
# @sleep_decorator
# def print_number(num):
#     return num
#
# print(print_number(222))
#
# for num in range(1, 6):
#     print(print_number(num))

from functools import wraps
from flask import g, request, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/secret')
@login_required
def secret():
    pass
