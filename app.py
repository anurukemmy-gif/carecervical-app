import streamlit as st

# --- 1. การตั้งค่าหน้าแอป ---
st.set_page_config(
    page_title="Knowledge of Cervical Cancer", 
    page_icon="🎗️", 
    layout="centered"
)

# --- 2. การตกแต่ง CSS (ปรับสีชื่อแอปให้เด่นชัด) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #FFF0F5 0%, #FFFFFF 100%); }
    
    .hero-section {
        background-color: #D81B60;
        padding: 50px 20px;
        border-radius: 0px 0px 35px 35px;
        text-align: center;
        margin: -60px -20px 30px -20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.2);
    }
    
    /* ปรับแต่งชื่อแอปให้ขาวชัดเจนและมีเงา */
    .hero-title {
        color: #FFFFFF !important;
        font-size: 2.5rem;
        font-weight: 800;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 10px;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        color: #FFEBEE !important;
        font-size: 1.2rem;
        font-weight: 400;
    }

    .content-box {
        background-color: white; padding: 25px; border-radius: 20px;
        border-left: 10px solid #D81B60; margin-bottom: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    
    .stButton>button { 
        background-color: #D81B60; color: white !important;
