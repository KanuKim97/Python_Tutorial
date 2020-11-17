# List []

subway = [10, 20, 30]
print(subway)

subway = ["김건우", "김건우2", "김건우3"]
print(subway)

print(subway.index("김건우3"))

# Add factor at List
subway.append("김건우4")
print(subway)

# Insert factor at List
subway.insert(1, "홍길동")
print(subway)

# Pop factor at List
subway.pop()
print(subway)

# Count same factor
subway.append("김건우")
print(subway)
print(subway.count("김건우"))

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

