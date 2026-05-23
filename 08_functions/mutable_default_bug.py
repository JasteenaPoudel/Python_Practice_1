def add_item(item, items = []):
    items.append(item)
    return items

print(add_item("Apple"))
print(add_item("Mango"))
print(add_item("Litchi"))

['Apple']
['Apple', 'Mango']
['Apple', 'Mango', 'Litchi']


def add_items(item, items = None):
    if items is None:
        items = []

    items.append(item)
    return items

print(add_items("Apple"))
print(add_items("Mango"))
print(add_items("Litchi"))

# listing out the names of vegetables

def list_vegies(item, items=[]):
    items.append(item)
    return items

print(list_vegies("Potato"))
print(list_vegies("Tomato"))
print(list_vegies("Spinach"))
print(list_vegies("Brinjal"))


# corrected version

def list_vegy(item , items = None):
    if items is None:
        items = []

    items.append(item)
    return items

print(list_vegy("Potato"))
print(list_vegy("Tomato"))
print(list_vegy("Spinach"))
print(list_vegy("Brinjal"))


