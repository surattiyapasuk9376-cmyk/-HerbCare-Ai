import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="HerbCare AI 🌿",
    page_icon="🍵",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#fffaf0,#eef9ef);
}

.title {
    text-align:center;
    color:#397653;
    font-size:42px;
    font-weight:800;
}

.subtitle {
    text-align:center;
    color:#718074;
    font-size:18px;
    margin-bottom:25px;
}

.card {
    background:white;
    padding:25px;
    border-radius:25px;
    box-shadow:0 5px 20px rgba(0,0,0,.07);
    margin-bottom:20px;
}

.character {
    text-align:center;
    font-size:90px;
    padding:25px;
}

.speech {
    background:#edf9ef;
    color:#397653;
    padding:20px;
    border-radius:25px;
    font-size:18px;
    text-align:center;
    font-weight:600;
}

.result {
    background:#edf9ef;
    border-left:6px solid #5da46d;
    padding:16px;
    border-radius:15px;
    margin:10px 0;
}

.warning {
    background:#fff4d5;
    border-left:6px solid #e3ad35;
    padding:16px;
    border-radius:15px;
    margin:10px 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🌿 HerbCare AI 🍵</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">ผู้ช่วยแนะนำชาสมุนไพรสำหรับผู้ป่วยเบาหวาน</div>',
    unsafe_allow_html=True
)

left, right = st.columns([1, 1.5])

# =========================
# INPUT
# =========================

