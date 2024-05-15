tea_types = {
    "Masala":"Spicy",
    "Ginger":"Zesty",
    "Green":"Mild",
}
print(tea_types["Masala"]) # return errors if not exits

print(tea_types.get("Green")) ## do not return errors if not exits

tea_types["Green"] = "Fresh"

for tea in tea_types:
    print(tea,tea_types[tea])

for key , value in tea_types.items():
    print(f"{key} : {value}")

if "Green" in tea_types:
    print(True)

# length
print(len(tea_types))

# add new item
tea_types["Earl Grey"] = "Citrus"

# pop() we need to pass key 
popped =  tea_types.pop("Ginger")
print(popped)

# popitem() don't need key
print(tea_types.popitem())

del tea_types["Green"] # deletes reference from memory

tea_types_copy = tea_types.copy() # creates new reference in memory

# nested dictionary
tea_shop = {
    "tea":{
        "Masala":"Spicy",
        "Ginger":"Zesty"
    },
    "coffee":{
        "cappuccino":"milk",
        "latte":"espresso",
        "affogato":"vanilla ice cream"
    }
}
# print(tea_shop["tea"]["Ginger"])

# list Comprehension
squared_num = {x: x**3 for x in range(6) }
# print(squared_num)
squared_num.clear() # {}


keys = ["Masala","Ginger","Lemon"]
values = ["Spicy","Zesty"] 
coffee_dict = dict(zip(keys,values))
print(coffee_dict)