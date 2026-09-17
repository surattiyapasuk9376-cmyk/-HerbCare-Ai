import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="HerbCare AI",
    page_icon="🌿",
    layout="wide"
)

# =========================
# STYLE
# =========================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f4fff5, #fffaf0);
}

.title {
    text-align: center;
    color: #397653;
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #78917d;
    font-size: 17px;
    margin-bottom: 25px;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 22px;
    border: 2px solid #dcefdc;
    margin-bottom: 18px;
}

.baicha {
    text-align: center;
    font-size: 80px;
    padding: 15px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown(
    '<div class="title">🌿 HerbCare AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">ผู้ช่วยแนะนำการดื่มชาสมุนไพรสำหรับผู้ที่เป็นเบาหวาน 💚</div>',
    unsafe_allow_html=True
)

# =========================
# INPUT
# =========================

left, right = st.columns(2)

with left:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("👤 ข้อมูลของคุณ")

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

    medicine_status = st.radio(
        "💊 วันนี้รับประทานยาตามที่แพทย์สั่งแล้วหรือยัง?",
        [
            "ยังไม่ได้รับประทานยา",
            "รับประทานยาแล้ว"
        ]
    )

    medication = st.text_input(
        "ชื่อยาที่กำลังรับประทาน (ถ้ามี)"
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


# =========================
# BAICHA
# =========================

with right:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🌿 น้องใบชา")

    st.markdown(
        '<div class="baicha">👧🏻🌿🍵</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="text-align:center;color:#397653;font-size:21px;font-weight:bold;">สวัสดีค่ะ~ ฉันคือน้องใบชา 💚</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="text-align:center;color:#78917d;">กรอกข้อมูล แล้วให้น้องใบชาช่วยวิเคราะห์กันนะคะ ✨</p>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================
# BMI
# =========================

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


# =========================
# DRINK AMOUNT
# =========================

if "โรคไต" in diseases:

    drink_amount = 200
    drink_times = "ควรปรึกษาแพทย์หรือเภสัชกรเรื่องความถี่"

elif age < 18 or age >= 65:

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


# =========================
# TEA INFO
# =========================

tea_info = {

    "ชาหญ้าหวาน":
        "เลือกแบบไม่เติมน้ำตาล และตรวจสอบส่วนผสมว่าไม่มีน้ำตาลแฝง",

    "ชาใบหม่อน":
        "เลือกดื่มแบบไม่เติมน้ำตาลได้",

    "ชาอบเชย":
        "ควรดื่มในปริมาณพอเหมาะ และหลีกเลี่ยงการเติมน้ำตาล",

    "ชาขิง":
        "สามารถดื่มแบบไม่เติมน้ำตาล และสังเกตการตอบสนองของร่างกาย",

    "ชาเขียว":
        "ควรเลือกสูตรไม่เติมน้ำตาล และระวังคาเฟอีนหากไวต่อคาเฟอีน"
}


# =========================
# ANALYZE
# =========================

if st.button(
    "✨ วิเคราะห์โดยน้องใบชา ✨",
    use_container_width=True
):

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🌿 ผลการวิเคราะห์เบื้องต้น")

    st.write(
        f"🍵 ชาที่เลือก: **{tea}**"
    )

    st.write(
        f"📊 BMI: **{bmi:.1f}** — {bmi_status}"
    )

    st.markdown("### 🥤 ปริมาณชาที่แนะนำเบื้องต้น")

    st.success(
        f"ประมาณ **{drink_amount} มิลลิลิตรต่อครั้ง**"
    )

    st.info(
        f"ความถี่: **{drink_times}**"
    )

    st.markdown("### 🌿 คำแนะนำ")

    st.write(tea_info[tea])


    # =========================
    # MEDICINE MESSAGE
    # =========================

    if medicine_status == "รับประทานยาแล้ว":

        st.success(
            "🎉💚 ยินดีด้วยนะคะ! วันนี้คุณรับประทานยาตามที่แพทย์สั่งแล้ว "
            "เก่งมากเลยค่ะ ✨"
        )

        speech = (
            f"เย้~! ยินดีด้วยนะคะ! "
            f"วันนี้คุณรับประทานยาแล้ว "
            f"เก่งมากเลยค่ะ~ "
            f"น้องใบชาดีใจด้วยนะคะ! "
            f"สำหรับ {tea} "
            f"อย่าลืมเลือกแบบไม่เติมน้ำตาลนะคะ~"
        )

    else:

        st.warning(
            "💊 อย่าลืมรับประทานยาตามที่แพทย์สั่งนะคะ "
            "หากลืมยา ไม่ควรเพิ่มขนาดยาเองค่ะ"
        )

        speech = (
            "สวัสดีค่ะ~ ฉันคือน้องใบชานะคะ~ "
            "วันนี้อย่าลืมรับประทานยาตามที่แพทย์สั่งนะคะ "
            f"สำหรับ {tea} "
            "อย่าลืมเลือกแบบไม่เติมน้ำตาลนะคะ~"
        )


    if "โรคไต" in diseases:

        st.warning(
            "⚠️ หากมีโรคไต ควรปรึกษาแพทย์หรือเภสัชกร "
            "ก่อนกำหนดปริมาณและความถี่ในการดื่ม"
        )


    if medication.strip():

        st.warning(
            "💊 หากกำลังใช้ยา ควรตรวจสอบปฏิกิริยาระหว่าง "
            "สมุนไพรกับยากับแพทย์หรือเภสัชกร"
        )


    st.markdown("</div>", unsafe_allow_html=True)


    # =========================
    # VOICE
    # =========================

    st.subheader("🔊 เสียงน้องใบชา")

    speech_json = json.dumps(
        speech,
        ensure_ascii=False
    )

    voice_html = """
    <div style="
        background:#f1fff3;
        padding:22px;
        border-radius:22px;
        text-align:center;
        border:2px solid #d9eedc;
    ">

    <div style="
        font-size:21px;
        color:#397653;
        font-weight:bold;
        margin-bottom:15px;
    ">
        🌿💚 น้องใบชาพร้อมพูดแล้ว! 💚🌿
    </div>

    <button id="speakButton" style="
        background:#78b77e;
        color:white;
        border:0;
        padding:14px 28px;
        border-radius:30px;
        font-size:18px;
        font-weight:bold;
        cursor:pointer;
    ">
        🔊✨ พูดให้ฟังหน่อยค่ะ
    </button>

    <script>

    const text = %s;

    document
    .getElementById("speakButton")
    .addEventListener("click", function() {

        window.speechSynthesis.cancel();

        const message =
            new SpeechSynthesisUtterance(text);

        message.lang = "th-TH";
        message.rate = 0.78;
        message.pitch = 1.65;
        message.volume = 1;

        const voices =
            window.speechSynthesis.getVoices();

        const thaiVoice =
            voices.find(
                function(v) {
                    return v.lang &&
                    v.lang.toLowerCase() === "th-th";
                }
            );

        if (thaiVoice) {
            message.voice = thaiVoice;
        }

        window.speechSynthesis.speak(message);

    });

    </script>

    </div>
    """ % speech_json

    components.html(
        voice_html,
        height=175
    )


# =========================
# DISCLAIMER
# =========================

st.markdown("---")

st.caption(
    "⚠️ HerbCare AI เป็นโปรเจกต์เพื่อการศึกษา "
    "คำแนะนำเป็นข้อมูลเบื้องต้น ไม่ใช่การวินิจฉัยหรือคำสั่งรักษา "
    "ผู้ที่มีโรคประจำตัวหรือใช้ยาควรปรึกษาแพทย์หรือเภสัชกร"
)

st.caption(
    "🌿 HerbCare AI — ดูแลสุขภาพด้วยความรู้ และเลือกอย่างเหมาะสม 💚"
)
