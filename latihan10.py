# Truthy --> nilai yang dianggap benar saat dievaluasi di if atau kondisi lain.
# Falsy --> nilai yang dianggap salah
"""
False       # boolean flase
None        # objek kosong
0, 0.0      # nagka nol
""          # string kosong
[]          # list kosong
{}          # dict kosong
set()       # set kosong
()          # tuple kosong
range(0)    # range kosong
"""
if "Python":
    print("Ini truthy!")  # string non-kosong --> True

print(bool([1, 2, 3]))


# Struktur if, elif dan else
nama = "Oded"
kota = "Jakarta"
if nama == "Oded":
    if kota == "Bandung":
        print("Halo Oded, dibandung gimana kondisinya!")
    else:
        print("Halo Oded!")
elif nama == "Tati":
    print("Halo Tati!")
else:
    print("Halo, siapa pun kamu!")


umur = 16
if umur >= 18:
    status = "Dewasa"
else:
    status = "Anak-anak"

# Looping: for
for nama in ["Oded", "Tati", "Tuti", "Dudi", "Bambang"]:
    print(f"Halo {nama}")
    if nama == "Tati":
        continue
    if nama == "Tuti":
        break
    print(f"kondisi yang terpenuhi nama: {nama}")

# looping: while
i = 1
while i <= 3:
    print(i)
    i += 1  # i = i + 1
# Nested loop

for i in range(1, 4):  # looping 1
    for j in ["A", "B"]:  # looping 2
        print(i, j)
angka = [x**2 for x in range(5)]
print(angka)

"""
0, 1, 2, 3, 4
"""
