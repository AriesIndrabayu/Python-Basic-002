import random


def menu():
    while True:
        print("\n=== GAME MENU ===")
        print("1. Tebak Angka")
        print("2. Batu-Gunting-Kertas")
        print("3. Zombie Escape")
        print("4. Guess the Word")
        print("5. Keluar")

        pilihan = input("Pilih (1-5): ")
        if pilihan == "1":
            game_tebak_angka()
        elif pilihan == "2":
            game_rps()
        elif pilihan == "3":
            game_zombie_escape()
        elif pilihan == "4":
            game_guess_word()
        elif pilihan == "5":
            print("Keluar, terima kasih!")
            break
        else:
            print("Pilihan tidak valid!")


def game_tebak_angka():
    print("\n== Tebak Angka ==")
    target = random.randint(1, 50)
    attempts = 0
    while True:
        Tebakan = input("Tebak angka 1-50: ")
        if not Tebakan.isdigit():
            print("Masukkan angka tidak valid")
            continue
        guess = int(Tebakan)
        attempts += 1
        if guess < target:
            print("Terlalu Kecil")
        elif guess > target:
            print("Terlalu Besar")
        else:
            print(f"Benar! Dalam {attempts} percobaan.")
            break


def game_rps():
    print("\n== Batu-Gunting-Kertas ==")
    choices = ["batu", "gunting", "kertas"]
    you = input("Pilih (batu/gunting/kertas): ").lower()
    if you not in choices:
        print("Pilihan tidak valid.")
        return
    comp = random.choice(choices)
    print("Komputer memilih:", comp)
    if you == comp:
        print("Seri!")
    elif (
        (you == "batu" and comp == "gunting")
        or (you == "gunting" and comp == "kertas")
        or (you == "kertas" and comp == "batu")
    ):
        print("Kamu menang")
    else:
        print("Kamu kalah!")


def game_zombie_escape():
    print("\n== Zombie Escape ==")
    safe_side = random.choice(["kiri", "kanan"])
    pilihan = input("Pilih jalan (kiri/kanan): ").lower()
    if pilihan not in ["kiri", "kanan"]:
        print("Pilihan tidak valid")
        return
    if pilihan == safe_side:
        print("Selamat! kamu lolos dari zombie.")
    else:
        print("Aduh! Zombie menyerang. Game over.")


def game_guess_word():
    print("\n== Guess the Word ==")
    words = ["python", "koding", "komputer", "belajar", "siswa"]
    word = random.choice(words)
    # koding => ["k", "o", "d", "i", "n", "g"]
    letters = list(word)
    random.shuffle(letters)
    scrambled = "".join(letters)
    print("Tebak kata dari:", scrambled)
    guess = input("Tebakan: ").lower()
    if guess == word:
        print("Benar! Kamu menang.")
    else:
        print("Salah. Kata yang benar:", word)


menu()
