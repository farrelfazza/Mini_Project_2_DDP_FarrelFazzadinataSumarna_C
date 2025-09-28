from prettytable import PrettyTable
from getpass import getpass


users = {
    "wasit": "Cek VAR",
    "wasit2": "hali kali"
}

pemain = {}


def login():
    print("===== LOGIN SISTEM TURNAMEN =====")
    for percobaan in range(3):
        username = input("Masukkan Username: ")
        password = getpass("Masukkan Password: ")
        if username in users and users[username] == password:
            print(f"Login berhasil. Selamat datang, {username}!\n")
            return True
        else:
            print("Username atau Password salah. Coba lagi.\n")
    print("Terlalu banyak percobaan gagal. Program keluar.")
    return False


def tambahkan_pemain():
    try:
        player_id = input("Masukkan ID pemain: ")
        if player_id in pemain:
            print("ID sudah digunakan, coba lagi.")
            return False
        name = input("Masukkan Nama pemain: ")
        score = int(input("Masukkan Score Awal: "))
        pemain[player_id] = {"nama": name, "score": score}
        print(f"pemain '{name}' berhasil ditambahkan.")
    except ValueError:
        print("Score harus berupa angka!")


def update_pemain():
    try:
        player_id = input("Masukkan ID pemain yang ingin diupdate: ")
        if player_id not in pemain:
            print("pemain tidak ditemukan.")
            return False
        print("1. Update Nama")
        print("2. Update Score")
        choice = input("Pilih data yang ingin diupdate (1/2): ")
        if choice == "1":
            new_name = input("Masukkan Nama Baru: ")
            pemain[player_id]["nama"] = new_name
            print("Nama berhasil diperbarui.")
        elif choice == "2":
            new_score = int(input("Masukkan Score Baru: "))
            pemain[player_id]["score"] = new_score
            print("Score berhasil diperbarui.")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Score harus berupa angka!")


def hapus_pemain():
    player_id = input("Masukkan ID pemain yang ingin dihapus: ")
    if player_id in pemain:
        deleted = pemain.pop(player_id)
        print(f"pemain '{deleted['nama']}' berhasil dihapus.")
    else:
        print("pemain tidak ditemukan.")


def menu():
    while True:
        print("\n===== Sistem Tournament Game =====")
        print("1. Tambah pemain")
        print("2. Update pemain")
        print("3. Hapus pemain")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambahkan_pemain()
        elif pilihan == "2":
            update_pemain()
        elif pilihan == "3":
            hapus_pemain()
        elif pilihan == "4":
            print("Keluar dari sistem. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
        
        table = PrettyTable()
        table.field_names = ["ID pemain", "Nama pemain", "Score"]
        for pid, data in pemain.items():
            table.add_row([pid, data["nama"], data["score"]])
        print(table)


# Main Program
if login():
    menu()