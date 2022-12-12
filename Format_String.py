# format string
# contoh generic

# string
nama = "martin"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka desimal
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# angka desimal -> .2f menunjukan 2 angka dibelakang koma
angka = 2005.54321
format_str = f"desimal = {angka:.2f}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan // jutaan
angka = 2000000
format_str = f"jutaan = {angka:,}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+d}"

print(format_minus)
print(format_plus)

# format persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)


# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)
