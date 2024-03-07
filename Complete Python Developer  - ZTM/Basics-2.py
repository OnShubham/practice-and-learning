# COnditonal Logic and Loops

# if, elif, else
# for loops
# while loops
# break, continue, pass
# range

a = 1
b = 2

if (a == b):
    print('a is equal to b')
else:
    print('a is not equal to b')


#######################

    password = int(1234)
    name = str('shubham')

    if (password == 1234 and name == 'shubham'):
        print('welcome')

###########

# ternary operator

is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"

# wrire in a single line if else statement
print(can_message)

# Short Circuiting

is_friend = True
is_user = True

if is_friend or is_user:
    print('best friend forever')


# Logical Operators

# and
# or
# not

# Example :

is_magician = True
is_expert = False

if is_magician and is_expert:
    print('you are a master magician')
elif is_magician and not is_expert:
    print('at least you are getting there')
else:
    print('you need magic power')


# Loops

for item in 'hello':
    print(item)

# iterate over a list

for item in [1, 2, 3, 4, 5]:
    print(item)

# iterate example

    item = {
        'password': 1234,
        'name': 'shubham',
        'email': 'shubam@gmail.com'

    }

    for user in item.items():
        print(user)
# Counter
my_list = [1, 2, 3, 4, 5, 6, 7]

counter = 0

for item in my_list:
    counter = counter + item
print(counter)


# Range ()

for number in range(10):
    print(number)


# Exercise : Chek a Duplicate  Value

    some_list = ['a', 'b', 'c', 'b', 'd', 'e', 'a']

duplicate = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicate:
            duplicate.append(value)

        print(duplicate)

# Function

# def keyword is used to define a function


def say_hello():   # function definition
    print('hello')


say_hello()  # function call

# function with parameter


def say_hello(name, emoji):  # function definition
    print(f'hello {name} {emoji}')  # function body


# function call
say_hello('shubham', '😊')

# function with default parameter


def say_hello(name='shubham', emoji='😊'):  # function definition
    print(f'hello {name} {emoji}')  # function body


# function call
say_hello()

# defalut parameter should be at the end of the parameter list

# return statement


def add(a, b):
    return a + b

# return statement is used to return a value from a function

# method vs function


# list()
# print()
# max()
# min()
# input()
# int()
# str()
# len()
# help()
# dir()
# type()
# id()

# Docstring
# it is a string that is written as a first line of a function and it is used to describe the function
# Docstring is used to describe the function

def test(a):
    '''
    info: this function test and print param a

    '''
    print(a)

    test('!!!!')


# Clean Code

# 1. descriptive variable name
# 2. descriptive function name
# 3. descriptive parameter name
# 4. descriptive docstring
# 5. descriptive comments
# 6. descriptive file name
# 7. descriptive folder name
# 8. descriptive class name
# 9. descriptive method name
# 10. descriptive module name
# 11. descriptive package name
# 12. descriptive argument name
# 13. descriptive return value name
# 14. descriptive constant name
# 15. descriptive loop variable name
# 16. descriptive exception name
# 17. descriptive code block name
# 18. descriptive code block comment
# 19. descriptive code block docstring
# 20. descriptive code block comment
# ================================================================

    def is_even(num):
        return num % 2 == 0

        print(is_even(50))

# highest number


def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([20, 10]))


# Scope of a variable

# Scope - What variables do I have access to?

print(name())  # NameError: name 'name' is not defined


# Scope rules

# 1. start with local
# 2. Parent local?
# 3. Global
# 4. built in python function

# LEGB Rule
# L - Local
# E - Enclosing function local
# G - Global
# B - Built in python function

# global keyword

# global keyword is used to declare a global variable inside a function

# nonlocal keyword
# nonlocal keyword is used to declare a variable in an enclosing function


# why do we need scope?
# 1. security
# 2. avoid namespace collision
# 3. code maintainability
# 4. code reusability
# 5. code readability
# 6. code optimization
# 7. code performance
# 8. code scalability
# 9. code reliability
# 10. code flexibility
# 11. code consistency
# 12. code portability
# 13. code simplicity
# 14. code complexity
# 15. code understandability
# 16. code predictability
# 17. code stability
# 18. code robustness
# 19. code flexibility
# 20. code maintainability
# 21. code reusability
# 22. code readability
# 23. code optimization
# 24. code performance
# 25. code scalability
