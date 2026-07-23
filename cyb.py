import streamlit as st

# إعداد الصفحة مع دعم اللغة العربية واتجاه اليمين لليسار
st.markdown(
    """
    <style>
    body, [data-testid="stAppViewContainer"] {
        direction: rtl;
        text-align: right;
    }
    .stRadio > label, .stMarkdown, p, h1, h2, h3 {
        direction: rtl;
        text-align: right;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# عنوان المنصة
st.title("🕵️‍♂️ AI Cyber Detective: حقيقة أم تزييف؟")
st.write(
    "مرحباً بك أيها المحقق! مهمتك اليوم هي كشف الرسائل الاحتيالية والصور المزيفة لحماية المجتمع."
)
st.markdown("---")

# تهيئة الأسئلة والنقاط
if "step" not in st.session_state:
    st.session_state.step = 1
if "score" not in st.session_state:
    st.session_state.score = 0

# --- السؤال الأول ---
if st.session_state.step == 1:
    st.subheader("التحدي الأول: اختبار الرسائل النصية")
    st.write("وصلتك هذه الرسالة على هاتفك:")
    st.info(
        "عزيزي العميل، تم تجميد حسابك البنكي لتحديث البيانات. يرجى الضغط على الرابط التالي فوراً: [www.bank-update.com]"
    )

    ans1 = st.radio(
        "هل هذه الرسالة حقيقية أم احتيالية؟",
        ["اختر الإجابة...", "حقيقية أمنية ✅", "احتيالية ومشبوهة 🚨"],
        key="r1",
    )

    if ans1 == "احتيالية ومشبوهة 🚨":
        st.success("إجابة صحيحة! البنوك لا تطلب تحديث البيانات عبر رسائل نصية.")
        if st.session_state.score == 0:
            st.session_state.score += 1
    elif ans1 == "حقيقية أمنية ✅":
        st.error("خطأ! هذه رسالة تصيد احتيالي هدفها سرقة بياناتك.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 2
        st.rerun()

# --- السؤال الثاني ---
elif st.session_state.step == 2:
    st.subheader("التحدي الثاني: كشف التزييف العميق (Deepfake)")
    st.write(
        "وصلك اتصال أو فيديو لشخص يطلب منك تحويل مبلغ طارئ بصوت أحد أصدقائك، ولكنه يقطع قليلاً."
    )

    ans2 = st.radio(
        "كيف تتصرف أو تحكم على هذا الاتصال؟",
        [
            "اختر الإجابة...",
            "أصدق فوراً وأحول المبلغ 💸",
            "أتحقق عبر وسيلة أخرى لأن الصوت قد يكون مولداً بالذكاء الاصطناعي 🤖",
        ],
        key="r2",
    )

    if (
        ans2
        == "أتحقق عبر وسيلة أخرى لأن الصوت قد يكون مولداً بالذكاء الاصطناعي 🤖"
    ):
        st.success("إجابة صحيحة جداً! التقنية تستخدم لتقليد الأصوات بحرفية.")
        st.session_state.score += 1
    elif ans2 == "أصدق فوراً وأحول المبلغ 💸":
        st.error("خطأ! هذا قد يكون فخ تزييف عميق (Deepfake).")

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ السابقة"):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("إظهار النتيجة النهائية 🏆"):
            st.session_state.step = 3
            st.rerun()

# --- النتيجة النهائية ---
elif st.session_state.step == 3:
    st.subheader("🏁 النتيجة النهائية للمحقق")
    st.write(f"لقد جمعت {st.session_state.score} من أصل 2 نقاط.")

    if st.session_state.score >= 2:
        st.balloons()
        st.success(
            "مذهل! أنت محقّق أمن سيبراني محترف وتمتلك عيناً فاحصة للتقنية!"
        )
    else:
        st.warning("حاول مرة أخرى لتطوير مهاراتك في كشف الاحتيال!")

    if st.button("🔄 إعادة اللعبة"):
        st.session_state.step = 1
        st.session_state.score = 0
        st.rerun()
