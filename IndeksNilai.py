#program menentukan indeks nilai (nilai mutu)
#I.S.: pengguna memasukkan sebuah nilai
#F.S.: menampilkan indeks nilai
import subprocess
subprocess.run('cls',shell = True)

#badan program
#memasukkan sebuah nilai

nilai = float(input('Nilai = '))

'''
nilai = int(input('nilai = '))

#menentukan indeks nilai menggunakan analisis banyak kasus
if (nilai >= 80) and (nilai <= 100):
    indeks = 'A'
elif (nilai >= 70) and (nilai <= 79):
    indeks = 'B'
elif (nilai >= 60) and (nilai <= 69):
    indeks = 'C'
elif (nilai >= 50) and (nilai <= 59):
    indeks = 'D'
else:
    indeks = 'E'
'''

#menyederhanakan kondisis majemuk menjadi kondisi tunggal
if (80<= nilai <= 100):
    indeks = 'A'
elif (70<= nilai < 80):
    indeks = 'B'
elif (60<= nilai < 70):
    indeks = 'C'
elif (50<= nilai < 60):
    indeks = 'D'
elif (0 <= nilai < 50):
    indeks = 'E'
else: #validasi nilai jika kurang dari 0 atau lebih dari 100
    indeks = 'Salah Nilai'

#menampilkan indeks nilai
print(f'Indeks Nilai = {indeks}')