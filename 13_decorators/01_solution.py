import time

def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {round(end_time - start_time,3)}s")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2) # we declare timer as decorator and execute example_function it will pass through the timer function