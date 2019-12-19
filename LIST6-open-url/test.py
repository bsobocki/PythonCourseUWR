import re

k = """"
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><head>
  <meta content="gedit" name="generator">
  <meta content="Marcin Młotkowski" name="author">
  <meta content="text/html; charset=UTF-8" http-equiv="Content-Type">
  <meta content="python" name="keywords">
  <meta content="opis wykładu" name="description">
  <title>... Rozszerzony kurs języka Python ...</title>
  <link href="Rozszerzony%20kurs%20j%C4%99zyka%20Python_pliki/zajecia.css" type="text/css" rel="stylesheet">
</head>
<body>
<!-- logo -->
<div class="logo">Rozszerzony kurs języka <a href="http://www.python.org/">Python</a> <br>
semestr zimowy 2019/2020<br>
</div>

<!-- komunikaty -->
<div class="lewy">

<h3>Spis rzeczy</h3>
<a href="#wykład">Opis wykładu</a><br>
<a href="#spis">Spis wykładów</a><br>
<a href="#inne">Przydatne linki</a><br>

<!--
<hr />
<div><a href="projekty.html">Projekty</a></div>
<hr />
-->

<hr>

<h3>Dane o wykładzie</h3>
<p><b>Wykładowca:</b> Marcin Młotkowski<br>
<b>Wykład:</b> środa 12:15-14:00, sala 25<br></p>

                                                                                



<h3>Komunikaty</h3>

<div class="info"><span class="info">2.10.2019: pierwszy wykład</span>
</div>

</div>

<div class="srodek">
<div class="item">
<h3 id="wykład">Parę słów o wykładzie</h3>
Python jest eleganckim obiektowo-zorientowanym językiem skryptowym, wykorzystywanym zarówno
do tworzenia serwisów interentowych jak i do tworzenia narzędzi do administrowania systemami
operacyjnymi (Linux Redhat). Składnia Pythona jest dość oryginalna: zakres pętli czy instrukcji
warunkowej jest wyznaczony za pomocą wcięć, jednak dzięki temu programy są przejrzyste i czytelne.
Silną stroną Pythona są listy będące częścią języka, dzięki czemu operacje na listach mają zwartą notację.

Programujący w Pythonie mają do swojej dyspozycji obszerną i rozwijaną bibliotekę standardową,
dzięki czemu można np. napisać klienta prostej sieci P2P w siedemnastowierszowym programie.
</div>

<div class="item">
<h3 id="spis">Wykłady</h3>
<table id="wyklady">
<tbody><tr><th>Lp</th><th>Data</th><th>Wykład</th><th>Zadania</th></tr>
<tr><td>1.</td><td>2.10.2019</td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/wstep.pdf">Wprowadzenie, sprawy organizacyjne</a></td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/lista01.pdf">Lista 1.</a></td></tr>
<tr><td>2.</td><td>9.10.2019</td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/obiekty.pdf">Programowanie obiektowe</a></td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/lista02.pdf">Lista 2.</a></td></tr>
<tr><td>3.</td><td>16.10.2019</td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/listy.pdf">Kolekcje, listy, iteratory, generatory</a></td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/lista03.pdf">Lista 3.</a></td></tr>
<tr><td>4.</td><td>23.10.2019</td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/generatory.pdf">Generatory</a></td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/lista04.pdf">Lista 4.</a></td></tr>
<tr><td>5.</td><td>06.11.2019</td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/tekstowe.pdf">Przetwarzanie tekstu: wyrażenia regularne, html, xml </a></td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/lista05.pdf">Lista 5.</a></td></tr>
<tr><td>6.</td><td>13.11.2019</td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/watki.pdf">Wątki</a></td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/lista06.pdf">Lista 6.</a></td></tr>
<tr><td>7.</td><td>20.11.2019</td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/numpy.pdf">numpy, matplotlib</a></td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/lista07.pdf">Lista 7.</a></td></tr>
<tr><td></td><td></td><td></td><td><a href="https://www.ii.uni.wroc.pl/~marcinm/dyd/python/lista08.pdf">Lista 8.</a></td></tr>

</tbody></table>
</div>

<div class="item">
<h3>Ćwiczenia i pracownie</h3>
<p>
Pracownia do zajęć z Pythona przez ok 10 tygodni będzie polegała na
zaprogramowaniu zadań z ogłaszanych po każdym wykładzie list.
Zadania należy oddać prowadzącemu do oceny na najbliższych zajęciach.
Na każdej liście będzie podany limit punktów, jakie można zdobyć za daną listę.
W przypadku spóźnienia o tydzień, za przedstawione zadania można uzyskać co najwyżej
połowę limitu. Po dwóch tygodniach po upływie terminu zadania nie będą oceniane.
</p>

<p>
Ostatni miesiąc pracowni jest przeznaczony na samodzielną realizację uzgodnionego
z prowadzącym pracownię projektu.
</p>


</div>


<div class="item">
<h3>Skala ocen</h3>
<p>
Suma punktów zdobytych za zaprogramowanie zadań z list oraz za projekt jest
podstawą do oceny.
Do zdobycia zaliczenia wymagane jest uzyskanie przynajmniej połowy
maksymalnej liczby punktów 
możliwych do zdobycia podczas całego semestru. Przedziały do pozostałych
ocen będą równo rozłożone (z dokładnością do różnych zaokrągleń etc.).

<!--
<table>
<tr><th>Punkty od</th><th>Punkty do</th><th>Ocena</th></tr>
<tr><td>25</td><td>29</td><td>3.0</td></tr>
<tr><td>30</td><td>34</td><td>3.5</td></tr>
<tr><td>35</td><td>39</td><td>4.0</td></tr>
<tr><td>40</td><td>44</td><td>4.5</td></tr>
<tr><td>45</td><td>50</td><td>5.0</td></tr>
</table>
-->
</p>
</div>

<div class="item">
<h3 id="inne">Gdzie szukać informacji</h3>
<h4> Python</h4>
<ul>
<li><a href="http://www.python.org/">
     Oficjalna strona o Pythonie wraz z dokumentacją</a></li>
<li><a href="https://diveintopython3.problemsolving.io/"><i>Dive into Python</i> Marka Pilgrima - znany
    podręcznik do Pythona</a></li>
<li>O Pythonie można poczytać na <a href="http://pl.wikipedia.org/wiki/Python">polskiej Wikipedii</a>
    oraz na <a href="http://en.wikipedia.org/wiki/Python_%28programming_language%29">anglojęzycznej Wikipedii</a>
    </li>
<li><a href="http://pl.python.org/">Polish Python Users Group</a></li>
</ul>
<h4>Tkinter</h4>
<ul>
<li><a href="">An Introduction to Tkinter, by Fredrik Lundh</a></li>
<li><a href="http://www.tkdocs.com/tutorial/">TkDocs</a></li>
</ul>
</div>

</div>



</body></html>
"""

l = "python"
pat = ".*[Pp][Yy][Tt][Hh][Oo][Nn].*"
pat2 = "[A-Z].*\."
kk = re.findall(pat2, k)

for i in kk : print(i,"\n\n")