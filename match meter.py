print ("Selamat Datang di Aplikasi Match Meter")
loop = True
while loop: #otomatis true

    cowok = input ("masukkan nama cowok : ")
    cewek = input ("masukkan nama cewek : ")
    zodiakco = input ("masukkan zodiak cowok : ")
    zodiakce = input ("masukkan zodiak cewek : ")
    print ("==================================")
    print ("nama cowok", cowok)
    print ("nama cewek", cewek)
    print ("zodiak cowok", zodiakco)
    print ("zodiak cewek", zodiakce)
    confrim = input ("apakah data yang dimasukan sudah benar? y/n :")
    if confrim == "y":
        print ("a")
        loop = False
import random
match = random.randrange(0,100)
print('match.meter',match, '%')
if match > 80:
    print ("rabi")
elif match > 60:
    print ("tunangan")
elif match > 40:
    print ("ndang rabi")
elif match > 20:
    print ("pacaran")
elif match > 0:
    print ("pendekatan")
elif match == 0:
    print ("putus")
else:
    print ("jomblo")
