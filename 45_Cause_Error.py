try:
     print("한자리수 나누기 전용 계산기 입니다")
     num1 = int(input("수를 입력 하세요 : "))
     num2 = int(input("수를 입력 하세요 : "))
     if num1 >= 10 or num2 >= 10:
         raise ValueError
     print(int(num1/num2))
except ValueError:
    print("잘못된 값을 입력")