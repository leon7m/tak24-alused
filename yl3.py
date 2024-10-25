# Kirjuta programm, mis küsib kasutajalt täisarvu n vahemikus 1-9.
#  Arvuta n + nn + nnn väärtus ja väljasta see.
#  (Näiteks kui kasutaja sisestab 2,
#  siis on vaja väljastada tulemus 2 + 	22 + 222 = 246).
#  Ära kasuta korrutamistehet.
#  Ülesanne on lahendatav ainult liitmise operaatorit kasuades.

n = input ("Sisesta taisarv vahemikus 1-9:")
nn = str(n + n)
nnn = str(n + n + n)
vastus = ( n "+" nn "+" nnn)

print ("n", n)
print ("nn", nn)
print ("nnn", nnn)
print ("vastus",vastus)