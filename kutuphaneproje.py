class Kitap:

    def __init__(self, isim, yazar, yil):
        self.isim = isim
        self.yazar = yazar
        self.yil = yil

    def __str__(self):
        return f"Kitap: {self.isim} | Yazar: {self.yazar} | Yıl: {self.yil}"


class Kutuphane:

    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, isim, yazar, yil):
        try:
            yil = int(yil)
            kitap = Kitap(isim, yazar, yil)
            self.kitaplar.append(kitap)
            print(f"\n✓ '{isim}' kitabı eklendi.")
        except ValueError:
            print("\n✗ Hata: Yayın yılı sayısal olmalıdır.")

    def kitap_sil(self, isim):
        for kitap in self.kitaplar:
            if kitap.isim.lower() == isim.lower():
                self.kitaplar.remove(kitap)
                print(f"\n✓ '{isim}' kitabı silindi.")
                return
        print(f"\n✗ '{isim}' adlı kitap bulunamadı.")

    def ada_gore_ara(self, isim):
        bulunanlar = []

        for kitap in self.kitaplar:
            if isim.lower() in kitap.isim.lower():
                bulunanlar.append(kitap)

        if bulunanlar:
            print("\n" + "=" * 60)
            print(f"'{isim}' için bulunan kitaplar:")
            print("=" * 60)
            for i, kitap in enumerate(bulunanlar, 1):
                print(f"{i}. {kitap}")
            print("=" * 60)
        else:
            print(f"\n✗ '{isim}' adında kitap bulunamadı.")

    def yazara_gore_ara(self, yazar):
        bulunanlar = []

        for kitap in self.kitaplar:
            if yazar.lower() in kitap.yazar.lower():
                bulunanlar.append(kitap)

        if bulunanlar:
            print("\n" + "=" * 60)
            print(f"'{yazar}' yazarına ait kitaplar:")
            print("=" * 60)
            for i, kitap in enumerate(bulunanlar, 1):
                print(f"{i}. {kitap}")
            print("=" * 60)
        else:
            print(f"\n✗ '{yazar}' adlı yazara ait kitap bulunamadı.")

    def kitaplari_listele(self):
        if not self.kitaplar:
            print("\n✗ Kütüphanede kitap yok.")
            return

        print("\n" + "=" * 60)
        print(f"KÜTÜPHANE KİTAPLARI (Toplam: {len(self.kitaplar)})")
        print("=" * 60)
        for i, kitap in enumerate(self.kitaplar, 1):
            print(f"{i}. {kitap}")
        print("=" * 60)


def menu_goster():
    print("\n" + "=" * 60)
    print("KÜTÜPHANE YÖNETİM SİSTEMİ")
    print("=" * 60)
    print("1. Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Kitap Ara (Ada Göre)")
    print("4. Kitap Ara (Yazara Göre)")
    print("5. Tüm Kitapları Listele")
    print("6. Çıkış")
    print("=" * 60)


def main():
    kutuphane = Kutuphane()

    kutuphane.kitap_ekle("Suç ve Ceza", "Fyodor Dostoyevski", 1866)
    kutuphane.kitap_ekle("Savaş ve Barış", "Lev Tolstoy", 1869)
    kutuphane.kitap_ekle("1984", "George Orwell", 1949)
    kutuphane.kitap_ekle("Hayvan Çiftliği", "George Orwell", 1945)
    kutuphane.kitap_ekle("Simyacı", "Paulo Coelho", 1988)

    while True:
        menu_goster()
        secim = input("Seçiminiz (1-6): ").strip()

        if secim == "1":
            isim = input("Kitap adı: ").strip()
            yazar = input("Yazar adı: ").strip()
            yil = input("Yayın yılı: ").strip()

            if isim and yazar and yil:
                kutuphane.kitap_ekle(isim, yazar, yil)
            else:
                print("\n✗ Tüm alanlar doldurulmalıdır.")

        elif secim == "2":
            isim = input("Silinecek kitap adı: ").strip()
            if isim:
                kutuphane.kitap_sil(isim)
            else:
                print("\n✗ Kitap adı boş olamaz.")

        elif secim == "3":
            isim = input("Aranacak kitap adı: ").strip()
            if isim:
                kutuphane.ada_gore_ara(isim)
            else:
                print("\n✗ Arama terimi boş olamaz.")

        elif secim == "4":
            yazar = input("Aranacak yazar adı: ").strip()
            if yazar:
                kutuphane.yazara_gore_ara(yazar)
            else:
                print("\n✗ Arama terimi boş olamaz.")

        elif secim == "5":
            kutuphane.kitaplari_listele()

        elif secim == "6":
            print("\nProgramdan çıkılıyor.")
            break

        else:
            print("\n✗ Geçersiz seçim!")


if __name__ == "__main__":
    main()

