def ters(kelime):
    vowel = "aeiouAEIOU"
    a=len(kelime)
    for i in range (1 , a+1):
        b=kelime[a-i]
        if b in vowel:
            b = "*"
            print (b)
        else:
            print(b)

ters("ebru")
