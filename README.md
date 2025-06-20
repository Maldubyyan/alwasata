
# الواسطة | Alwasata

**منصة ذكية لبناء السيرة الذاتية وخطاب التغطية باستخدام الذكاء الاصطناعي، مع إرسال تلقائي لجهات التوظيف.**

---

## 🚀 نظرة عامة

الواسطة هو مشروع يدمج بين **الذكاء الاصطناعي** و**تجربة المستخدم الذكية** لتقديم خدمة احترافية تساعد الباحثين عن العمل على:

- بناء **سيرة ذاتية احترافية**.
- توليد **خطاب تغطية مخصص** لكل وظيفة.
- إرسال الملفات مباشرة إلى البريد الإلكتروني الخاص بجهة التوظيف، بعد موافقة العميل.
- العمل بنظام **باقات مدفوعة** مدمجة ببوابة دفع إلكترونية.

---

## 🧠 كيف يعمل الذكاء الاصطناعي؟

1. المستخدم يملأ نموذج مبسط لمعلوماته المهنية.
2. الذكاء الاصطناعي يحلل البيانات ويولّد:
   - سيرة ذاتية (CV) بصيغة PDF.
   - خطاب تغطية (Cover Letter) مناسب لكل مجال.
3. بعد اعتماد العميل، تُرسل الملفات تلقائيًا إلى جهة التوظيف.

---

## 🔌 REST API Endpoints

| Method | Endpoint              | الوصف                             |
|--------|------------------------|-----------------------------------|
| POST   | `/generate`            | توليد السيرة وخطاب التغطية       |
| POST   | `/payment/create`      | إنشاء عملية دفع جديدة            |
| GET    | `/status/<job_id>`     | تتبع حالة التوليد                |
| POST   | `/send/email`          | إرسال السيرة والخطاب عبر الإيميل |

> **ملاحظة**: التوثيق الكامل للـ API سيكون ضمن `/docs` في الإصدارات القادمة.

---

## 💳 بوابة الدفع

المنصة تدعم الدفع الإلكتروني عبر دمج API خاص ببوابات مثل:
- **Stripe**
- **Tabby**
- **Hyperpay**
- **STC Pay**

> يتم إنشاء جلسة دفع بناءً على الباقة المختارة، مع تتبع حالة الدفع وربطها بتفعيل الخدمة تلقائيًا.

---

## 🏗️ هيكل المشروع

```
simple_app_v2/
│
├── src/
│   └── application.py  # نقطة تشغيل تطبيق Flask
│
├── requirements.txt     # المكتبات المستخدمة
├── Procfile             # تعليمات التشغيل لـ AWS EB
└── .ebextensions/
    └── python.config    # إعدادات بيئة AWS
```

---

## ☁️ قابلية النشر

✅ مهيأ بالكامل للنشر على [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/)  
✅ يدعم HTTPS وبيئات الإنتاج  
✅ قابل للربط مع نطاق مخصص عبر Route 53

---

## 📩 تواصل

هل ترغب بالتعاون أو الشراكة؟  
راسلنا عبر الإيميل: `contact@alwasata.com`

---

> تم تطوير هذا المشروع بحُب 💙 لتسهيل الوصول للوظائف ورفع جودة التوظيف في العالم العربي.
