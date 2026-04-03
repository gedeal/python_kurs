# Övningsuppgifter: Pythons Datatyper
Dessa 10 uppgifter är utformade för att testa din förståelse för int , float , bool , str ,
list , tuple och dict . Försök att förklara varje steg du tar!
## Del 1: Grundläggande Typer ( int , float , bool , str )
### Uppgift 1: Typ- och Aritmetiktest
Skriv kod som:
Uppgift 2: Strängmanipulation och Konvertering
## Del 2: Listor ( list ) - Muterbara sekvenser
### Uppgift 3: Lista – Ändra och Lägg till
Du har en lista över veckans dagar.
### Uppgift 4: Lista – Ta bort och Sortera
1. Skapar en variabel a med heltalet 10 .
2. Skapar en variabel b med flyttalet 3.5 .
3. Beräknar och skriver ut a dividerat med b med vanlig division ( / ). Vilken datatyp får
resultatet?
4. Beräknar och skriver ut a dividerat med b med heltalsdivision ( // ). Vilken datatyp
får resultatet?
5. Skapar en variabel jämförelse som är True om a är större än 10, annars False .
Skriv ut jämförelse .
1. Skapa en sträng variabel text med värdet " python är roligt! " .
2. Ta bort blankstegen i början och slutet, gör första bokstaven stor, och skriv ut den nya
strängen.
3. Skapa två variabler: nummer_strang_1 med värdet "15" och nummer_strang_2 med
värdet "20" .
4. Konvertera strängarna till heltal och skriv ut summan av dem.
1. Skapa listan veckodagar = ["måndag", "tisdag", "onsdag", "torsdag",
"fredag"] .
2. Lägg till helgen ("lördag" och "söndag") i slutet av listan med en enda metod.
3. Anta att du gjorde fel och vill byta ut "torsdag" mot "LÄSDAG". Ändra elementet direkt via
dess index.
4. Skriv ut den slutgiltiga listan.
Du har en lista med osorterade siffror.
### Uppgift 5: List Comprehension
Använd list comprehension för att:
## Del 3: Tupler ( tuple ) - Oföränderliga sekvenser
### Uppgift 6: Tupelns natur
### Uppgift 7: Tupel med muterbart element
## Del 4: Ordböcker ( dict ) - Nyckel-värde-par
### Uppgift 8: Ordbok – Skapa och Åtkomst
1. Skapa listan siffror = [50, 10, 50, 5, 20, 10] .
2. Ta bort den första förekomsten av värdet 10 .
3. Ta bort det sista elementet i listan och spara det borttagna värdet i en variabel. Skriv ut
det borttagna värdet.
4. Sortera den kvarvarande listan i fallande ordning.
5. Skriv ut den sorterade listan.
1. Skapa en ny lista resultat som innehåller kvadraten (talet upphöjt till 2) av alla heltal
från 1 till 10 (båda inkluderade).
2. Skapa en annan lista namn_som_startar_med_s baserat på listan namn = ["Sara",
"Olle", "Stina", "Adam", "Simon"] . Den nya listan ska endast innehålla namn som
börjar med bokstaven 'S' (case-sensitivt).
1. Skapa tupeln koordinater = (15, 30) .
2. Försök (genom att kommentera ut koden som ger fel) att ändra värdet 15 till 100 .
Förklara varför det misslyckas.
3. Skapa en ny tupel ny_koordinater genom att lägga till värdet 45 till koordinater
med hjälp av konkatenering ( + ).
4. Använd tupel-uppackning för att tilldela de tre värdena i ny_koordinater till
variablerna x , y och z . Skriv ut x .
1. Skapa en tupel t = ("data", [1, 2, 3], 100) .
2. Ändra innehållet i listan inuti tupeln genom att lägga till värdet 4 till listan.
3. Skriv ut tupeln och förklara varför du kunde ändra listans innehåll men inte byta ut listan
mot ett nytt värde.
1. Skapa en ordbok produkt med nycklarna "id" , "namn" och "pris" och tilldela dem
lämpliga värden.
2. Ändra värdet för "pris" till ett nytt, högre värde.
### Uppgift 9: Ordbok – Iteration
Du har ordboken poäng = {"Anna": 85, "Bertil": 92, "Cecilia": 78} .
### Uppgift 10: Nyckelkrav och Muterbarhet
3. Försök hämta värdet för nyckeln "lagerstatus" med metoden .get() . Om nyckeln
saknas ska den returnera standardvärdet "Finns ej i lager" . Skriv ut resultatet.
4. Lägg till ett nytt nyckel-värde-par: "kategori" med värdet "Elektronik" .
5. Skriv ut hela ordboken.
1. Loopa igenom ordboken och skriv ut endast nycklarna (namnen).
2. Loopa igenom ordboken och skriv ut endast värdena (poängen).
3. Loopa igenom ordboken och skriv ut både nyckeln och värdet i formatet: "Anna fick 85
poäng."
1. Skapa en lista min_lista = [1, 2] och försök använda den som nyckel i en ordbok d
= {min_lista: "fel"} . Förklara felet.
2. Skapa en tupel min_tupel = (1, 2) och använd den som nyckel i en ordbok d2 =
{min_tupel: "rätt"} . Förklara varför detta fungerar, men listan inte.