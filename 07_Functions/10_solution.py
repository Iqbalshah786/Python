def recursive(num):
    if(num == 0):
        return 1
    return num * recursive(num - 1)

# 1 * (0) => 1 * 1 = 1 
# 2 * (1) => 2 * 1 = 2 
# 3 * (2) => 3 * 2 = 6
# 4 * (3) => 4 * 3 = 24
# 5 * (4) => 5 * 24 = 120 

print(recursive(5))