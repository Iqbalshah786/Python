alist = [1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20]
key = 5

# Function to find the first occurrence of key

def find_first(alist,key):
    start = 0
    end = len(alist) - 1
    result = -1
    while start <= end :
        mid = ( start + end ) // 2
        if alist[mid] == key :
            result = mid
            end = mid - 1
        elif alist[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return result

def find_last(alist, key):
    start = 0
    end = len(alist) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if alist[mid] == key:
            result = mid
            start = mid + 1  
        elif alist[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return result

first_occurrence = find_first(alist, key)
last_occurrence = find_last(alist, key)


print("First occurrence:", first_occurrence)
print("Last occurrence:", last_occurrence)

