## 1

- Villkor(if) - I funktionen hamta_servrar() i filen lagring.py använder jag ett if vilkor som kontrollerar om JSON filen finns. Om vilkoret är sant så kommer koden efter if köras, om filen finns läser programmet in informationen och om den inte finns så returneras en tom lista. Detta är så att programmet kan starta även om datafilen saknas och inte bara krascha direkt

- Loop(for) - I kontroller.py har jag en for-loop under funktionen kontrollera_alla_servrar() för att kunna gå igenom alla servrar som finns med i listan. Denna funkar så att den går igenom varje server i listan en i taget och kontrollerar de en i taget för att se om de är tillängliga, detta gör att man slipper skriva samma kod flera gånger.

- Funktion med parameter och return - hamta_servrar(datafil) i lagring.py tar emot parametern datafil som anger vilken fil programmet ska läsa. Parametern gör att funktionen kan användas med flera olika filnamn och när informationen har lästs in så använder den terutn för att sen skicka tillbaka serverinformationen som en lista, genom detta kan andra delar av programmet använda informationen.

## 2

Har valt lagra serverna med dictionaries i en lista då programmet måste kunna hantera flera servrar samtidigt. Detta upplägget gör det lätt att lägga till, ta bort samt gå igenom servrarna och varje server är indelad i sina egna dictionaries där informationen är uppdelad med olika nycklar som t.ex namn, adress, miljö osv. värdena i servrarna använder sig av datatypen string

## 3 

Använder JSON för att lagra servernas information eftersom det passar bra för strukturerad data. Varje server innehåller flera värden som namn, adress, miljö, status och i filen lagring.py använder jag mig av funktionerna hamta_servrar() och spara_servrar() för att spara informationen så att det fortfarande finns kvar när programmet avslutas. I funktionen exportera_csv() i lagring.py skapas en CSV-fil med information om alla servrar, och använder mig av detta för det är enkelare att kunna öppna, läsa och dela rapporter med detta

## 4 

Programmet är uppdelat i main.py, meny.py, lagring.py och kontroller.py där varje fil ska ha sitt eget ansvarsområde så att koden ska kunna vara enklare att förstå och navigera sig då de olika funktionerna inte ska behöva blandes ihop emellan alla olika filer. Detta gör då också att det är lättare att hitta fel samt lägga till och ändra kod
- `main.py` - Startar programmet och hanterar kommandoradsargument genom argparse 
- `meny.py` – Hanterar den interaktiva menyn och funktioner för att visa, lägga till, ta bort och filtrera servrarna
- `lagring.py` – Hanterar inläsning och sparning av JSON samt export till CSV
- `kontroller.py` – Kontrollerar om servrar är tillgängliga med ping

## 5

- `json` – Används i `lagring.py` för att läsa och spara serverinformationen
- `os` – Används i `lagring.py` för att hämta miljövariabeln `INVENTORY_DATAFIL`
- `csv` – Används i `lagring.py` för att exportera serverinformationen till CSV-rapporter
- `pathlib` – Används i `lagring.py` för att hantera filsökvägar och skapa kataloger
- `datetime` – Används i `lagring.py` och `kontroller.py` för att hämta datum och tid
- `subprocess` – Används i `kontroller.py` för att köra ping och kontrollera om servrar är tillgängliga.
- `argparse` – Används i `main.py` för att hantera kommandoradsargument, exempelvis `--lista` och `--export`
- `sys` – Används i `main.py` för att avsluta programmet med olika avslutningskoder

## 6 

1. Koden är uppdelad i olika filer med sina egna ansvarsområden för att lättare kunna läsa, hitta och ändra i koden

2. I meny.py under funktionen lagg_till_servrar() kontrollerar jag att användarens inmatning, att t.ex miljön är giltig, att samma namn inte redan finns och detta förhindrar felaktig information eller dubbla servrar. 

3. I kontroller.py använder jag mig av try och except för att hantera att ping kommndo inte ska ta för lång tid, där jag har gett den en tidsgräns på 5 sekunder. Detta gör då att programmet inte ska fastna om en server inte ger svar. 

## 7

- Presentationerna publicerade i learnpoint när jag inte vetat   t.ex exakt vilken funktion jag ville använda

- Har använt mig av min bror vad det gäller struktur och när jag åkt lite fast då han hjälper mig alltid så lite som de krävs och tvingar mig hitta svaren själv så att det fortfarande jag som gör det och samtidigt lär mig

- AI mestadels när det gäller felmeddelande som att jag kanske råkat sätta en funktion inuti en annan och använt den som hjälp att avstämma så att jag upfyller krav