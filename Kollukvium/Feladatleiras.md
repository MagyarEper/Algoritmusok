[text](https://www.spoj.com/problems/PIGBANK/)

# Feladatleírás:

Adott egy malacpersely, amelynek súlya üresen EE gramm, és feltöltve FF gramm. Ismerjük a rendelkezésre álló pénzérmék különböző típusait, ahol minden érme két értékkel rendelkezik:

    PP: az érme értéke pénzegységben,
    WW: az érme súlya grammban.

A cél az, hogy megtudjuk, mi a lehető legkisebb összeg, ami a malacperselyben lehet, ha pontosan F−EF−E gramm súlyú érmékkel érjük el a kitöltött állapotot.

### Bemenet:

    TT: tesztesetek száma.
    Minden tesztesetben:
        E,FE,F: a malacpersely üres és tele súlya.
        NN: az érmetípusok száma.
        NN sor, ahol minden sor PP-t és WW-t tartalmaz.

### Kimenet:

    Ha a cél súly elérhető az érmékkel:
    The minimum amount of money in the piggy-bank is "X".
    Ha a cél súly nem érhető el:
    This is impossible.