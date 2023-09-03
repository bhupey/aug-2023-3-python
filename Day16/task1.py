import time
def execution_time(func):
    def inner_fxn(*args, **kwargs):
        start = time.time()
        a= func(*args, **kwargs)
        end = time.time()
        print("TIme executinon is", end-start)
        return a
        
    return inner_fxn


@execution_time
def text_fxn():
    for i in range(10000000000):
        pass
        print("Task completed!!!")
    

text_fxn()