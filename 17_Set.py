my_set = {1, 2, 3, 4, 5, 6, 7, 7, 8, 8}
print(my_set)

name = {"mike", "mike2", "mike3"}
name_2 = set(["mike", "mike4"])

print(name & name_2)
print(name.intersection(name_2))

print(name | name_2)
print(name.union(name_2))

print(name - name_2)
print(name.difference(name_2))

name_2.add("mike2")
print(name_2)

name.remove("mike2")
print(name)