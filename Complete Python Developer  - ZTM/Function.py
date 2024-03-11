# Fucntional Programming
# Pure Functions

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


