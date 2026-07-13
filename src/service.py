import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI(title="Credit Scoring API", version="1.0")

# Загружаем модель и скейлер при старте
try:
    model = joblib.load("models/model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    logging.info("Модель и скейлер успешно загружены")
except Exception as e:
    logging.error(f"Ошибка загрузки модели: {e}")
    raise e

class ClientData(BaseModel):
    age: int
    income: float
    education: bool
    work: bool
    car: bool

@app.get("/health")
def health_check():
    return {"status": "ok", "model_loaded": True}

@app.post("/score")
def score(data: ClientData):
    try:
        # Преобразуем bool в int для корректной работы с массивом
        features = [[data.age, data.income, int(data.education), int(data.work), int(data.car)]]
        
        # ВАЖНО: масштабируем входные данные так же, как при обучении!
        features_scaled = scaler.transform(features)
        
        # model.predict возвращает 1 (дефолт) или 0 (нет дефолта). 
        # Нам нужно approved = True, если дефолта НЕТ (предсказание == 0)
        is_default = bool(model.predict(features_scaled)[0])
        approved = not is_default
        
        logging.info(f"Запрос: {data.dict()} | Результат: {'Approved' if approved else 'Rejected'}")
        return {"approved": approved, "risk_level": "high" if not approved else "low"}
    except Exception as e:
        logging.error(f"Ошибка предсказания: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")