#seleksi pemilu
#I.S.: pengguna memasukkan umur dan status pernikahan
#F.S.: menampilkan boleh memilih atau tidak
import subprocess
subprocess.run('cls',shell = True)

#badan program
#masukan umur
umur = int(input(f'Masukan Umur Anda :' ))
if(umur < 17):
    menikah = str(input('Menikah [Y/T] : ')).upper()
    if (menikah == 'Y'):
        print ('Anda boleh ikut pemilu')
    else:
        print('Anda belum boleh ikut pemilu')
else:
    print('Anda boleh ikut pemilu')