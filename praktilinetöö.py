#1
ümbermõõt = float(input("Sisesta puu ümbermõõt: "))
läbimõõt = ümbermõõt / 3.14
print("Puu läbimõõt on " + str(läbimõõt) + " meetrit.")
#2
N = float(input("Sisesta ristküliku pikkus N meetrites: "))
M = float(input("Sisesta ristküliku laius M meetrites: "))
diagonaal = (N**2 + M**2)**0.5
print("Ristkülikukujulise maatüki diagonaal on " + str(diagonaal) + " meetrit.")
#3
aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print("Sinu kiirus oli " + str(kiirus) + " km/h")
#4
a = int(input("Sisesta esimene arv: "))
b = int(input("Sisesta teine arv: "))
c = int(input("Sisesta kolmas arv: "))
keskmine = (a + b + c) / 3
print("Arvude aritmeetiline keskmine on " + str(keskmine))
#5
print("   @..@")
print("   (----)")
print("  ( \__/ )")
print("^^ \"\" ^^")


#6
a = int(input("Sisestage esimese külje pikkus: "))
b = int(input("Sisestage teise külje pikkus: "))
c = int(input("Sisestage kolmanda külje pikkus: "))

P = a + b + c

print("Kolmnurga ümbermõõt on", P)
#7
pitsa_hind = 12.90
jootraha_protsent = 10

inimesi = int(input("Mitu inimest jagavad pitsat? "))

maksmine = (pitsa_hind * (1 + jootraha_protsent / 100)) / inimesi

print("Igaüks peab maksma", round(maksmine, 2), "eurot.")
#8
def new_func():
    kütuse_liitrid = float(input("Sisestage kütusekogus liitrites: "))
    return kütuse_liitrid

def new_func1(new_func):
    kütuse_liitrid = new_func()
    return kütuse_liitrid

kütuse_liitrid = new_func1(new_func)
läbitud_km = float(input("Sisestage läbitud kilomeetrite arv: "))

kütusekulu = 100 * kütuse_liitrid / läbitud_km

print("Kütusekulu 100 km kohta on", round(kütusekulu, 2), "liitrit.")
#9
keskmine_kiirus = 29.9

M = int(input("Sisestage aeg minutites: "))

kaugus = keskmine_kiirus * M / 60

print("Rulluisutaja jõuab", round(kaugus, 2), "kilomeetri kaugusele.")
#10
aeg_minutites = int(input("Sisestage aeg minutites: "))

tunnid = aeg_minutites // 60
minutid = aeg_minutites % 60

print("Aeg on", tunnid, "tundi ja", minutid, "minutit.")
