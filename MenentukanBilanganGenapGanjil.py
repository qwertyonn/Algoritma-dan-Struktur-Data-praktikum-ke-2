#Program Menentukan Bilangan Genap atau Bilangan Ganjil
#I.S. : pengguna memasukkan sebuah bilangan
#F.S.: menampilkan keterangan "Bilangan Genap" atau "Bilangan Ganjil
import subprocess
subprocess.run('cls',shell = True)

#badan program
#memasukkan bilangan
bilangan = int(input('masukan sebuah bilangan = '))

'''
#mengecek bilangan menggunakan analisis satu kasus
keterangan = 'Bilangan Ganjil'
if (bilangan % 2 == 0):
    keterangan = 'Bilangan Genap'
'''
#mengecek bilangan menggunakan analisis dua kasus
if (bilangan % 2 == 0):
    keterangan = 'Bilangan Genap'
else:
    keterangan = 'Bilangan Ganjil'

#menampilkan isi variabel keterangan
print(f'{bilangan} adalah {keterangan}')