# operator dalam bentuk methods

# merubah case dari string

# merubah semua ke uppercase

salam = "bro!!"
print("normal =" + salam)
salam = salam.upper()
print("upper =" + salam)

# merubah semua ke lower case
alay = "PyThoN KeCe AbiezzZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

# pengecekan dengan is method

# contoh pengecekan lower case
salam = "shalom"
apakah_lower = salam.islower()
print(salam + " is lower =  " + str(apakah_lower))

# isalpha() <-- untuk mengecek semua nya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "Top Gun Maverick"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

# ngecek komponen startswith() endswith()
print("Martin Marbun")
cek_start = "Martin Marbun".startswith("Martin")
print("Awal kalimat apakah benar ? " + str(cek_start))

print("Martin Marbuns")
cek_end = "Martin Marbun".endswith("Marbuns")
print("Akhir kalimat apakah benar ? " + str(cek_end))

# penggabungan komponen join() split()
pisah = ['aku', 'suka', 'fender', 'stratocaster']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(pisah)
print(gabungan)

gabungan = "aku_suka_fender_stratocaster"
print(gabungan)
print(gabungan.split('_'))

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

# strip() -> menghilangkan karakter dalam method rjust(),ljust(),center()
