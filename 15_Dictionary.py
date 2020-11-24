Dictionary = {1: "mike", 2: "chris"}
print(Dictionary[1])
print(Dictionary[2])

print(Dictionary.get(1))

# print(Dictionary[3])
# Key Error

print(Dictionary.get(3))  # None
print(Dictionary.get(3, "Able"))

print(1 in Dictionary)
print(3 in Dictionary)

Dictionary = {"A-1": "k", "A-2": "i"}
print(Dictionary["A-1"])

print(Dictionary)
Dictionary["A-3"] = "L"
Dictionary["A-1"] = "A"
print(Dictionary)

del Dictionary["A-3"]
print(Dictionary)

print(Dictionary.keys())

print(Dictionary.values())

print(Dictionary.items())

Dictionary.clear()
print(Dictionary)