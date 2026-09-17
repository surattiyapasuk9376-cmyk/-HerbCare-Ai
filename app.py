import streamlit as st
import streamlit.components.v1 as components
import json
import base64
from pathlib import Path

# =========================
# 🌿 HerbCare AI
# =========================

st.set_page_config(
    page_title="HerbCare AI 🌿",
    page_icon="🌿",
    layout="wide"
)

# =========================
# 🎨 CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f4fff7, #fffdf2);
}

/* หัวเว็บ */
.main-title {
    text-align: center;
    color: #4f8060;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #777;
    font-size: 18px;
    margin-bottom: 30px;
}

/* กล่อง */
.card {
    background-color: white;
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

/* 🌿 Animation น้องใบชา */
.baicha-wrap {
    text-align: center;
    padding: 10px;
}

.baicha-img {
    width: 330px;
    max-width: 90%;
    animation: baichaFloat 3s ease-in-out infinite;
    filter: drop-shadow(0px 10px 12px rgba(80,120,80,0.15));
}

@keyframes baichaFloat {

    0% {
        transform: translateY(0px) rotate(0deg);
    }

    50% {
        transform: translateY(-12px) rotate(1deg);
    }

    100% {
        transform: translateY(0px) rotate(0deg);
    }
}

.baicha-name {
    color: #5d896a;
    font-size: 27px;
    font-weight: bold;
    margin-top: 8px;
}

.speech {
    display: inline-block;
    background-color: #f1faef;
    border-radius: 20px;
    padding: 15px 22px;
    font-size: 17px;
    color: #42634b;
    margin-top: 10px;
    animation: speechFloat 2.5s ease-in-out infinite;
}

@keyframes speechFloat {

    0%, 100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.03);
    }
}

