import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="HerbCare AI 🌿",
    page_icon="🍵",
    layout="centered"
)

# =========================
# STYLE
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fff8ed, #eefaf1);
}

.title {
    text-align: center;
    color: #4d7c5b;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 0;
}

.subtitle {
    text-align: center;
    color: #777;
    font-size: 17px;
    margin-bottom: 15px;
}

.character-box {
    background: white;
    padding: 18px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0 5px 20px rgba(0,0,0,0.07);
    margin: 15px 0 25px 0;
}

.character {
    font-size: 75px;
    margin-bottom: 5px;
}

.speech {
    background: #eefaf1;
    border-radius: 18px;
    padding: 12px;
    color: #4d7c5b;
    font-size: 17px;
    font-weight: 600;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 22px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.07);
    margin-bottom: 20px;
}

.warning {
    background: #fff3cd;
    padding: 15px;
    border-radius: 15px;
    border-left: 5px solid #e0a800;
    margin-bottom: 10px;
}

.safe {
    background: #eaf7ed;
    padding: 15px;
    border-radius: 15px;
    border-left: 5px solid #5b9b6d;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown(
    '<div class="title">🌿 HerbCare AI 🍵</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">ผู้ช่วยแนะนำชาสมุนไพรสำหรับผู้ป่วยเบาหวาน</div>',
    unsafe_allow_html=True
)

# =========================
# HERB CHARACTER
# =========================

st.markdown("""
<div class="character-box">

<div class="character">
🌿<br>
(｡•ᴗ•｡)<br>
🍵
</div>

<div class="speech">
💚 สวัสดีค่ะ! ฉันคือน้องใบชา<br>
มาช่วยดูข้อมูลชาสมุนไพรให้กันนะคะ 🌱
</div>

</div>
""", unsafe_allow_html=True)

st.info(
    "💚 ระบบนี้เป็นเครื่องมือให้ข้อมูลเบื้องต้น "
    "ไม่ใช่การวินิจฉัยหรือคำสั่งรักษาจากแพทย์"
)

# =========================
# USER INFORMATION
# =========================

st.markdown("### 👤 ข้อมูลผู้ใช้งาน")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input(
        "⚖️ น้ำหนัก (กิโลกรัม)",
        min_value=20.0,
        max_value=300.0,
        value=60.0,
        step=0.5
    )

with col2:
    height = st.number_input(
        "📏 ส่วนสูง (เซนติเมตร)",
        min_value=100.0,
        max_value=220.0,
        value=160.0,
        step=1.0
    )

age = st.number_input(
    "🎂 อายุ",
    min_value=1,
    max_value=120,
    value=40
)

# =========================
# BMI
# =========================

height_m = height / 100
bmi = weight / (height_m ** 2)

