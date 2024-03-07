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
