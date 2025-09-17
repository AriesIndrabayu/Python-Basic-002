"""
Tuple:
- Urutan(sequence) seperti list, tetap(immutable): setelah dibuat elemennya tidak bisa diubah, ditambah atau dihapus
- Menyimpan heteogeneous data (tipe campuran) dan berurutan (indexable & sliceable)
- Sering dipakai untuk record yang tetap
"""

t = (1, 2, 3)  # literal tuple
t = 1, 2, 3  # packing
singel = (42,)  # tuple elemen: Harus pakai koma
non_tuple = 42  # ini hanya angka 42 (bukan tuple)
nested = (1, (2, 3), [4, 5])
from_iter = tuple("abcd")  # ('a', 'b', 'c', 'd')
