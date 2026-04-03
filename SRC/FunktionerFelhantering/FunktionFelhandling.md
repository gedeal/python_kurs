# Övningsfil – Funktioner & Felhantering
## Uppgift 1 – Säker kalkylator
Skapa ett program som fungerar som en enkel kalkylator.

### Krav:
- Skapa minst 3 funktioner:

-- add(a, b)
-- sub(a, b)
-- div(a, b)

- Använd felhantering:
Hantera om användaren skriver text istället för tal (ValueError)
Hantera division med noll (ZeroDivisionError)

- Programmet ska:
-- Be användaren välja operation (+, -, /)
-- Be om två tal
-- Skriva ut resultatet

### Extra 
- Använd else för att skriva ut resultat om inget fel uppstår

### Info: 
- https://www.geeksforgeeks.org/python/python-print-exception/

---- 
## Krav:
Extra:
Uppgift 2 – Användarhantering (funktion + raise)
Du ska skapa ett system som kontrollerar användardata.
- 
Skapa en funktion:
def skapa_anvandare(namn, alder):
Funktion ska:
Kontrollera att ålder inte är negativ
Om negativ → kasta eget fel med raise ValueError
Returnera en text som beskriver användaren
Huvudprogram:
Fråga efter namn och ålder
Använd try-except för att fånga fel
Extra:
Uppgift 3 – Menyprogram med funktioner (större uppgift)
Bygg ett program med en meny där användaren kan välja olika funktioner.
Funktioner som ska finnas:
Programmet ska:
Felhantering:
Skriv ut tydliga felmeddelanden
Lägg till en docstring i funktionen
summa_lista(lista)
medelvarde(lista)
max_varde(lista)
1. Be användaren skriva in flera tal (t.ex. separerade med komma)
2. Omvandla input till lista
3. Visa meny:
1. Summa
2. Medelvärde
3. Max
4. Anropa rätt funktion beroende på val
Fel input (text istället för tal)
Tom lista
Fel menyval