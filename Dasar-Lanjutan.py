"""
RANGKUMAN MATERI PYTHON LENGKAP
Dasar hingga Lanjutan
"""

# ==========================================
# 1. HELLO WORLD
# ==========================================
print("--- 1. HELLO WORLD ---")
print("Hello World!")
print("Selamat belajar Python.")


# ==========================================
# 2. TIPE DATA
# ==========================================
print("\n--- 2. TIPE DATA ---")
data_integer = 10         # Bilangan bulat
data_float = 3.14         # Desimal
data_boolean = True       # Kebenaran (True/False)
data_string = "Ayam"      # Teks

print(f"Integer: {data_integer}")
print(f"Float: {data_float}")
print(f"Boolean: {data_boolean}")


# ==========================================
# 3. FUNGSI BUILT-IN (DASAR)
# ==========================================
print("\n--- 3. FUNGSI BUILT-IN ---")
print(type(data_integer)) # Mengecek tipe data
print(abs(-50))           # Nilai absolut (mutlak)
print(pow(2, 3))          # Pangkat (2 pangkat 3)
print(len("Halo"))        # Menghitung panjang karakter


# ==========================================
# 4. VARIABLE
# ==========================================
print("\n--- 4. VARIABLE ---")
nama_depan = "Budi"       # Snake case (disarankan di Python)
usia = 25
# Mengubah nilai variabel
usia = 26 
print(f"Nama: {nama_depan}, Usia: {usia}")


# ==========================================
# 5. KOMENTAR
# ==========================================
# Ini adalah komentar satu baris (tidak akan dieksekusi)
"""
Ini adalah komentar
lebih dari satu baris (multiline)
biasanya untuk dokumentasi
"""


# ==========================================
# 6. OPERATOR
# ==========================================
print("\n--- 5. OPERATOR ---")
a = 10
b = 3
print(f"{a} + {b} = {a + b}")   # Tambah
print(f"{a} / {b} = {a / b}")   # Bagi (hasil float)
print(f"{a} // {b} = {a // b}") # Floor Division (pembulatan ke bawah)
print(f"{a} % {b} = {a % b}")   # Modulus (sisa bagi)
print(f"{a} ** {b} = {a ** b}") # Pangkat

# Operator Logika
print(True and False) # Hasil: False
print(True or False)  # Hasil: True


# ==========================================
# 7. STRING
# ==========================================
print("\n--- 6. STRING ---")
teks = "Belajar Python"
print(teks.upper())       # Huruf besar semua
print(teks.lower())       # Huruf kecil semua
print(teks[0:7])          # Slicing (mengambil karakter indeks 0 sampai 6)
print(teks.replace("Python", "Coding")) # Mengganti teks


# ==========================================
# 8. COLLECTION (LIST, TUPLE, SET, DICT)
# ==========================================
print("\n--- 7. COLLECTION ---")

# --- LIST (Dapat diubah, Terurut) ---
print("[LIST]")
buah = ["Apel", "Jeruk", "Mangga"]
buah.append("Pisang")     # Menambah data
buah[0] = "Anggur"        # Mengubah data
print(buah)

# --- TUPLE (Tidak dapat diubah, Terurut) ---
print("[TUPLE]")
koordinat = (10, 20)
# koordinat[0] = 50 -> Akan Error jika dijalankan
print(koordinat)

# --- SET (Unik, Tidak Terurut, Tidak ada duplikat) ---
print("[SET]")
angka_unik = {1, 2, 3, 3, 3, 4} 
print(angka_unik) # Output: {1, 2, 3, 4} (angka 3 hanya muncul sekali)

# --- DICTIONARY (Key-Value) ---
print("[DICTIONARY]")
siswa = {
    "nama": "Andi",
    "kelas": "10A",
    "nilai": 90
}
print(siswa["nama"])


# ==========================================
# 9. COLLECTION MULTIDIMENSION
# ==========================================
print("\n--- 8. MULTIDIMENSION ---")
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Baris 2 Kolom 3: {matriks[1][2]}") # Mengambil angka 6


# ==========================================
# 10. FUNGSI BUILT-IN COLLECTION
# ==========================================
print("\n--- 9. FUNGSI COLLECTION ---")
angka = [10, 5, 20, 1]
print(f"Max: {max(angka)}")
print(f"Min: {min(angka)}")
print(f"Sum: {sum(angka)}")
print(f"Sorted: {sorted(angka)}")


# ==========================================
# 11. UNPACKING
# ==========================================
print("\n--- 10. UNPACKING ---")
data = ("Budi", 25, "Jakarta")
nama, umur, kota = data
print(f"{nama} tinggal di {kota}")


# ==========================================
# 12. PENGKONDISIAN (IF-ELIF-ELSE)
# ==========================================
print("\n--- 11. PENGKONDISIAN ---")
nilai = 75
if nilai >= 80:
    print("Nilai A")
elif nilai >= 70:
    print("Nilai B")
else:
    print("Nilai C")


# ==========================================
# 13. PERULANGAN (LOOP)
# ==========================================
print("\n--- 12. PERULANGAN ---")

print("For Loop:")
for i in range(1, 4): # Loop 1 sampai 3
    print(f"Angka ke-{i}")

print("While Loop:")
count = 3
while count > 0:
    print(f"Hitung mundur: {count}")
    count -= 1


# ==========================================
# 14. FUNCTION
# ==========================================
print("\n--- 13. FUNCTION ---")
def sapa_user(nama, waktu="Pagi"):
    """Fungsi untuk menyapa user"""
    return f"Selamat {waktu}, {nama}!"

hasil_sapa = sapa_user("Citra", "Sore")
print(hasil_sapa)


# ==========================================
# 15. LAMBDA (ANONYMOUS FUNCTION)
# ==========================================
print("\n--- 14. LAMBDA ---")
# Fungsi biasa:
# def kuadrat(x): return x * x

# Versi Lambda:
kuadrat = lambda x: x ** 2
tambah = lambda x, y: x + y

print(f"Kuadrat 5: {kuadrat(5)}")
print(f"10 + 20: {tambah(10, 20)}")

print("\n--- SELESAI ---")
