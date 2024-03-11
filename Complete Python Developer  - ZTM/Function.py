# Fucntional Programming
# Pure Functions

import functools
from functools import reduce


def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([1, 2, 3, 4, 4]))

# Remove the Duplicated Values


def remove_duplicates(lis):
    new_list = []
    for item in lis:
        if item not in new_list:
            new_list.append(item)
    return new_list


print(remove_duplicates([1, 2, 3, 4, 4, 4, 5, 6, 7, 7, 8]))

# Used a Dictionary


def list_of_products(products):
    result = []
    for product in products:
        result.append({
            "Name": product["Name"],
            "Price": product["Price"],
            "Quantity": product["Quantity"]
        })
    return result


# Example products dictionary
products = [
    {"Name": "Book", "Price": 3.99, "Quantity": 10},
    {"Name": "Pen", "Price": 1.49, "Quantity": 20},
    {"Name": "Notebook", "Price": 4.99, "Quantity": 15}
]

# Call the function to list products
listed_products = list_of_products(products)

# Print the listed products
for product in listed_products:
    print(product)


# Mao, Filter, Zip, Reduce

    def multiply_by2(x):
        return x * 2

    print(list(map(multiply_by2, [1, 2, 3,])))

# filter

    def only_odd(item):
        return item % 2 != 0

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(only_odd, my_list)))

# Zip

zip_list = [1, 2, 3]
zip_list2 = [10, 20, 30]

print(list(zip(zip_list, zip_list2)))


# string

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

print(str(zip(a, b)))


# reduce
# importing functools for reduce()

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# lambda function

my_list = [1, 2, 3]

new_list = list(map(lambda item: item*2, my_list))
print(new_list)
