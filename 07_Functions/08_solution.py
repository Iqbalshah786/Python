def print_kwargs(**kwargs):
   # print(kwargs) # {'name': 'Iqbal', 'power': 'lazer'}
                   # {'name': 'Ali'} 
                   #  {'name': 'Iqbal', 'power': 'lazer', 'enemy': 'Spiderman'}
    for key,value in kwargs.items():
         print(f"{key} : {value}")



print_kwargs(name="Iqbal",power="lazer")
print_kwargs(name="Ali")
print_kwargs(name="Iqbal",power="lazer",enemy = "Spiderman")


