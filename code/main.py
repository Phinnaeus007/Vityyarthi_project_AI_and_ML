# Student Score Predictor using Kaggle Dataset (StudentsPerformance.csv)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Load Dataset
# -----------------------------
df = pd.read_csv(r"dataset\StudentsPerformance.csv")

# -----------------------------
# Step 2: Feature Engineering
# -----------------------------
df["Study Hours"] = df["math score"] / 10
df["Sleep Hours"] = 6 + (df["reading score"] % 3)
df["Attendance"] = 60 + (df["writing score"] % 40)
df["Previous Score"] = df["reading score"]

df["Final Score"] = df["math score"]

df = df[["Study Hours", "Sleep Hours", "Attendance", "Previous Score", "Final Score"]]

# -----------------------------
# Step 3: Split Data
# -----------------------------
X = df.drop("Final Score", axis=1)
y = df["Final Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Step 4: Train Model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# Step 5: Predict & Evaluate
# -----------------------------
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", round(mae, 2))

# -----------------------------
# Step 6: Feature Importance
# -----------------------------
print("\nFeature Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.2f}")

# -----------------------------
# Step 7: Graph
# -----------------------------
plt.scatter(y_test, predictions)
plt.xlabel("Actual Scores")
plt.ylabel("Predicted Scores")
plt.title("Actual vs Predicted Scores")
plt.show()

# -----------------------------
# Step 8: User Input Prediction
# -----------------------------
print("\nEnter values to predict final score:")

study = float(input("Study Hours: "))
sleep = float(input("Sleep Hours: "))
attendance = float(input("Attendance (%): "))
previous = float(input("Previous Score: "))

user_data = pd.DataFrame(
    [[study, sleep, attendance, previous]],
    columns=["Study Hours", "Sleep Hours", "Attendance", "Previous Score"]
)

result = model.predict(user_data)

# Clamp output between 0 and 100
final_score = max(0, min(100, result[0]))

print("Predicted Final Score:", round(final_score, 2))