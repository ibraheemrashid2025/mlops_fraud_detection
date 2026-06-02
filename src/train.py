import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import mlflow
import mlflow.sklearn
import os

# 1. Dataset Load Karna
print("Data load ho raha hai (Credit Card Fraud Dataset)...")
data_path = os.path.join("data", "creditcard.csv")
df = pd.read_csv(data_path)

# 2. Data Preprocessing (Features aur Target alag karna)
# 'Class' column humara target hai (0 = Normal, 1 = Fraud)
X = df.drop('Class', axis=1)
y = df['Class']

# Data ko train aur test mein split karna (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3. MLflow Setup
mlflow.set_experiment("Fraud_Detection_Experiment")

with mlflow.start_run():
    print("Model train ho raha hai (Is mein 1-2 minute lag sakte hain kyunke data bara hai)...")
    
    # Model ke Hyperparameters
    n_estimators = 100
    max_depth = 10
    
    # Random Forest Model Initialize aur Train karna
    # 'class_weight=balanced' bohat zaroori hai kyunke fraud transactions bohat kam hain
    rf_model = RandomForestClassifier(
        n_estimators=n_estimators, 
        max_depth=max_depth, 
        class_weight='balanced', 
        random_state=42,
        n_jobs=-1  # Faster training ke liye saare CPU cores use karna
    )
    rf_model.fit(X_train, y_train)
    
    # 4. Predictions aur Evaluation
    print("Model evaluate ho raha hai...")
    y_pred = rf_model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    print(f"\n--- Results ---")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")
    
    # 5. MLflow mein Metrics aur Model Log (Save) Karna
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1_score", f1)
    
    # Model ko registry ke liye save karna
    mlflow.sklearn.log_model(rf_model, "random_forest_model")
    
    print("\nTraining Complete! Model aur metrics MLflow mein save ho gaye hain.")