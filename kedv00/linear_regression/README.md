# Regresní analýza - Predikce známek studenta
Model používá vícenásobnou lineární regresní analýzu, tj. na základě dvou nezávislých proměnných aproximuje jednu závislou proměnnou. Regresní funkce v tomto případě reprezentuje rovinu ve 3D prostoru.

Model predikuje známky studentů na základě toho, kolik mají zapsaných kurzů a kolik času věnují studiu.

Data jsou rozdělena na trénovací a testovací. Po natrénování modelu jsou predikce porovnávány s hodnotami v testovacích datech.

## Použité knihovny
* Pandas
* scikit-learn

## Použitý dataset
* https://www.kaggle.com/datasets/yasserh/student-marks-dataset

## Výsledky
Model má vysoký koeficient determinace (0.93), ten značí, že model je přetrénován, tj. regresní funkce až příliš přesně pasuje na trénovací data. Model může mít problém s predikcí na nových datech.

Model predikuje přesně na testovacích datech, nicméně v jednom případě byla odhadnutá známka studenta záporná (Predicted mark: -0.827 --- Actual mark: 5.609). To může být způsobeno přetrénováním modelu.

Zmenšení objemu testovacích dat nemělo vliv na koeficient determinace.

## Výstup scriptu

======== TRAINING ========

Coefficient of determination: 0.93

-> Over fitted.

======== TESTING PREDICTIONS ========

Predicted mark: 47.918 --- Actual mark: 51.343

Predicted mark: 5.578 --- Actual mark: 10.522

Predicted mark: 12.726 --- Actual mark: 10.844

Predicted mark: 23.04 --- Actual mark: 19.59

Predicted mark: 23.869 --- Actual mark: 21.379

Predicted mark: 6.247 --- Actual mark: 12.591

Predicted mark: 15.125 --- Actual mark: 13.562

Predicted mark: 29.134 --- Actual mark: 27.569

Predicted mark: 0.519 --- Actual mark: 6.185

Predicted mark: 7.087 --- Actual mark: 8.92

Predicted mark: 24.889 --- Actual mark: 21.4

Predicted mark: 19.743 --- Actual mark: 16.606

Predicted mark: 15.158 --- Actual mark: 13.416

Predicted mark: 22.593 --- Actual mark: 20.398

Predicted mark: 6.353 --- Actual mark: 7.014

Predicted mark: 37.14 --- Actual mark: 39.952

Predicted mark: 1.887 --- Actual mark: 6.217

Predicted mark: 36.032 --- Actual mark: 36.746

Predicted mark: 39.9 --- Actual mark: 38.278

Predicted mark: 45.826 --- Actual mark: 49.544

Predicted mark: 1.898 --- Actual mark: 6.349

Predicted mark: 48.562 --- Actual mark: 54.321

Predicted mark: 19.773 --- Actual mark: 17.705

Predicted mark: 39.606 --- Actual mark: 44.099

Predicted mark: 18.829 --- Actual mark: 16.106

Predicted mark: 18.259 --- Actual mark: 16.461

Predicted mark: 41.068 --- Actual mark: 39.957

Predicted mark: 27.532 --- Actual mark: 23.149

Predicted mark: 3.131 --- Actual mark: 6.053

Predicted mark: 11.293 --- Actual mark: 11.253

Predicted mark: 40.015 --- Actual mark: 40.024

Predicted mark: 28.153 --- Actual mark: 24.394

Predicted mark: 22.303 --- Actual mark: 19.564

Predicted mark: 26.723 --- Actual mark: 23.916

Predicted mark: 42.528 --- Actual mark: 42.426

Predicted mark: 28.731 --- Actual mark: 24.451

Predicted mark: 22.796 --- Actual mark: 19.128

Predicted mark: -0.827 --- Actual mark: 5.609

Predicted mark: 38.27 --- Actual mark: 41.444

Predicted mark: 7.215 --- Actual mark: 12.027

Predicted mark: 39.783 --- Actual mark: 40.602

Predicted mark: 25.873 --- Actual mark: 22.184

Predicted mark: 3.714 --- Actual mark: 7.892

Predicted mark: 38.247 --- Actual mark: 36.653

Predicted mark: 48.583 --- Actual mark: 53.158

Predicted mark: 21.293 --- Actual mark: 18.238

Predicted mark: 48.853 --- Actual mark: 53.359

Predicted mark: 46.897 --- Actual mark: 51.583

Predicted mark: 31.054 --- Actual mark: 31.236

Predicted mark: 31.794 --- Actual mark: 32.357

## Zdroje
* https://realpython.com/linear-regression-in-python/#multiple-linear-regression
* https://medium.com/geekculture/simple-linear-regression-analysis-using-python-c5b2f637942
* https://www.w3schools.com/python/python_ml_multiple_regression.asp