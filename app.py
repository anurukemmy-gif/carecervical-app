import streamlit as st
import streamlit.components.v1 as components

# --- 1. การตั้งค่าหน้าแอป ---
st.set_page_config(
    page_title="Knowledge of Cervical Cancer", 
    page_icon="🎗️", 
    layout="centered"
)

# --- 2. การตกแต่ง (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5; }
    h1 { color: #C2185B !important; text-align: center; }
    h2, h3 { color: #D81B60 !important; }
    p, span, label, li { color: #333333 !important; font-size: 1.05rem !important; }
    .stButton>button { 
        background-color: #D81B60; color: white !important; 
        border-radius: 20px; font-weight: bold; width: 100%; height: 50px;
    }
    .content-box {
        background-color: white; padding: 25px; border-radius: 15px;
        border-top: 5px solid #D81B60; margin-bottom: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    }
    .highlight { color: #D81B60; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ส่วนหัว ---
st.title("🎗️ Knowledge of Cervical Cancer")
st.subheader("ศูนย์เรียนรู้และสนับสนุนการคัดกรองมะเร็งปากมดลูก")
st.divider()

# --- 4. เมนูหลัก ---
tab1, tab2, tab3 = st.tabs(["📊 ส่วนที่ 1: ประเมิน", "📖 ส่วนที่ 2: ความรู้และวิธีตรวจ", "📍 ส่วนที่ 3: ค้นหา รพ.สต."])

# --- ส่วนที่ 1: การประเมิน ---
with tab1:
    st.header("📋 แบบประเมินเบื้องต้น")
    age = st.number_input("ข้อที่ 1: อายุของคุณ (ปี)", min_value=0, max_value=120, value=30)
