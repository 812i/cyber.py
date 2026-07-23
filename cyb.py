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
    "مرحباً بك أيها المحقق! مهمتك اليوم هي اجتياز 10 تحديات أمنية لكشف الاحتيال الرقمي والتزييف العميق."
)
st.markdown("---")

# تهيئة الخطوات والنقاط (10 تحديات)
if "step" not in st.session_state:
    st.session_state.step = 1
if "score" not in st.session_state:
    st.session_state.score = 0

# --- السؤال 1: آمن (المصادقة الثنائية) ---
if st.session_state.step == 1:
    st.subheader("التحدي 1 من 10: المصادقة الثنائية (2FA)")
    st.write(
        "حاولت تسجيل الدخول لحسابك الشخصي، وطلب منك النظام إدخال رمز التحقق (OTP) المُرسل عبر رسالة نصية قصيرة لرقم هاتفك المسجل."
    )
    choice1 = st.radio(
        "هل هذه الخطوة آمنة وطبيعية؟",
        ["اختر...", "نعم، هذه ميزة المصادقة الثنائية الآمنة 🔒", "لا، تعتبر عملية اختراق ⚠️"],
        key="q1",
    )
    if choice1 == "نعم، هذه ميزة المصادقة الثنائية الآمنة 🔒":
        st.success("✅ إجابة صحيحة! المصادقة الثنائية تحمي حسابك حتى لو تم معرفة كلمة المرور.")
        if st.session_state.score < 1:
            st.session_state.score = 1
    elif choice1 == "لا، تعتبر عملية اختراق ⚠️":
        st.error("❌ خطأ! رموز التحقق هي خط دفاع أساسي وآمن.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 2
        st.rerun()

# --- السؤال 2: غير آمن (التصيد الإلكتروني) ---
elif st.session_state.step == 2:
    st.subheader("التحدي 2 من 10: الرسائل الوبرية (Phishing Email)")
    st.write(
        "وصلتك رسالة إيميل من (Netflix) تخبرك بأن اشتراكك سينتهي ويجب الدفع عبر رابط خارج الموقع الرسمي."
    )
    choice2 = st.radio(
        "ما الإجراء السليم؟",
        ["اختر...", "أدخل بيانات البطاقة مباشرة 💳", "أتجاهل الرابط وأدخل للتطبيق الرسمي 🔒"],
        key="q2",
    )
    if choice2 == "أتجاهل الرابط وأدخل للتطبيق الرسمي 🔒":
        st.success("✅ إجابة صحيحة! لا تضغط على روابط الإيميلات الخارجية أبداً.")
        if st.session_state.score < 2:
            st.session_state.score = 2
    elif choice2 == "أدخل بيانات البطاقة مباشرة 💳":
        st.error("❌ خطأ! هذا إيميل احتيالي لسرقة حسابك.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 3
        st.rerun()

# --- السؤال 3: غير آمن (الرسائل النصية) ---
elif st.session_state.step == 3:
    st.subheader("التحدي 3 من 10: الرسائل النصية للبنوك")
    st.write(
        "وصلتك رسالة نصية تقول: *(تم تجميد حسابك البنكي، اضغط هنا لتحديث البيانات [www.bank-update.com])*."
    )
    choice3 = st.radio(
        "هل تعتقد أن هذه الرسالة آمنة أم احتيالية؟",
        ["اختر...", "آمنة وحقيقية ✅", "احتيالية ومشبوهة 🚨"],
        key="q3",
    )
    if choice3 == "احتيالية ومشبوهة 🚨":
        st.success("✅ إجابة صحيحة! البنوك لا تطلب التحديث عبر روابط نصية.")
        if st.session_state.score < 3:
            st.session_state.score = 3
    elif choice3 == "آمنة وحقيقية ✅":
        st.error("❌ خطأ! هذه رسالة تصيد هدفها سرقة بياناتك.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 4
        st.rerun()

# --- السؤال 4: غير آمن (المتاجر الوهمية) ---
elif st.session_state.step == 4:
    st.subheader("التحدي 4 من 10: المتاجر الإلكترونية الوهمية")
    st.write(
        "وجدت إعلاناً بخصوص متجر شهير يبيع ماركة عالمية بخصم 90% والرابط منتهي بـ (.xyz) أو حروف غير مرتبة."
    )
    choice4 = st.radio(
        "هل تثق في هذا الموقع وتشتري منه؟",
        ["اختر...", "نعم، الفرصة لا تعوض 🛒", "لا، متجر مشبوه واحتيالي 🛑"],
        key="q4",
    )
    if choice4 == "لا، متجر مشبوه واحتيالي 🛑":
        st.success("✅ إجابة صحيحة! المتاجر الوهمية تستغل الخصومات الخيالية لسرقة البطاقات.")
        if st.session_state.score < 4:
            st.session_state.score = 4
    elif choice4 == "نعم، الفرصة لا تعوض 🛒":
        st.error("❌ خطأ! غالباً هذه المتاجر وهمية تسرق بيانات الدفع.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 5
        st.rerun()

# --- السؤال 5: آمن (تحديثات التطبيقات) ---
elif st.session_state.step == 5:
    st.subheader("التحدي 5 من 10: التحديثات الرسمية للتطبيقات")
    st.write(
        "ظهر لك إشعار داخل تطبيق البنك الرسمي الموثق بجوالك يطلب منك التحديث لتحسين الأمان، وعند الضغط وجهك لمتجر التطبيقات الرسمي."
    )
    choice5 = st.radio(
        "هل هذا الإجراء آمن؟",
        ["اختر...", "آمن وموثوق ✅", "غير آمن ويجب حذفه 🚨"],
        key="q5",
    )
    if choice5 == "آمن وموثوق ✅":
        st.success("✅ إجابة صحيحة! التعامل من خلال المتاجر الرسمية والتطبيقات الأصلية آمن تماماً.")
        if st.session_state.score < 5:
            st.session_state.score = 5
    elif choice5 == "غير آمن ويجب حذفه 🚨":
        st.error("❌ خطأ! التحديث من المتاجر الرسمية آمن.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 6
        st.rerun()

# --- السؤال 6: آمن (كلمات المرور القوية - جديد) ---
elif st.session_state.step == 6:
    st.subheader("التحدي 6 من 10: كلمات المرور القوية")
    st.write(
        "تلقيت نصيحة من أحد الأصدقاء باستخدام كلمة مرور قوية تحتوي على أحرف كبيرة وصغيرة وأرقام ورموز، وتفعيل المصادقة الثنائية."
    )
    choice6 = st.radio(
        "هل هذه النصيحة صحيحة؟",
        ["اختر...", "نعم، هذه أفضل الممارسات الأمنية 🔐", "لا، كلمات المرور البسيطة أسهل للتذكر"],
        key="q6",
    )
    if choice6 == "نعم، هذه أفضل الممارسات الأمنية 🔐":
        st.success("✅ إجابة صحيحة! كلمات المرور القوية والمصادقة الثنائية تزيد الأمان بشكل كبير.")
        if st.session_state.score < 6:
            st.session_state.score = 6
    elif choice6 == "لا، كلمات المرور البسيطة أسهل للتذكر":
        st.error("❌ خطأ! كلمات المرور الضعيفة تسهل الاختراق.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 7
        st.rerun()

# --- السؤال 7: غير آمن (الاتصالات الصوتية Deepfake) ---
elif st.session_state.step == 7:
    st.subheader("التحدي 7 من 10: الاتصالات الصوتية (Deepfake)")
    st.write(
        "تلقيت اتصالاً بصوت مديرك يطلب منك تحويل مبلغ طارئ لحساب خارجي وبشكل عاجل جداً."
    )
    choice7 = st.radio(
        "كيف تتصرف؟",
        ["اختر...", "أحول المبلغ فوراً 💸", "أتحقق عبر قناة رسمية أخرى 🤖"],
        key="q7",
    )
    if choice7 == "أتحقق عبر قناة رسمية أخرى 🤖":
        st.success("✅ إجابة صحيحة! تقنيات التزييف العميق للأصوات منتشرة وخطيرة.")
        if st.session_state.score < 7:
            st.session_state.score = 7
    elif choice7 == "أحول المبلغ فوراً 💸":
        st.error("❌ خطأ! قد يكون هذا الصوت مولداً بالذكاء الاصطناعي.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 8
        st.rerun()

# --- السؤال 8: آمن (التحقق عبر البريد الإلكتروني - جديد) ---
elif st.session_state.step == 8:
    st.subheader("التحدي 8 من 10: التحقق الإضافي عبر البريد")
    st.write(
        "عند تسجيل الدخول إلى حسابك، طلب منك النظام إدخال رمز تحقق تم إرساله إلى بريدك الإلكتروني المسجل، مع التأكد من أن البريد مرسل من النطاق الرسمي للخدمة."
    )
    choice8 = st.radio(
        "هل هذا الإجراء آمن؟",
        ["اختر...", "نعم، هذا طبقة أمان إضافية 🔒", "لا، قد يكون احتيالاً 🚨"],
        key="q8",
    )
    if choice8 == "نعم، هذا طبقة أمان إضافية 🔒":
        st.success("✅ إجابة صحيحة! التحقق عبر البريد الإلكتروني من نطاق رسمي يعزز الأمان.")
        if st.session_state.score < 8:
            st.session_state.score = 8
    elif choice8 == "لا، قد يكون احتيالاً 🚨":
        st.error("❌ خطأ! هذه ممارسة آمنة إذا تأكدت من مصدر البريد.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 9
        st.rerun()

# --- السؤال 9: غير آمن (الصور المزيفة) ---
elif st.session_state.step == 9:
    st.subheader("التحدي 9 من 10: الصور الذكية المزيفة (Deepfake Images)")
    st.write(
        "انتشرت صورة لشخصية مشهورة في موقف غريب جداً، ولاحظت وجود تشوهات بسيطة في أطراف الأصابع والخلفية."
    )
    choice9 = st.radio(
        "كيف تحكم على هذه الصورة؟",
        ["اختر...", "صورة حقيقية 100% 📸", "صورة مولدة بالذكاء الاصطناعي 🎨"],
        key="q9",
    )
    if choice9 == "صورة مولدة بالذكاء الاصطناعي 🎨":
        st.success("✅ إجابة صحيحة! تفاصيل الأطراف والخلفيات غالباً تفضح الصور المزيفة.")
        if st.session_state.score < 9:
            st.session_state.score = 9
    elif choice9 == "صورة حقيقية 100% 📸":
        st.error("❌ خطأ! هذه الصورة ولدت بواسطة الذكاء الاصطناعي.")

    st.markdown("---")
    if st.button("السؤال التالي ➡️"):
        st.session_state.step = 10
        st.rerun()

# --- السؤال 10: غير آمن (الروابط المختصرة - جديد) ---
elif st.session_state.step == 10:
    st.subheader("التحدي 10 من 10: الروابط المختصرة المشبوهة")
    st.write(
        "استلمت رسالة من جهة غير معروفة تحتوي على رابط مختصر (مثل bit.ly) يدعي أنه يمنحك جائزة قيمة، وعند الضغط سيطلب منك بياناتك."
    )
    choice10 = st.radio(
        "كيف تتعامل مع هذا الرابط؟",
        ["اختر...", "أضغط عليه لمعرفة الجائزة 🎁", "أتجاهله ولا أضغط نهائياً 🚫"],
        key="q10",
    )
    if choice10 == "أتجاهله ولا أضغط نهائياً 🚫":
        st.success("✅ إجابة صحيحة! الروابط المختصرة تخفي وجهات خطيرة غالباً.")
        if st.session_state.score < 10:
            st.session_state.score = 10
    elif choice10 == "أضغط عليه لمعرفة الجائزة 🎁":
        st.error("❌ خطأ! هذه حيلة شائعة للتصيد ونشر البرمجيات الخبيثة.")

    st.markdown("---")
    if st.button("إظهار النتيجة النهائية 🏆"):
        st.session_state.step = 11
        st.rerun()

# --- النتيجة النهائية (تم تعديلها لـ 10) ---
elif st.session_state.step == 11:
    st.subheader("🏁 تقرير المحقق النهائي")
    st.write(f"لقد اجتزت التحديات وجمعت **{st.session_state.score} من أصل 10** نقاط.")

    if st.session_state.score >= 8:
        st.balloons()
        st.success("🌟 استثنائي! أنت خبير أمن سيبراني محترف وامتلكت عيناً فاحصة للتهديدات!")
    elif st.session_state.score >= 5:
        st.info("👍 أداء جيد! لكن تحتاج لزيادة الحذر في بعض التهديدات الرقمية.")
    else:
        st.warning("⚠️ تحتاج لمراجعة أساليب الحماية الرقمية وتطوير مهارتك في كشف الاحتيال.")

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