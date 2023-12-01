import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Loading dataset
df = pd.read_csv("diabetes.csv")

# Array of names of features
feature_columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

# Rows of features
X = df[feature_columns]

# Rows of outcomes
y = df.Outcome

# Splitting data into training and testing categories
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

# Decision tree classifier object
classifier = DecisionTreeClassifier(criterion="entropy", max_depth=3)

# Fitting the classifier object with training data
classifier = classifier.fit(X_train, y_train)

# Making a prediction based on features of testing data and calculating the accuracy score
y_prediction = classifier.predict(X_test)
prediction_accuracy = round(metrics.accuracy_score(y_test, y_prediction), 2)

print("Prediction accuracy: " + str(prediction_accuracy))
