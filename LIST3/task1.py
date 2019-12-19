import math
from operator import itemgetter

def wyniki_mandatow(glosy, liczba_mandatow):
    wyniki = []

# ?????????????????????????????????????

    return wyniki

def mandaty_wyborcze(glosy, liczba_mandatow):
    mandaty = {}
    wyniki = wyniki_mandatow(glosy, liczba_mandatow).sort(key=itemgetter(1), reverse=True)
    
    return glosy

glosy = [
    ("Jaroslaw Kaczynski", "PiS", 394902), 
    ("Jan Wilk", "Konfederacja", 34052), 
    ("Janusz Korwin-Mikke", "Konfederacja", 3459), 
    ("Patryk Jaki", "PiS", 345567), 
    ("Adam Adam", "FajnaPartia", 46777)]
    
print(mandaty_wyborcze(glosy, 130))