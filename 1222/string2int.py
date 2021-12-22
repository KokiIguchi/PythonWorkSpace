def int_true(x):
    if type(x) is str:
        if x.isnumeric():
            return int(x)
        else:
            return(0)
    else:
        return(x)


#main
print(int_true('aaa'))
print(int_true('10'))
print(int_true('bbb'))
print(int_true(100))


