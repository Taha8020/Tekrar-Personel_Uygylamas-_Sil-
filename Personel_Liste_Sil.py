def hazir_personeller():
    # Hazır personel listemiz
    personel_listesi = [
        {"isim": "Ali", "soyisim": "Yılmaz", "departman": "IT", "maas": 5000, "yas": 30},
        {"isim": "Ebru", "soyisim": "Kara", "departman": "HR", "maas": 4500, "yas": 28},
        {"isim": "Mehmet", "soyisim": "Demir", "departman": "Finance", "maas": 6000, "yas": 35},
        {"isim": "Elif", "soyisim": "Çelik", "departman": "Marketing", "maas": 4800, "yas": 26},
        {"isim": "Can", "soyisim": "Öztürk", "departman": "Sales", "maas": 5200, "yas": 32}
    ]
    return personel_listesi

def personel_ekle(mevcut_liste):
    while True:
        try:
            girilecek_personel_sayisi = int(input("Kaç personel eklemek istiyorsunuz? "))
            if girilecek_personel_sayisi > 0:
                break
            print("Lütfen 0'dan büyük bir sayı giriniz.")
        except ValueError:
            print("Hatalı giriş! Lütfen bir sayı giriniz.")
            
    for i in range(girilecek_personel_sayisi):
        print(f"\n--- {i+1}. Personel ---")
        isim = input("İsim: ")
        soyisim = input("Soyisim: ")
        departman = input("Departman: ")
        
        while True:
            try:
                maas = float(input("Maaş: "))
                break
            except ValueError:
                print("Hatalı giriş! Lütfen maaşı sayı olarak giriniz.")
                
        while True:
            try:
                yas = int(input("Yaş: "))
                break
            except ValueError:
                print("Hatalı giriş! Lütfen yaşı tam sayı olarak giriniz.")
                
        yeni_personel = {
            "isim": isim,
            "soyisim": soyisim,
            "departman": departman,
            "maas": maas,
            "yas": yas
        }
        mevcut_liste.append(yeni_personel)
        print(f"Başarıyla eklendi: {isim} {soyisim}")
    
    return mevcut_liste

def personel_sil(personel_listesi):
    print("\n" + "-"*30)
    print("Personel Silme Ekranı")
    print("-" * 30)
    
    if len(personel_listesi) == 0:
        print("Sistemde silinecek personel bulunamadı.")
        return personel_listesi

    for sira, personel in enumerate(personel_listesi, 1):
        print(f"{sira}. İsim: {personel['isim']} {personel['soyisim']} | Yaş: {personel['yas']}")

    while True:
        try:
            secim = int(input("\nSilmek istediğiniz personelin numarasını girin (İptal için 0): "))
            if secim == 0:
                print("Silme işlemi iptal edildi.")
                break
                
            index = secim - 1
            if 0 <= index < len(personel_listesi):
                silinen = personel_listesi.pop(index)
                print(f"Başarıyla silindi: {silinen['isim']} {silinen['soyisim']}")
                break
            else:
                print("Hata: Geçersiz personel numarası. Tekrar deneyin.")
        except ValueError:
            print("Hatalı Giriş! Lütfen bir sayı giriniz.")
            
    return personel_listesi

def giris():
    ana_liste = hazir_personeller()

    while True:
        print("\n----- Personel Kayıt Sistemi -----")
        print("1. Hazır ve Eklenen Personelleri Görüntüle")
        print("2. Yeni Personel Ekle")
        print("3. Personel Sil")
        print("4. Çıkış")
        
        secim = input("Lütfen bir seçenek giriniz (1-2-3-4): ").strip()
        
        if secim == "1":
            print("\n--- Personel Listesi ---")
            if len(ana_liste) == 0:
                print("Sistemde kayıtlı personel bulunamadı.")
            else:
                for sira, p in enumerate(ana_liste, 1):
                    print(f"{sira}. İsim: {p['isim']} {p['soyisim']} | Departman: {p['departman']} | Yaş: {p['yas']} | Maaş: {p['maas']}")
                
        elif secim == "2":
            ana_liste = personel_ekle(ana_liste)
            gorme_istegi = input("\nKayıt işlemi tamamlandı. Güncel listeyi şimdi görmek ister misiniz? (E/H): ").strip().upper()
            if gorme_istegi == 'E':
                print("\n--- Güncel Personel Listesi ---")
                for sira, p in enumerate(ana_liste, 1):
                    print(f"{sira}. İsim: {p['isim']} {p['soyisim']} | Departman: {p['departman']} | Yaş: {p['yas']} | Maaş: {p['maas']}")
                
        elif secim == "3":
            ana_liste = personel_sil(ana_liste)
            
        elif secim == "4":
            print("Sistemden çıkılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim! Lütfen 1, 2, 3 veya 4 girin.")

if __name__ == "__main__":
    giris()