# Algorytmy

## Czasy wykonywania

Notacja dużego O – określa czas działania (ilość operacji), w najgorszym przypadku.

Ignoruje się w zapisie stałe jak np: $\frac{1}{2}$, 2, itp.

Przykładowe:

- O($log_{2} n$) – czas logarytmiczny, wyszukiwanie binarne

- O($n$) – czas liniowy, wyszukiwanie proste

- O( $n \cdot log _{2}n$) – szybkie sortowanie

- O($n^{2}$) – sortowanie przez wybieranie

- O($n!$) – problem podróżującego komiwojażera

## Wyszukiwanie binarne

wejście: **posortowana** lista elementów

wyjście: znaleziony indeks elementu lub null

sposób działania:

- przykład: wyobraź sobie taką sytuację, że próbujesz znaleźć numer, który wybrała sobie osoba z przedziału 1-100.

- zamiast jak głupki lecieć od początku (1, 2, 3…) to „strzelamy” w środek i zaczynamy od 50.

- następnie sprawdzamy czy nasz strzał był zbyt wysoki, czy zbyt niski
  
  - zbyt wysoki: maksymalna wartość to nasz strzał - 1
  
  - zbyt niski: minimalna wartość to nasz strzał + 1

- i tak aż znajdziemy odpowiedź, jak mimo to nie odnaleźliśmy odpowiedzi to znaczy że taka rzecz w tablicy nie istnieje

Przykładowy kod:

```py
# list - nasza lista elementów
# item - wartość rzeczy, której poszukujemy
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]

        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1

    return None
```

## Sortowanie przez wybór

Sytuacja: mamy listę utworów z liczbą odwtorzeń i chcemy zrobić sobie TOP 10.

W naszej liście sprawdzamy każdy element i szukamy największego, jak znajdziemy wpisujemy go do nowej listy. Tak robimy dla każdej rzeczy w pierwotnej liście.

Czas wykonania: O($n^{2}$)

## Sortowanie szybkie

Algorytm rekurencyjny

Sposób działania: weź ustal sobie jakiś element, następnie podziel tablicę na mniejsze i większe od tego elementu, następnie wywołaj ten sam algorytm dla podtablic: mniejsze + pivot + większe.

Czas wykonania – zależy od wyboru pivota (elementu osiowego):

- najgorszy: $O(n^{2})$ – np. pivot to element pierwszy, a sortujemy tablicę już posortowaną

- średni: $O(n \times log_{2}n)$ – np. pivot to element w środku (czyli jest losowy), a sortujemy tablicę posortowaną

Dlaczego tak? Wszystko zależy od pivota + wszystko mnożymy przez $n$, dlatego że za każdym razem "dotykamy" każdego elementu, kiedy dzielimy je na mniejsze i większe od pivota. Dlaczego od pivota? To jest wysokość naszego stosu wywołań, czyli ile razy wywołujemy rekurencyjnie naszą funkcję. Jak damy go w złym miejscu, to będziemy wywoływać naszą funkcję wiele razy.

W porównaniu do np. sortowania przez scalanie czas O jest taki sam ALE:

Notacja dużego O tak naprawdę oblicza się w ten sposób: $c\space*\space O $, gdzie $c$ – stała ilość czasu wykorzystywana przez algorytm, O – wartość notacji dużego O

No i tak sortowanie przez scalanie jest wolniejsze bo ma wyższą stałą, niż średni czas sortowania szybkiego! Ale to działa tylko dla algorytmów z tym samym $O$.

## Wyszukiwanie wszerz

>  ang: breadth-first search (**BFS**)

Znajduje najkrótszą drogę w grafie – czyli z najmniejszą liczbą węzłów, przez które musimy przejść lub czy w ogóle taka droga istnieje

Czas wykonywania: $O(V + E)$

    gdzie: **V** – liczba wierzchołków (vertex), **E** – liczba krawędzi (edge)

Działanie: zaczynamy od utworzenia kolejki od wierzchołka początkowego, sprawdzamy każdy wierzchołek i sprawdzamy czy spełnia wymaganie, jeśli nie to dodajemy sąsiadów tego wierzchołka do kolejki oraz do tablicy przetworzonych wierzchołków (tak żeby nie sprawdzać go więcej niż raz)

### Algorytm Dijkstry

Znajduje najkrótszą drogę (o najniższym koszcie) w grafie ważonym.

> UWAGA! Graf musi być acykliczny i skierowany (directed acyclic graph – **DAG**) oraz nie może mieć ujemnych wag (do tego służy algorytm Bellmana-Forda)

A tak naprawdę to znajduje najkrótszą drogę do <u>każdego</u> wierzchołka oraz koszt jej przejścia.