st.markdown(
    f"""
    <div class="card">
        <h3>📊 ข้อมูลร่างกาย</h3>
        <p><b>BMI:</b> {bmi:.1f}</p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# DISEASES
# =========================

st.markdown("### 🩺 โรคประจำตัว")

diseases = st.multiselect(
    "เลือกโรคประจำตัวที่มี",
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

# =========================
# MEDICATION
# =========================

st.markdown("### 💊 ยาที่ใช้อยู่")

medication = st.text_area(
    "ระบุชื่อยา (ถ้าทราบ)",
    placeholder="เช่น Metformin, ยาความดัน..."
)

# =========================
# TEA
# =========================

st.markdown("### 🍵 ชาสมุนไพรที่สนใจ")

tea = st.selectbox(
    "เลือกชา",
    [
        "ชาคาโมมายล์",
        "ชาเขียว",
        "ชาอบเชย",
        "ชาขิง",
        "ชาใบเชียงดา",
        "ชาใบหม่อน",
        "ชาตะไคร้",
        "ยังไม่แน่ใจ"
    ]
)

# =========================
# ANALYSIS
# =========================

if st.button("🌿 วิเคราะห์คำแนะนำ", use_container_width=True):

    recommendations = []
    warnings = []

    # BMI
    if bmi >= 30:
        recommendations.append(
            "BMI อยู่ในช่วงที่ควรให้ความสำคัญกับการควบคุมน้ำหนัก "
            "ควรเลือกเครื่องดื่มที่ไม่เติมน้ำตาล"
        )

    elif bmi >= 25:
        recommendations.append(
            "BMI ค่อนข้างสูง ควรเน้นเครื่องดื่มไม่หวาน "
            "และควบคุมปริมาณอาหารร่วมด้วย"
        )

    else:
        recommendations.append(
            "BMI ไม่ได้อยู่ในช่วงสูงตามเกณฑ์ทั่วไป "
            "แต่ควรพิจารณาร่วมกับระดับน้ำตาลและสุขภาพโดยรวม"
        )

    # Kidney
    if "โรคไต" in diseases:
        warnings.append(
            "⚠️ หากมีโรคไต ควรปรึกษาแพทย์หรือเภสัชกรก่อนใช้ "
            "สมุนไพรหรือผลิตภัณฑ์เสริมอาหาร"
        )

    # Liver
    if "โรคตับ" in diseases:
        warnings.append(
            "⚠️ หากมีโรคตับ ควรหลีกเลี่ยงการใช้สมุนไพรเข้มข้น "
            "โดยไม่ปรึกษาผู้เชี่ยวชาญ"
        )

    # Blood pressure
    if "ความดันโลหิตสูง" in diseases:
        warnings.append(
            "⚠️ หากใช้ยาความดัน ควรตรวจสอบการเกิดปฏิกิริยา "
            "ระหว่างยาและสมุนไพรกับบุคลากรทางการแพทย์"
        )

    # =========================
    # TEA RECOMMENDATIONS
    # =========================

    if tea == "ชาอบเชย":

        recommendations.append(
            "ชาอบเชยอาจดื่มเป็นเครื่องดื่มได้ "
            "แต่ยังไม่มีหลักฐานเพียงพอที่จะใช้แทนการรักษาเบาหวาน"
        )

        if "โรคตับ" in diseases:
            warnings.append(
                "⚠️ หากมีโรคตับ ควรระวังการบริโภคอบเชยปริมาณมาก "
                "โดยเฉพาะชนิด Cassia"
            )

    elif tea == "ชาเขียว":

        recommendations.append(
            "ชาเขียวแบบไม่เติมน้ำตาลสามารถเป็นทางเลือกของเครื่องดื่มได้ "
            "แต่ควรระวังผลิตภัณฑ์สารสกัดชาเขียวเข้มข้น"
        )

    elif tea == "ชาคาโมมายล์":

        recommendations.append(
            "คาโมมายล์สามารถใช้เป็นเครื่องดื่มได้ในบางคน "
            "แต่หากใช้ยาหลายชนิดควรตรวจสอบการโต้ตอบกับยาก่อน"
        )

    elif tea == "ชาขิง":

        recommendations.append(
            "ชาขิงแบบไม่เติมน้ำตาลสามารถใช้เป็นเครื่องดื่มได้ "
            "แต่ไม่ควรใช้แทนการรักษาเบาหวาน"
        )

    elif tea == "ชาใบเชียงดา":

        recommendations.append(
            "ชาใบเชียงดาสามารถดื่มเป็นเครื่องดื่มสมุนไพรได้ "
            "แต่หลักฐานเกี่ยวกับผลต่อระดับน้ำตาลในเลือดยังมีข้อจำกัด "
            "จึงไม่ควรใช้แทนยาหรือการรักษาเบาหวาน"
        )

    elif tea == "ชาใบหม่อน":

        recommendations.append(
            "ชาใบหม่อนสามารถดื่มเป็นเครื่องดื่มสมุนไพรได้ "
            "แต่หลักฐานเกี่ยวกับการควบคุมระดับน้ำตาลยังมีข้อจำกัด "
            "จึงไม่ควรใช้แทนยาหรือการรักษาเบาหวาน"
        )

    elif tea == "ชาตะไคร้":

        recommendations.append(
            "สามารถพิจารณาเป็นเครื่องดื่มสมุนไพรที่ไม่เติมน้ำตาลได้ "
            "แต่ไม่ควรกล่าวอ้างว่าสามารถรักษาเบาหวาน"
        )

    else:

        recommendations.append(
            "หากยังไม่แน่ใจเกี่ยวกับชนิดชา ควรเลือกเครื่องดื่ม "
            "ที่ไม่เติมน้ำตาล และตรวจสอบกับบุคลากรทางการแพทย์ก่อน"
        )

    # Medication
    if medication.strip():

        warnings.append(
            "💊 เนื่องจากคุณระบุว่ากำลังใช้ยาอยู่ "
            "ระบบไม่สามารถยืนยันความปลอดภัยของสมุนไพรกับยาทุกชนิดได้ "
            "ควรนำรายชื่อยาให้แพทย์หรือเภสัชกรตรวจสอบ"
        )

    # =========================
    # RESULT
    # =========================

    st.markdown("## 💚 ผลการวิเคราะห์")

    for item in recommendations:

        st.markdown(
            f"""
            <div class="safe">
                🌱 {item}
            </div>
            """,
            unsafe_allow_html=True
        )

    for warning in warnings:

        st.markdown(
            f"""
            <div class="warning">
                {warning}
            </div>
            """,
            unsafe_allow_html=True
        )

    # =========================
    # HERB CHARACTER SPEECH
    # =========================

    st.markdown("### 🌿 น้องใบชาพูดให้ฟัง")

    speech_text = (
        f"สวัสดีค่ะ ฉันคือน้องใบชา "
        f"จาก HerbCare AI ค่ะ "
        f"วันนี้คุณเลือก {tea} "
        f"คำแนะนำคือ "
        + " ".join(recommendations)
        + " หากกำลังใช้ยา หรือมีโรคประจำตัว "
        "ควรปรึกษาแพทย์หรือเภสัชกรก่อนนะคะ"
    )

    st.components.v1.html(
        f"""
        <div style="
            background:#ffffff;
            padding:20px;
            border-radius:20px;
            text-align:center;
            box-shadow:0 5px 20px rgba(0,0,0,0.07);
        ">

        <div style="font-size:65px;">
        🌿<br>
        (｡•ᴗ•｡)<br>
        🍵
        </div>

        <p style="
            color:#4d7c5b;
            font-size:18px;
            font-weight:bold;
        ">
        💬 น้องใบชากำลังพูด...
        </p>

        <button onclick="speakText()" style="
            background:#75a878;
            color:white;
            border:none;
            padding:13px 28px;
            border-radius:30px;
            font-size:18px;
            cursor:pointer;
        ">
        🔊 ให้น้องใบชาพูด
        </button>

        <script>

        function speakText() {{

            const text = `{speech_text}`;

            const speech =
                new SpeechSynthesisUtterance(text);

            speech.lang = "th-TH";
            speech.rate = 0.9;
            speech.pitch = 1.15;

            window.speechSynthesis.cancel();

            window.speechSynthesis.speak(speech);
        }}

        </script>

        </div>
        """,
        height=300
    )

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "🌿 HerbCare AI | Educational prototype "
    "สำหรับการให้ข้อมูลเบื้องต้นเกี่ยวกับชาสมุนไพร"
)

st.caption(
    "⚠️ ไม่ใช่เครื่องมือวินิจฉัยโรค และไม่ควรใช้แทนคำแนะนำจากแพทย์"
)
