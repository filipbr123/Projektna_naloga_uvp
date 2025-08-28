# Analiza smučišč v Alpah

## Cilj projekta
Cilj projektne naloge je zajem in analiza podatkov o alpskih smučiščih iz spletne strani https://www.skiresort.info/ski-resorts/alps/.
Javna spletna stran https://www.skiresort.info/ski-resorts/ je ena najboljših strani za iskanje smučišč po svetu. 
Osredotočil sem se le na smučišča v gorovju Alpe, da bo analiza bolj natančna in poglobljena. 
Smučišča v Alpah so Slovencem najblžja in najbolj priljubljena izbira za smučarske izlete.

## Struktura projekta
<pre>
Projektna_naloga_uvp/
├── Podatki/
│   └── vsi_podatki.csv
├── Zajem_podatkov/
│   └── podatki.py
├── analiza.ipynb
├── main.py
├── .gitignore
└── README.md
</pre>

V mapi Podatki je csv datoteka podatkov, ki smo jih zajeli.    
V mapi Zajem_podatkov je python datoteka podatki.py, ki zajame želene podatke iz spletne strani in ustvari zgoraj omenjeno csv datoteko.    
Analiza podatkov je narejena v datoteki analiza.ipynb.    
Z main.py zaženenemo programe iz podatki.py.    
V README.md je kratka predstavitev projektne naloge.

## Struktura analize

Analiza podatkov je razčlenjena na 5 poglavij:
- Povprečja pomembnih podatkov
- Velikost smučišč
- Težavnost smučišč
- Izkoristek žičnic
- Cena

## Knjižnice

Za zagon programa so potrebne naslednje knjižnice:
- requests,
- re,
- pandas,
- numpy,
- matplotlib.pyplot

## Uporaba

Če imamo potrebne knjižnice naložene, samo poženemo main.py, ki bo ustvarila csv datoteko s podatki, nato odpremo še analiza.ipynb.
