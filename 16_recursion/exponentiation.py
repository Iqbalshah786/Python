def power(base,expo):
    if expo <=1:
        return base
    else:
        return base * power(base,expo -1)

print(power(2,4))