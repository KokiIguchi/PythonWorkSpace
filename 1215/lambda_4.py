import random  # 乱数用モジュール

# 初期化
marks = ('S','H','C','D') # 4種類のマーク
cards = [] # デッキ用リスト
for m in marks:
    for n in range(1,14):
        t = (m,n) # タプルでカード生成
        cards.append(t) # リストに追加
#5枚選択
select_cards = random.sample(cards,5)
#並び替え
select_cards.sort(reverse = True, key=lambda x: x[1])
#出力
print(select_cards)

'''ライブラリを読み込んで、自分で色々試してみるのが一番。by後藤T'''