# Megoldás


### Használt algoritmus:
    Szélességi keresés
    

### Megoldás menete:
    Először létrehozunk egy listát, amelyben felvesszük minden csúcs közvetlen szomszédját.
    Inicializálunk egy listát a távolságoknak, a kezdőpont távolságát 0-ra állítva.
    Ezután Szélességi keresést alkalmazunk egy sor(queue) segítségével, azokra az utakra amelyek nincsenek benne a paraméterül kapott listában.

    Végül visszaadjunk a távolság lista nem 0 elemeit.


### Bonyolultság:
    A megoldás időkomlexitása O(m+n^2) 