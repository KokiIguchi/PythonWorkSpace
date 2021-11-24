#この関数を使って作る
def word_lower(string):
    return string.lower()

def delete_char(string):
    ng_list = ' .,:()"[]'
    for c in ng_list:
        string = string.replace(c,' ')
        return string

def word_sprit(string):
    words =string.split(' ')
    return words

def remove_null(words_list):
    if''in words_list:
        del words_list['']
    if' 'in words_list:
        del words_list[' ']
    return words_list

DATA_FILENAME = 'files/sentence.txt'

word_dic ={}   #空の辞書作成
with open (DATA_FILENAME)as f:
    for line in f:
        line = line.strip()
        line = word_lower(line)
        line = delete_char(line)
        #上の関数を使って行った処理の後の状態を表示
        print(line)
        words = word_sprit(line)
        for word in words:
            if word in word_dic:
                word_dic[word] += 1
            else:
                word_dic[word] = 1
        word_dic = remove_null(word_dic)



