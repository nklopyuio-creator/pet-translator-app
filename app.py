import streamlit as st
import numpy as np
import librosa
import time

st.set_page_config(page_title="مترجم لغة الحيوانات الأليفة", page_icon="🐾", layout="centered")

st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; text-align: center; color: #4F46E5; direction: rtl; }
    .sub-title { font-size: 18px; text-align: center; color: #6B7280; margin-bottom: 30px; direction: rtl; }
    .result-box { padding: 20px; border-radius: 10px; background-color: #F3F4F6; text-align: center; font-size: 20px; font-weight: bold; margin-top: 20px; direction: rtl;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🐾 مترجم الذكاء الاصطناعي للكلاب والقطط</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">سجل أو ارفع صوت حيوانك الأليف لترجمة مشاعره واحتياجاته فوراً</div>', unsafe_allow_html=True)

pet_type = st.radio("اختر نوع الحيوان الأليف:", ("قطة 🐱", "كلب 🐶"), horizontal=True)
uploaded_file = st.file_uploader("قم برفع ملف الصوت بصيغة (WAV أو MP3)", type=["wav", "mp3"])

def analyze_pet_voice(file, is_dog):
    try:
        y, sr = librosa.load(file, duration=5.0)
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
        avg_pitch = np.mean(pitches[pitches > 0]) if np.any(pitches > 0) else 150.0
        
        if not is_dog:
            if avg_pitch > 1500:
                return "القطة تشعر بالخوف أو التهديد وتطلب الحماية! 🙀"
            elif avg_pitch > 800:
                return "القطة تشعر بالجوع الشديد وتريد الطعام الآن 🐈‍⬛"
            else:
                return "مواء ودود وسعيد، القطة ترغب في اللعب معك! 😻"
        else:
            if avg_pitch > 1000:
                return "نباح تنبيهي عالي: الكلب يحذر من شيء غريب أو يشعر بالخوف! 🐕"
            elif avg_pitch > 500:
                return "أنين منخفض: قد يكون الكلب يشعر بالملل أو يطلب الاهتمام 🦮"
            else:
                return "الكلب سعيد جداً ومتحمس ومستعد للعب والتنزه! 🐶"
    except Exception as e:
        return f"حدث خطأ أثناء معالجة الصوت: {str(e)}"

if uploaded_file is not None:
    st.write("---")
    st.markdown("### 🎙️ الصوت المرفوع:")
    st.audio(uploaded_file, format='audio/wav')
    
    if st.button("اضغط لبدء ترجمة الصوت عبر الذكاء الاصطناعي ✨"):
        with st.spinner("جاري تنقية الصوت وفك تشفير الأنماط الصوتية الترددية..."):
            time.sleep(2.5)
            is_dog_selected = (pet_type == "كلب 🐶")
            result = analyze_pet_voice(uploaded_file, is_dog_selected)
            
        st.balloons()
        st.markdown(f'<div class="result-box">💡 تحليل الذكاء الاصطناعي:<br><br>{result}</div>', unsafe_allow_html=True)
      
