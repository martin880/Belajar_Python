# operator bitwise, operasi biner, binary
# operasi pada masing-masing bit

# Bitwise ini dipakai untuk coding interface / import data dari Analog to Digital,
# (Multimeter Digital, Parameter Engine seperti Suhu, tekanan dan lain2 dari sensor2 yang di pasang di mesin, PLC, robotika dan Hacking bikin BOT untuk Farming.

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('\n==========OR===========')
print('nilai :', a, ', binary :', format(a, '08b'))
print('nilai :', b, ', binary :', format(b, '08b'))
print('------------------------------- (|)')
print('nilai :', c, ', binary :', format(c, '08b'))

# # bitwise AND (&)
c = a & b
print('\n==========AND===========')
print('nilai :', a, ', binary :', format(a, '08b'))
print('nilai :', b, ', binary :', format(b, '08b'))
print('----------------------------- (AND)')
print('nilai :', c, ', binary :', format(c, '08b'))

# # bitwise XOR (^)
c = a ^ b
print('\n==========XOR===========')
print('nilai :', a, ', binary :', format(a, '08b'))
print('nilai :', b, ', binary :', format(b, '08b'))
print('----------------------------- (^)')
print('nilai :', c, ', binary :', format(c, '08b'))

# bitwise NOT (~)
c = ~ a
print('nilai :', a, ', binary :', format(a, '08b'))
print('----------------------------- (~)')
print('nilai :', c, ', binary :', format(c, '08b'))
print('----------------------------- (^)')
d = 0b00001001
e = 0b11111111
print('nilai:', e ^ d, ', binary :', format(e ^ d, '08b'))

# shifting

# shift right (>>)
c = a >> 2
print('\n===========>>============')
print('nilai :', a, ',binary:', format(a, '08b'))
print('------------------------------- (>>)')
print('nilai :', c, ',binary:', format(c, '08b'))

# shift right (>>)
c = a << 2
print('\n===========<<============')
print('nilai :', a, ',binary:', format(a, '08b'))
print('------------------------------- (<<)')
print('nilai :', c, ',binary:', format(c, '08b'))

# Next
