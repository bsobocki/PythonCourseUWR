import re

def wynik(string):
    print("kompresja( \"",string, "\" ) = \"",kompresja(string),"\"")

def kompresja(tekst):
    lista_znakow = list(tekst)
    kompresja = []
    licznik = 1
    for i in range(0, len(lista_znakow)-1):
        if lista_znakow[i+1] == lista_znakow[i]:
            licznik += 1
        elif licznik == 1:
            kompresja += lista_znakow[i]
        else:
            kompresja += str(licznik) + str(lista_znakow[i])
            licznik = 1
    # ostatni znak
    if licznik == 1:
            kompresja += lista_znakow[len(lista_znakow)-1]
    else:
        kompresja += str(licznik) + str(lista_znakow[len(lista_znakow)-1])

    return list_to_str(kompresja)

def dekompresja(tekst):
    lista_znakow = list(tekst)
    dekompresja = []
    licznik = ""
    for znak in lista_znakow:
        if znak.isalpha():
            dekompresja += [znak] *  wartosc_licznika(licznik)
            licznik = ""
        else:
            licznik += znak

    return list_to_str(dekompresja)

def wartosc_licznika(licznik):
    return 1 if licznik == ""  else int(licznik)

def list_to_str(lista):
    return "".join(lista)

print("(1)",end=' ')
wynik("AAabababbbbbbbbbb")
wynik("suuuuper")
wynik("aaaaa")

print("dekompresja (1) = ",dekompresja(kompresja("AAabababbbbbbbbbb")))
print("dekompresja (\"7a5b3we\") = ",dekompresja("7a5b3we"))