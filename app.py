import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

st.set_page_config(
    page_title="HerbCare AI 🌿",
    page_icon="🍵",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff8ed, #eefaf1);
}
.title {
    text-align: center;
    color: #4d7c5b;
    font-size: 42px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: #6b806e;
    font-size: 18px;
}
.card {
    background: rgba(255,255,255,0.92);
    padding: 22px;
    border-radius: 24px;
    margin: 15px 0;
    box-shadow: 0 6px 20px rgba(70,100,70,0.12);
}
.mascot {
    text-align: center;
    animation: float 3s ease-in-out infinite;
}
.mascot img {
    max-width: 210px;
}
.speech {
    background: #fffdf5;
    border: 2px solid #dcebd8;
    border-radius: 22px;
    padding: 18px;
    text-align: center;
    color: #55705a;
    animation: float 3s ease-in-out infinite;
}
.result {
    background: #f5fff6;
    border-radius: 20px;
    padding: 20px;
    border: 1px solid #dcebd8;
}
.success-box {
    background: #fff9d9;
    border-radius: 20px;
    padding: 20px;
    text-align: center;
}
@keyframes float {
    0% {transform:translateY(0)}
    50% {transform:translateY(-8px)}
    100% {transform:translateY(0)}
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🌿 HerbCare AI 🍵</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">ผู้ช่วยให้ข้อมูลเบื้องต้นเกี่ยวกับการดื่มชาสมุนไพร</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">
💚 <b>HerbCare AI</b> เป็นต้นแบบเพื่อการศึกษา
ช่วยประเมินข้อมูลเบื้องต้นและให้คำแนะนำทั่วไปเกี่ยวกับ
ชาสมุนไพร ไม่ใช่เครื่องมือสำหรับวินิจฉัยหรือรักษาโรค
</div>
""", unsafe_allow_html=True)

img = Path("nong_baicha_mascot.png")

if img.exists():
    data = base64.b64encode(img.read_bytes()).decode()
    st.markdown(
        f"""
        <div class="mascot">
            <img src="data:image/png;base64,{data}">
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        '<div class="speech">🌱 น้องใบชาพร้อมให้คำแนะนำแล้วค่ะ</div>',
        unsafe_allow_html=True
    )

st.markdown("## 👤 ข้อมูลผู้ใช้งาน")

left, right = st.columns(2)

with left:
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

with right:
    age = st.number_input(
        "🎂 อายุ (ปี)",
        min_value=1,
        max_value=120,
        value=18,
        step=1
    )

    diseases = st.multiselect(
        "🩺 โรคประจำตัว",
        [
            "เบาหวาน",
            "ความดันโลหิตสูง",
            "โรคไต",
            "โรคหัวใจ",
            "ไม่มีโรคประจำตัว"
        ]
    )

st.markdown("### 💊 การใช้ยา")

medicine = st.text_input(
    "ยาที่ใช้อยู่ (ถ้าทราบ)",
    placeholder="เช่น ยาเบาหวาน / ยาความดัน"
)

medicine_taken = st.radio(
    "วันนี้กินยาตามแพทย์สั่งแล้วหรือยัง?",
    ["กินแล้ว", "ยังไม่ได้กิน", "ไม่มียาที่แพทย์สั่ง"]
)

st.markdown("## 🍵 สูตรชาสมุนไพร")

tea = "ชาใบเชียงดาผสมใบหม่อน"

