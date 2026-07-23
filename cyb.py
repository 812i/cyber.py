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
    "مرحباً بك أيها المحقق! مهمتك اليوم هي اجتياز 7 تحديات أمنية لكشف الاحتيال الرقمي والتزييف العميق."
)
st.markdown("---")

# تهيئة الخطوات والنقاط
if "step" not in st.session_state:
    st.session_state.step = 1
if "score" not in st.session_state:
    st.session_state.score = 0

# --- السؤال الأول (معاد ترتيبه): التصيد عبر الإيميل (كان سؤال 4) ---
if st.session_state.step == 1:
    st.subheader("التحدي 1 من 7: الرسائل الوبرية (Phishing Email)")
    st.write(
        "وصلتك رسالة إيميل من (Netflix) تخبرك بأن اشتراكك سينتهي ويجب الدفع عبر رابط خارج الموقع الرسمي."
    )

    choice1 = st.radio(
        "ما الإجراء السليم؟",
        [
            "اختر...",
            "أدخل لتسجيل بيانات البطاقة مباشرة 💳",
            "أتجاهل الرابط وأدخل للتطبيق الرسمي للتأكد 🔒",
        ],
        key="q1",
    )

    if choice1 == "أتجاهل الرابط وأدخل للتطبيق الرسمي للتأكد 🔒":
        st.success("إجابة صحيحة! لا تضغط على روابط الإيميلات الخارجية أبداً.")
        if st.session_state.score < 1:
            st.session_state.score = 1
    elif choice1 == "أدخل لتسجيل بيانات البطاقة مباشرة 💳":
        st.error("خطأ! هذا إيميل احتيالي لسرقة حسابك.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 2
        st.rerun()

# --- السؤال الثاني: الرسائل النصية للبنوك (كان سؤال 1) ---
elif st.session_state.step == 2:
    st.subheader("التحدي 2 من 7: الرسائل النصية للبنوك")
    st.write(
        "وصلتك رسالة نصية تقول: *(تم تجميد حسابك البنكي، اضغط هنا لتحديث البيانات [www.bank-update.com])*."
    )

    choice2 = st.radio(
        "هل تعتقد أن هذه الرسالة آمنة أم احتيالية؟",
        ["اختر...", "آمنة وحقيقية ✅", "احتيالية ومشبوهة 🚨"],
        key="q2",
    )

    if choice2 == "احتيالية ومشبوهة 🚨":
        st.success("إجابة صحيحة! البنوك لا تطلب التحديث عبر روابط نصية.")
        if st.session_state.score < 2:
            st.session_state.score = 2
    elif choice2 == "آمنة وحقيقية ✅":
        st.error("خطأ! هذه رسالة تصيد هدفها سرقة بياناتك.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 3
        st.rerun()

# --- السؤال الثالث: المتاجر الإلكترونية الوهمية (كان سؤال 3) ---
elif st.session_state.step == 3:
    st.subheader("التحدي 3 من 7: المتاجر الإلكترونية الوهمية")
    st.write(
        "وجدت إعلاناً بخصوص متجر شهير يبيع ماركة عالمية بخصم 90% والرابط منتهي بـ (.xyz) أو حروف غير مرتبة."
    )

    choice3 = st.radio(
        "هل تثق في هذا الموقع وتشتري منه؟",
        ["اختر...", "نعم، الفرصة لا تعوض 🛒", "لا، متجر مشبوه واحتيالي 🛑"],
        key="q3",
    )

    if choice3 == "لا، متجر مشبوه واحتيالي 🛑":
        st.success(
            "إجابة صحيحة! المتاجر الوهمية تستغل الخصومات الخيالية لسرقة البطاقات."
        )
        if st.session_state.score < 3:
            st.session_state.score = 3
    elif choice3 == "نعم، الفرصة لا تعوض 🛒":
        st.error("خطأ! غالباً هذه المتاجر وهمية تسرق بيانات الدفع.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 4
        st.rerun()

# --- السؤال الرابع: الاتصالات الصوتية Deepfake (كان سؤال 2) ---
elif st.session_state.step == 4:
    st.subheader("التحدي 4 من 7: الاتصالات الصوتية (Deepfake)")
    st.write(
        "تلقيت اتصالاً بصوت مديرك يطلب منك تحويل مبلغ طارئ لحساب خارجي وبشكل عاجل جداً."
    )

    choice4 = st.radio(
        "كيف تتصرف؟",
        [
            "اختر...",
            "أحول المبلغ فوراً طالما أنه صوت المدير 💸",
            "أتحقق عبر قناة اتصال رسمية أخرى للتأكد 🤖",
        ],
        key="q4",
    )

    if (
        choice4
        == "أتحقق عبر قناة اتصال رسمية أخرى للتأكد 🤖"
    ):
        st.success("إجابة صحيحة! تقنيات التزييف العميق للأصوات منتشرة وخطيرة.")
        if st.session_state.score < 4:
            st.session_state.score = 4
    elif choice4 == "أحول المبلغ فوراً طالما أنه صوت المدير 💸":
        st.error("خطأ! قد يكون هذا الصوت مولداً بالذكاء الاصطناعي.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 5
        st.rerun()

# --- السؤال الخامس: الصور الذكية المزيفة (كان سؤال 5) ---
elif st.session_state.step == 5:
    st.subheader("التحدي 5 من 7: الصور الذكية المزيفة (Deepfake Images)")
    st.write(
        "انتشرت صورة لشخصية مشهورة في موقف غريب جداً، ولاحظت وجود تشوهات بسيطة في أطراف الأصابع والخلفية."
    )

    choice5 = st.radio(
        "كيف تحكم على هذه الصورة؟",
        ["اختر...", "صورة حقيقية 100% 📸", "صورة مولدة بالذكاء الاصطناعي 🎨"],
        key="q5",
    )

    if choice5 == "صورة مولدة بالذكاء الاصطناعي 🎨":
        st.success(
            "إجابة صحيحة! تفاصيل الأطراف والخلفيات غالباً تفضح الصور المزيفة."
        )
        if st.session_state.score < 5:
            st.session_state.score = 5
    elif choice5 == "صورة حقيقية 100% 📸":
        st.error("خطأ! هذه الصورة ولدت بواسطة الذكاء الاصطناعي.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 6
        st.rerun()

# --- السؤال السادس: التحديثات الرسمية للتطبيقات (كان سؤال 6) ---
elif st.session_state.step == 6:
    st.subheader("التحدي 6 من 7: التحديثات الرسمية للتطبيقات")
    st.write(
        "ظهر لك إشعار داخل تطبيق البنك الرسمي الموثق بجوالك يطلب منك التحديث لتحسين الأمان، وعند الضغط وجهك لمتجر التطبيقات الرسمي (App Store / Google Play)."
    )

    choice6 = st.radio(
        "هل هذا الإجراء آمن؟",
        ["اختر...", "آمن وموثوق طالما أنه داخل التطبيق الرسمي ومتجر معتمد ✅", "غير آمن ويجب حذفه 🚨"],
        key="q6",
    )

    if choice6 == "آمن وموثوق طالما أنه داخل التطبيق الرسمي ومتجر معتمد ✅":
        st.success("إجابة صحيحة! التعامل من خلال المتاجر الرسمية والتطبيقات الأصلية آمن تماماً.")
        if st.session_state.score < 6:
            st.session_state.score = 6
    elif choice6 == "غير آمن ويجب حذفه 🚨":
        st.error("خطأ! التحديث من المتاجر الرسمية والتطبيقات الأصلية آمن وليس احتيالاً.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 7
        st.rerun()

# --- السؤال السابع: المصادقة الثنائية (2FA) (كان سؤال 7) ---
elif st.session_state.step == 7:
    st.subheader("التحدي 7 من 7: المصادقة الثنائية (2FA)")
    st.write(
        "حاولت تسجيل الدخول لحسابك الشخصي، وطلب منك النظام إدخال رمز التحقق (OTP) المُرسل عبر رسالة نصية قصيرة لرقم هاتفك المسجل."
    )

    choice7 = st.radio(
        "هل هذه الخطوة آمنة وطبيعية؟",
        ["اختر...", "نعم، هذه ميزة المصادقة الثنائية الآمنة لحماية حسابي 🔒", "لا، تعتبر عملية اختراق واضحة ⚠️"],
        key="q7",
    )

    if choice7 == "نعم، هذه ميزة المصادقة الثنائية الآمنة لحماية حسابي 🔒":
        st.success("إجابة صحيحة! المصادقة الثنائية تحمي حسابك حتى لو تم معرفة كلمة المرور.")
        if st.session_state.score < 7:
            st.session_state.score = 7
    elif choice7 == "لا، تعتبر عملية اختراق واضحة ⚠️":
        st.error("خطأ! رموز التحقق (OTP) هي خط الدفاع الأساسي الآمن للحسابات.")

    st.markdown("---")
    if st.button("إظهار النتيجة النهائية 🏆"):
        st.session_state.step = 8
        st.rerun()

# --- النتيجة النهائية ---
elif st.session_state.step == 8:
    st.subheader("🏁 تقرير المحقق النهائي")
    st.write(f"لقد اجتزت التحديات وجمعت **{st.session_state.score} من أصل 7** نقاط.")

    if st.session_state.score >= 5:
        st.balloons()
        st.success(
            "استثنائي! أنت خبير أمن سيبراني محترف وامتلكت عيناً فاحصة للتهديدات!"
        )
    elif st.session_state.score >= 3:
        st.info("أداء جيد! لكن تحتاج لزيادة الحذر في بعض التهديدات الرقمية.")
    else:
        st.warning("تحتاج لمراجعة أساليب الحماية الرقمية وتطوير مهارتك في كشف الاحتيال.")

    # إضافة بصمتك واسمك الكريم في أسفل الصفحة
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray; font-size: 14px;'>"
        "تم تطوير هذه المنصة بواسطة المحققة البارعة: <b>نورة مبارك</b> 💻✨"
        "</div>",
        unsafe_allow_html=True,
    )

    if st.button("🔄 إعادة التحدي من جديد"):
        st.session_state.step = 1
        st.session_state.score = 0
        st.rerun()