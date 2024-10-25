# Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi 
# (ära kasuta max funktsiooni). (loogikatehted - logic operators)
x = int(input("Sisesta arv: "))
y = int(input("Sisesta teine arv: "))
w = int(input("Sisesta kolmas arv: "))

if x > y and x > w :
    print(x, "on maksimum")

elif y > w :
    print(w, "on maksimum")

else:
    print(w, "on maksimum")