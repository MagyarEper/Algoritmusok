# Megoldás


### Használt algoritmus:
    Dinamikus programozás


### Megoldás menete:
    Inicializálunk egy segédtömböt, amely minden értékhez (1 től k-ig) eltárolja a maximális elérhető súlyt.
    
    Ezután végigiterálunk 1 től k-ig, és minden elemet megvizsgálunk az inputként kapott tömbben.
    Ha a vizsgált érték kissebb vagy egyenlő az iterálás jelenlegi indexével, akkor a segédtömbb azon elemét beállítjuk a  max(dp[j], weight + dp[j - weight]) -re.

    végül visszaadjuk a segédtömbb[k] -t.

## Plusz:
    A tesztelő részt át kellett variálni, mert inputként több tesztesetet kapunk, de az eredetileg megírt csak az elsőt veszi figyelembe. A teszt résznél for cilkusba kellett raknom a kódot, hogy minden teszt esetet rendeltetés szerűen beolvasson.

### Bonyolultság:
    A megoldás időkomplexitása O(k*n) mivel a külső cikluson k-szor haladunk végig, a belsőn pedig n-szer.