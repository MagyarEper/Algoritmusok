# Megoldás


### Használt algoritmus:
    SRekurzió és memorizáció
    

### Megoldás menete:
    A bázisesetek:
        -Ha az aktuális részösszeg 0, akkor elértük a cél súlyt így nincs szükség további tárgyra. 
        -Ha az aktuális részösszeg negtív, vagy az index meghaladja a tömb hosszát akkor a visszatérési érték float('inf')

    Memorizáció:
        -Minden (index, jelenlegi) kombinációt eltároljuk egy memo nevű szótárban.

    Rekurzív elágazások:
        -Ha a jelenlegi nagyobb vagy egynő az aktuális tárgy súlyával, akkor meghívjuk a függvényt a következő indexre.
        -Kihagyjuk a tárgyat, vagyis meghívjuk a függvényt a következő indexre ajelenlegi érték módosítása nélkül.

    Eredmény kiszámítása:
        -A tárgy súlyának figyelembevételével és anélkül kapott eredmények közül a kisebbiket választjuk.

    Eredmény visszaadása:
        -A meghívásból kapott eredmény értékét ellenőrizzük, amennyiben nem float('inf'), akkor visszaadjuk az eredményt.


### Bonyolultság:
    A sima rekurzív algoritmus O(2^n) komplexitású, de ez jelentősen csökken a memorizációval, így O(n*k) lesz a komplexitás.