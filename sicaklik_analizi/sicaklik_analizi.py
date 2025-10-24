# Bu script, 7 günlük sıcaklık verilerinden ortalama, en yüksek ve en düşük değerleri hesaplar.

sicaklik = {
    "gun1": 19,
    "gun2": 23,
    "gun3": 24,
    "gun4": 22,
    "gun5": 16,
    "gun6": 18,
    "gun7": 21
}

ortalama = sum(sicaklik.values()) / 7
en_yuksek = max(sicaklik.values())
en_dusuk = min(sicaklik.values())

print("Ortalama sıcaklık:", ortalama,
      "\nEn yüksek sıcaklık:", en_yuksek,
      "\nEn düşük sıcaklık:", en_dusuk)
