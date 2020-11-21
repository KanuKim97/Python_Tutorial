class BigNumberErr(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한자리수 나누기 전용 계산기 입니다")

    num1 = int(input("수를 입력 하세요 : "))
    num2 = int(input("수를 입력 하세요 : "))

    if num1 >= 10 or num2 >= 10:
        raise BigNumberErr("입력값 : {0}, {1}".format(num1, num2))
    print(int(num1 / num2))

except ValueError:
    print("잘못된 값을 입력")

except BigNumberErr as err:
    print("에러")
    print(err)

finally:
    print("이용 감사 합니다")
