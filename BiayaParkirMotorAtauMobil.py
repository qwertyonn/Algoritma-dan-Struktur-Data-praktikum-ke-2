#program biaya parkir
#I.S.: pengguna memasukkan jenis kendaraan (kendaraan), nomor polisi (nopol), waktu masuk (jamMasuk dan menitMasuk), waktu keluar (jamKeluar dan menitKeluar)
#F.S.: menampilkan lama parkir dan biaya parkir
import subprocess
subprocess.run('cls',shell = True)

#badan program
#memasukkan jenis kendaraan (kendaraan), nomor polisi (nopol), waktu masuk (jamMasuk dan menitMasuk), waktu keluar (jamKeluar dan menitKeluar)
kendaraan       = str(input('Masukan jenis kendaraan Anda         : ')).upper()
nopol           = str(input('masukan nomor polisi kendaraan Anda  : '))
jamMasuk        = int(input('masukan jam masuk                    : '))
menitMasuk      = int(input('masukan menit masuk                  : '))
jamKeluar       = int(input('masukan jam keluar                   : '))
menitKeluar     = int(input('masukan menit keluar                 : '))

#menentukan lama parkir
if (menitKeluar < menitMasuk):
    menitKeluar = menitKeluar + 60
    jamKeluar = jamKeluar - 1

menit = menitKeluar - menitMasuk

if (jamKeluar < jamMasuk):
    jamKeluar = jamKeluar + 12

jam = jamKeluar - jamMasuk
#menampilkan lama parkir (jam dan menit)
import subprocess
subprocess.run('cls',shell = True)
print('               <<BIAYA PARKIR>>\n')
print(f'Jenis Kendaraan             : {kendaraan}')
print(f'Nomor Polisi                : {nopol}')
print(f'Jam Masuk (Jam:Menit)       : {jamMasuk}:{menitMasuk}')
print(f'Jam Keluar (Jam:Menit)      : {jamKeluar}:{menitKeluar}')
print(f'Lama parkir                 : {jam} Jam {menit} Menit')

#mengubah jam jika menit parkir lebih dari 0
if(menit > 0):
    jam = jam + 1

print(f'                            : {jam} Jam')

#menghitung biaya parkir
if(kendaraan == 'MOTOR'):
    biaya = 1500 + (jam-1)*500
else:
    biaya = 3000 + (jam-1)*1000

print(f'Biaya Parkir                : Rp. {biaya:,}')