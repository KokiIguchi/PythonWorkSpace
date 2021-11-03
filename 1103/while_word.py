import os
word_list=[]
#os.psth.exists(word.txt)
#読み込む処理がまだ書けてない
#下の部分で書き込み処理かけて入ればok
while  True:
    word = input("単語を入力してください:")
    if word == "":
        print("終了します")
        break
    elif word == "LIST":
        print("単語リスト:",word_list)
        continue
    elif word in word_list:
        print("すでに登録済みです")
        continue
    else:
        word_list.append(word)
print("これまでに覚えた単語",word_list)

with open('word.txt','w')as f:
    for d in word_list:
        f.write("%s\n" % d)
