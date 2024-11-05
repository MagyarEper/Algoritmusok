# Megoldás

### Használt algoritmus:
Mohó algoritmus

### Megoldás menete:
első lépésként a házakat növekvő sorrendbe rendezzük.

ezután inicializáljuk a szükséges változókat:
        minimum -> az aktuálisan lefedett tartomány kezdőháza
        antennak -> az eddig elhelyezett antennák száma
        kozep -> a ház ahova az antennát célszerű rakni a legnagyobb lefedettség érdekében

Az adók elhelyezése:
    Egy for ciklussal végigiterálunk a rendezett házak listáján
    Ellenőrizzük hogy az adott ház k egységen belül van-e
    Ha igen, akkor a közép értéket frissítsük
    Ha egy ház tartományon kívül van, új adót telepítünk és a minimum értékét frissítsük

Az adók számával térünk vissza.

### Magyarázat:
Az algoritmus azért mohó, mert minden adót a lehető legtávolabb helyezünk el egymástól, így biztosítva hogy a legkisebb számú antennával a legnagyobb lefedettséget érjük el.

### Bonyolultság:
A rendezés a python beépített sorted() funkciójával O(n log n) időt igényel, míg az antennák pozíciójának meghatározása O(n), így a teljes algoritmus O(n log n) időt vesz igénybe.