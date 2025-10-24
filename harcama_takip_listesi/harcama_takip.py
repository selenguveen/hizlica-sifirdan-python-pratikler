# Bu script, kullanıcıdan iki harcamayı ve fiyatlarını alır, toplam harcamayı hesaplar.

liste = []
fiyatlar = []

harcama1 = input("Harcamalarınızı giriniz: ")
fiyat1 = int(input("Fiyatını giriniz: "))
harcama2 = input("Harcamalarınızı giriniz: ")
fiyat2 = int(input("Fiyatını giriniz: "))

liste.append(harcama1)
fiyatlar.append(fiyat1)
liste.append(harcama2)
fiyatlar.append(fiyat2)

toplam_harcama = sum(fiyatlar)
print("Yaptığın toplam harcama gideri:", toplam_harcama, "TL")
