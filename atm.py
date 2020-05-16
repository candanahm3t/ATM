hak=3
while True:
  
    pin = int(input("Lütfen 4 Haneli Pin Numaranızı Girin:")) 
    if (pin == (1234)):

        print("""***********************************
        Atm Makinesine Hoşgeldiniz

        İşlemler;

        1. Bakiye Sorgulama

        2. Para Yatırma 

        3. Para Çekme

        Programdan Çıkmak İçin 'q' ya basın
        ***********************************""")
        bakiye = 1000

        while True:
            islem=input("İşleminizi Seçin:")
            if (islem=="q"):
                print("Yine Bekleriz")
                break
            elif (islem== "1"):
                print("Bakiyeniz {}'dir".format(bakiye))

            elif (islem== "2"):
                miktar = int(input("Miktarı Giriniz"))
                bakiye += miktar

            elif (islem== "3"):
                miktar = int(input("Miktarı Giriniz"))
                if (bakiye-miktar < 0):
                    print("Bakiye Yetersiz")
                    continue
                bakiye -= miktar

            else:
                print("Geçersiz İşlem")
    else:
        print("PIN Yanlış Lütfen Tekrar Deneyin")
        hak -=1  
    if (hak == 0):
        print("Kartınız Bloke Olmuştur En Yakın Şubeye Başvurun")
        break