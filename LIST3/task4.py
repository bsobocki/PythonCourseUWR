import random

def list_to_string(l):
    return ' '.join(l)

def uprosc_tekst(tekst, dl_slowa, liczba_slow):
    slowa = tekst.split()
    noLongWords = [x for x in slowa if len(x) <= dl_slowa]
    while len(noLongWords) > liczba_slow:
        del noLongWords[random.randrange(len(noLongWords))]
    return list_to_string(noLongWords)

for i in range (0, 10):
    print(uprosc_tekst("ddddd gggg ttt r ew dsar dsasdf bggbgbg fdsasdf bbb bb gg ff dd  rr tt ewq qass zcfs", 4, 10))

tekst = """ Literatura staropolska obejmuje następujące epoki: średniowiecze, ordodzenie,, barok i oświecenie. Epoki te różniły się między sobą filozofią życia, rozwijały się w różnych warunkach społeczno- ekonomiczno- politycznych, różniło je również inne spojżenie na świat, człowieka, różny stosunek do Boga, życia i śmierci.
W poszczególnych okresach pisarze i twórcy proponowali różne ideały, wzorce osobowe, dawali rozmaite propozycje na to jak żyć, jakim być człowiekiem, w co wierzyć.Wydawać by się mogło, że o losie człowieka decyduje on sam, jednak tak nie jest i nie było. Stosunek człowieka do Boga, zycia i śmierci jest i był bowiem kształtowany poprzez normy religijne, prawne i moralne jakie obowiązują wśród ludzi, którzy nas otaczają i w społeczeństwie w jakim żyjemy.
Tak jak juz wspomniałam, w różnych epokach wpływy wywierane na człowieka były różne. Uważam, że warto spojrzeć na nie z odrobinę bliższej perspektywy, dlatego też postaram się to zrobić w dalszej części mojej pracy."""

print("\n\n",uprosc_tekst(tekst, 8, 1000))

tekst = "Podział peryklinalny inicjałów wrzecionowatych \
    kambium charakteryzuje się ścianą podziałową inicjowaną \
        w płaszczyźnie maksymalnej."
print("\n\n",uprosc_tekst(tekst, 10, 5))