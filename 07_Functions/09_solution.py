def even_generater(limit):
    for i in range(2,limit + 1,2):
        yield i # yield statement, saves current state, including local variables' values of the function in to memory

for num in even_generater(10):
    print(num)