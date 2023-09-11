def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

#twice
from decorators import do_twice
@do_twice
def say_wheel():
    print("Whee!")

say_wheel()

def greet(name):
    print(f"Hello {name}")

greet("World")

def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greeting("Adam")
print(hi_adam)

# print(say_wheel)
# print(say_wheel.__name__)
help(say_wheel)