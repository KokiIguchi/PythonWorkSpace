import math

def input_int(message):
    value = input(f'{message}を入力してください')
    if value.isnumeric():
        value =int(value)
    else:
        value = 0
    return value

def calc_payment(total,num_people):
    money = total / num_people
    money = math.ceil(money/100)*100
    pay_codinator =total - money*(num_people -1)
    return [money,pay_codinator]

def output_payment(money,pay_codinator,num_people):
    print(f'支払金額：{money}円({num_people -1}人)')
    print(f'幹事金額:{pay_codinator}円')





total =input_int('支払合計金額')
num_people = input_int('参加者人数')
[money,pay_codinator] = calc_payment(total,num_people)
output_payment(money,pay_codinator,num_people)

#____________________________________
#↓素体はこれ(関数つかえてない{特に0や空白を入力された場合を含んでない})

# tomoney = int(input('支払合計金額を入力してください：'))
# people = int(input('参加者人数を入力してください：'))

# only = tomoney /people
# only = math.ceil(only/100)*100
# cordinator = tomoney - only*(people -1)

# print(f'支払金額：{only}円({people -1}人)')
# print(f'幹事金額：{cordinator}円')

#____________________________________