/* ผลลัพธ์ */
.result {
    background-color: #f7fff5;
    border-left: 6px solid #79ad83;
    padding: 20px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# 🌿 Header
# =========================

st.markdown(
    '<div class="main-title">🌿 HerbCare AI 🍵</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'ผู้ช่วยแนะนำการดื่มชาสมุนไพรเบื้องต้นสำหรับผู้ที่เป็นเบาหวาน'
    '</div>',
    unsafe_allow_html=True
)


# =========================
# 🍵 สูตรชา
# =========================

tea = "ชาใบเขียวดาวเรืองผสมใบหม่อน"


# =========================
# 👤 ข้อมูลผู้ใช้
# =========================

col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("👤 ข้อมูลของคุณ")

    weight = st.number_input(
        "น้ำหนัก (กิโลกรัม)",
        min_value=20.0,
        max_value=200.0,
        value=60.0,
        step=0.5
    )

    height = st.number_input(
        "ส่วนสูง (เซนติเมตร)",
        min_value=100.0,
        max_value=220.0,
        value=160.0,
        step=1.0
    )

    age = st.number_input(
        "อายุ (ปี)",
        min_value=10,
        max_value=100,
        value=18,
        step=1
    )

    disease = st.multiselect(
        "โรคประจำตัว",
        [
            "เบาหวาน",
            "ความดันโลหิตสูง",
            "โรคไต",
            "โรคหัวใจ",
            "ไม่มีโรคประจำตัว"
        ]
    )

    medicine_status = st.radio(
        "วันนี้รับประทานยาตามที่แพทย์สั่งแล้วหรือยัง?",
        [
            "ยังไม่ได้รับประทานยา",
            "รับประทานยาแล้ว"
        ]
    )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================
# 🌱 น้องใบชา
# =========================

with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    mascot_path = Path("nong_baicha_mascot.png")

    if mascot_path.exists():

        image_data = base64.b64encode(
            mascot_path.read_bytes()
        ).decode()

        st.markdown(
            f"""
            <div class="baicha-wrap">

                <img
                    class="baicha-img"
                    src="data:image/png;base64,{image_data}"
                >

                <div class="baicha-name">
                    น้องใบชา 🌱
                </div>

                <div class="speech">
                    สวัสดีค่ะ 💚<br>
                    วันนี้มาดูแลตัวเองไปด้วยกันนะคะ 🍵✨
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.warning(
            "⚠️ ไม่พบไฟล์ nong_baicha_mascot.png "
            "กรุณาใส่ไฟล์ไว้ในโฟลเดอร์เดียวกับ app.py"
        )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================
# 🎯 เป้าหมายการดื่มชา
# =========================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🎯 เป้าหมายการดื่มชาวันนี้")

target = st.number_input(
    "ตั้งเป้าหมายการดื่มชาวันนี้ (ครั้ง)",
    min_value=1,
    max_value=3,
    value=1,
    step=1
)

completed = st.number_input(
    "วันนี้ดื่มชาไปแล้วกี่ครั้ง?",
    min_value=0,
    max_value=3,
    value=0,
    step=1
)


# =========================
# 💚 ระบบให้กำลังใจ
# =========================

if completed >= target:

    st.success(
        "🎉🌿 เก่งมากเลยค่ะ! "
        "วันนี้เธอดื่มชาสมุนไพรครบตามเป้าหมายแล้ว 💚🍵\n\n"
        "น้องใบชาภูมิใจในตัวเธอมาก ๆ เลยค่ะ ✨ "
        "ค่อย ๆ ดูแลตัวเองแบบนี้ต่อไปนะคะ "
        "ไม่ต้องกดดันตัวเอง แค่ทำได้อย่างสม่ำเสมอก็เก่งมากแล้วค่ะ 🥰"
    )

    encouragement = (
        "เก่งมากเลยค่ะ วันนี้เธอดื่มชาสมุนไพรครบตามเป้าหมายแล้ว "
        "น้องใบชาภูมิใจในตัวเธอมาก ๆ เลยค่ะ "
        "ค่อย ๆ ดูแลตัวเองแบบนี้ต่อไปนะคะ "
        "ไม่ต้องกดดันตัวเอง แค่ทำได้อย่างสม่ำเสมอ "
        "ก็เก่งมากแล้วค่ะ"
    )

    speech_json = json.dumps(
        encouragement,
        ensure_ascii=False
    )

    components.html(
        """
        <script>

        const text = %s;

        function speakBaicha() {

            if (!("speechSynthesis" in window)) {
                return;
            }

            window.speechSynthesis.cancel();

            const voices =
                window.speechSynthesis.getVoices();

            let thaiVoice = voices.find(
                voice =>
                voice.lang.toLowerCase().startsWith("th")
            );

            const msg =
                new SpeechSynthesisUtterance(text);

            if (thaiVoice) {
                msg.voice = thaiVoice;
            }

            msg.lang = "th-TH";

            /* 🌸 เสียงสาววัยเรียน น่ารักสมวัย */
            msg.rate = 0.90;
            msg.pitch = 1.25;
            msg.volume = 1.0;

            window.speechSynthesis.speak(msg);
        }

        if (
            window.speechSynthesis.getVoices().length > 0
        ) {
            speakBaicha();
        } else {
            window.speechSynthesis.onvoiceschanged =
                speakBaicha;
        }

        </script>
        """ % speech_json,
        height=0
    )


elif completed > 0:

    remaining = target - completed

    st.info(
        f"🌱 อีกนิดเดียวเองค่ะ! "
        f"วันนี้เหลืออีก {remaining} ครั้ง "
        f"ก็จะครบเป้าหมายแล้วนะคะ 💚🍵 "
        f"ค่อย ๆ ทำไป ไม่ต้องรีบค่ะ ✨"
    )


else:

    st.info(
        "🌿 วันนี้มาเริ่มดูแลตัวเองไปพร้อมกับน้องใบชา "
        "กันนะคะ 💚 ค่อย ๆ ทำตามเป้าหมายที่ตั้งไว้ "
        "ไม่ต้องกดดันตัวเองค่ะ 🍵✨"
    )

st.markdown("</div>", unsafe_allow_html=True)


# =========================
# 🧮 BMI
# =========================

height_m = height / 100

bmi = weight / (height_m ** 2)


# =========================
# 💧 ปริมาณตัวอย่าง
# =========================

if "โรคไต" in disease:

    drink_amount = (
        "ควรปรึกษาแพทย์หรือเภสัชกร "
        "ก่อนกำหนดปริมาณการดื่ม"
    )

elif age < 18:

    drink_amount = (
        "ประมาณ 200 มล. ต่อครั้ง "
        "และควรปรึกษาผู้ปกครองหรือบุคลากรทางการแพทย์"
    )

elif age >= 65:

    drink_amount = (
        "ประมาณ 200 มล. ต่อครั้ง "
        "และควรสังเกตการตอบสนองของร่างกาย"
    )

elif bmi >= 30:

    drink_amount = "ประมาณ 200 มล. ต่อครั้ง"

elif bmi >= 25:

    drink_amount = "ประมาณ 250 มล. ต่อครั้ง"

else:

    drink_amount = "ประมาณ 250 มล. ต่อครั้ง"


# =========================
# 🌿 ข้อมูลชา
# =========================

tea_info = {

    "name":
        "ชาใบเขียวดาวเรืองผสมใบหม่อน",

    "description":
        "ชาสมุนไพรสูตรผสมใบเขียวดาวเรือง "
        "และใบหม่อน สำหรับใช้เป็นเครื่องดื่ม "
        "ในชีวิตประจำวัน",

    "advice":
        "ควรดื่มโดยไม่เติมน้ำตาลหรือน้ำเชื่อม "
        "และไม่ควรใช้ชาแทนยาที่แพทย์สั่ง"
}


# =========================
# 🔍 วิเคราะห์
# =========================

st.markdown('<div class="card">', unsafe_allow_html=True)

if st.button(
    "🌿 วิเคราะห์คำแนะนำให้ฉัน",
    use_container_width=True
):

    st.subheader("💚 ผลการวิเคราะห์เบื้องต้น")

    st.markdown(
        f"""
        <div class="result">

        <h3>🍵 {tea_info["name"]}</h3>

        <p>
        <b>📏 BMI:</b> {bmi:.1f}
        </p>

        <p>
        <b>💧 ปริมาณตัวอย่างต่อครั้ง:</b>
        {drink_amount}
        </p>

        <p>
        <b>🌿 คำแนะนำ:</b>
        {tea_info["advice"]}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =========================
    # 💊 สถานะยา
    # =========================

    if medicine_status == "รับประทานยาแล้ว":

        st.success(
            "🎉💚 ยินดีด้วยนะคะ! "
            "วันนี้คุณรับประทานยาตามที่แพทย์สั่งแล้ว "
            "เก่งมากเลยค่ะ ✨"
        )

    else:

        st.warning(
            "💊 อย่าลืมรับประทานยาตามที่แพทย์สั่งนะคะ "
            "ชาไม่สามารถใช้แทนยารักษาโรคได้ค่ะ 🌿"
        )


    # =========================
    # 💬 ข้อความเฉพาะบุคคล
    # =========================

    if "โรคไต" in disease:

        message = (
            "เนื่องจากมีข้อมูลเกี่ยวกับโรคไต "
            "ควรปรึกษาแพทย์หรือเภสัชกร "
            "ก่อนดื่มเป็นประจำค่ะ 💚"
        )

    elif "เบาหวาน" in disease:

        message = (
            "ถ้าเป็นเบาหวาน แนะนำเลือกดื่มแบบไม่เติมน้ำตาล "
            "และติดตามระดับน้ำตาลตามคำแนะนำ "
            "ของ
