======
- Konrad Konopka
- Informatyka i Elektronika Medyczna
- Projekt realizujący materiał z:
 -**Eksploracja danych i głosowa łączność z komputerem**
- &
- **Projektowanie aplikacji webowych**

Opis
==============

Projekt aplikacji webowej, jest projektem zaliczeniowym wspomnianych przedmiotów, gdyż pokrywa wymagania stawiane w obu przypadkach.

Pliki źródłowe projektu są zamieszczone w repozytorium https://github.com/konradkonopka/Appweb
W gałęzi *Heroku* znajdują się pliki wrzucone na serwer, więc powinny być najbardziej aktualne.
Applikacja została wrzucona na serwer https://afternoon-plains-78371.herokuapp.com

Wymagania systemowe
==============
- środowisko programistyczne (np. PyCharm Community Edition 2015.1.3)
- python 2.7 (polecany zbiór bibliotek oferowany przez Anaconda - https://www.continuum.io/downloads)
- reszta wymagań znajduje się w pliku requirements.txt

Wykorzystane zasoby (frameworki, biblioteki...)
==============

- Scrapy - przeszukiwanie treści na witrynach internetowych
- Flask - Web Server Gateway Interface
- Sqlite - Baza danych
- Google charts - Tworzenie wykresów


Opis zawartości
==============
Zakładka "Formularz"
--------------

Na tej stronie można uzupełnić formularz. Rodzaj gromadzonych danych pokrywa się z danymi prezentowanymi przez
rejestr MSBase.org Dane gromadzone są w bazie sqlite w pliku formdata.db

Zakładka "Surowe dane"
--------------

Przedstawienie wyników zgromadzonych w formularzu.

Zakładka Wyniki MSBase
--------------
Przedstawia w postaci wykresów (wykorzystane google charts) dane zebrane przy pomocy spidera.

Opis czynności skryptu:
-crawling danych z witryny: https://www.msbase.org/cms/benchmarking.json
    Dane te są pobierane na bieżąco z docelowej witryny, a dane gromadzone w postaci pliku json
    Za te operacje odpowiada moduł *dirbot*
-przekonwertowanie zebranych danych do postaci akceptowalnej przez wykresy google (moduł *unit5*)
-przedstawienie zgromadzonych wyników za pomocą piechart:
    https://developers.google.com/chart/interactive/docs/gallery/piechart
