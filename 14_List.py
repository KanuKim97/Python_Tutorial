# List []

subway = [10, 20, 30]
print(subway)

subway = ["mike", "mike2", "mike3"]
print(subway)

print(subway.index("mike3"))

# Add factor at List
subway.append("mike4")
print(subway)

# Insert factor at List
subway.insert(1, "chris")
print(subway)

# Pop factor at List
subway.pop()
print(subway)

# Count same factor
subway.append("mike")
print(subway)
print(subway.count("mike"))

# Sort
List_num = [1, 3, 2, 5, 7]
List_num.sort()
print(List_num)

# Reverse List Factor
List_num.reverse()
print(List_num)

# Remove All
List_num.clear()
print(List_num)

# Extend List
List_Upper = ["A", "B"]
subway.extend(List_Upper)
print(subway)

