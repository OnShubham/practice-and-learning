# Decorators
# Decorators are a way to modify the behavior of a function without changing its code.
# Decorators are a higher order function, which means they take another function as an argument and return another function.
# Decorators are used to add functionality to an existing function.

# Example 1

def my_decorator(func):
    def wrap_func():
        print("**********")
        func()
        print("**********")
    return wrap_func


# Highet order Function HOC

def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func

# Decrator


def my_decorator(func):
    def wrap_func(self, a, b):
        x = a * b
        return x

    func()

    return wrap_func


@my_decorator
def hello():
    a = 2
    b = 4

    return a * b