st.markdown(
    f"""
    <div class="card">
    🌿 <h3>{tea}</h3>
    เป็นสูตรชาสมุนไพรที่ใช้ใบเชียงดาผสมกับใบหม่อน
    <br><br>
    💚 แนะนำให้ดื่มแบบ <b>ไม่เติมน้ำตาลหรือน้ำเชื่อม</b>
    <br>
    ⚠️ ชาสมุนไพรไม่ควรใช้แทนยาที่แพทย์สั่ง
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("## 🎯 เป้าหมายการดื่มชา")

goal = st.number_input(
    "ตั้งเป้าหมายการดื่มชาต่อวัน (ครั้ง)",
    min_value=1,
    max_value=3,
    value=1,
    step=1
)

drunk = st.number_input(
    "วันนี้ดื่มไปแล้วกี่ครั้ง?",
    min_value=0,
    max_value=goal,
    value=0,
    step=1
)

remaining = max(goal - drunk, 0)

if drunk < goal:
    st.info(
        f"🌱 วันนี้เธอยังเหลืออีก {remaining} ครั้งถึงจะครบเป้าหมายค่ะ"
    )
else:
    st.markdown(
        """
        <div class="success-box">
        🎉 <h3>เก่งมากค่ะ! ครบเป้าหมายแล้ว 💚</h3>
        🌿 น้องใบชาภูมิใจในตัวเธอนะคะ
        </div>
        """,
        unsafe_allow_html=True
    )

    components.html("""
    <button onclick="speakGoal()" style="
        background:#75a878;
        color:white;
        border:none;
        padding:12px 24px;
        border-radius:25px;
        font-size:16px;
        cursor:pointer;">
        🔊 น้องใบชาพูดให้กำลังใจ
    </button>

    <script>
    function speakGoal() {
        let msg = new SpeechSynthesisUtterance(
            "เก่งมากค่ะ วันนี้เธอดื่มชาครบตามเป้าหมายแล้วนะคะ อย่าลืมดูแลสุขภาพและกินยาตามแพทย์สั่งด้วยค่ะ น้องใบชาเป็นกำลังใจให้นะคะ"
        );
        msg.lang = "th-TH";
        msg.rate = 0.90;
        msg.pitch = 1.20;
        msg.volume = 1.0;
        speechSynthesis.cancel();
        speechSynthesis.speak(msg);
    }
    </script>
    """, height=65)
    # =========================
# Analyze
# =========================

st.markdown("## 🧮 วิเคราะห์ข้อมูล")

if st.button("🌱 วิเคราะห์คำแนะนำ", use_container_width=True):

    # BMI
    bmi = weight / ((height / 100) ** 2)

    if bmi < 18.5:
        bmi_text = "น้ำหนักน้อยกว่าเกณฑ์"
    elif bmi < 23:
        bmi_text = "อยู่ในเกณฑ์ปกติ"
    elif bmi < 25:
        bmi_text = "เริ่มมีน้ำหนักเกิน"
    elif bmi < 30:
        bmi_text = "น้ำหนักเกิน"
    else:
        bmi_text = "อ้วน"

    st.markdown(
        f"""
        <div class="result">
        📊 <b>BMI ของเธอ: {bmi:.1f}</b>
        <br>
        สถานะโดยประมาณ: {bmi_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # Sample Amount
    # =========================

    amount = 200

    if age < 12:
        amount = 100
    elif age < 18:
        amount = 150
    elif age >= 60:
        amount = 150

    if "โรคไต" in diseases:
        amount = 100

    if bmi >= 30:
        amount = min(amount, 150)
    elif bmi >= 25:
        amount = min(amount, 200)

    st.markdown(
        f"""
        <div class="card">
        💧 <b>ปริมาณตัวอย่างต่อครั้ง</b>
        <br><br>
        ประมาณ <b>{amount} มล.</b> ต่อครั้ง
        <br>
        <span style="font-size:14px;color:#718071;">
        *เป็นเพียงตัวอย่างสำหรับต้นแบบ ไม่ใช่คำสั่งทางการแพทย์
        </span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # BMI Condition
    # =========================

    if bmi >= 30:
        st.warning(
            "⚖️ จากค่า BMI ควรให้ความสำคัญกับการควบคุมอาหาร "
            "การออกกำลังกาย และเลือกเครื่องดื่มที่ไม่เติมน้ำตาลค่ะ"
        )

    elif bmi >= 25:
        st.info(
            "⚖️ จากค่า BMI ควรเลือกเครื่องดื่มที่ไม่เติมน้ำตาล "
            "และดูแลอาหารร่วมกับการเคลื่อนไหวร่างกายค่ะ"
        )

    else:
        st.success(
            "💚 ควรดูแลสุขภาพโดยรวม เลือกอาหารที่เหมาะสม "
            "และพักผ่อนให้เพียงพอค่ะ"
        )

    # =========================
    # Age Condition
    # =========================

    if age < 18:
        st.info(
            "🎂 เนื่องจากอายุต่ำกว่า 18 ปี "
            "ควรให้ผู้ปกครองหรือบุคลากรทางการแพทย์ "
            "ช่วยพิจารณาก่อนใช้สมุนไพรเป็นประจำค่ะ"
        )

    elif age >= 65:
        st.info(
            "🎂 สำหรับผู้สูงอายุ ควรระมัดระวังการใช้สมุนไพร "
            "โดยเฉพาะหากมีโรคประจำตัวหรือใช้ยาหลายชนิดค่ะ"
        )

    # =========================
    # Kidney Condition
    # =========================

    if "โรคไต" in diseases:
        st.warning(
            "🩺 หากมีโรคไต ควรปรึกษาแพทย์หรือเภสัชกร "
            "ก่อนดื่มชาสมุนไพรเป็นประจำค่ะ"
        )

    # =========================
    # Diabetes Condition
    # =========================

    if "เบาหวาน" in diseases:
        st.info(
            "🍵 หากเป็นเบาหวาน แนะนำให้ดื่มแบบไม่เติมน้ำตาล "
            "หรือน้ำเชื่อม และไม่ใช้ชาแทนยารักษาเบาหวานค่ะ"
        )

    # =========================
    # Heart Condition
    # =========================

    if "โรคหัวใจ" in diseases:
        st.warning(
            "❤️ หากมีโรคหัวใจ ควรแจ้งแพทย์หรือเภสัชกร "
            "เกี่ยวกับสมุนไพรที่ต้องการใช้ค่ะ"
        )

    # =========================
    # Hypertension Condition
    # =========================

    if "ความดันโลหิตสูง" in diseases:
        st.info(
            "💚 หากมีความดันโลหิตสูง ควรเลือกเครื่องดื่ม "
            "ที่ไม่เติมน้ำตาล และปรึกษาผู้เชี่ยวชาญ "
            "หากใช้สมุนไพรเป็นประจำค่ะ"
        )

    # =========================
    # Medicine Condition
    # =========================

    if medicine_taken == "ยังไม่ได้กิน":
        st.warning(
            "💊 วันนี้ยังไม่ได้กินยาตามแพทย์สั่ง "
            "ไม่ควรใช้ชาสมุนไพรแทนยานะคะ "
            "ควรปฏิบัติตามคำสั่งแพทย์ค่ะ"
        )

    elif medicine_taken == "กินแล้ว":
        st.success(
            "💊 ดีมากค่ะ กินยาตามแพทย์สั่งแล้ว "
            "อย่าลืมปฏิบัติตามคำแนะนำของแพทย์อย่างต่อเนื่องนะคะ"
        )

    if medicine.strip():
        st.warning(
            "💊 เนื่องจากเธอมีการใช้ยาอยู่ "
            "ควรแจ้งชื่อยาให้แพทย์หรือเภสัชกรตรวจสอบ "
            "ก่อนใช้สมุนไพรเป็นประจำค่ะ"
        )

    # =========================
    # AI Message
    # =========================

    if "โรคไต" in diseases:

        message = (
            "สวัสดีค่ะ 🌿 เนื่องจากเธอมีโรคไต "
            "ควรปรึกษาแพทย์หรือเภสัชกรก่อนดื่ม "
            "ชาสมุนไพรเป็นประจำค่ะ "
            "และไม่ควรใช้ชาแทนยาที่แพทย์สั่งนะคะ 💚"
        )

    elif "เบาหวาน" in diseases:

        message = (
            "สวัสดีค่ะ 🌿 สำหรับเธอที่เป็นเบาหวาน "
            "แนะนำให้เลือกชาใบเชียงดาผสมใบหม่อน "
            "แบบไม่เติมน้ำตาลหรือน้ำเชื่อมค่ะ "
            "และควรกินยาตามแพทย์สั่งตามปกตินะคะ 💚"
        )

    elif medicine.strip():

        message = (
            "สวัสดีค่ะ 🌿 เนื่องจากเธอมียาที่ใช้อยู่ "
            "ควรให้แพทย์หรือเภสัชกรตรวจสอบ "
            "การใช้ร่วมกับสมุนไพรค่ะ "
            "ดูแลตัวเองดี ๆ นะคะ 💚"
        )

    else:

        message = (
            "สวัสดีค่ะ 🌿 จากข้อมูลของเธอ "
            "สามารถดูแลสุขภาพโดยเลือกชา "
            "ใบเชียงดาผสมใบหม่อนแบบไม่เติมน้ำตาล "
            "ร่วมกับการดูแลสุขภาพโดยรวมค่ะ 💚"
        )

    st.markdown("## 🤖 น้องใบชา")

    st.markdown(
        f"""
        <div class="speech">
        {message}
        </div>
        """,
        unsafe_allow_html=True
    )

    # =========================
    # Voice
    # =========================

    safe_message = (
        message
        .replace("\\", "\\\\")
        .replace("`", "\\`")
    )

    components.html(
        f"""
        <button onclick="speakAI()" style="
            background:#75a878;
            color:white;
            border:none;
            padding:12px 24px;
            border-radius:25px;
            font-size:16px;
            cursor:pointer;">
            🔊 ให้น้องใบชาพูด
        </button>

        <script>
        function speakAI() {{

            let msg = new SpeechSynthesisUtterance(
                `{safe_message}`
            );

            msg.lang = "th-TH";
            msg.rate = 0.90;
            msg.pitch = 1.20;
            msg.volume = 1.0;

            let voices = speechSynthesis.getVoices();

            let thaiVoice = voices.find(
                v => v.lang &&
                v.lang.toLowerCase().startsWith("th")
            );

            if (thaiVoice) {{
                msg.voice = thaiVoice;
            }}

            speechSynthesis.cancel();
            speechSynthesis.speak(msg);
        }}
        </script>
        """,
        height=65
    )


# =========================
# Tea Information
# =========================

st.markdown("---")

st.markdown("""
<div class="card">

🍵 <b>ข้อมูลสูตรชา</b>

<br><br>

🌿 สูตรชาที่ใช้ในต้นแบบนี้คือ
<b>ชาใบเชียงดาผสมใบหม่อน</b>

<br><br>

💚 แนะนำให้ดื่มแบบ
<b>ไม่เติมน้ำตาลหรือน้ำเชื่อม</b>

<br><br>

⚠️ ชาสมุนไพรไม่ควรใช้แทนยาที่แพทย์สั่ง

<br>

🩺 หากมีโรคประจำตัวหรือใช้ยา
ควรปรึกษาแพทย์หรือเภสัชกร
ก่อนใช้สมุนไพรเป็นประจำ

</div>
""", unsafe_allow_html=True)


# =========================
# Footer
# =========================

st.markdown("---")

st.caption("🌿 HerbCare AI | Educational Prototype")

st.caption(
    "⚠️ ข้อมูลทั้งหมดเป็นข้อมูลเบื้องต้นเพื่อการศึกษา "
    "ไม่ใช่การวินิจฉัยหรือคำสั่งการรักษาจากแพทย์"
)

st.caption(
    "⚠️ ปริมาณการดื่มที่แสดงเป็นตัวอย่างสำหรับต้นแบบ "
    "ควรได้รับคำแนะนำจากบุคลากรทางการแพทย์ตามแต่ละบุคคล"
)
