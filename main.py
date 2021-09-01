print('\n  Program Menghitung Nilai Akhir Mahasiswa  ')
print('=======================================================')
Nama = input("Nama :")
while (all(x.isalpha() for x in Nama) or all(x.isspace() for x in Nama) or  all(x.isalpha() or x.isspace() for x in Nama)) !=True:
    print ("Input Harus Huruf")
    Nama = input ("Nama :") 
   


Nim = input ("NIM   :")
while (all(x.isnumeric() for x in Nim)) !=True:
    print ("Input Harus Angka")
    Nim = input ("NIM :") 

Kelas = input ("Kelas   :")
while (all(x.isalnum() for x in Kelas) or all(x.isspace() for x in Kelas) or  all(x.isalnum() or x.isspace() for x in Kelas)) !=True:
    print("Hanya huruf dan Angka")
    Kelas = input("Kelas  :")


absensi = (input ("\nMasukkan Nilai Absensi   :"))#Nilai Absensi 20%
while (all(x.isnumeric() for x in absensi) or "." in absensi) !=True:
    print ("Input Harus Angka")
    absensi = input ("Masukkan Nilai Absensi :") 




tugas = (input("\nMasukkan Nilai Tugas    :"))#Nilai Tugas 30%
while (all(x.isnumeric() for x in tugas) or "." in tugas) !=True:
    print ("Input Harus Angka")
    absensi = input ("Masukkan Nilai Tugas :") 



uts = (input("\nMasukkan Nilai Uts    :"))#Nilai Uts 20%
while (all(x.isnumeric() for x in uts) or "." in uts) !=True:
    print ("Input Harus Angka")
    uts = input ("Masukkan Nilai UTS :") 

uas = (input("\nMasukkan Nilai Uas    :"))#Nilai uas 30%
while (all(x.isnumeric() for x in uas) or "." in uas) !=True:
    print ("Input Harus Angka")
    absensi = input ("Masukkan Nilai UAS :") 

#casting 
absensi = float(absensi)
tugas = float(tugas)
uts = float(uts)
uas = float(uas)



print ("\n NILAI GRADE    ")

print ("Nilai Absensi = ",absensi)
print ("Nilai Tugas   = ",tugas)
print ("Nilai UTS     = ",uts)
print ("Nilai UAS     = ",uas)

na = (0.20 * absensi) + (0.30 * tugas) + (0.20 * uts) + (0.30 *uas)
if (na >= 85) and (na <= 100) :
    grade = 'A'
elif (na >= 80) and (na <= 85) :
    grade = 'A-'
elif (na >= 75) and (na <= 80) :
    grade = 'B+'
elif (na >= 70) and (na <= 75) :
    grade = 'B'
elif (na >= 65) and (na <= 70) :
    grade = 'B'
elif (na >= 60) and (na <= 65) :
    grade = 'B-'
elif (na >= 55) and (na <= 60) :
    grade = 'C'
elif (na >= 40) and (na <= 55) :
    grade = 'D'
else :
    grade = 'E'




print ("\n--HASIL PERHITUNGAN--")

print("Nama         : ", Nama)
print("NIM          : ", Nim)
print("Kelas        : ", Kelas)
print("\nNilai Akhir Mahasiswa = %0.3f" % na)
print("\nNilai Grade Mahasiswa = %s" % grade)