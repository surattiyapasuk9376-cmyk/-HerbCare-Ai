import streamlit as st
import streamlit.components.v1 as components

# ==================================================
# CONFIG
# ==================================================

st.set_page_config(
    page_title="HerbCare AI 🌿",
    page_icon="🍵",
    layout="wide"
)

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fffaf0, #edf9ef);
}

.main-title {
    text-align:center;
    color:#347653;
    font-size:44px;
    font-weight:800;
    margin-top:10px;
}

.subtitle {
    text-align:center;
    color:#6d806f;
    font-size:18px;
    margin-bottom:25px;
}

.box {
    background:white;
    border-radius:24px;
    padding:24px;
    box-shadow:0 5px 20px rgba(0,0,0,0.07);
    margin-bottom:20px;
}

.section-title {
    color:#347653;
    font-size:22px;
    font-weight:700;
}

.result {
    background:#eff9f0;
    border-left:6px solid #63a875;
    padding:16px;
    border-radius:15px;
    margin:10px 0;
}

.warning {
    background:#fff5d9;
    border-left:6px solid #e8ae32;
    padding:16px;
    border-radius:15px;
    margin:10px 0;
}

.voice-box {
    background:#f3faf4;
    border-radius:20px;
    padding:18px;
    text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

st.markdown(
    '<div class="main-title">🌿 HerbCare AI 🍵</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'ผู้ช่วยแนะนำชาสมุนไพรสำหรับผู้ป่วยเบาหวาน'
    '</div>',
    unsafe_allow_html=True
)

# ==================================================
# LAYOUT
# ==================================================

left, right = st.columns([0.9, 1.5], gap="large")

# ==================================================
# LEFT : USER DATA
# ==================================================

with left:

    st.markdown('<div class="box">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">👤 ข้อมูลผู้ใช้งาน</div>',
        unsafe_allow_html=True
    )

    weight = st.number_input(
        "⚖️ น้ำหนัก (กิโลกรัม)",
        min_value=20.0,
        max_value=300.0,
        value=60.0,
        step=0.5
    )

    height = st.number_input(
        "📏 ส่วนสูง (เซนติเมตร)",
        min_value=100.0,
        max_value=220.0,
        value=160.0,
        step=1.0
    )

    age = st.number_input(
        "🎂 อายุ (ปี)",
        min_value=1,
        max_value=120,
        value=40
    )

    # BMI
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.markdown(
        f"""
        <div style="
            background:#edf8ed;
            padding:15px;
            border-radius:16px;
            margin:15px 0;
        ">
        <b>📊 ข้อมูลร่างกาย</b><br>
        BMI: <b>{bmi:.1f}</b>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Diseases
    st.markdown("### 🩺 โรคประจำตัว")

    diseases = st.multiselect(
        "เลือกโรคประจำตัว",
        [
            "เบาหวาน",
            "ความดันโลหิตสูง",
            "โรคไต",
            "โรคตับ",
            "โรคหัวใจ",
            "ไขมันในเลือดสูง",
            "ไม่มีโรคประจำตัวอื่น"
        ]
    )

    # Medicine
    st.markdown("### 💊 ยาที่ใช้อยู่")

    medication = st.text_input(
        "ชื่อยา (ถ้าทราบ)",
        placeholder="เช่น Metformin"
    )

    # Tea
    st.markdown("### 🍵 ชาสมุนไพรที่สนใจ")

    tea = st.selectbox(
        "เลือกชา",
        [
            "ชาใบเชียงดา",
            "ชาใบหม่อน",
            "ชาเขียว",
            "ชาขิง",
            "ชาอบเชย",
            "ชาคาโมมายล์",
            "ชาตะไคร้",
            "ยังไม่แน่ใจ"
        ]
    )

    analyze = st.button(
        "🌿 วิเคราะห์คำแนะนำ",
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


# ==================================================
# RIGHT : NONG BAICHA
# ==================================================

with right:

    st.markdown('<div class="box">', unsafe_allow_html=True)

    # Character
    try:
        st.image(
            "assets/nong_baicha.png",
            use_container_width=True
        )
    except:
        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:100px;
                padding:50px;
            ">
            🌿🍵
            </div>
            """,
            unsafe_allow_html=True
        )

    # Speech bubble
    st.markdown(
        """
        <div style="
            background:#eff9ef;
            border-radius:22px;
            padding:20px;
            color:#397653;
            font-size:19px;
            font-weight:600;
            text-align:center;
        ">
        💬 สวัสดีค่ะ! ฉันคือน้องใบชา 🌿<br>
        มาช่วยดูข้อมูลชาสมุนไพรให้กันนะคะ 💚
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


# ==================================================
# ANALYSIS
# ==================================================

if analyze:

    recommendations = []
    warnings = []

    # BMI
    if bmi >= 30:
        recommendations.append(
            "BMI ค่อนข้างสูง ควรเลือกเครื่องดื่มที่ไม่เติมน้ำตาล "
            "และควบคุมอาหารร่วมด้วย"
        )

    elif bmi >= 25:
        recommendations.append(
            "BMI อยู่ในช่วงค่อนข้างสูง ควรเลือกเครื่องดื่มไม่หวาน"
        )

    else:
        recommendations.append(
            "ควรดูแลน้ำหนักและสุขภาพโดยรวมร่วมกับระดับน้ำตาลในเลือด"
        )

    # Tea
    if tea == "ชาใบเชียงดา":

        recommendations.append(
            "ชาใบเชียงดาสามารถดื่มเป็นเครื่องดื่มสมุนไพรได้ "
            "แต่ยังไม่ควรใช้แทนยา หรือการรักษาโรคเบาหวาน"
        )

    elif tea == "ชาใบหม่อน":

        recommendations.append(
            "ชาใบหม่อนสามารถดื่มเป็นเครื่องดื่มสมุนไพรได้ "
            "แต่หลักฐานเกี่ยวกับการควบคุมระดับน้ำตาลยังมีข้อจำกัด"
        )

    elif tea == "ชาเขียว":

        recommendations.append(
            "ชาเขียวที่ไม่เติมน้ำตาลสามารถเป็นทางเลือกของเครื่องดื่มได้"
        )

    elif tea == "ชาขิง":

        recommendations.append(
            "ชาขิงแบบไม่เติมน้ำตาลสามารถดื่มเป็นเครื่องดื่มได้ "
            "แต่ไม่ควรใช้แทนการรักษาเบาหวาน"
        )

    elif tea == "ชาอบเชย":

        recommendations.append(
            "ชาอบเชยสามารถดื่มเป็นเครื่องดื่มได้ "
            "แต่ยังไม่มีหลักฐานเพียงพอที่จะใช้แทนการรักษาเบาหวาน"
        )

    elif tea == "ชาคาโมมายล์":

        recommendations.append(
            "คาโมมายล์สามารถดื่มเป็นเครื่องดื่มได้ "
            "หากใช้ยาหลายชนิดควรตรวจสอบการโต้ตอบกับยาก่อน"
        )

    elif tea == "ชาตะไคร้":

        recommendations.append(
            "สามารถเลือกเป็นเครื่องดื่มสมุนไพรแบบไม่เติมน้ำตาลได้"
        )

    else:

        recommendations.append(
            "หากยังไม่แน่ใจ ควรเลือกเครื่องดื่มที่ไม่เติมน้ำตาล "
            "และปรึกษาแพทย์หรือเภสัชกรก่อนใช้สมุนไพร"
        )

    # Kidney
    if "โรคไต" in diseases:

        warnings.append(
            "หากมีโรคไต ควรปรึกษาแพทย์หรือเภสัชกร "
            "ก่อนใช้สมุนไพรเป็นประจำ"
        )

    # Liver
    if "โรคตับ" in diseases:

        warnings.append(
            "หากมีโรคตับ ควรหลีกเลี่ยงการใช้สมุนไพรเข้มข้น "
            "โดยไม่ปรึกษาผู้เชี่ยวชาญ"
        )

    # Medication
    if medication.strip():

        warnings.append(
            f"คุณระบุว่ากำลังใช้ยา {medication} "
            "ควรให้แพทย์หรือเภสัชกรตรวจสอบการใช้ร่วมกับสมุนไพร"
        )

    # ==================================================
    # RESULT
    # ==================================================

    st.markdown("## 📊 ผลการวิเคราะห์")

    for rec in recommendations:

        st.markdown(
            f"""
            <div class="result">
            🌱 <b>คำแนะนำ</b><br>
            {rec}
            </div>
            """,
            unsafe_allow_html=True
        )

    for warning in warnings:

        st.markdown(
            f"""
            <div class="warning">
            ⚠️ <b>ข้อควรระวัง</b><br>
            {warning}
            </div>
            """,
            unsafe_allow_html=True
        )

    # ==================================================
    # VOICE
    # ==================================================

    speech = (
        f"สวัสดีค่ะ ฉันคือน้องใบชา "
        f"วันนี้คุณเลือก {tea} "
        f"คำแนะนำคือ "
        + " ".join(recommendations)
        + " "
        "หากกำลังใช้ยา หรือมีโรคประจำตัว "
        "ควรปรึกษาแพทย์หรือเภสัชกรก่อนนะคะ"
    )

    st.markdown("## 🔊 น้องใบชาพูดให้ฟัง")

    # Escape characters for JavaScript
    safe_speech = (
        speech
        .replace("\\", "\\\\")
        .replace("`", "\\`")
        .replace("${", "\\${")
    )

    components.html(
        f"""
        <div class="voice-box">

            <div style="
                font-size:20px;
                color:#397653;
                font-weight:bold;
                margin-bottom:15px;
            ">
            🌿 💬 น้องใบชาพร้อมพูดแล้ว!
            </div>

            <button onclick="speakText()" style="
                background:#4d9863;
                color:white;
                border:none;
                padding:14px 30px;
                border-radius:30px;
                font-size:18px;
                font-weight:bold;
                cursor:pointer;
            ">
            🔊 ให้น้องใบชาพูด
            </button>

            <script>

            function speakText() {{

                const text = `{safe_speech}`;

                window.speechSynthesis.cancel();

                const speech =
                    new SpeechSynthesisUtterance(text);

                speech.lang = "th-TH";
                speech.rate = 0.9;
                speech.pitch = 1.15;

                window.speechSynthesis.speak(speech);
            }}

            </script>

        </div>
        """,
  
