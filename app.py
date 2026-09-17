import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="HerbCare AI 🌿",
    page_icon="🌿",
    layout="wide"
)

# ==============================
# 🎨 STYLE
# ==============================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#f4fff5,#fffaf0);
}

.main-title {
    text-align:center;
    color:#397653;
    font-size:42px;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    color:#78917d;
    font-size:18px;
    margin-bottom:25px;
}

.card {
    background:white;
    padding:25px;
    border-radius:25px;
    border:2px solid #dcefdc;
    box-shadow:0 5px 15px rgba(80,140,90,.08);
    margin-bottom:20px;
}

.baicha {
    text-align:center;
    font-size:90px;
    padding:15px;
}

.congrats {
    background:linear-gradient(135deg,#effff0,#fff9d9);
    padding:20px;
    border-radius:25px;
    border:2px solid #cde8c9;
    text-align:center;
    font-size:20px;
    color:#397653;
    margin:15px 0;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# 🌿 HEADER
# ==============================

st.markdown(
    '<div class="main-title">🌿 HerbCare AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">ผู้ช่วยแนะนำการดื่มชาสมุนไพรสำหรับผู้ที่เป็นเบาหวาน 💚</div>',
    unsafe_allow_html=True
)

# ==============================
# 👤 USER DATA
# ==============================

col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### 👤 ข้อมูลของคุณ")

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
        value=165.0,
        step=1.0
    )

    age = st.number_input(
        "🎂 อายุ",
        min_value=1,
        max_value=120,
        value=18
    )

    diseases = st.multiselect(
        "🩺 โรคประจำตัว",
        [
            "เบาหวาน",
            "โรคไต",
            "โรคตับ",
            "ความดันโลหิตสูง",
            "โรคหัวใจ",
            "ไม่มีโรคประจำตัวอื่น"
        ]
    )

    # 💊 เพิ่มสถานะการกินยา
    medicine_status = st.radio(
        "💊 วันนี้รับประทานยาตามที่แพทย์สั่งแล้วหรือยัง?",
        [
            "ยังไม่ได้รับประทานยา",
            "รับประทานยาแล้ว"
        ]
    )

    medication = st.text_input(
        "ชื่อยาที่กำลังรับประทาน (ถ้ามี)",
        placeholder="เช่น ยาลดน้ำตาล / ยาความดัน"
    )

    tea = st.selectbox(
        "🍵 เลือกชาสมุนไพร",
        [
            "ชาหญ้าหวาน",
            "ชาใบหม่อน",
            "ชาอบเชย",
            "ชาขิง",
            "ชาเขียว"
        ]
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ==============================
# 👧🏻 NONG BAICHA
# ==============================

with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("### 🌿 น้องใบชา")

    st.markdown(
        '<div class="baicha">👧🏻🌿🍵</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
        text-align:center;
        color:#397653;
        font-size:21px;
        font-weight:bold;">
        สวัสดีค่ะ~ ฉันคือน้องใบชา 💚
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
        text-align:center;
        color:#78917d;
        margin-top:10px;">
        กรอกข้อมูล แล้วให้น้องใบชาช่วยวิเคราะห์กันนะคะ ✨
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ==============================
# 📊 BMI
# ==============================

bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
    bmi_status = "น้ำหนักน้อย"
elif bmi < 23:
    bmi_status = "อยู่ในเกณฑ์ปกติ"
elif bmi < 25:
    bmi_status = "น้ำหนักเกิน"
elif bmi < 30:
    bmi_status = "อ้วนระดับ 1"
else:
    bmi_status = "อ้วนระดับ 2 ขึ้นไป"


# ==============================
# 🥤 DRINK AMOUNT
# ==============================

if "โรคไต" in diseases:
    drink_amount = 200
    drink_times = "ควรปรึกษาแพทย์หรือเภสัชกรเรื่องความถี่"

elif age < 18:
    drink_amount = 200
    drink_times = "วันละ 1 ครั้ง"

elif age >= 65:
    drink_amount = 200
    drink_times = "วันละ 1 ครั้ง"

elif bmi >= 30:
    drink_amount = 200
    drink_times = "วันละ 1–2 ครั้ง"

elif bmi >= 25:
    drink_amount = 250
    drink_times = "วันละ 1 ครั้ง"

else:
    drink_amount = 250
    drink_times = "วันละ 1–2 ครั้ง"


# ==============================
# 🍵 TEA INFORMATION
# ==============================

tea_info = {

    "ชาหญ้าหวาน":
    "เลือกแบบไม่เติมน้ำตาล และตรวจสอบส่วนผสมว่าไม่มีน้ำตาลแฝง",

    "ชาใบหม่อน":
    "สามารถเลือกดื่มแบบไม่เติมน้ำตาลได้",

    "ชาอบเชย":
    "ควรดื่มในปริมาณพอเหมาะ และหลีกเลี่ยงการเติมน้ำตาล",

    "ชาขิง":
    "สามารถดื่มแบบไม่เติมน้ำตาล และสังเกตการตอบสนองของร่างกาย",

    "ชาเขียว":
    "ควรเลือกสูตรไม่เติมน้ำตาล และระวังคาเฟอีนหากไวต่อคาเฟอีน"
}

recommendation = tea_info[tea]


# ==============================
# 🔎 ANALYZE
# ==============================

if st.button(
    "✨ วิเคราะห์โดยน้องใบชา ✨",
    use_container_width=True
):

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.markdown("## 🌿 ผลการวิเคราะห์เบื้องต้น")

    st.markdown(
        f"### 🍵 ชาที่เลือก: **{tea}**"
    )

    st.markdown(
        f"### 📊 BMI: **{bmi:.1f}**"
    )

    st.write(
        f"สถานะ BMI: **{bmi_status}**"
    )

    st.markdown("---")

    # ==============================
    # 💊 CONGRATULATIONS
    # ==============================

    if medicine_status == "รับประทานยาแล้ว":

        st.markdown(
            """
            <div class="congrats">
            🎉💚 ยินดีด้วยนะคะ! 💚🎉<br><br>
            เก่งมากเลยค่ะที่รับประทานยาตามที่แพทย์สั่งแล้ว ✨<br>
            อย่าลืมดูแลตัวเองและทำตามคำแนะนำของแพทย์อย่างสม่ำเสมอนะคะ 🌿
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.warning(
            "💊 อย่าลืมรับประทานยาตามที่แพทย์สั่งนะคะ "
            "หากลืมรับประทานยา ไม่ควรเพิ่มขนาดยาเองค่ะ"
        )

    # ==============================
    # 🥤 DRINK
    # ==============================

    st.markdown("### 🥤 ปริมาณชาที่แนะนำเบื้องต้น")

    st.success(
        f"ประมาณ **{drink_amount} มิลลิลิตรต่อครั้ง**"
    )

    st.info(
        f"ความถี่: **{drink_times}**"
    )

    st.markdown("### 🌿 คำแนะนำ")

    st.write(recommendation)

    if "โรคไต" in diseases:

        st.warning(
            "⚠️ เนื่องจากมีโรคไต ควรปรึกษาแพทย์หรือเภสัชกร "
            "ก่อนกำหนดปริมาณและความถี่ในการดื่ม"
        )

    if medication.strip():

        st.warning(
            "💊 หากกำลังใช้ยา ควรตรวจสอบปฏิกิริยาระหว่างสมุนไพรกับยา "
            "กับแพทย์หรือเภสัชกร"
        )

    st.markdown("---")

    st.markdown("### 💚 ข้อความจากน้องใบชา")

    if medicine_status == "รับประทานยาแล้ว":

        st.write(
            f"สวัสดีค่ะ~ 🌿 วันนี้คุณรับประทานยาแล้ว "
            f"น้องใบชาดีใจด้วยนะคะ! 🎉💚 "
            f"สำหรับ {tea} แนะนำให้เลือกแบบไม่เติมน้ำตาลค่ะ "
            f"และควรดื่มในปริมาณที่เหมาะสมค่ะ~"
        )

    else:

        st.write(
            f"สวัสดีค่ะ~ 🌿 "
            f"วันนี้อย่าลืมรับประทานยาตามที่แพทย์สั่งนะคะ 💚 "
            f"สำหรับ {tea} ควรเลือกแบบไม่เติมน้ำตาลค่ะ~"
        )

    st.markdown("</div>", unsafe_allow_html=True)


    # ==============================
    # 🔊 ANIME VOICE
    # ==============================

    if medicine_status == "รับประทานยาแล้ว":

        speech = (
            f"เย้~! ยินดีด้วยนะคะ! "
            f"วันนี้คุณรับประทานยาแล้ว เก่งมากเลยค่ะ~ "
            f"น้องใบชาดีใจด้วยนะคะ! "
            f"อย่าลืมดูแลตัวเองต่อไปนะคะ~ "
            f"สำหรับ {tea} อย่าลืมเลือกแบบไม่เติมน้ำตาลนะคะ!"
        )

    else:

        speech = (
            "สวัสดีค่ะ~ ฉันคือน้องใบชานะคะ~ "
            "วันนี้อย่าลืมรับประทานยาตามที่แพทย์สั่งนะคะ "
            "ดูแลตัวเองดี ๆ นะคะ~ "
            f"และสำหรับ {tea} "
            "อย่าลืมเลือกแบบไม่เติมน้ำตาลนะคะ~"
        )

    speech_js = json.dumps(speech)

    st.markdown("## 🔊 เสียงน้องใบชา")

    components.html(
        f"""
        <div style="
            background:linear-gradient(135deg,#f1fff3,#fffaf0);
            padding:24px;
            border-radius:25px;
            text-align:center;
            border:2px solid #d9eedc;
        ">

        <div style="
            font-size:22px;
            color:#397653;
            font-weight:bold;
            margin-bottom:12px;">
            🌿💚 น้องใบชาพร้อมพูดแล้ว! 💚🌿
        </div>

        <div style="
            font-size:15px;
            color:#78917d;
            margin-bottom:18px;">
            ✨ กดปุ่มให้น้องใบชาพูด ✨
        </div>

        <button onclick="speakBaicha()" style="
            background:linear-gradient(135deg,#72b47b,#91c98f);
            color:white;
            border:none;
            padding:15px 32px;
            border-radius:35px;
            font-size:19px;
            font-weight:bold;
            box-shadow:0 5px 12px rgba(80,140,90,.25);
            cursor:pointer;">
            🔊✨ พูดให้ฟังหน่อยค่ะ
        </button>

        <script>

        function speakBaicha() {{

            const text = {speech_js};

            window.speechSynthesis.cancel();

            const msg =
                new SpeechSynthesisUtterance(text);

            msg.lang = "th-TH";

            // 💕 ฟีลเสียงอนิเมะน่ารัก
            msg.rate = 0.78;
            msg.pitch = 1.70;
            msg.volume = 1.0;

            const voices =
                window.speechSynthesis.getVoices();

            let thaiVoice = voices.find(
                v => v.lang &&
                v.lang.toLowerCase() === "th-th"
            );

            if (!thaiVoice) {{

                thaiVoice = voices.find(
                    v => v.lang &&
                    v.lang.
