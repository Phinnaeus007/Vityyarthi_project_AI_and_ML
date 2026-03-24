# Student Score Predictor (AI/ML Project)

## Overview
This project uses Linear Regression to predict a student's final exam score based on factors such as study hours, sleep hours, attendance, and previous performance. The model is trained using a real-world dataset and demonstrates a complete machine learning pipeline from data processing to prediction.

---

## Features
- Uses a real dataset (StudentsPerformance.csv)
- Applies feature engineering to create meaningful inputs
- Trains a Linear Regression model
- Evaluates model using Mean Absolute Error (MAE)
- Displays feature importance
- Visualizes actual vs predicted scores
- Accepts user input for live prediction

---

## Dataset
The dataset used is **Students Performance in Exams** from Kaggle.

Original columns:
- math score
- reading score
- writing score

Engineered features:
- Study Hours
- Sleep Hours
- Attendance
- Previous Score
- Final Score (target)

---

## How It Works
1. Load dataset  
2. Create new features  
3. Split data into training and testing sets  
4. Train Linear Regression model  
5. Evaluate model performance  
6. Display graph  
7. Take user input and predict score  

---

## How to Run

### 1. Install dependencies
```
pip install pandas scikit-learn matplotlib
```

### 2. Place dataset
Make sure `StudentsPerformance.csv` is in the same folder as `main.py`

### 3. Run program
```
python main.py
```

### 4. Important Step
After running the program, a graph will appear.  
**You must close the graph window first**, then the program will allow you to enter input values in the terminal.

### 5. Enter inputs
Example:
```
Study Hours: 5
Sleep Hours: 7
Attendance (%): 80
Previous Score: 75
```

---

## Output
- Model accuracy (MAE)
- Feature coefficients
- Graph of actual vs predicted values
- Predicted final score (0–100 range)

---

## Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  

---

## Conclusion
This project demonstrates how machine learning can be used to analyze student performance and make predictions based on multiple factors. It highlights the importance of data preprocessing, model training, and real-world application through user input.
