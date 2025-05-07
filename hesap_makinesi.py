def topla(x,y):
    return x+y

def cikar(x,y):
    return x-y

def carp(x,y):
    return x*y

def bol(x,y):
    if y==0:
     print("sayi sifira bölünemez!")
    return x/y

print("Basit hesap makinesi")
print("1.Toplama")
print("2.Çikarma")
print("3.Çarpma")
print("4.Bölme")

seçim=input("Seçiminizi yapin (1,2,3,4):")

sayi1=float(input("1.Sayiyi giriniz: "))
sayi2=float(input("2.Sayiyi giriniz: "))

if seçim=='1':
   print(sayi1+sayi2)
elif seçim=='2':
   print(sayi1-sayi2)
elif seçim=='3':
   print(sayi1*sayi2)
else :
   print(sayi1/sayi2)
   

   
   



