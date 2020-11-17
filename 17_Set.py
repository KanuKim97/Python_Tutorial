my_set = {1, 2, 3, 4, 5, 6, 7, 7, 8, 8}
print(my_set)

name = {"김건우", "김건우2", "김건우3"}
name_2 = set(["김건우", "김건우4"])

print(name & name_2)
print(name.intersection(name_2))

print(name | name_2)
print(name.union(name_2))

print(name - name_2)
print(name.difference(name_2))

name_2.add("김건우2")
print(name_2)

name.remove("김건우2")
print(name)