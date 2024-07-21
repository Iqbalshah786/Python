import random

coins = {"head":0,"tail":0}

for _ in range(1000):
    coin = random.choice(["head","tail"])
    coins[coin] += 1


print(f"Head: {coins['head']}")
print(f"Tail: {coins['tail']}")