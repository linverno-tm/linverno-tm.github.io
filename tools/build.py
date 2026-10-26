"""Saytni yig'adi: index.html (o'zbekcha) va en/index.html (inglizcha).

    python tools/build.py

Matn shu faylda, uslub tools/uslub.css da, skript tools/skript.js da (ikkalasi sahifa ichiga qo'yiladi),
rasmlar img/ da (o'lchamlari tools/rasmlar.json da).
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T_ = lambda *p: os.path.join(ROOT, "tools", *p)
RASM = json.load(open(T_("rasmlar.json"), encoding="utf-8"))
CSS = open(T_("uslub.css"), encoding="utf-8").read()
JS = open(T_("skript.js"), encoding="utf-8").read()
QR = open(T_("qr-path.txt"), encoding="utf-8").read().strip()
SAYT = "https://linverno-tm.github.io/"
TG = "https://t.me/m_tojiddinov7"

# Loyiha ranglari (R G B)
RANG = {"crm": "139 92 246", "mijoz": "167 139 250", "kino": "245 179 1", "qogoz": "47 129 247",
        "hamkor": "223 208 31", "shuxrat": "200 162 74", "oltinkol": "249 115 22", "minges": "34 197 154",
        "media": "251 113 133", "buklet": "236 72 153", "boshqa": "148 163 184", "avto": "45 212 191"}

T = {
    "uz": {
        "lang": "uz",
        "title": "Muhammadabdulloh Tojiddinov — CRM, mobil ilova, Telegram bot va sayt",
        "desc": "Biznes uchun CRM, mobil ilova, Telegram bot, mini app va sayt yarataman. Hamkor CRM muallifi: to‘rtta filialning 1C bazasini bitta tizimga birlashtirgan muddatli to‘lov savdo tizimi.",
        "skip": "Asosiy qismga o‘tish",
        "nav": [("#ishlar", "Ishlar"), ("#aloqa", "Aloqa")],
        "til_link": "en/", "til_label": "EN", "til_aria": "English version",
        "tg_btn": "Telegram’da yozish",
        "kasb": "Hamkor CRM muallifi",
        "h1_bosh": "Biznesingiz uchun", "h1_oxir": "yarataman.",
        "h1_sozlar": ["CRM", "mobil ilova", "Telegram bot", "mini app", "sayt"],
        "h1_statik": "CRM, mobil ilova, Telegram bot, mini app va sayt",
        "lid": "<b>To‘rtta filialning alohida 1C bazasini bitta tizimga birlashtirdim.</b> Savdo, nasiya, kassa va ombor endi bir joyda va internet uzilsa ham ishlaydi. G‘oyadan ishlaydigan dasturgacha hammasini o‘zim yozaman.",
        "cta2": "Ishlarni ko‘rish",
        "t_crm_chip": "Savdo tizimi · 1C o‘rnida",
        "t_crm_p": "Savdo, nasiya shartnomalari, to‘lovlar, kassa, ombor va hisobotlar. Bosing — batafsil.",
        "t_son_chip": "Hamkor CRM",
        "t_son_p": "o‘zgarish bir oyda: sentabr–oktabr 2026",
        "t_tez_chip": "Bu sayt",
        "t_tez": ["Tezlik", "Qulaylik", "Amaliyot", "SEO"],
        "t_tez_p": "Lighthouse, kompyuter versiyasi",
        "t_chat_chip": "Telegram bot",
        "t_chat_p": "KINO TV botining haqiqiy javobi",
        "t_tel_chip": "Mobil ilova",
        "t_tel_h": "Hamkor — mijozlar ilovasi",
        "t_tel_p": "Flutter: Android va iPhone uchun bitta kod.",
        "t_xiz_chip": "Nima qilaman",
        "t_xiz": ["Savdo va nasiya CRM", "Mobil ilova", "Telegram bot", "Mini app", "Sayt", "Avtomatlashtirish", "Video va dizayn"],
        "t_xiz_p": "1C, Telegram, Excel va PDF bilan bog‘layman; takrorlanadigan qo‘l ishini dasturga topshiraman.",
        "lenta": ["Hamkor CRM", "Mijozlar ilovasi", "KINO TV", "Qog‘oz Bino", "Hamkor Savdo", "Shuxrat o‘g‘li", "Oltinko‘l", "MINI GES", "ChatForge"],
        "ishlar_h": "Ishlar",
        "ishlar_p": "Hammasi haqiqiy loyiha. Plitkani bosing — maqsad, yechim va natija ochiladi.",
        "batafsil": "Batafsil", "yopish": "Yopish", "konsept": "konsept", "kod": "Kodi",
        "qadam": ("Muammo", "Yechim", "Natija"), "qadam_m": ("Maqsad", "Yechim", "Natija"),
        "crm_alt": ("Hamkor CRM: bosh sahifa, summalar yopilgan", "Hamkor CRM: mijozlar ro‘yxati, ism va summalar yopilgan"),
        "ishlar": [
            {"id": "crm", "chip": "Savdo tizimi", "nom": "Hamkor CRM",
             "tavsif": "1C o‘rnini bosgan muddatli to‘lov savdo tizimi. Sentabr 2026 dan ishlab chiqyapman, platforma meniki.",
             "teglar": ["Next.js", "PostgreSQL", "Tauri", "1C sinxron", "Oflayn"],
             "qadamlar": [
                 "To‘rtta do‘kon to‘rtta alohida 1C bazasida ishlardi va bir-birini ko‘rmasdi. Bir do‘konda qora ro‘yxatga tushgan mijoz keyingisida yana nasiyaga tovar olishi mumkin edi.",
                 "Hammasi uchun bitta tizim: savdo, nasiya shartnomalari, to‘lovlar, kassa, ombor, ish haqi va hisobotlar. 1C bilan ikki tomonlama sinxronlanadi, shuning uchun o‘tish davrida ikkalasi yonma-yon ishladi.",
                 "Bir oyda 1 373 ta o‘zgarish, 230 dan ortiq ekran, 65 ta hisobot. Mijozlar ilovasi shu bazaga ulangan. Shu platformani sizning savdongizga ham moslab beraman."],
             "faktlar": [
                 ("Internet uzilsa ham ishlaydi", "Kompyuterdagi shifrlangan nusxa bilan har bir oyna ochilaveradi. Amallar navbatga yoziladi va aloqa tiklanganda o‘zi yuboriladi."),
                 ("Windows dasturi", "Chekni so‘ramasdan chop etadi va o‘zi yangilanadi."),
                 ("Har bir yangilanish oldin sinovdan o‘tadi", "Savdo, shartnoma, to‘lov va hisobotlar vaqtinchalik bazada tekshiriladi, keyin ishga chiqadi."),
                 ("Mijoz telefonida ham", "Shartnoma, to‘lov grafigi va qolgan qarzni mijoz o‘z ilovasida ko‘radi.")],
             "rasmlar": [("crm-mijozlar", "Mijozlar va ularning ishonch bahosi"), ("crm-qarz", "Muddati o‘tgan qarzlar"), ("crm-kassa", "Kassalar filiallar kesimida")],
             "izoh": "Ekranlar demo bazadan; summalar, ismlar va filial nomlari yopilgan.",
             "havolalar": [("https://hamkorcrm.uz/", "hamkorcrm.uz")]},
            {"id": "mijoz", "chip": "Mobil ilova", "nom": "Hamkor — mijozlar ilovasi",
             "tavsif": "Mijoz shartnomalari, qolgan qarz, keyingi to‘lov va to‘lov tarixi telefonda; katalogdan muddatli to‘lovga buyurtma va do‘kon bilan chat.",
             "teglar": ["Flutter", "Riverpod", "Android", "iPhone"], "maqsad": True,
             "qadamlar": [
                 "Muddatli to‘lov bilan xarid qilgan mijoz shartnomasi, keyingi to‘lovi va limitini do‘konga bormasdan ko‘rsin; do‘kon esa unga xabar va aksiyani to‘g‘ridan-to‘g‘ri yuborsin.",
                 "Flutter va Riverpod; har bo‘lim to‘rt qatlamda (model, ma’lumot, holat, ekran). Kirish SMS kod bilan, token telefonning xavfsiz xotirasida. Avval Expo (React Native) da yozilgan edi, 7-oktabrda to‘liq Flutter’ga ko‘chirildi.",
                 "Android, iPhone va web uchun bitta kod; uch tilda (o‘zbek kirill va lotin, rus), yorug‘ va qorong‘i mavzu. Ilova do‘konlarga chiqarishga tayyorlanmoqda."],
             "tel": ["mobil-bosh", "mobil-katalog", "mobil-tolovlar"],
             "rasmlar": [("mobil-bosh", "Bosh sahifa: summalar ilovaning o‘zida yashirilgan"), ("mobil-katalog", "Katalog va oylik to‘lov"), ("mobil-tolovlar", "To‘lovlar tarixi")],
             "izoh": "Demo mijoz; ism va summalar yopilgan.", "havolalar": []},
            {"id": "kino", "chip": "Telegram bot · mini app", "nom": "KINO TV",
             "tavsif": "Seriallar va kinolar uchun bot va mini app: bo‘limlar, qidiruv, qismlar; to‘xtagan joydan davom ettiradi.",
             "teglar": ["Python", "aiogram 3", "SQLite", "Cloudflare Pages"], "maqsad": True,
             "qadamlar": [
                 "Ko‘p qismli serialni Telegram’da qulay ko‘rish: kerakli qismni tez topish va qayerda to‘xtaganini yo‘qotmaslik.",
                 "Bot yopiq ombor kanaldagi postlarni o‘zi katalogga yozadi: admin faqat video joylaydi, kodni bot beradi. Video nusxa sifatida yuboriladi, hajm chegarasi yo‘q. Mini app yig‘ishsiz HTML/CSS/JS, katalog Cloudflare chekkasida keshlanadi.",
                 "Katalogda 158 ta serial va 543 ta kino, 8 ta bo‘lim. Mini app keyingi qismdan davom ettiradi va saqlanganlar ro‘yxatini yuritadi."],
             "tel": ["kino-bosh", "kino-serial"],
             "rasmlar": [("kino-bosh", "Bosh sahifa"), ("kino-serial", "Serial va qismlar")],
             "havolalar": [("https://t.me/linvkino_bot", "@linvkino_bot")]},
            {"id": "qogoz", "chip": "Mini app", "nom": "Qog‘oz Bino",
             "tavsif": "Telegram kanal uchun mini app: yangi qismlar, eng ko‘p ko‘rilganlar, qidiruv va «Mening ro‘yxatim».",
             "teglar": ["HTML/CSS/JS", "Telegram Web App", "Python"], "maqsad": True,
             "qadamlar": [
                 "Do‘stning @QogozBinoTVbot boti uchun posterli katalog — botning kodiga tegmasdan va tokenisiz.",
                 "Katalogni botning o‘zidan yig‘adigan skript: har kodga /start yuboradi va javobni o‘qiydi. Mini app kirill va lotinda jonli qidiradi, bo‘lim va janr bo‘yicha saralaydi.",
                 "Bot tokeni ishlatilmaydi. To‘liq yig‘ish taxminan 10 daqiqa, yangi kodlar alohida tez qo‘shiladi."],
             "tel": ["qogoz-bosh", "qogoz-serial"],
             "rasmlar": [("qogoz-bosh", "Bosh sahifa"), ("qogoz-serial", "Serial va qismlar")],
             "havolalar": [("https://qogoz-bino.pages.dev/", "qogoz-bino.pages.dev")]},
            {"id": "hamkor", "chip": "Sayt", "nom": "Hamkor Savdo",
             "tavsif": "To‘rt filialli savdo tarmog‘i sayti: katalog, filiallar va muddatli to‘lovga ariza. Sichqonchani olib boring — sayt aylanadi.",
             "teglar": ["Next.js 16", "React 19", "Tailwind v4"], "maqsad": True,
             "qadamlar": [
                 "To‘rt filialli tarmoqni tanishtirish: kompaniya, taklif, har filial va bog‘lanish yo‘llari. Asosiy shart: sekin internetda ham tez ochilsin.",
                 "Animatsiya kutubxonasisiz: hamma harakat CSS va taxminan 1 KB JavaScript. Logotip brendbukdagi rasmdan vektorga o‘tkazilgan.",
                 "O‘qiladigan sahifa (HTML va CSS) 35 KB gzip, JavaScript’siz ham ishlaydi. Matn kontrasti hamma joyda 4.5:1 dan yuqori; to‘qima sharh va ma’lumot yo‘q."],
             "uzun": "uzun-hamkor", "havolalar": [("https://hamkorsavdo.uz/", "hamkorsavdo.uz")]},
            {"id": "shuxrat", "chip": "Sayt", "nom": "Shuxrat o‘g‘li", "belgi": True,
             "tavsif": "Parranda brendi uchun uch tilli sayt: mahsulotlar, ulgurji buyurtma, Veo bilan yaratilgan jonli video.",
             "teglar": ["HTML/CSS/JS", "SVG animatsiya", "Veo"], "maqsad": True,
             "qadamlar": [
                 "«Baraka hamkor parranda» XK markasi uchun brend sayti: mahsulot, ulgurji savdo va qayerdan sotib olish.",
                 "SVG logo animatsiyasi, assortiment jadvali, ulgurji buyurtma arizasi, xarita va jonli video. Matn bitta faylda; ruscha va inglizcha sahifalar skript bilan yasaladi.",
                 "Namuna holatida topshirilgan: mijozdan keladigan ma’lumot joylari maxsus rejimda belgilanadi, soxta sharh qo‘yilmagan."],
             "uzun": "uzun-shuxrat", "havolalar": [("https://linverno-tm.github.io/shuxrat-ogli-v2/", "Saytni ochish")]},
            {"id": "oltinkol", "chip": "Sayt", "nom": "Oltinko‘l charm-poyabzal zonasi", "belgi": True,
             "tavsif": "Kichik sanoat zonasi sayti: do‘konlar, to‘lov hisoblagichi, investorlar va rezidentlar uchun bo‘limlar, admin panel.",
             "teglar": ["HTML/CSS/JS", "Admin panel", "3 til"], "maqsad": True,
             "qadamlar": [
                 "Charm-poyabzal kichik sanoat zonasida do‘kon sotish va investor jalb qilish.",
                 "Do‘konlar, kredit va to‘lov hisoblagichi, imtiyozlar, investorlar va rezidentlar sahifalari; arizalar, do‘konlar va foydalanuvchilarni boshqaradigan admin panel.",
                 "14 ta bo‘lim, o‘zbek, rus va ingliz tilida."],
             "uzun": "uzun-oltinkol", "havolalar": [("https://linverno-tm.github.io/oltinkol-zona/", "Saytni ochish")]},
            {"id": "minges", "chip": "Sayt", "nom": "MINI GES",
             "tavsif": "Kichik gidroelektrostansiyalar sayti: loyihalar, qanday ishlashi, xizmatlar va ariza.",
             "teglar": ["Statik sayt", "SVG", "CI"], "maqsad": True,
             "qadamlar": [
                 "Ulug‘nor GES (600 kVt, ishlab turibdi) va Baliqchi GES (1 000 kVt) ni tanishtirish va mini-GES qurish xizmatini sotish.",
                 "Freymvorksiz statik sayt. «Qanday ishlaydi» bo‘limi 3D model o‘rniga izometrik SVG (~53 KB). Soha yangiliklari sayt yig‘ilayotganda yoziladi; o‘zbek va rus tilida.",
                 "Telefonda birinchi ochilishda taxminan 170 KB (gzip), rasm yuklanmaydi. Har o‘zgarishni CI tekshirib, o‘zi chiqaradi."],
             "uzun": "uzun-minges", "havolalar": [("https://linverno-tm.github.io/mini-ges-site/", "Saytni ochish")]},
        ],
        "boshqa_chip": "Mobil ilovalar", "boshqa_h": "Boshqa ilovalarim",
        "boshqa": [("ChatForge", "Flutter’da messenjer: shaxsiy yozishmalar, kerakli odamga push-xabarnoma.", "https://github.com/linverno-tm/chatforge"),
                   ("Ommaviy SMS", "Android: Excel yoki CSV ro‘yxatdan SMS; telefon o‘chib yonsa ham navbat yo‘qolmaydi.", "https://github.com/linverno-tm/bulk-sms"),
                   ("Vazifalar ilovasi", "Internet yo‘qda ham ishlaydi, aloqa tiklanganda o‘zi sinxronlanadi.", "https://github.com/linverno-tm/task-manager")],
        "media_chip": "Video", "media_h": "Veo bilan jonli video",
        "media_p": "Shuxrat o‘g‘li sayti uchun. Remotion’da esa matn va raqamli motion roliklar yig‘aman.",
        "veo_pauza": "Videoni to‘xtatish", "veo_davom": "Videoni davom ettirish",
        "buklet_chip": "Bosma dizayn", "buklet_h": "Yevrobuklet, Hamkor Savdo",
        "buklet_p": "A4, uch buklama, bosmaga tayyor vektor fayl.",
        "buklet_alt": "Hamkor Savdo yevrobukleti: «24 oygacha muddatli to‘lov», tovarlar va oylik to‘lovlar",
        "avto_chip": "Avtomatlashtirish", "avto_h": "Qo‘l ishini dasturga topshirish",
        "avto": [("Narx kuzatuvi", "Raqobatchilarning Telegram guruhlaridagi e’lonlari narxlarga aylanadi; har do‘konga kunlik PDF faqat yangi va o‘zgargan narxlar bilan."),
                 ("Kameral hisobot", "Hisob-faktura va kassa cheklaridan soliq tekshiruvi uchun hisobotni o‘zi yig‘adigan dastur."),
                 ("O‘z ulagichlarim", "YouTube va Pinterest bilan ishlaydigan MCP serverlar: kanal va kontent ishini sun’iy intellekt orqali bajarish.")],
        "aloqa_h": "Loyihangiz bormi? Telegram’da yozing.",
        "aloqa_p": "Qisqacha yozing: biznesingiz nima bilan shug‘ullanadi va nimani tezlashtirmoqchisiz. O‘zim javob beraman.",
        "qr": "Telefon kamerasi bilan skanerlang",
        "footer_til": "English",
    },
    "en": {
        "lang": "en",
        "title": "Muhammadabdulloh Tojiddinov — CRMs, mobile apps, Telegram bots and websites",
        "desc": "I build CRMs, mobile apps, Telegram bots, mini apps and websites for businesses. Author of Hamkor CRM, an installment-sales system that joined four stores’ 1C databases into one.",
        "skip": "Skip to content",
        "nav": [("#ishlar", "Work"), ("#aloqa", "Contact")],
        "til_link": "../", "til_label": "UZ", "til_aria": "O‘zbekcha versiya",
        "tg_btn": "Message on Telegram",
        "kasb": "Author of Hamkor CRM",
        "h1_bosh": "I build", "h1_oxir": "for businesses.",
        "h1_sozlar": ["CRMs", "mobile apps", "Telegram bots", "mini apps", "websites"],
        "h1_statik": "CRMs, mobile apps, Telegram bots, mini apps and websites",
        "lid": "<b>I joined four stores’ separate 1C databases into one system.</b> Sales, installments, cash and stock now live in one place and keep working when the internet drops. From idea to working software, I write it all myself.",
        "cta2": "See the work",
        "t_crm_chip": "Sales system · replaces 1C",
        "t_crm_p": "Sales, installment contracts, payments, cash, stock and reports. Click for details.",
        "t_son_chip": "Hamkor CRM",
        "t_son_p": "changes in one month: September–October 2026",
        "t_tez_chip": "This site",
        "t_tez": ["Speed", "Access", "Practices", "SEO"],
        "t_tez_p": "Lighthouse, desktop",
        "t_chat_chip": "Telegram bot",
        "t_chat_p": "a real reply from the KINO TV bot (in Uzbek)",
        "t_tel_chip": "Mobile app",
        "t_tel_h": "Hamkor — the customer app",
        "t_tel_p": "Flutter: one codebase for Android and iPhone.",
        "t_xiz_chip": "What I do",
        "t_xiz": ["Sales & installment CRM", "Mobile apps", "Telegram bots", "Mini apps", "Websites", "Automation", "Video & design"],
        "t_xiz_p": "I connect 1C, Telegram, Excel and PDF, and hand repetitive manual work over to software.",
        "lenta": ["Hamkor CRM", "Customer app", "KINO TV", "Qog‘oz Bino", "Hamkor Savdo", "Shuxrat o‘g‘li", "Oltinko‘l", "MINI GES", "ChatForge"],
        "ishlar_h": "Work",
        "ishlar_p": "Every one is a real project. Click a tile to see the goal, the solution and the result.",
        "batafsil": "Details", "yopish": "Close", "konsept": "concept", "kod": "Code",
        "qadam": ("Problem", "Solution", "Result"), "qadam_m": ("Goal", "Solution", "Result"),
        "crm_alt": ("Hamkor CRM home screen, amounts hidden", "Hamkor CRM customer list, names and amounts hidden"),
        "ishlar": [
            {"id": "crm", "chip": "Sales system", "nom": "Hamkor CRM",
             "tavsif": "An installment-sales system that replaced 1C. In development since September 2026; I own the platform.",
             "teglar": ["Next.js", "PostgreSQL", "Tauri", "1C sync", "Offline"],
             "qadamlar": [
                 "Four stores ran on four separate 1C databases that couldn’t see each other. A customer blacklisted in one store could get new credit in the next.",
                 "One system for all of them: sales, installment contracts, payments, cash, warehouse, payroll and reports. It syncs with 1C both ways, so the two ran side by side during the switch.",
                 "1,373 changes, 230+ screens and 65 reports in one month. The customer app is connected to the same database. I can adapt the platform to your business."],
             "faktlar": [
                 ("Works without internet", "An encrypted local copy keeps every window usable. Actions queue up and sync back on their own when the line returns."),
                 ("Windows app", "Prints receipts silently and updates itself."),
                 ("Every release is tested first", "Sales, contracts, payments and reports run on a throw-away database before a build goes live."),
                 ("On the customer’s phone too", "Customers see their contract, payment schedule and remaining debt in their own app.")],
             "rasmlar": [("crm-mijozlar", "Customers and their trust score"), ("crm-qarz", "Overdue debt"), ("crm-kassa", "Cash by branch")],
             "izoh": "Screens from a demo database; amounts, names and branch names are hidden.",
             "havolalar": [("https://hamkorcrm.uz/", "hamkorcrm.uz")]},
            {"id": "mijoz", "chip": "Mobile app", "nom": "Hamkor — the customer app",
             "tavsif": "Contracts, remaining debt, next payment and payment history on the phone; installment orders from the catalog and a chat with the store.",
             "teglar": ["Flutter", "Riverpod", "Android", "iPhone"], "maqsad": True,
             "qadamlar": [
                 "Customers who bought on installments see their contract, next payment and limit without visiting the store, and the store can send them notices and offers directly.",
                 "Flutter and Riverpod, each feature in four layers (model, data, state, screen). Sign-in with an SMS code, the token kept in the phone’s secure storage. First written in Expo (React Native), fully moved to Flutter on 7 October.",
                 "One codebase for Android, iPhone and web; three languages (Uzbek Cyrillic and Latin, Russian), light and dark themes. The app is being prepared for the stores."],
             "tel": ["mobil-bosh", "mobil-katalog", "mobil-tolovlar"],
             "rasmlar": [("mobil-bosh", "Home: amounts hidden by the app itself"), ("mobil-katalog", "Catalog with the monthly payment"), ("mobil-tolovlar", "Payment history")],
             "izoh": "Demo customer; name and amounts are hidden.", "havolalar": []},
            {"id": "kino", "chip": "Telegram bot · mini app", "nom": "KINO TV",
             "tavsif": "A bot and mini app for series and films: sections, search, episodes; continues where you stopped.",
             "teglar": ["Python", "aiogram 3", "SQLite", "Cloudflare Pages"], "maqsad": True,
             "qadamlar": [
                 "Watching long series in Telegram comfortably: find the right episode fast and never lose where you stopped.",
                 "The bot turns posts in a private storage channel into the catalog on its own: the admin only uploads videos, the bot assigns codes. Videos are sent as copies, with no size limit. The mini app is plain HTML/CSS/JS with the catalog cached at Cloudflare’s edge.",
                 "158 series and 543 films in 8 sections. The mini app continues from the next episode and keeps a saved list."],
             "tel": ["kino-bosh", "kino-serial"],
             "rasmlar": [("kino-bosh", "Home"), ("kino-serial", "Series and episodes")],
             "havolalar": [("https://t.me/linvkino_bot", "@linvkino_bot")]},
            {"id": "qogoz", "chip": "Mini app", "nom": "Qog‘oz Bino",
             "tavsif": "A mini app for a Telegram channel: new episodes, most watched, search and a personal list.",
             "teglar": ["HTML/CSS/JS", "Telegram Web App", "Python"], "maqsad": True,
             "qadamlar": [
                 "A poster catalog for a friend’s bot, @QogozBinoTVbot, without touching its code or using its token.",
                 "A script builds the catalog from the bot itself: it sends /start for each code and reads the reply. The mini app searches live in Cyrillic and Latin and filters by section and genre.",
                 "No bot token needed. A full rebuild takes about 10 minutes; new codes are added quickly on their own."],
             "tel": ["qogoz-bosh", "qogoz-serial"],
             "rasmlar": [("qogoz-bosh", "Home"), ("qogoz-serial", "Series and episodes")],
             "havolalar": [("https://qogoz-bino.pages.dev/", "qogoz-bino.pages.dev")]},
            {"id": "hamkor", "chip": "Website", "nom": "Hamkor Savdo",
             "tavsif": "Site for a four-branch retail chain: catalog, branches and an installment application. Hover — the site scrolls.",
             "teglar": ["Next.js 16", "React 19", "Tailwind v4"], "maqsad": True,
             "qadamlar": [
                 "Introduce a four-branch chain: the company, the offer, each branch and every way to reach it. The main constraint: fast on slow connections.",
                 "No animation library: all motion is CSS plus about 1 KB of JavaScript. The logo was traced to vector from the brand book artwork.",
                 "The readable page (HTML and CSS) is 35 KB gzipped and works without JavaScript. Every text pair is above 4.5:1 contrast; no invented reviews or facts."],
             "uzun": "uzun-hamkor", "havolalar": [("https://hamkorsavdo.uz/", "hamkorsavdo.uz")]},
            {"id": "shuxrat", "chip": "Website", "nom": "Shuxrat o‘g‘li", "belgi": True,
             "tavsif": "A three-language site for a poultry brand: products, wholesale orders and a live video made with Veo.",
             "teglar": ["HTML/CSS/JS", "SVG animation", "Veo"], "maqsad": True,
             "qadamlar": [
                 "A brand site for the “Baraka hamkor parranda” poultry brand: products, wholesale and where to buy.",
                 "SVG logo animation, a full range table, a wholesale order form, a map and a live video. The text lives in one file; Russian and English pages are generated by a script.",
                 "Delivered as a concept: places waiting for the client’s data are marked in a review mode, and no fake reviews were added."],
             "uzun": "uzun-shuxrat", "havolalar": [("https://linverno-tm.github.io/shuxrat-ogli-v2/", "Open the site")]},
            {"id": "oltinkol", "chip": "Website", "nom": "Oltinko‘l leather and footwear zone", "belgi": True,
             "tavsif": "Site for a small industrial zone: shops, a payment calculator, pages for investors and residents, an admin panel.",
             "teglar": ["HTML/CSS/JS", "Admin panel", "3 languages"], "maqsad": True,
             "qadamlar": [
                 "Sell shops and attract investors for a small leather and footwear industrial zone.",
                 "Pages for shops, a credit and payment calculator, incentives, investors and residents, plus an admin panel for applications, shops and users.",
                 "14 sections in Uzbek, Russian and English."],
             "uzun": "uzun-oltinkol", "havolalar": [("https://linverno-tm.github.io/oltinkol-zona/", "Open the site")]},
            {"id": "minges", "chip": "Website", "nom": "MINI GES",
             "tavsif": "Site for small hydro-power plants: projects, how it works, services and an application form.",
             "teglar": ["Static site", "SVG", "CI"], "maqsad": True,
             "qadamlar": [
                 "Present Ulug‘nor GES (600 kW, running) and Baliqchi GES (1,000 kW) and sell the service of building small hydro plants.",
                 "A static site without a framework. “How it works” is an isometric SVG (~53 KB) instead of a 3D model. Industry news is written in at build time; Uzbek and Russian.",
                 "About 170 KB gzipped on a phone’s first visit, with no images loaded. CI checks and publishes every change."],
             "uzun": "uzun-minges", "havolalar": [("https://linverno-tm.github.io/mini-ges-site/", "Open the site")]},
        ],
        "boshqa_chip": "Mobile apps", "boshqa_h": "Other apps I built",
        "boshqa": [("ChatForge", "A Flutter messenger: one-to-one chats, push notifications to the right person.", "https://github.com/linverno-tm/chatforge"),
                   ("Bulk SMS", "Android: SMS from an Excel or CSV list; the queue survives a phone restart.", "https://github.com/linverno-tm/bulk-sms"),
                   ("Task app", "Works offline and syncs on its own when the connection returns.", "https://github.com/linverno-tm/task-manager")],
        "media_chip": "Video", "media_h": "Live video made with Veo",
        "media_p": "For the Shuxrat o‘g‘li site. For type and number driven motion clips I use Remotion.",
        "veo_pauza": "Pause video", "veo_davom": "Play video",
        "buklet_chip": "Print design", "buklet_h": "Tri-fold booklet, Hamkor Savdo",
        "buklet_p": "A4, three panels, print-ready vector file.",
        "buklet_alt": "Hamkor Savdo tri-fold booklet: “installments up to 24 months”, products and monthly payments",
        "avto_chip": "Automation", "avto_h": "Handing manual work to software",
        "avto": [("Price watch", "Competitors’ posts in Telegram groups become prices; each store gets a daily PDF with only the new and changed prices."),
                 ("Tax audit report", "A program that builds the tax-audit report from invoices and cash receipts on its own."),
                 ("My own connectors", "MCP servers for YouTube and Pinterest, so channel and content work can be done through AI.")],
        "aloqa_h": "Have a project? Message me on Telegram.",
        "aloqa_p": "A few lines are enough: what your business does and what you want to speed up. I answer myself.",
        "qr": "Scan with your phone camera",
        "footer_til": "O‘zbekcha",
    },
}

# KINO TV botining haqiqiy salomlashuvi (kino-bot/bot/korinish.py: salom_matn, salom_kb; ism bo'lmasa «do'stim»)
CHAT = [("men", "/start"),
        ("yoz", ""),
        ("bot", "Salom, <b>do‘stim</b>! 🍿<br>Bu yerda <b>158</b> ta serial va <b>543</b> ta kino — hammasi o‘zbek tilida, bepul.<br>Nomini yoki kodini yozing — darhol topib beraman."),
        ("kb", "")]
KB = [("🎬 Katalog", True), ("🔥 Trendda", False), ("🆕 Yangilar", False), ("✨ Siz uchun", False), ("🎲 Tasodifiy", False), ("📂 Bo‘limlar", False), ("⭐ Ro‘yxatim", False)]

TG_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M21.4 4.2 2.9 11.3c-1.3.5-1.2 1.2-.2 1.5l4.7 1.5 1.8 5.6c.2.6.1.9.8.9.5 0 .7-.2 1-.5l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.1-14.8c.3-1.3-.5-1.9-1.5-1.8ZM8.6 14l9.3-5.9c.5-.3.9-.1.5.2l-7.9 7.2-.3 3.4L8.6 14Z"/></svg>'
OQ = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
X = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>'
YULDUZ = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="{c}" d="M12 0c.9 6.6 5.4 11.1 12 12-6.6.9-11.1 5.4-12 12-.9-6.6-5.4-11.1-12-12C6.6 11.1 11.1 6.6 12 0Z"/></svg>'
LENTA_RANG = ["#b9a2ff", "#c4b5fd", "#ffc93d", "#6cb2ff", "#dfd01f", "#c8a24a", "#f97316", "#4fe0b6", "#94a3b8"]


def e(s):
    return html.escape(s, quote=True)


def picture(root, name, alt, sizes, lazy=True, high=False):
    m = RASM[name]
    ws = sorted(m["widths"])
    def srcset(ext):
        return ", ".join(f"{root}img/{name}-{w}.{ext} {w}w" for w in ws)
    w0, h0 = ws[-1], round(m["h"] * ws[-1] / m["w"])
    attrs = f'width="{w0}" height="{h0}" alt="{e(alt)}" decoding="async"'
    if lazy:
        attrs += ' loading="lazy"'
    if high:
        attrs += ' fetchpriority="high"'
    return (f'<picture><source type="image/avif" srcset="{srcset("avif")}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{srcset("webp")}" sizes="{sizes}">'
            f'<img src="{root}img/{name}-{ws[0]}.webp" {attrs}></picture>')


def yorliq(matn):
    return f'<span class="yorliq"><i></i>{e(matn)}</span>'


def page(k):
    t = T[k]
    root = "" if k == "uz" else "../"
    url = SAYT if k == "uz" else SAYT + "en/"
    css = CSS.replace("{ROOT}", root)
    boshqa_til = "en" if k == "uz" else "uz"
    nav = "".join(f'<a class="bolim" href="{h}">{e(l)}</a>' for h, l in t["nav"])
    ish = {x["id"]: x for x in t["ishlar"]}

    sozlar = t["h1_sozlar"] + t["h1_sozlar"][:1]
    h1 = (f'<span class="q">{e(t["h1_bosh"])}</span>'
          f'<span class="q aylan" aria-hidden="true"><span class="aylan-ichi">'
          + "".join(f"<span>{e(x)}</span>" for x in sozlar) +
          f'</span></span><span class="statik">{e(t["h1_statik"])}</span>'
          f'<span class="q">{e(t["h1_oxir"])}</span>')

    halqa = "".join(
        f'<div class="halqa"><svg viewBox="0 0 58 58" aria-hidden="true"><circle class="orqa" cx="29" cy="29" r="24"/>'
        f'<circle class="old" cx="29" cy="29" r="24"/></svg><b>100</b>{e(x)}</div>' for x in t["t_tez"])

    chat = []
    for i, (kim, matn) in enumerate(CHAT):
        if kim == "yoz":
            chat.append(f'<div class="yozmoqda" style="--k:{i}" aria-hidden="true"><i></i><i></i><i></i></div>')
        elif kim == "kb":
            chat.append(f'<div class="tugmachalar" style="--k:{i}">' + "".join(
                f'<span{" class=keng" if keng else ""}>{e(x)}</span>' for x, keng in KB) + "</div>")
        else:
            chat.append(f'<div class="xabar {kim}" style="--k:{i}">{matn}</div>')

    lenta_bir = "".join(f'<span class="soz{" kontur" if i % 2 else ""}">{e(x)}</span>{YULDUZ.format(c=LENTA_RANG[i % len(LENTA_RANG)])}'
                        for i, x in enumerate(t["lenta"]))

    # --- ish plitkalari ---
    def ish_plitka(x, vizual):
        belgi = f'<span class="yorliq">{e(t["konsept"])}</span>' if x.get("belgi") else ""
        teg = "".join(f"<span>{e(s)}</span>" for s in x["teglar"])
        return (f'<article class="plitka ish ish-{x["id"]}" style="--rang:{RANG[x["id"]]}" data-oyna="oyna-{x["id"]}">'
                f'<div class="ish-bosh">{yorliq(x["chip"])}{belgi}</div>'
                f'<h3>{e(x["nom"])}</h3><p class="tavsif">{e(x["tavsif"])}</p><div class="teglar">{teg}</div>'
                f'<button class="ochish" type="button" aria-haspopup="dialog" aria-controls="oyna-{x["id"]}">{e(t["batafsil"])}{OQ}</button>'
                f'<div class="vizual">{vizual}</div></article>')

    def tel_qator(nomlar, sizes):
        return '<div class="telefon-qator">' + "".join(
            f'<div class="tel">{picture(root, n, "", sizes)}</div>' for n in nomlar) + "</div>"

    plitkalar = [
        ish_plitka(ish["crm"], f'<div class="ramka">{picture(root, "crm-mijozlar", t["crm_alt"][1], "(min-width: 1100px) 62vw, 100vw")}</div>'),
        ish_plitka(ish["mijoz"], tel_qator(ish["mijoz"]["tel"], "(min-width: 1100px) 10vw, 30vw")),
        ish_plitka(ish["kino"], tel_qator(ish["kino"]["tel"], "(min-width: 1100px) 13vw, 40vw")),
        ish_plitka(ish["qogoz"], tel_qator(ish["qogoz"]["tel"], "(min-width: 1100px) 13vw, 40vw")),
        f'<article class="plitka ish ish-boshqa" style="--rang:{RANG["boshqa"]}"><div class="ish-bosh">{yorliq(t["boshqa_chip"])}</div>'
        f'<h3>{e(t["boshqa_h"])}</h3><ul>' + "".join(
            f'<li><b>{e(a)}</b><span>{e(b)}</span><a href="{h}" rel="noopener">{e(t["kod"])}: {e(a)}</a></li>' for a, b, h in t["boshqa"]) + "</ul></article>",
    ]
    for sid in ("hamkor", "shuxrat", "oltinkol", "minges"):
        x = ish[sid]
        plitkalar.append(ish_plitka(x, f'<div class="ramka oqim">{picture(root, x["uzun"], "", "(min-width: 700px) 48vw, 100vw")}</div>'))
    plitkalar.append(
        f'<article class="plitka ish ish-media" style="--rang:{RANG["media"]}"><div class="ish-bosh">{yorliq(t["media_chip"])}</div>'
        f'<h3>{e(t["media_h"])}</h3><p class="tavsif">{e(t["media_p"])}</p><div class="vizual"><div class="ramka video-ramka">'
        f'<video muted loop playsinline preload="none" poster="{root}img/veo-kadr-800.webp" width="960" height="540" data-src="{root}media/veo-tovuq.mp4" aria-label="{e(t["media_h"])}"></video>'
        f'<button class="pauza" type="button" hidden data-pauza="{e(t["veo_pauza"])}" data-davom="{e(t["veo_davom"])}" aria-label="{e(t["veo_pauza"])}"></button></div></div></article>')
    plitkalar.append(
        f'<article class="plitka ish ish-buklet" style="--rang:{RANG["buklet"]}"><div class="ish-bosh">{yorliq(t["buklet_chip"])}</div>'
        f'<h3>{e(t["buklet_h"])}</h3><p class="tavsif">{e(t["buklet_p"])}</p><div class="vizual"><div class="ramka">'
        f'{picture(root, "buklet", t["buklet_alt"], "(min-width: 1100px) 56vw, 100vw")}</div></div></article>')
    plitkalar.append(
        f'<article class="plitka ish ish-avto" style="--rang:{RANG["avto"]}"><div class="ish-bosh">{yorliq(t["avto_chip"])}</div>'
        f'<h3>{e(t["avto_h"])}</h3><ul>' + "".join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in t["avto"]) + "</ul></article>")

    # --- loyiha oynalari ---
    oynalar = []
    for x in t["ishlar"]:
        q = t["qadam_m"] if x.get("maqsad") else t["qadam"]
        qadam = "".join(f'<div class="qadam"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in zip(q, x["qadamlar"]))
        if x.get("tel"):
            rasm = '<div class="oyna-rasmlar tel">' + "".join(
                f'<figure><div class="ramka">{picture(root, n, c, "(min-width: 800px) 280px, 45vw")}</div><figcaption>{e(c)}</figcaption></figure>'
                for n, c in x["rasmlar"]) + "</div>"
        elif x.get("uzun"):
            rasm = (f'<div class="oyna-rasmlar"><figure><div class="ramka uzun-ramka" tabindex="0" role="region" aria-label="{e(x["nom"])}">'
                    f'{picture(root, x["uzun"], x["nom"], "(min-width: 1000px) 920px, 100vw")}</div></figure></div>')
        else:
            rasm = '<div class="oyna-rasmlar">' + "".join(
                f'<figure><div class="ramka">{picture(root, n, c, "(min-width: 1000px) 920px, 100vw")}</div><figcaption>{e(c)}</figcaption></figure>'
                for n, c in x["rasmlar"]) + "</div>"
        fakt = ""
        if x.get("faktlar"):
            fakt = '<dl class="oyna-faktlar">' + "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in x["faktlar"]) + "</dl>"
        havola = "".join(f'<a class="btn btn-shaffof" href="{h}" rel="noopener">{e(l)}{OQ}</a>' for h, l in x["havolalar"])
        izoh = f'<p class="izoh">{e(x["izoh"])}</p>' if x.get("izoh") else ""
        oynalar.append(
            f'<dialog class="oyna" id="oyna-{x["id"]}" style="--rang:{RANG[x["id"]]}" aria-labelledby="oyna-{x["id"]}-h">'
            f'<div class="oyna-ichi"><div class="oyna-bosh"><div>{yorliq(x["chip"])}<h2 id="oyna-{x["id"]}-h">{e(x["nom"])}</h2></div>'
            f'<button class="yop" type="button" aria-label="{e(t["yopish"])}">{X}</button></div>'
            f'<p class="lid">{e(x["tavsif"])}</p><div class="qadamlar">{qadam}</div>{fakt}{rasm}{izoh}'
            f'<div class="oyna-oxir">{havola}<a class="btn btn-oq" href="{TG}" rel="noopener">{TG_ICON}{e(t["tg_btn"])}</a></div></div></dialog>')

    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<meta name="theme-color" content="#07080c">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="uz" href="{SAYT}">
<link rel="alternate" hreflang="en" href="{SAYT}en/">
<link rel="alternate" hreflang="x-default" href="{SAYT}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(t['title'])}">
<meta property="og:description" content="{e(t['desc'])}">
<meta property="og:image" content="{SAYT}og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="preload" href="{root}unbounded.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{root}onest.woff2" as="font" type="font/woff2" crossorigin>
<style>{css}</style>
<script>if (!matchMedia("(prefers-reduced-motion: reduce)").matches) document.documentElement.classList.add("harakat");</script>
</head>
<body>
<a class="skip" href="#asosiy">{e(t['skip'])}</a>
<header class="tepa"><div class="wrap">
  <a class="belgi-nom" href="{root or './'}"><span class="monogram" aria-hidden="true">MT</span><span class="ism"><b>Muhammadabdulloh Tojiddinov</b><small>{e(t['kasb'])}</small></span><span class="sr">Muhammadabdulloh Tojiddinov</span></a>
  <nav aria-label="{'Bo‘limlar' if k == 'uz' else 'Sections'}">{nav}</nav>
  <a class="til" href="{t['til_link']}" hreflang="{boshqa_til}" lang="{boshqa_til}" aria-label="{e(t['til_aria'])}">{t['til_label']}</a>
  <a class="btn btn-oq" href="{TG}" rel="noopener" aria-label="{e(t['tg_btn'])}">{TG_ICON}<span>{e(t['tg_btn'])}</span></a>
</div></header>
<main id="asosiy">
<section class="wrap boshi" aria-labelledby="h1">
  <div class="bento">
    <div class="plitka t-hero">
      <div>{yorliq(t['kasb'])}</div>
      <div><h1 id="h1">{h1}</h1><p class="lid">{t['lid']}</p>
      <div class="tugmalar"><a class="btn btn-oq" href="{TG}" rel="noopener">{TG_ICON}{e(t['tg_btn'])}</a><a class="btn btn-shaffof" href="#ishlar">{e(t['cta2'])}</a></div></div>
    </div>
    <div class="plitka t-crm" data-oyna="oyna-crm">
      {yorliq(t['t_crm_chip'])}
      <h2>Hamkor CRM</h2><p>{e(t['t_crm_p'])}</p>
      <div class="ekran-quti"><div class="ekran">{picture(root, "crm-bosh", t["crm_alt"][0], "(min-width: 1100px) 46vw, 110vw", lazy=False, high=True)}</div></div>
      <button class="sr" type="button" aria-haspopup="dialog" aria-controls="oyna-crm">{e(t['batafsil'])}: Hamkor CRM</button>
    </div>
    <div class="plitka t-son">
      {yorliq(t['t_son_chip'])}
      <div><div class="katta-son" data-son="1373">{'1 373' if k == 'uz' else '1,373'}</div><p>{e(t['t_son_p'])}</p></div>
    </div>
    <div class="plitka t-tez">
      {yorliq(t['t_tez_chip'])}
      <div class="halqalar">{halqa}</div>
      <p class="izoh-kichik">{e(t['t_tez_p'])}</p>
    </div>
    <div class="plitka t-chat">
      {yorliq(t['t_chat_chip'])}
      <div class="chat">
        <div class="chat-bosh"><span class="av" aria-hidden="true">TV</span><span><b>KINO TV</b><small>@linvkino_bot · {e(t['t_chat_p'])}</small></span></div>
        {''.join(chat)}
      </div>
    </div>
    <div class="plitka t-tel" data-oyna="oyna-mijoz">
      {yorliq(t['t_tel_chip'])}
      <h2>{e(t['t_tel_h'])}</h2><p class="kichik-p">{e(t['t_tel_p'])}</p>
      <div class="telefon-quti"><div class="telefon-kichik">{picture(root, "mobil-bosh", "", "(min-width: 1100px) 16vw, 50vw", lazy=False)}</div></div>
      <button class="sr" type="button" aria-haspopup="dialog" aria-controls="oyna-mijoz">{e(t['batafsil'])}: {e(t['t_tel_h'])}</button>
    </div>
    <div class="plitka t-xiz">
      {yorliq(t['t_xiz_chip'])}
      <ul>{''.join(f'<li>{e(x)}</li>' for x in t['t_xiz'])}</ul>
      <p>{e(t['t_xiz_p'])}</p>
    </div>
  </div>
</section>
<div class="lenta" aria-hidden="true"><div class="lenta-ichi">{lenta_bir}{lenta_bir}</div></div>
<section class="wrap bolim ishlar" id="ishlar" aria-labelledby="ishlar-h">
  <div class="bolim-sarlavha"><h2 id="ishlar-h">{e(t['ishlar_h'])}</h2><p>{e(t['ishlar_p'])}</p></div>
  <div class="bento">{''.join(plitkalar)}</div>
</section>
<section class="wrap bolim" id="aloqa" aria-labelledby="aloqa-h">
  <div class="plitka t-aloqa">
    <div>
      <h2 id="aloqa-h">{e(t['aloqa_h'])}</h2>
      <p>{e(t['aloqa_p'])}</p>
      <div class="tugmalar"><a class="btn btn-oq" href="{TG}" rel="noopener">{TG_ICON}{e(t['tg_btn'])}</a></div>
      <a class="dastak" href="{TG}" rel="noopener">@m_tojiddinov7</a>
      <div class="havolalar"><a href="https://hamkorcrm.uz/" rel="noopener">hamkorcrm.uz</a><a href="https://github.com/linverno-tm" rel="noopener">GitHub</a></div>
    </div>
    <div class="qr" aria-hidden="true"><div class="kod"><svg viewBox="0 0 27 27"><path d="{QR}"/></svg></div><small>{e(t['qr'])}</small></div>
  </div>
</section>
</main>
{''.join(oynalar)}
<footer><div class="wrap"><span>© 2026 Muhammadabdulloh Tojiddinov</span><a href="{t['til_link']}" hreflang="{boshqa_til}">{e(t['footer_til'])}</a></div></footer>
<script>{JS}</script>
</body>
</html>
"""


for k, out in (("uz", "index.html"), ("en", os.path.join("en", "index.html"))):
    p = os.path.join(ROOT, out)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(page(k))
    print(out, os.path.getsize(p), "bayt")
