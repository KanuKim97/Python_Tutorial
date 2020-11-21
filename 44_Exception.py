try:
    print("For Division")
    nums = []

    nums.append(int(input("숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 수를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))


except ValueError:
    print("잘못된 입력값")
except ZeroDivisionError as err:
    print(err)
except IndexError:
    print("알 수 없는 오류가 발생함")
except Exception as err:
    print(err)