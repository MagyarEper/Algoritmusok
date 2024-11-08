link : [text](https://www.hackerrank.com/challenges/rust-murderer/problem?isFullScreen=true)
# Feladatleírás:

    A feladatban egy gyilkost keresünk, akiről tudott hogy a meneküléshez mellékutakat használt, de a térképünkön csupán a főutak vannak jelölve.

    A feladatban egy gráfot kapunk, ami N csúcsból áll (1 től N-ig) valamint egy S csúcsot ami a detektív kezdő pozícióját jelöli.
    Megkapjuk még a főutak listáját is, ezeken kívül minden él mellékút.

    Az lesz a feladat hogy a kezdőpozíciótól minden lehetséges csúcsba el kell jutnunk és megnézni hogy milyen távolságra vannak ha csak mellékutatkat használunk.

## Példa:

főutak = [[1,2], [1,4], [2,3]]
kezdőpont = 1

A 2-es pontba úgy jutunk el hogy 1->3->4->2 ezért a távolság 3
A 3-mas pontba 1->3 tehát a távolság 1
A 4-es pontba pedig 1->3->4 ,így a távolság 2