# print("a" + "b")
# print("a", "b")

# method 1

print("나는 %d 살입니다." % 20)
print("나는 %s 입니다." % "mike")
print("나의 학점은 %c입니다." % "A")
print("나는 %s와 %s 가 좋습니다" % ("사과", "바나나"))

# method 2
print("나는 {}살입니다".format(20))
print("나는 {}와 {}가 좋습니다".format("사과", "바나나"))
print("나는 {0}와 {1}가 좋습니다".format("사과", "바나나"))
print("나는 {1}와 {0}가 좋습니다".format("사과", "바나나"))

# method 3
print("나는 {age}살이며, {favorite}를 가장 좋아합니다".format(age=20, favorite="전자제품"))
print("나는 {age}살이며, {favorite}를 가장 좋아합니다".format(favorite="전자제품", age=20))

# method 4 (ver 3.6 over)
age = 20
favorite = "전자제품"
print(f"나는 {age}살이며, {favorite}을 가장 좋아합니다")
