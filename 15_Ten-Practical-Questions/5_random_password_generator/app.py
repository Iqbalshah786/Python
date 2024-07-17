import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"

password = random.sample(characters,6)
password = "".join(password)

print(password)


