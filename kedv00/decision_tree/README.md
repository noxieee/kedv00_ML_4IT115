# Decision tree - Rozhodování, zda má pacient cukrovku

Rozhodovací strom je bezparametrický model, který na základě příznaků predikuje výsledek. Na vrchu se nachází kořenový list,
ze kterého algoritmus pokračuje do dalších rozhodovacích listů. Algoritmus na základě trénovacích dat odvodí
optimální místa pro dělení listů. Tento proces je rekurzivní dokud většina záznamů není rozdělena do homogenních skupin.

Dataset obsahuje údaje o pacientech (Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age), 
model na základě těchto dat predikuje, zda má pacient cukrovku, či nikoli (Outcome - 1 nebo 0).

Dataset byl rozdělen na trénovací a testovací v poměru 25:75. Po natrénování byla vypočtena přesnost predikce na testovacích datech.

## Použité knihovny
* Pandas
* scikit-learn

## Použitý dataset
* https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

## Výsledky

Model na testovacích datech dokázál rozhodnout s přesností 78%.

Bohužel se mi nepovedlo zprovoznit knihovny pro vizualizaci rozhodovacího stromu :(.

## Výstup scriptu

Prediction accuracy: 0.78 %

## Zdroje
https://www.ibm.com/topics/decision-trees
https://scikit-learn.org/stable/modules/tree.html