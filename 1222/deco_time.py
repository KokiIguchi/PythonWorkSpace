from functools import wraps
import time
def stop_watch(func) :
    @wraps(func)
    def wrapper(*args, **kargs) :
        start = time.time()
        result = func(*args,**kargs)
        process_time =  time.time() - start
        print(f"実行関数：{func.__name__} 実行時間{process_time}")
        return result
    return wrapper


# main
@stop_watch
def test(n):
    for i in range(n):
        time.sleep(i)





test(3)
test(5)