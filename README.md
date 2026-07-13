# 💳 AI Credit Scoring ML Pipeline

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25+-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**End-to-End ML пайплайн для кредитного скоринга** — от разведочного анализа данных до веб-приложения с API.

---

## 📋 Оглавление
- [О проекте](#-о-проекте)
- [Архитектура](#-архитектура)
- [Датасет](#-датасет)
- [Быстрый старт](#-быстрый-старт)
- [Стек технологий](#-стек-технологий)
- [Метрики модели](#-метрики-модели)
- [Автор](#-автор)

---

##  О проекте

Проект демонстрирует **полный цикл разработки ML-продукта**:
- ✅ Разведочный анализ данных (EDA)
- ✅ Обучение модели с балансировкой классов
- ✅ REST API на FastAPI для инференса
- ✅ Интерактивный веб-интерфейс на Streamlit

---

## 🏗 Архитектура
┌─────────────────┐       ┌──────────────────┐       ┌─────────────────┐
│ Streamlit       │ ────▶│ FastAPI API      │ ────▶ │ ML Model        │
│      (Frontend) │       │       (Backend)  │       │  (Scikit-Learn) │
└─────────────────┘       └──────────────────┘       └─────────────────┘

**Компоненты системы:**
1. **`src/train.py`** — ML пайплайн: обучение Logistic Regression с `StandardScaler`
2. **`src/service.py`** — FastAPI микросервис с валидацией данных (Pydantic)
3. **`app.py`** — Веб-интерфейс для подачи заявок
4. **`exploratory_analysis.ipynb`** — EDA анализ данных

 **[Открыть ноутбук с EDA анализом](exploratory_analysis.ipynb)**

---

##  Датасет

Данные структурированы по принципу реальных кредитных скоринговых моделей (вдохновлено датасетами **Т-Банка**).

| Признак | Тип | Описание |
|---------|-----|----------|
| `age` | Числовой | Возраст заемщика |
| `income` | Числовой | Ежемесячный доход (тыс. ₽) |
| `education` | Бинарный | Наличие высшего образования |
| `work` | Бинарный | Официальное трудоустройство |
| `car` | Бинарный | Наличие автомобиля |

**Целевая переменная:** `default` (1 = дефолт, 0 = успешное погашение)

>  **Проблема дисбаланса классов:** В реальных данных дефолтов значительно меньше.  
> **Решение:** Используем `class_weight="balanced"` для повышения Recall.

---

##  Быстрый старт

### 1️ Установка зависимостей
```bash
pip install -r requirements.txt

2️ Обучение модели
    python src/train.py

Создаст файлы модели в папке models/

3️⃣ Запуск API сервиса
    uvicorn src.service:app --reload

4️ Запуск веб-интерфейса
# Откройте НОВЫЙ терминал
streamlit run app.py

 Интерфейс: http://localhost:8501


 Стек технологий
Machine Learning
Scikit-Learn: Logistic Regression, StandardScaler
Pandas & NumPy: Обработка данных
Backend
FastAPI: REST API
Pydantic: Валидация данных
Uvicorn: ASGI сервер
Frontend
Streamlit: Интерактивный веб-интерфейс
Tools
Git: Контроль версий
Jupyter Notebook: EDA анализ
📈 Метрики модели
Метрика
Значение
Описание
Precision
~0.75
Минимизация ложных одобрений
Recall
~0.70
Выявление реальных рисков
Особенности:
✅ Использован class_weight="balanced" для работы с дисбалансом
✅ Масштабирование признаков (StandardScaler)
✅ Разделение данных: 80% train / 20% test
👤 Автор
Mikhail Demashov
📧 noo_noo1999@mail.ru
Санкт-Петербург