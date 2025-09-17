import random

# 1. Bilangan Acak
print(random.random())
print(random.uniform(1, 10))
print(random.randrange(0, 10, 2))

# 2. Random List
nama = ["Oded", "Udung", "Ocim", "Ocah"]
print(random.sample(nama, 3))
