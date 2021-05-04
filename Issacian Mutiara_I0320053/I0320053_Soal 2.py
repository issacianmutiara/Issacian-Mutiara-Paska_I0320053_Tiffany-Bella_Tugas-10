kata = 'Program Biodata Diri'
print(kata.center(50))

title = 'Biodata'
print(title.center(50,"="))

#User Menginput
Name    = input('Nama   : ')
Class   = input('Kelas  : ')
Age     = input('Umur   : ')
Hobby   = input('Hobi   : ')
Address = input('Alamat : ')
print("Halo, nama saya %s, saya berasal dari kelas %s, umur saya %s tahun, "
      "hobi saya adalah %s, saya tinggal di %s"%(Name,Class,Age,Hobby,Address))

#format teks
teks = 'Nama: {}\nKelas: {}\nUmur: {}\nHobi: {}\nAlamat: {}'.format(Name, Class, Age, Hobby, Address)

#buka file untuk ditulis
file_bioku = open('BiodataDiri.txt', 'w')

#tulis teks ke file
file_bioku.write(teks)

#tutup file
file_bioku.close()