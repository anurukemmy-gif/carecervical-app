import streamlit as st

# --- 1. ตั้งค่าหน้าแอป ---
st.set_page_config(
    page_title="Knowledge of Cervical Cancer", 
    page_icon="🎗️", 
    layout="centered"
)

# --- 2. การตกแต่งสีและรูปแบบ (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5; }
    h1 { color: #C2185B !important; text-align: center; }
    h2, h3 { color: #D81B60 !important; }
    p, span, label, .stMarkdown { color: #333333 !important; font-size: 1.1rem !important; }
    .stButton>button { 
        background-color: #D81B60; color: white !important; 
        border-radius: 20px; font-weight: bold; width: 100%; height: 50px;
    }
    .info-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #D81B60;
        margin-bottom: 15px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }
    .highlight { color: #D81B60; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ส่วนหัวแอป ---
st.title("🎗️ Knowledge of Cervical Cancer")
st.subheader("ศูนย์เรียนรู้และสนับสนุนการคัดกรองมะเร็งปากมดลูก")
st.divider()

# --- 4. เมนูหลัก ---
tab1, tab2, tab3 = st.tabs([
    "📊 ส่วนที่
