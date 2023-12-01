# KNN
K nearest neighbors algoritmus klasifikuje nové hodnoty podle kategorií K nejbližších sousedů.
Pro určení vzdálenosti k sousedům je použita Euklidovská vzdálenost. Kategorie je přiřazena na základě "hlasu většiny",
 tj. podle toho, jaká kategorie se v okolí vyskytuje nejčastěji.

Můj model předpokládá 2 vlastnosti (souřadnice), 3 kategorie a porovnává úspěšnosti pro KNN = 5 a KNN = 1 a výsledky vizualizuje.

## Použité knihovny

* scikit-learn
* Matplotlib

## Výsledky

Přesnost predikce pro KNN = 5 je 0.74, pro KNN = 1 je 0.65.
KNN = 5 přinášelo nejpřesnější predikce. Výsledky predikcí pro obě KNN jsou uloženy v png v této složce.

## Výstup scriptu

Prediction accuracy knn=5: 0.74

Prediction accuracy knn=1: 0.65

## Zdroje

https://www.ibm.com/topics/knn

https://www.datacamp.com/tutorial/k-nearest-neighbor-classification-scikit-learn

https://scikit-learn.org/stable/modules/neighbors.html
