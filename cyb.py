import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="AI Cyber Detective", page_icon="🕵️‍♂️", layout="centered"
)

# عنوان المنصة
st.title("🕵️‍♂️ AI Cyber Detective: حقيقة أم تزييف؟")
st.write(
    "مرحباً بك أيها المحقق! مهمتك اليوم هي كشف الرسائل الاحتيالية والصور المزيفة التي تولدت بالذكاء الاصطناعي لحماية المجتمع."
)
st.markdown("---")

# تخزين النقاط في حالة الجلسة
if "score" not in st.session_state:
    st.session_state.score = 0

# السؤال الأول: رسالة تصيد احتيالي (Phishing)
st.subheader("التحدي الأول: اختبار الرسائل النصية")
st.write("وصلتك هذه الرسالة على هاتفك:")
st.info(
    "عزيزي العميل، تم تجميد حسابك البنكي لتحديث البيانات. يرجى الضغط على الرابط التالي فوراً لتجنب إيقاف الخدمات: [www.bank-update-secure.com]"
)

answer1 = st.radio(
    "هل هذه الرسالة حقيقية أم احتيالية؟",
    ["اختر الإجابة...", "حقيقية أمنية ✅", "احتيالية ومشبوهة 🚨"],
    key="q1",
)

if answer1 == "احتيالية ومشبوهة 🚨":
    st.success("إجابة صحيحة! 🎯 البنوك لا تطلب تحديث البيانات عبر روابط نصية.")
    st.session_state.score += 1
elif answer1 == "حقيقية أمنية ✅":
    st.error("خطأ! هذه رسالة تصيد احتيالي هدفها سرقة بياناتك.")

st.markdown("---")

# زر إنهاء التحدي وعرض النتيجة والبالونات
if st.button("إظهار النتيجة النهائية 🏆"):
    st.write(f"لقد جمعت {st.session_state.score} من أصل 1 نقطة.")
    if st.session_state.score > 0:
        st.balloons()  # حركة البالونات المجنونة والجميلة!
        st.success("أنت محقّق أمن سيبراني ممتاز!")
    else:
        st.warning("حاول مرة أخرى في الجلسة القادمة!")
