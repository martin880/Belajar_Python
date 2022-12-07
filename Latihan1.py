# Latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# inputUser = float(
#     input("Masukkan angka lebih kecil dari 3 atau lebih besar dari 10 \n= "))

# isKurangDari = (inputUser < 3)

# print(inputUser, " kurang dari 3 = ", isKurangDari)

# isLebihDari = (inputUser > 10)

# print(inputUser, " lebih dari 10 = ", isLebihDari)

# # +++++3------------------10+++++
# isCorrect = isKurangDari or isLebihDari
# print("Angka yang anda masukkan: ", isCorrect)

# inputUser = float(
#     input("Masukkan angka lebih kecil dari 3 atau lebih besar dari 10 \n= "))

# isLebihDari = (inputUser > 3)

# print(inputUser, "lebih dari 3 =", isLebihDari)

# isKurangDari = (inputUser < 10)

# print(inputUser, "kurang dari 10 =", isKurangDari)

# # +++++3------------------10+++++
# isCorrect = isLebihDari or isKurangDari
# print("Angka yang anda masukkan:", isCorrect)


# inputUser = float(
#     input("Masukkan angka lebih besar dari 3 dan lebih kecil dari 10 \n= "))

# isLebihDari = (inputUser > 3)
# print("lebih besar dari 3 =", isLebihDari)

# isKurangDari = (inputUser < 10)
# print("kurang dari 10 =", isKurangDari)

# # +++++3------------------10+++++
# isCorrect = isLebihDari and isKurangDari
# print("Angka yang anda masukkan:", isCorrect)

# inputUser = float(
#     input("Masukkan angka lebih besar dari 0 dan kurang dari 5 dan lebih dari 8 dan kurang dari 11 \n= "))

# task1 = (inputUser > 0), (inputUser < 5)
# print("lebih besar dari 0 dan kurang dari 5 =", task1)

# task2 = (inputUser > 8), (inputUser < 11)
# print("kurang dari 8 dan lebih dari 11 =", task2)

# # ----0+++++5----------8+++++11-------
# isCorrect = task1 and task2
# print("Angka yang anda masukkan:", isCorrect)

inputUser = float(
    input("Masukkan angka kurang dari 0 dan lebih dari 5 dan kurang dari 8 dan lebih dari 11 \n= "))

task1 = (inputUser > 0), (inputUser < 5)
print("kurang dari 0 dan lebih dari 5 =", task1)

task2 = (inputUser > 8), (inputUser < 11)
print("lebih dari 8 dan kurang dari 11 =", task2)

# ----0+++++5----------8+++++11-------
isCorrect = task1 and task2
print("Angka yang anda masukkan:", isCorrect)
