import streamlit as st
import streamlit.components.v1 as components

# --- 1. การตั้งค่าหน้าแอป ---
st.set_page_config(
    page_title="Knowledge of Cervical Cancer", 
    page_icon="🎗️", 
    layout="centered"
)

# --- 2. การตกแต่ง CSS (แบบปลอดภัย ไม่ทำให้ Error) ---
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
    h2, h3 { color: #D81B60 !important; }
    p, span, label, li { color: #444444 !important; font-size: 1.05rem !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. หน้าปกแอป ---
st.markdown("""
    <div class="hero-section">
        <h1 style="color: white !important;">🎗️ Knowledge of Cervical Cancer</h1>
        <p style="color: #FFEBEE !important;">ตรวจไว ป้องกันได้ มั่นใจในสุขภาพสตรี</p>
    </div>
    """, unsafe_allow_html=True)

# --- 4. เมนูหลัก (Tabs) ---
tab1, tab2, tab3 = st.tabs(["📊 การประเมิน", "📖 ความรู้และวิธีตรวจ", "📍 ติดต่อจุดบริการ"])

# --- ส่วนที่ 1: การประเมิน ---
with tab1:
    st.header("📋 ประเมินความเสี่ยง")
    with st.container():
        st.write("กรุณาตอบคำถามเพื่อวิเคราะห์ความเสี่ยงเบื้องต้น")
        age = st.number_input("อายุของคุณ (ปี)", min_value=0, max_value=120, value=30)
        status = st.radio("คุณเคยตรวจคัดกรองมะเร็งปากมดลูกหรือไม่?", ["ไม่เคย", "เคยตรวจภายใน 5 ปี", "เคยตรวจนานกว่า 5 ปี"])
        if st.button("บันทึกข้อมูล"):
            st.balloons()
            st.success("บันทึกข้อมูลเรียบร้อยแล้ว")

# --- ส่วนที่ 2: ความรู้และวิธีตรวจ (ครบถ้วน) ---
with tab2:
    st.header("📖 ข้อมูลความรู้ที่ครบถ้วน")

    with st.expander("🔍 1. ความรู้เรื่องมะเร็งปากมดลูก", expanded=True):
        st.write("📺 **วิดีโอโดย: คณะแพทยศาสตร์โรงพยาบาลรามาธิบดี**")
        # ฝังวิดีโอ Facebook ด้วย Iframe (วิธีที่เสถียรที่สุด)
        fb_url = "https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2Frama.rccc%2Fvideos%2F342186893395115%2F&show_text=0&width=560"
        components.iframe(fb_url, height=315)
        
        st.markdown("""
        <div class='content-box'>
        <b>ข้อมูลสำคัญ:</b><br>
        -
