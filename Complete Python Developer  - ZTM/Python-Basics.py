# int
a = 23
print(type(a))

# Float
a = 23.4
print(type(a))

# math functions
print(round(3.1))
print(abs(-20))

# optional bin() function

a = " heyy what is up"

print(type(a))

# string methods

print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.strip())
print(a.replace("h", "j"))
print(a.find("h"))
print(a.count("h"))
print(a.startswith("h"))
print(a.endswith("h"))
print(a.split(" "))
print(a.join(" "))
print(a.partition(" "))
print(a.rpartition(" "))


# string concatenation

a = "hello"
b = "world"
print(a + " " + b)

# type Conversion

a = "100"
b = "200"
print(int(a) + str(b))


# formatted strings

name = "Shubahm"
age = 23

print(f"hi {name}. You are {age} years old")


# build in function

print(len("hello"))
print(type(3))
print(id(3))
print(help(int))
print(dir(int))

# list

a = [1, 2, 3, 4, 5]
print(a)


# type conversion

name = 'shubhma'
a = 1
b = 2.5

print(type(list(name)))


# type conversion programe a like age

birth_year = input('what the your age ?')

age = 2024 - int(birth_year)

print(f'your age is: {age}')


# List
# list are mutables
# list are ordered
# list can have duplicate values
# list can have different data types

# list are write in a square bracket [  ]

a = [1, 2, 3, 4, 5]  # list of integers
b = ["a", "b", "c", "d"]  # list of strings
c = [1, "a", 2.5, True]  # list of different data types
print(a)


# list slicing

cart = [
    "notebook",
    "pen",
    "pencil",
    "eraser",
    "sharpner",
    "scale",
    "compass",
    "divider",
]

print (cart[0:4])

# tuple are immutable
# tuple are ordered
# tuple can have duplicate values
# tuple can have different data types
# tuple are write in a round bracket (  )

a = (1, 2, 3, 4, 5)  # tuple of integers
b = ("a", "b", "c", "d")  # tuple of strings
c = (1, "a", 2.5, True)  # tuple of different data types
print(a)