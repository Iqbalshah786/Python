def apply_discount(product,discount):
    assert isinstance(discount, (int, float)), "Discount must be a number"
    discounted_price = int(product["price"] * (1.0 - discount))
    assert 0 <= discounted_price <= product['price'] , "The discount can not be more than 100 or negative number"
    return discounted_price


shoes = {'name':"shoe","price":1400}



# Valid cases
print(apply_discount(shoes, 0.25))


# Invalid cases
try:
    print(apply_discount(shoes,200))
except AssertionError as e:
    print(e)

try:
    print(apply_discount(shoes,-10))
except AssertionError as e:
    print(e)

try:
    print(apply_discount(shoes,"a"))
except AssertionError as e:
    print(e)