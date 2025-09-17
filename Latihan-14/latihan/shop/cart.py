class Cart:
    def __init__(self):
        self.__items = []

    def tambah(self, item):
        self.__items.append(item)

    def daftar(self):
        return list(self.__items)
