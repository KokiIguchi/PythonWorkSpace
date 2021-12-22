import datetime
def log_file(func):
    def funcname(*args,**kwargs):
        '''ここのファイルを使う書き方とか、functionの部分書けるようにしとく。'''
        #ファイルを使用します
        LOG_FILENAME = 'python.log'
        dt_now = datetime.datetime.now();
        #ファイル操作
        with open(LOG_FILENAME,'a')as f:
            f.write(
                f'{dt_now}function:{func.__name__}args:{args}kwargs:{kwargs}\n'
            )

        # print('function',function,'args:',args,'kwargs:',kwargs)
        result = func(*args,**kwargs)
        return result
    return funcname






# main
@log_file
def test(n):
    print('test->{}'.format(n))

# 呼出
test(100)

# 呼出
for i in range(5):
    test(i)