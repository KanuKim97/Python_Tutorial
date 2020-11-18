def open_accoount():
    print("새로운 계좌가 생성되었습니다")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+ money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다 잔액은 {0}원 입니다".format(balance - money))
        return balance-money
    else:
        print("잔액이 부족합니다")
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 10000)
commission, balance = withdraw_night(balance, 500)
print(commission, balance)
