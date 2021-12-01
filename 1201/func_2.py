def tax_included(price, tax=10):
    """税込み金額を計算する。税率を省略した場合は10%になる。"""
    if tax < 0:
        return None
    else:
        return int (price*(1+tax/100))

#5000円の税込み金額は5500円
print('{}の税込み金額は{}円'.format(5000,tax_included(5000)))
#5000円の消費税8%の税込み金額は5400円
print('{}の税込み金額は{}円'.format(5000,tax_included(5000,8)))
#5000円の消費税-5%の税込み金額はNone円
print('{}の税込み金額は{}円'.format(5000,tax_included(5000,-5)))
