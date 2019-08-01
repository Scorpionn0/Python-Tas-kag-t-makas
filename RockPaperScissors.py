#Enes Kasapoğlu. http://eneskasapoglu.ml/
import random 
try:
    
    print("1-Taş")
    print("2-Kağıt")
    print("3-Makas")

    bilgisayar_secimi = int(random.uniform(1,3))
    kullanici_secimi = int(input("Seçiminiz: "))

    if kullanici_secimi == 1 and bilgisayar_secimi == 1:
        print("Bilgisayarın seçimi: " + str(bilgisayar_secimi))
        print("Aynı seçimler tekrar dene")

    elif kullanici_secimi == 1 and bilgisayar_secimi == 2:
        print("Bilgisayarın seçimi: " + str(bilgisayar_secimi))
        print("Kaybettin")
        
    elif kullanici_secimi == 1 and bilgisayar_secimi == 3:
        print("Bilgisayarın seçimi: " + str(bilgisayar_secimi))
        print("Kazandın!")



    if kullanici_secimi == 2 and bilgisayar_secimi == 1:
        print("Bilgisayarın seçimi: " + str(bilgisayar_secimi))
        print("Kazandın")
        
    
    elif kullanici_secimi == 2 and bilgisayar_secimi == 2:
        print("Bilgisayarın seçimi: " + str(bilgisayar_secimi))
        print("Aynı seçimler tekrar dene")
        
    elif kullanici_secimi == 2 and bilgisayar_secimi == 3:
        print("Bilgisayarın seçimi: " + str(bilgisayar_secimi))
        print("Kaybettin")
        



        
    if kullanici_secimi == 3 and bilgisayar_secimi == 1:
        print("Bilgisayarın seçimi: " + str(bilgisayar_secimi))
        print("Kaybettin")
        
    elif kullanici_secimi == 3 and bilgisayar_secimi == 2:
        print("Bilgisayarın seçimi: " + str(bilgisayar_secimi))
        print("Kazandın!")
    
    elif kullanici_secimi == 3 and bilgisayar_secimi == 3:
        print("Bilgisayarın seçimi: " + str(bilgisayar_secimi))
        print("Aynı seçim tekrar dene")
        
        
           


except ValueError:
    print("Lütfen seçiminizi sadece sayı olarak yapın")
    