with left:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### 👤 ข้อมูลผู้ใช้งาน")

    weight = st.number_input(
        "⚖️ น้ำหนัก (กิโลกรัม)",
        20.0,
        300.0,
        60.0
    )

    height = st.number_input(
        "📏 ส่วนสูง (เซนติเมตร)",
        100.0,
        220.0,
        160.0
    )

    age = st.number_input(
        "🎂 อายุ",
        1,
        120,
        40
    )

    height_m = height / 100
    bmi = weight / (height_m * height_m)

    st.info(f"📊 BMI ของคุณ: **{bmi:.1f}**")

    st.markdown("### 🩺 โรคประจำตัว")

    diseases = st.multiselect(
        "เลือกโรค",
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

    st.markdown("### 💊 ยาที่ใช้อยู่")

    medication = st.text_input(
        "ชื่อยา",
        placeholder="เช่น Metformin"
    )

    st.markdown("### 🍵 ชาสมุนไพร")

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


# =========================
# CHARACTER
# =========================

with right:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("""
    <div class="character">
        🌿<br>
        👧🏻<br>
        🍵
    </div>

    <div class="speech">
        💚 สวัสดีค่ะ! ฉันคือน้องใบชา<br>
        มาช่วยดูข้อมูลชาสมุนไพรให้กันนะคะ 🌱
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# =========================
# ANALYSIS
# =========================

if analyze:

    recommendations = []
    warnings = []

    if bmi >= 30:
        recommendations.append(
            "BMI ค่อนข้างสูง ควรเลือกเครื่องดื่มที่ไม่เติมน้ำตาล"
        )
    elif bmi >= 25:
        recommendations.append(
            "BMI ค่อนข้างสูง ควรควบคุมน้ำหนักและเลือกเครื่องดื่มไม่หวาน"
        )
    else:
        recommendations.append(
            "ควรดูแลน้ำหนักและสุขภาพโดยรวมร่วมกับระดับน้ำตาล"
        )

    if tea == "ชาใบเชียงดา":
        recommendations.append(
            "ชาใบเชียงดาสามารถดื่มเป็นเครื่องดื่มสมุนไพรได้ "
            "แต่ไม่ควรใช้แทนยาหรือการรักษาเบาหวาน"
        )

    elif tea == "ชาใบหม่อน":
        recommendations.append(
            "ชาใบหม่อนสามารถดื่มเป็นเครื่องดื่มสมุนไพรได้ "
            "แต่ไม่ควรใช้แทนการรักษาเบาหวาน"
        )

    elif tea == "ชาเขียว":
        recommendations.append(
            "ชาเขียวแบบไม่เติมน้ำตาลสามารถเป็นทางเลือกของเครื่องดื่มได้"
        )

    elif tea == "ชาขิง":
        recommendations.append(
            "ชาขิงแบบไม่เติมน้ำตาลสามารถดื่มได้ "
            "แต่ไม่ควรใช้แทนการรักษา"
        )

    elif tea == "ชาอบเชย":
        recommendations.append(
            "ชาอบเชยสามารถดื่มเป็นเครื่องดื่มได้ "
            "แต่ไม่ควรใช้แทนการรักษาเบาหวาน"
        )

    elif tea == "ชาคาโมมายล์":
        recommendations.append(
            "คาโมมายล์สามารถดื่มเป็นเครื่องดื่มได้ "
            "หากใช้ยาหลายชนิดควรตรวจสอบการใช้ร่วมกัน"
        )

    elif tea == "ชาตะไคร้":
        recommendations.append(
            "สามารถเลือกเป็นเครื่องดื่มสมุนไพรแบบไม่เติมน้ำตาลได้"
        )

    else:
        recommendations.append(
            "ควรเลือกเครื่องดื่มที่ไม่เติมน้ำตาล "
            "และปรึกษาแพทย์หรือเภสัชกรก่อนใช้สมุนไพร"
        )

    if "โรคไต" in diseases:
        warnings.append(
            "หากมีโรคไต ควรปรึกษาแพทย์หรือเภสัชกรก่อนใช้สมุนไพร"
        )

    if "โรคตับ" in diseases:
        warnings.append(
            "หากมีโรคตับ ควรปรึกษาผู้เชี่ยวชาญก่อนใช้สมุนไพรเข้มข้น"
        )

    if medication.strip():
        warnings.append(
            "เนื่องจากมีการใช้ยา ควรให้แพทย์หรือเภสัชกรตรวจสอบ "
            "การใช้ยาร่วมกับสมุนไพร"
        )

    # =========================
    # RESULT
    # =========================

    st.markdown("## 📊 ผลการวิเคราะห์")

    for item in recommendations:
        st.markdown(
            f'<div class="result">🌱 {item}</div>',
            unsafe_allow_html=True
        )

    for item in warnings:
        st.markdown(
            f'<div class="warning">⚠️ {item}</div>',
            unsafe_allow_html=True
        )

    # =========================
    # VOICE
    # =========================

    speech = (
        f"สวัสดีค่ะ ฉันคือน้องใบชา "
        f"วันนี้คุณเลือก {tea} "
        + " ".join(recommendations)
        + " หากกำลังใช้ยา หรือมีโรคประจำตัว "
        "ควรปรึกษาแพทย์หรือเภสัชกรก่อนนะคะ"
    )

    st.markdown("### 🔊 น้องใบชาพูดให้ฟัง")

    # ใช้ JSON.dumps เพื่อป้องกันข้อความทำ JavaScript พัง
    import json
    speech_js = json.dumps(speech)

    components.html(
        f"""
        <div style="
            background:#edf9ef;
            padding:20px;
            border-radius:20px;
            text-align:center;
        ">

        <button onclick="speak()" style="
            background:#4d9863;
            color:white;
            border:none;
            padding:14px 28px;
            border-radius:30px;
            font-size:18px;
            font-weight:bold;
        ">
        🔊 ให้น้องใบชาพูด
        </button>

        <script>
        function speak() {{
            const text = {speech_js};

            window.speechSynthesis.cancel();

            const msg =
                new SpeechSynthesisUtterance(text);

            msg.lang = "th-TH";
            msg.rate = 0.9;
            msg.pitch = 1.15;

            window.speechSynthesis.speak(msg);
        }}
        </script>

        </div>
        """,
        height=100
    )


st.markdown("---")

st.caption(
    "🌿 HerbCare AI | Educational Prototype | "
    "ไม่ใช่เครื่องมือวินิจฉัยโรค"
)
