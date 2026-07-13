# 💳 AI Credit Scoring System

End-to-End машинное обучение пайплайн для скоринга кредитных заявок. Проект демонстрирует полный цикл разработки ML-продукта: от обучения модели до деплоя через FastAPI и создания пользовательского интерфейса на Streamlit.

## 🏗 Архитектура
1. **ML Pipeline (`src/train.py`)**: Обучение Logistic Regression с балансировкой классов и обязательным масштабированием признаков (`StandardScaler`).
2. **API Service (`src/service.py`)**: FastAPI микросервис для инференса модели с валидацией данных через Pydantic и логированием запросов.
3. **Frontend (`app.py`)**: Интерактивный веб-интерфейс на Streamlit для подачи заявок.
4. **Infrastructure**: Полная контейнеризация через Docker Compose для развертывания в один клик.

## 🚀 Быстрый старт

### Вариант А: Через Docker (Рекомендуется)
```bash
# 1. Склонировать репозиторий
git clone <твой-репо>
cd credit-scoring-app

# 2. Запустить все сервисы
docker-compose up --build

# 3. Открыть в браузере:
# Frontend: http://localhost:8501
# API Docs: http://localhost:8000/docs