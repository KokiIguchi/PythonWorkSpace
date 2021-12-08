def func1():
    print("Hello")

def func2():
    print("Goodbye")
# main


run_list = {'a': func1, 'b': func2}

while True:
    select =input('どちらを実行しますか？')

    #P.104 制御構文について
    if select == '':#入力された文字が空文字だった場合
        break

    if select in run_list.keys(): #run_list(辞書)のKeyに入力値が存在するとき
        run_list[select]()
    else:
        print('どちらかを選択して下さい')


print(run_list.keys())