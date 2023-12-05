
def todo_list():
    icerik= []

    while True:
        print("\nTo Do LIST")
        print("1. Gorev ekle")
        print("2. Gorevleri Listele")
        print("3. Gorevleri Sil")
        print("4. Cikis")

        secim = input("Seciminizi yapiniz:")

        if secim =='1':
            metin = input("Eklemek istediginiz gorevi girin: ")
            icerik.append(metin)
            print("Gorev eklendi.")

        elif secim == '2':
            print("Gorevler:\n")
            for index, metin in enumerate(icerik,start=1):
                print(f"{index} . {metin}")


        elif secim == '4':
            print("Programdan cikiliyor.")
            break
        else:
            print("Gecersiz secenek.Lutfen tekrar giriniz.")
            


if __name__ == "__main__":
    todo_list()



