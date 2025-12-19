import streamlit as st
import streamlit.components.v1 as components

# --- 1. การตั้งค่าหน้าแอป (ต้องอยู่บรรทัดแรก) ---
st.set_page_config(
    page_title="Knowledge of Cervical Cancer", 
    page_icon="🎗️", 
    layout="centered"
)

# --- 2. การตกแต่ง CSS ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #FFF0F5 0%, #FFFFFF 100%); }
    .hero-section {
        background-color: #D81B60;
        padding: 40px 20px;
        border-radius: 0px 0px 30px 30px;
        text-align: center;
        color: white;
        margin: -60px -20px 30px -20px;
    }
    .content-box {
        background-color: white; padding: 20px; border-radius: 15px;
        border-top: 5px solid #D81B60; margin-bottom: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    .stButton>button { 
        background-color: #D81B60; color: white !important; 
        border-radius: 25px; font-weight: bold; width: 100%; height: 50px;
    }
    h2, h
