print ("Program Menghitung Luas dan Volume Balok")

p = (input("Panjang    :"))
while (all(x.isnumeric() for x in p) or "." in p) !=True:
    print ("Input Harus Angka")
    p = input ("Panjang :")

l = (input("Lebar      :"))
while (all(x.isnumeric() for x in l) or "." in l) !=True:
    print ("Input Harus Angka")
    l = input ("Lebar :")

t = (input("Tinggi     :"))
while (all(x.isnumeric() for x in t) or "." in t) !=True:
    print ("Input Harus Angka")
    t = input ("Tinggi :")

#casting
p = float(p)
l = float(l)
t = float(t)




luas = (2*p*l) * (2*p*t) + (2*l*t)
volume = p*l*t

print ("Luas Balok          :", luas)
print ("Volume Balok         :", volume)