import pandas as pd
from sklearn import linear_model

# Testing data columns: number_courses,time_study,Marks
df = pd.read_csv("Student_Marks_Training.csv")

# Independent variables
X = df[['number_courses', 'time_study']]

# Dependent variables
y = df['Marks']

# ====== Training ==============================================
print("======== TRAINING ========")
regr = linear_model.LinearRegression()
regr = regr.fit(X.values, y)

# Coefficient of determination
r_sq = round(regr.score(X.values, y), 2)
print("Coefficient of determination: " + str(r_sq))

# Over fitted, under fitted, well fitted
if r_sq < 0.6:
    print("-> Under fitted.")
elif r_sq > 0.9:
    print("-> Over fitted.")
else:
    print("-> Well fitted.")

# ====== Testing predictions ===================================
print("\n======== TESTING PREDICTIONS ========")

# Testing data
testing_data = pd.read_csv("Student_Marks_Testing.csv")

# For row in testing data, make prediction of marks and compare it to the actual value
for i, row in testing_data.iterrows():
    number_courses = row['number_courses']
    time_study = row['time_study']
    actual_marks = row['Marks']

    predicted_marks = regr.predict([[number_courses, time_study]])

    print("Predicted mark: " + str(round(predicted_marks[0], 3)) + " --- " + "Actual mark: " + str(actual_marks) + "\n")
