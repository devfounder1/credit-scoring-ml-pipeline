import requests
import streamlit as st

st.set_page_config(page_title="Premium Credit Card", page_icon="💳")
st.title("Кредитная карта Premium")
st.write("Мгновенное одобрение на основе AI-скоринга!")

with st.form("credit_form"):
    st.subheader("Анкета заемщика")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Ваш возраст", min_value=18, max_value=100, value=30)
        income = st.number_input("Ежемесячный доход (тыс. ₽)", min_value=0, value=50)
    with col2:
        education = st.checkbox("Высшее образование", value=True)
        work = st.checkbox("Официальное трудоустройство", value=True)
        car = st.checkbox("Наличие автомобиля", value=False)
    
    submit = st.form_submit_button("Подать заявку", type="primary")

if submit:
    data = {
        "age": age, 
        "income": income, 
        "education": education, 
        "work": work, 
        "car": car
    }
    
    with st.spinner("Анализируем вашу заявку..."):
        try:
            # Обрати внимание на URL: если запускаешь через docker-compose, имя сервиса 'api'
            response = requests.post("http://localhost:8000/score", json=data, timeout=5)
            response.raise_for_status()
            result = response.json()
            
            if result["approved"]:
                st.success("🎉 Поздравляем! Ваша заявка ОДОБРЕНА!")
                st.info("Курьер доставит карту в течение 24 часов.")
            else:
                st.warning("😔 К сожалению, по кредитной карте пришел отказ.")
                st.info("💡 Но мы подобрали для вас альтернативу: **Дебетовая карта с 3% кешбэком** и бесплатным обслуживанием!")
        except requests.exceptions.ConnectionError:
            st.error("⚠️ Ошибка: Сервис скоринга временно недоступен. Попробуйте позже.")
        