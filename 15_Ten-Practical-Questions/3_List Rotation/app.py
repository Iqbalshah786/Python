lst = [1, 10, 20, 0, 59, 86, 32, 11, 9, 40]


def reverse_list(lst,start,end):
    while start < end:
        lst[start],lst[end] = lst[end],lst[start]
        start += 1
        end -= 1
    
def rotate_list(lst,N):
    length  = len(lst)
    N = N % length
    if N < 0:
        N+= length

    # Step 1: Reverse the entire list
    reverse_list(lst,0,length-1)

    # Step 2: Reverse the first N elements
    reverse_list(lst,0,N-1)

    # Step 3: Reverse the remaining elements
    reverse_list(lst,N,length-1)




rotate_list(lst, 2)
print(lst) # [9, 40, 1, 10, 20, 0, 59, 86, 32, 11]