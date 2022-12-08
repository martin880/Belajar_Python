# Operasi dan manipulasi string

# 1. Menyambung string (concatenate)
nama_pertama = "Martin"
nama_tengah = "Halomoan"
nama_akhir = "Lumbangaol"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari nama " + nama_lengkap + " = " + str(panjang))

# 3. Mengecek apakah ada komponen char atau string di string
d = "m"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

e = "o"
status = e not in nama_lengkap  # negasi / kebalikan
print(e + " ada di " + nama_lengkap + " = " + str(status))

# 4. Mengulang string
print("wk"*10)
print(15*"wk")

# 5. Indexing
print(nama_lengkap)
print("Index ke-0 : " + nama_lengkap[0])
print("Index ke-7 : " + nama_lengkap[7])
print("Index ke-(-1) : " + nama_lengkap[-1])
print("Index ke-(-2) : " + nama_lengkap[-2])
print("Index ke-[3:7] : " + nama_lengkap[3:7])
print("index ke-[0,2,4,6,8,10]", nama_lengkap[0:11:2])

# 6. Item paling kecil
print("paling kecil : " + min(nama_lengkap))
# 7. Item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))

data = 111
print("Char untuk ASCII 111 adalah " + chr(data))

# 8. Oeprator dalam bentuk method
data = "Iska Heriyati Sigalingging"
jumlah = data.count("i")
print("Jumlah huruf i pada " + data + " = " + str(jumlah))
