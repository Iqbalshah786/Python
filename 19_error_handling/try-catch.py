foobar = 1 # comment this line to see the error 
try: 
    foobar
except:
    print("PROBLEM!")
print("after the try")



def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
d = {"name":"iqbal"}

print(get(d,"name")) # comment this line to see the error
print(get(d,"city"))


try:
    num = int(input("please enter a number: "))
except :
    print("That's not a number!")
else:
    print("I'm in the else")
finally:
    print("finally, runs no matter what")

# enter a string to see the except block. When except is executed, the else block is not executed.