Podstawową ideą jest to, że znajdujemy najtańszy węzeł w grafie – nie ma tańszego sposobu na dotarcie do tego węzła od startu przy zdejmowaniu go z kolejki

Implementacja: tworzymy trzy tablice skrótów: z grafem, z kosztami dotarcia do wierzchołka i rodzicami wierzhołków oraz tablicę przetworzonych węzłów. Na początku koszt dotarcia do mety wynosi **nieskończoność**.

Wrzucami do kolejki węzły będące sąsiadami początkowego.

Pobieramy z kolejki węzeł, aktualizujemy koszty jego sąsiadów jeśli są krótsze niż w tablicy z kosztami oraz aktualizujemy wtedy jego rodziców, na koniec oznaczamy węzeł jako przetworzony.

# Inne sprawy

## Dziel i rządź

Dzielimy element na jak najmniejsze części

Wykorzystywany w rekurencji: podziel na przypadek podstawowy i rekurencyjny.

Dla tablic to często pusta tablica lub tablica z jednym elementem.

## Stos

LIFO – Last In, First Out

Działa jak stos karteczek samoprzylepnych... jeśli chcemy się dostać na sam dół to musimy zdjąć wszystkie z góry.

Stos wykorzystywany jest przy wywołaniach nowych funkcji, każda nowa funkcja jest wrzucana na stos (zapewnia to system operacyjny).

## Kolejka

FIFO – First In, First Out

Tak jak w rzeczywistości...

Nie mamy swobodnego dostępu do elementów, można wykonać tylko: dodawanie i usuwanie.

Dodajemy na koniec kolejki, a usuwamy z początku (czyli jeśli byłeś pierwszy, to też pierwszy załatwisz sprawę w kolejce – stąd FIFO)

## Tablice skrótów

W Pythonie to Dictionary

Czas wykonywania zależy od współczynnika zapełnienia i przy dobrym (tzn. 0,7 i mniejszym) czas wykonywania jest stały $O(1)$.

Współczynnik zapełniania: liczba elementów w tablicy skrótów / liczba wszystkich miejsc (zazwyczaj się tym nieprzejmujemy, bo implementację zapewnia język programowania)

Dlaczego? Bo inaczej szukamy rzeczy w liście powiązanej, w wyniku kolizji – czyli ta sama rzecz znajduje się pod tym samym `key`.

Key ustalany jest przez funkcję haszującą (stąd nazwa, btw). Ta funkcja musi dla tego samego wejścia, zawsze zwracać to samo wyjście (stabilna)

Czas wykonywania:

- średni:
  
  - wyszukiwanie: $O(1)$
  
  - wstawianie: $O(1)$
  
  - usuwanie: $O(1)$

- najgorszy:
  
  - wyszukiwanie, wstawianie, usuwanie: $O(n)$
  
  - jest wtedy, kiedy musimy szukać rzeczy w liście powiązanej

Do czego się nadaje?

    Modelowanie relacji między elementami (np. graf)

    Pamięć podręczna

    Wykrywanie duplikatów (np. głosowanie więcej niż 2 razy)

## Graf

to model zbioru połączeń

składa się z wezłów i krawędzi

![Scan 20200320-004249.jpeg](/Users/jonatanwitoszek/Desktop/Matura informatyka/Notatki/foto/Scan 20200320-004249.jpeg)

jeśli węzeł jest bezpośrednio połączony z innym to jest jego sąsiadem

### Rodzaje grafów

Grafy mogą być:

- skierowane (występują tylko jednokierunkowe relacje, nie ma cyklów)

![IMG_4D87B105E5D7-1.jpeg](/Users/jonatanwitoszek/Desktop/Matura informatyka/Notatki/foto/IMG_4D87B105E5D7-1.jpeg)

- nieskierowane (węzły są swoimi sąsiadami nawzajem, nie ma "strzałek")

![IMG_DA17D3ECCE50-1.jpeg](/Users/jonatanwitoszek/Desktop/Matura informatyka/Notatki/foto/IMG_DA17D3ECCE50-1.jpeg)

- ważone (krawędzie mają wagi)

![IMG_1A10011186FC-1.jpeg](/Users/jonatanwitoszek/Desktop/Matura informatyka/Notatki/foto/IMG_1A10011186FC-1.jpeg)

- nieważone

- cykliczne (występują cykle)
  
  ![IMG_613C04800326-1.jpeg](/Users/jonatanwitoszek/Desktop/Matura informatyka/Notatki/foto/IMG_613C04800326-1.jpeg)

- acykliczne

### Sortowanie topologiczne

### Drzewo

To szczególny rodzaj grafu, w którym wszystkie krawędzie wskazują w jedną stronę
