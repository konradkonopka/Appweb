======
- Konrad Konopka
- Informatyka i Elektronika Medyczna

- Projekt zaliczeniowy spełniający wymagania dla przedmiotów:
 -**Eksploracja danych i głosowa łączność z komputerem**
- &
- **Projektowanie aplikacji webowych (przedmiot w ramach różnic programowych)**

Opis
==============
Projekt ten zawiera przykład aplikacji webowej, której celem była nauka tworzenia tego rodzaju aplikacji.

Pliki źródłowe projektu są zamieszczone w repozytorium https://github.com/konradkonopka/Appweb
Aplikacja została zbudowana i wrzucona na serwer **Heroku**, z gałędzi #build. Dlatego tam, powinny znajdować się pliki najbardziej aktualne.
Applikacja została wrzucona na serwer https://afternoon-plains-78371.herokuapp.com


Wymagania systemowe
==============
- plik requirements.txt zawiera spis wszystkich potrzebnych modułów wraz z wersją softu.
- środowisko programistyczne (np. PyCharm Community Edition 2016.1.4)
- python 2.7 (polecany zbiór bibliotek oferowany przez Anaconda - https://www.continuum.io/downloads)

Opis zawartości
==============
Zakładka "INFO"
--------------
Powitalna zakładka, z którkim opisem działania aplikacji. Z tego miejsca można również przejść do kolejnych zadań aplikacji.
Aplikacja została oprata o wzorzec przygotowany w ramach wykładów z powyższych przedmiotów. (unit5)

Zakładka "Formularz"
--------------
Formularz jest przygotowany w formie anonimowej ankiety, symulującej badanie zadowolenia zawodowego oraz warunków wynagrodzenia.
Dane zebrane w formularzu, są przesyłane do stworzonej bazy sqlite w pliku formdata.db.
Plik formdata został edytowany i przerobiony za pomocą narzędzia SQLiteManager, umożliwiający przygotowanie najprostrzej tabeli bazodanowej i dodanie nowych rekordów.

Zakładka "Zebrane dane"
--------------
W tej zakładce odpytywana jest baza sqlite w celu wyświetlenia wszytskich dodanych rekordów. Wyniki te są wyświetlane w postaci tabeli.

Zakładka MSBase.org
--------------
W tej części można zobaczyć zwizualizowane dane pobrane z pewnej witryny.
Zdecydowano się na tą witrynę, ze względu na przejrzystość zawartych w niej danych i łątwość w ekstrachowaniu wybranych informacji.

Dane z tej witryy są pobierane przy pomocy bota - webcrawlera, którego szkic zapożyczono z następującego repozytorium: https://github.com/scrapy/dirbot
Wykorzystano ten kod źródłowy, w celu pozyskania i zapisania do pliku *.json informacji w zawartych na stronie tabelach dotyczących statystyk zachorowania na pewne skorzenie.

Dane są bierane w momencie wyświetlenia tej zakładki, za co odpowiada moduł *dirbot*. Dane te są w odpowiedni sposób konwertowane na taką formę, którą w prosty sposób można podać na wejście modułów wykresów google. Konwersja ta odbywa się w module głównym aplikacji *unit5*.
Dane są wyświetlane w postacji wykresów kołowych, wykorzystując gotowe rozwiązanie wykresów google piechart: https://developers.google.com/chart/interactive/docs/gallery/piechart

Serwer
==============
W celu wrzucenia i uruchomienia aplikacji na serwerze, wykorzstano darmowy deplyment serwisu *Hiroku*. Aplikacja ta została wrzucona z gałęzi #build i znajduje się na koncie Konrad.Konopka@gmail.com

Kontrola wersji
==============
W celu kontrolowania postępów przygotowania aplikacji, wykorzystano repozytorium GitHub oraz pomocnicze toole GitHub i Git Shell.



