# import sys

print("python", "java", "JS", sep=" vs ")
print("python", "java", sep=" , ")
print("python", "java", sep=",", end="?")
print("!")

# print("python", "Java", file=sys.stdout)
# print("python", "java", file=sys.stderr)

scores = {"수학": 0, "영어": 10, "과학": 20}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=": ")

for num in range(1, 21):
    print("Number : " + str(num).zfill(3))

NUMBER_int = input("정수 값 입력")  # 항상 문자열 형태로 저장
print(NUMBER_int)
print(type(NUMBER_int))
