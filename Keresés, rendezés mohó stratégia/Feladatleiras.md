# Feladatleírás:

Hackerland egy egydimenziós város, ahol a házak egész számokkal jelölt helyeken helyezkednek el az út mentén. A polgármester rádióadók telepítését tervezi a város házainak tetejére. Minden adónak van egy fix hatótávolsága, ami azt jelenti, hogy jelet tud sugározni minden ház felé, amelyik ezen a meghatározott távolságon belül található.

Adott Hackerland térképe és az adók hatótávolsága. Határozd meg a minimális adók számát, hogy minden ház legalább egy adó hatókörén belül legyen. Minden adót egy létező ház tetejére kell telepíteni.

## Példa:

x = [1,2,3,4,5,9]
k = 1

Az adók a 2, 5, 9 házaknál találhatók, és teljes lefedettséget biztosítanak. Nincs ház a 7. helyen, hogy 5-t és 9-t is lefedje. A lefedett tartományok: [1,2,3], [5], és [9] .