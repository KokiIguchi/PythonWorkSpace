DATA_FILENAME = 'files/word_list.txt'

word_dic ={}#空の辞書作成
with open (DATA_FILENAME)as f:
    for word in f:
        word = word.strip()
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
#練習4 アルファベット昇順並び替え sorted()


Len_max = 0
for word in word_dic.keys():
    Len_max = max(Len_max,len(word))

for word in sorted(word_dic):
    for word in sorted(word_dic.keys()):
        print(f'{word}:{word_dic[word]}')

# print(word_dic)
