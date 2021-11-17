def str2int(s):
    """str2int 文字列を数値に変換した値を返す"""
    if type(s) is str:
        if s.isdigit():#先生は.numericを使用してた
            return int(s)
        else:
            return 0
    else:
        return s

def list2int(s):
    """list2int 文字列を数値に変換した値を返す（List対応）"""
    # if type (s) is str:
    #     return str2int(s)
    # elif type (s) is list:
    #     result = []
    #     for i in s:
    #         result.append(str2int(i))
    #     return result
    # else:
    #     return None
    if isinstance(s,list):
        str_list = []
        for i in s:
            str_list.append(str2int(i))
        return str_list
    elif type(s) is str:
        return str2int(s)
    else:
        return None

print(list2int(['5','ab','100',10,1]))
print(list2int('100'))
print(list2int('xyz'))
