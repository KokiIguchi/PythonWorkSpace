import os
import pickle

DATA_FILENAME = 'word.pkl'

if os.path.isfile(DATA_FILENAME):   # ファイルが有るか？
    # ファイルから単語リストを読み込む
    with open(DATA_FILENAME) as f: #ファイルを「f」として開く
        words_list = pickle.load(f)#P.15
else:                               # ファイルが無い時
    words_list = []

while True:
    input_word = input('単語を入力してください：') #input_wordに入力値格納
    if input_word == "": #入力値が""(空)だった場合
        break   #breakで抜ける
    if input_word == 'LIST':    #LISTと入力された時の処理
        print('単語リスト：', words_list)   #単語が入っているリストを出力
        continue    #continue で続ける
    if input_word in words_list:    #入力された値がリストに存在している場合
        print('すでに登録済です')
        continue    #continue で続ける
    else:   #入力された値がリストに存在していない場合
        words_list.append(input_word)   #入力値をリスト(words_list)に繋げている
else:
    pass

# 終了時のメッセージ
print('終了します')
print('これまでに覚えた単語：', words_list)

# ファイルに単語リストを書き込む
with open(DATA_FILENAME, 'wb') as f: #モード:wとは？
    pickle.dump(words_list,f)
