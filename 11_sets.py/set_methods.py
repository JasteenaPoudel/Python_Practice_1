names = {"Ram", "Jiggu","Tiggu", "Hari"}
names.add("jenny")

names.remove("Hari")

print(names)

names.discard("unknown")
print(names)

names.remove("Jiggu")
print(names)


# even if item is not in present in the set, discard would not show any error but if we use remove it shows the erroe

names.clear()
print(names)


color = {"Violet", "Indigo", "Blue", "Green", "Lime"}
print(color)

color.remove("Indigo")
print(color)

# color.remove("Red")
# print(color)

color.discard("blue")
print(color)

color.clear()
print(color)

