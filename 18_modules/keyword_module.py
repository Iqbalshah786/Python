import keyword 

def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item):
            return True
    return False

print(contains_keyword("iif","elseif"))
print(contains_keyword("if","elseif"))
print(contains_keyword("iqbal"))
