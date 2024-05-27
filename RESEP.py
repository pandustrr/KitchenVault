import psycopg2
import time
import oscc;,c';a,c';,sC';S,AC',SA

# Fungsi untuk melakukan koneksi ke database
def connect_db():
    conn = psycopg2.connect(database='KitchenVault', user='postgres', password='123123', host='localhost', port='5432')
    return conn

def menu():
    print(
        """
===============================
|   \033[32mWelcome To Kitchen Vault\033[0m  |
===============================
|                             |
|  1. Register Account        |
|  2. Login                   |
|                             |
|  0. Exit                    |
|_____________________________|
    """
    )


# Fungsi untuk login
def login(username, password):
    conn = connect_db()
    if conn is None:
        return False
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM account WHERE username = %s AND password = %s", (username, password))
    row = cur.fetchone()
    if row:
        print("-" * 40)
        print(">>> \033[32m Login Success! \033[0m <<<".center(48))
        print("-" * 40)
        time.sleep(0.7)
        return True
    else:
        print("-" * 40)
        print(">>> \033[31m Login Gagal! \033[0m <<<".center(48))
        print(" \033[31m Username atau Password salah !! \033[0m".center(48))
        print("-" * 40)
        return False

def register(nama, username, password, email):
    conn = connect_db()
    if conn is None:
        print("Gagal terhubung ke database.")
        return False
    
    cur = conn.cursor()
    success = True
    
    # Tambahkan nilai default atau nilai yang sesuai untuk kolom "jenis_akun"
    jenis_akun = "User"  # Misalnya, jenis akun diatur sebagai "Regular" secara default
    
    cur.execute("INSERT INTO account (nama, username, password, email, jenis_akun) VALUES (%s, %s, %s, %s, %s)", (nama, username, password, email, jenis_akun))
    conn.commit()
    print("-" * 40)
    print(">>> \033[32m Registrasi Berhasil! \033[0m <<<".center(48))
    print("-" * 40)
    time.sleep(0.7)

    # Tutup koneksi
    if conn is not None:
        conn.close()

    return success


# Main program
while True:
    menu()
    x = input("Pilih Nomor = ")
    if x == '1':
        os.system('cls')
        print("=" * 40)
        print(">>> \033[033mRegister Account\033[0m <<<".center(48))
        print("=" * 40)
        nama = input("Masukkan Nama = ")
        username = input("Masukkan Username = ")
        password = input("Masukkan Password = ")
        email = input("Masukkan Email = ")
        register(nama, username, password, email)
        os.system('cls')
        time.sleep(1)
    elif x == '2':
        os.system('cls')
        print("-" * 40)
        print(">>>  \033[33mUser Account\033[0m <<<".center(48))
        print("-" * 40)
        username = input("Masukkan Username = ")
        password = input("Masukkan Password = ")
        login(username, password)
    elif x == '0':
        print("Keluar dari program...")
        time.sleep(2)
        break
    else:
        print("Pilihan tidak valid. Silakan pilih nomor yang sesuai.")
