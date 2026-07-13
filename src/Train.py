"""
Credit Scoring ML Pipeline
Dataset: Inspired by real-world credit scoring data (T-Bank structure)
Author: Mikhail Demashov
Description: Training pipeline for credit default prediction with class balancing and feature scaling.
"""
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, recall_score, classification_report

# 1. Генерация данных, если файла нет (чтобы проект запускался у любого с нуля)
try:
    data = pd.read_csv("data/scoring.csv")
except FileNotFoundError:
    print("[INFO] Файл не найден. Генерирую синтетические данные...")
    np.random.seed(42)
    n = 1000
    data = pd.DataFrame({
        "age": np.random.randint(18, 70, n),
        "income": np.random.randint(20, 300, n),
        "education": np.random.choice([0, 1], n),
        "work": np.random.choice([0, 1], n, p=[0.1, 0.9]),
        "car": np.random.choice([0, 1], n, p=[0.4, 0.6]),
        "default": np.random.choice([0, 1], n, p=[0.8, 0.2]) # 20% дефолтов
    })
    import os
    os.makedirs("data", exist_ok=True)
    data.to_csv("data/scoring.csv", index=False)

X = data.drop(columns=["default"])
y = data["default"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. ВАЖНО: Масштабирование
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Обучение
model = LogisticRegression(class_weight="balanced", random_state=42)
model.fit(X_train_scaled, y_train)

# 4. Сохраняем И модель, И скейлер!
joblib.dump(model, "models/model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

# 5. Оценка
y_pred = model.predict(X_test_scaled)
print("\n--- Метрики модели ---")
print(f"Точность (Precision): {precision_score(y_test, y_pred):.3f}")
print(f"Полнота (Recall): {recall_score(y_test, y_pred):.3f}")
print(classification_report(y_test, y_pred))