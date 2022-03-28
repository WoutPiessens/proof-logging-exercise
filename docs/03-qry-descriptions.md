## 3.0 Afspraken geldig voor alle vragen

**Beschrijving**

1. Gebruik voor statistieken altijd de informatie tijdens het (volledige) seizoen, dus zonder mogelijke post-season matches.

2. Gebruik bij vragen rond numerieke waarden (bv. jaar, gewicht) uitsluitend informatie met waarden die (op zich gezien, zonder rekening te houden met onderlinge verbanden) plausibel zijn in de context van een sport die pas sinds de 18de eeuw bestaat. Bv.: birthDay=31 is plausibel (onafhankelijk van birthMonth), birthDay=42 is dat niet; birthYear=1847 is plausibel, birthYear=1066 is dat niet; weight=250 (in pond) is plausibel, weight=10 is dat niet.

3. Resultaten mogen geen duplicaten bevatten.

## 3.1 Query 01

**Beschrijving**

Voor elke speler, voor elke keer dat deze speler meer dan X stemmen heeft ontvangen voor de hall of fame, geef: de voornaam en de achternaam van de speler, het jaar en het aantal stemmen.

Sorteer achtereenvolgens alfabetisch oplopend op voornaam en achternaam, dan oplopend op jaar en dan aflopend op het aantal stemmen.

## 3.2 Query 02

**Beschrijving**

Geef de geboortestad, achternaam en voornaam van iedereen die in deelstaat X is geboren, als manager heeft gewerkt en bij de Allstars is verschenen.
 
Sorteer achtereenvolgens alfabetisch oplopend op geboortestad, achternaam en voornaam.

## 3.3 Query 03

**Beschrijving**

Maak een lijst van teams en hun managers die in de jaren N tot en met M in league X division Y de eerste plaats hebben behaald.

De lijst bevat voor elk van die teams, voor elke manager van het team in dat jaar: het jaar, de naam van het team, het nummer van de manager binnen dit team in dit jaar, de achternaam van de manager, de voornaam van de manager, het percentage gewonnen matches van het team en het percentage gewonnen matches van die manager.

Sorteer achtereenvolgens oplopend op jaar, naam van het team en nummer van de manager.


## 3.4 Query 04

**Beschrijving**

Maak een lijst van alle spelers die voldoen aan deze drie voorwaarden:

- De speler was na jaar Y nog actief als pitcher,

- de speler heeft tijdens zijn matches als pitcher in totaal meer verloren dan gewonnen, en 

- de speler had  tijdens zijn matches als pitcher in totaal in meer dan X percent van zijn hits een homerun.

De lijst bevat achternaam, voornaam en geboortejaar van deze spelers.

Sorteer achtereenvolgens alfabetisch oplopend op achternaam en voornaam, dan oplopend op geboortejaar.


## 3.5 Query 05

**Beschrijving**

Maak een lijst van alle spelers die minder dan "X" jaar voor het jaar dat ze stierven nog minstens één keer meer dan "Y" stemmen kregen voor de Hall of Fame, en die  in dezelfde maand van het jaar geboren werden en stierven. 

Geef voor elke speler het hoogste aantal stemmen in die periode, het geboortejaar, het sterfjaar, en voor- en achternaam.

Sorteer achtereenvolgens aflopend op aantal stemmen, oplopend op geboortejaar en sterfjaar, dan  alfabetisch op voornaam en achternaam.


## 3.6 Query 06

**Beschrijving**

Maak een lijst van iedereen die

- als manager in totaal meer dan "X" games en meer dan "Y" wins heeft, en

- meer dan "Z" jaar voor de eerste match als manager zijn laatste match als pitcher speelde.

De lijst bevat voornaam en achternaam, het totaal aantal games als manager en het totaal aantal wins als manager.

Sorteer achtereenvolgens alfabetisch oplopend op voornaam en achternaam, dan telkens aflopend op aantal games en aantal wins.


## 3.7 Query 07

**Beschrijving**

Maak een lijst met de voornaam, achternaam en grootte van alle spelers die bij  minstens twee verschillende teams pitcher waren en tijdens hun laatste jaar als pitcher (1) bij maar één team hebben gespeeld, (2) een award (als speler) hebben gewonnen, en (3)  minstens "X" inches kleiner waren dan de (op dat moment) grootste pitcher in hun team.

Sorteer alfabetisch oplopend op voornaam en achternaam, dan oplopend op grootte.



## 3.8 Query 08

**Beschrijving**

Maak een lijst van spelers die minstens N Allstar matches hebben gespeeld voor hetzelfde team. De lijst bevat:

- achternaam en voornaam van de speler

- de meest recente naam van het team

- het aantal Allstar matches dat de speler bij het team heeft gespeeld, het jaar van het eerste van die matches, en het jaar van het laatste van die matches

- het aantal speler-prijzen gewonnen door die speler, het jaar van de eerste prijs en het jaar van de laatste prijs (indien van toepassing)

Sorteer achtereenvolgens alfabetisch oplopend op voornaam en achternaam, dan aflopend op aantal games, dan alfabetisch oplopend op team naam.
