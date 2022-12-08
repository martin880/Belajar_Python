data = "String adalah kumpulan dari karakter"
print(data)
print(type(data))

# 1. Cara membuat string

# dengan menggunakan single quote '...'
# dengan menggunakan double quote "..."

data2 = 'g\'day, isn\'t it?'
print(data2)  # menggunakan tanda \ agar string single quote tidak error

data3 = "Menggunakan double quote"
print(data3)

print('"Halo, apa kabar"')

# new line khusus windows..seperti EOL nya PHP
print("Baris pertama.\r\nbaris kedua.")  # CLRF -> line feed carriage return

# String Literal raw string
print('C:\new folder')  # salah
print(r'C:\new folder')  # benar

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")
