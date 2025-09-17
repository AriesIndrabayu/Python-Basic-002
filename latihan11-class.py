class Orang:
    # class sederhana tanpa atribut awal
    pass


# Membuat object (instance)
o1 = Orang()
o2 = Orang()

print(type(o1))
print(o1 is o2)  # objek berbeda

print(o1)
print(o2)

o3 = o1
print(o1 is o3)

# == vs is
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
