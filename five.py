import sys
def sifrele(metin):
    metin ="ebru"
    sifre = ""
    for k in metin:
        print(ord(k))
        #ord yi ascii karşılıklarını bulmak için kulllanıyoruz
        print(k, "=>", chr(ord(k) + 5))
        sifre = sifre + chr(ord(k) + 5)

    print(sifre)
    print(metin, "=>", sifre)

def sifrecoz(sifre):
    metin = ""
    for k in sifre():
    print(k, "=>", chr(ord(k)-5))
    metin = metin + chr(ord(k)-5)
print(sifre, "=>", metin)
