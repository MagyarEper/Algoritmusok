# Megoldás

### Használt algoritmus:
Dinamikus programozás

### Megoldás menete:
1.Dinamikus programozás használata:
    Készítünk egy dpdp tömböt, ahol dp[w]dp[w] azt jelenti, hogy ww gramm súlyt a lehető legkisebb összeggel hogyan tudjuk elérni.

    Az elején minden dpdp értéket "végtelennek" veszünk, kivéve dp[0]dp[0]-t, ami 00 (nulla súlyhoz nulla összeg kell).

2.Érmékkel való frissítés:
    Végignézzük az összes érmét, és megnézzük, hogy ha egy adott súlyt már elértünk, akkor onnan mennyi lenne az érték, ha hozzáadnánk az aktuális érme súlyát és értékét.

    Ha ezzel kisebb összértéket kapunk, akkor frissítjük a dpdp-t.

3.Prioritási sor (min-heap):

    Ahelyett, hogy sorban végigmennénk a súlyokon, a prioritási sort használjuk, hogy mindig a legkisebb összeggel elérhető súlyt dolgozzuk fel először.
    Ez segít, hogy ne pazaroljunk időt olyan súlyokra, amiket később úgyis jobb értékkel érünk el.

4.Eredmény meghatározása:

    Ha dp[F−E]dp[F−E] végtelen maradt, akkor nincs megoldás, azaz a cél súly nem érhető el.
    Egyébként a dp[F−E]dp[F−E] érték a megoldás, ami a minimális összeg.

### Bonyolultság:
   Mivel a prioritási sor műveletei gyorsak (log⁡WlogW, ahol WW a cél súly), ezért a teljes idő nagyjából 
   O(Wlog⁡W)O(WlogW).