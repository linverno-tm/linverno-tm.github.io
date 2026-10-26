"""Saytni yig'adi.

    python tools/build.py

Chiqadi: index.html, ishlar/<slug>/index.html (o'zbekcha) va en/... (inglizcha), sitemap.xml.
Matn shu faylda; uslub tools/uslub.css, skript tools/skript.js (ikkalasi sahifa ichiga qo'yiladi);
rasm o'lchamlari tools/rasmlar.json da.
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RASM = json.load(open(os.path.join(ROOT, "tools", "rasmlar.json"), encoding="utf-8"))
CSS = "".join(open(os.path.join(ROOT, "tools", f), encoding="utf-8").read() for f in ("uslub.css", "chuqurlik.css"))
JS = open(os.path.join(ROOT, "tools", "skript.js"), encoding="utf-8").read()
SAYT = "https://linverno-tm.github.io"
TG = "https://t.me/m_tojiddinov7"
GITHUB = "https://github.com/linverno-tm"
MANBA = "https://github.com/linverno-tm/linverno-tm.github.io"

TG_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M21.4 4.2 2.9 11.3c-1.3.5-1.2 1.2-.2 1.5l4.7 1.5 1.8 5.6c.2.6.1.9.8.9.5 0 .7-.2 1-.5l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.1-14.8c.3-1.3-.5-1.9-1.5-1.8ZM8.6 14l9.3-5.9c.5-.3.9-.1.5.2l-7.9 7.2-.3 3.4L8.6 14Z"/></svg>'

# --------------------------------------------------------------------------------------------
# Umumiy matn
# --------------------------------------------------------------------------------------------
U = {
    "uz": {
        "title": "Muhammadabdulloh Tojiddinov — dasturchi",
        "desc": "Biznes uchun savdo va nasiya tizimlari, mobil ilovalar, Telegram botlar va saytlar yozaman. Hamkor CRM muallifi.",
        "skip": "Asosiy qismga o‘tish",
        "ishlar": "Ishlar", "aloqa": "Aloqa",
        "til": "English", "til_qisqa": "EN", "til_kod": "en",
        "kirish_1": "Biznes uchun dastur yozaman: savdo va nasiya tizimlari, mobil ilovalar, Telegram botlar va saytlar. Dizayndan serverga chiqarishgacha o‘zim qilaman.",
        "kirish_2": "Hozir <b>Hamkor CRM</b> ustida ishlayapman. Bu to‘rt filialli savdo tarmog‘i uchun 1C o‘rnini bosgan tizim va uning mijozlar ilovasi.",
        "tg": "Telegram’da yozish",
        "tanlangan": "Tanlangan ishlar",
        "boshqa": "Boshqa ishlar",
        "aloqa_1": "Loyihangiz bo‘lsa, Telegram’da yozing: <a href=\"" + TG + "\">@m_tojiddinov7</a>.",
        "aloqa_2": "Qisqacha yozing: biznesingiz nima bilan shug‘ullanadi va nimani tezlashtirmoqchisiz.",
        "manba": "Sayt manbasi",
        "orqaga": "Barcha ishlar",
        "keyingi": "Keyingi loyiha",
        "meta": ("Davr", "Rol", "Texnologiyalar", "Holat"),
        "rol": "Muallif: dizayn va dasturlash",
        "konsept": "Konsept",
        "pauza": "Videoni to‘xtatish", "davom": "Videoni davom ettirish",
        "oy": ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"],
        "hozir": "hozir",
        "kod": "Kodi",
        "nusxa": "Nusxa olish", "nusxa_ok": "Nusxa olindi", "nusxa_xato": "Qo‘lda nusxa oling",
        "aloqa_k": "Loyihangiz bo‘lsa, Telegram’da yozing. Qisqacha yozing: biznesingiz nima bilan shug‘ullanadi va nimani tezlashtirmoqchisiz.",
        "yoq_t": "Sahifa topilmadi", "yoq_p": "Havola eskirgan yoki xato yozilgan. Ishlardan birini oching yoki bosh sahifaga qayting.", "bosh_sahifa": "Bosh sahifa",
    },
    "en": {
        "title": "Muhammadabdulloh Tojiddinov — software developer",
        "desc": "I build sales and installment systems, mobile apps, Telegram bots and websites for businesses. Author of Hamkor CRM.",
        "skip": "Skip to content",
        "ishlar": "Work", "aloqa": "Contact",
        "til": "O‘zbekcha", "til_qisqa": "UZ", "til_kod": "uz",
        "kirish_1": "I build software for businesses: sales and installment systems, mobile apps, Telegram bots and websites. I do the whole thing myself, from design to deployment.",
        "kirish_2": "Right now I’m working on <b>Hamkor CRM</b>, a system that replaced 1C for a four-branch retail chain, and its customer app.",
        "tg": "Message on Telegram",
        "tanlangan": "Selected work",
        "boshqa": "Other work",
        "aloqa_1": "If you have a project, message me on Telegram: <a href=\"" + TG + "\">@m_tojiddinov7</a>.",
        "aloqa_2": "A few lines are enough: what your business does and what you want to speed up.",
        "manba": "Site source",
        "orqaga": "All work",
        "keyingi": "Next project",
        "meta": ("Period", "Role", "Stack", "Status"),
        "rol": "Author: design and development",
        "konsept": "Concept",
        "pauza": "Pause video", "davom": "Play video",
        "oy": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "hozir": "present",
        "kod": "Code",
        "nusxa": "Copy", "nusxa_ok": "Copied", "nusxa_xato": "Copy it manually",
        "aloqa_k": "If you have a project, message me on Telegram. A few lines are enough: what your business does and what you want to speed up.",
        "yoq_t": "Page not found", "yoq_p": "The link is outdated or mistyped. Open one of the projects or go back home.", "bosh_sahifa": "Home",
    },
}

# --------------------------------------------------------------------------------------------
# Loyihalar. kadr: ("keng", rasm) | ("tel", [rasmlar]) | ("uzun", rasm)
# Bloklar: ("h", matn) | ("p", matn) | ("ul", [..]) | ("rasm", nom, izoh) | ("tel", [(nom, izoh)])
#          | ("butun", nom, izoh) | ("video", izoh)
# --------------------------------------------------------------------------------------------
LOYIHALAR = [
    {"slug": "hamkor-crm", "boshi": (2026, 9), "oxiri": None, "kadr": ("keng", "crm-bosh"),
     "stack": "Next.js, TypeScript, PostgreSQL 16, Tauri v2",
     "havola": ("https://hamkorcrm.uz/", "hamkorcrm.uz"),
     "uz": {"nom": "Hamkor CRM", "tur": "Savdo va nasiya tizimi",
            "lid": "To‘rt filialli savdo tarmog‘i uchun 1C o‘rnini bosgan muddatli to‘lov savdo tizimi.",
            "holat": "Ishlatilmoqda",
            "alt": "Hamkor CRM bosh sahifasi: kassalar, nasiya qarzi va oylik foyda grafigi; summalar yopilgan",
            "bloklar": [
                ("h", "Vazifa"),
                ("p", "Tarmoqdagi to‘rtta do‘kon to‘rtta alohida 1C bazasida ishlardi va ular bir-birini ko‘rmasdi. Bir do‘konda qora ro‘yxatga tushgan mijoz boshqasida yana nasiyaga tovar olishi mumkin edi, umumiy hisobot uchun esa ma’lumotni to‘rt joydan yig‘ish kerak edi."),
                ("h", "Yechim"),
                ("p", "Hamma do‘kon uchun bitta baza va bitta tizim: savdo, nasiya shartnomalari, to‘lov grafigi, kassa, ombor, ish haqi va hisobotlar. Tizim 1C bilan ikki tomonlama sinxronlanadi, shuning uchun o‘tish davrida ikkalasi yonma-yon ishladi."),
                ("rasm", "crm-mijozlar", "Mijozlar ro‘yxati: ishonch bahosi, shartnomalar va muddati o‘tgan qarz."),
                ("ul", ["Internet uzilsa ham ishlaydi: kompyuterdagi shifrlangan nusxa bilan oynalar ochilaveradi, amallar navbatga yoziladi va aloqa tiklanganda yuboriladi.",
                        "Xodimlar Windows dasturida ishlaydi (Tauri v2): chek so‘ramasdan chop etiladi, dastur o‘zi yangilanadi.",
                        "Har bir yangilanish ishga chiqishidan oldin vaqtinchalik PostgreSQL bazada savdo, shartnoma, to‘lov va hisobot ssenariylari bilan tekshiriladi.",
                        "Mijozlar o‘z shartnomasi va to‘lovlarini alohida mobil ilovada ko‘radi; ilova shu bazaga ulangan."]),
                ("rasm", "crm-qarz", "Muddati o‘tgan qarzlar kechikish kunlari bo‘yicha, undiruvchi uchun qo‘ng‘iroq natijasi bilan."),
                ("rasm", "crm-kassa", "Kassalardagi qoldiq filiallar va to‘lov turlari kesimida."),
                ("h", "Natija"),
                ("p", "25-sentabrdan 26-oktabrgacha 1 421 ta commit va 244 ta sahifa. Platforma meniki, shuning uchun uni boshqa savdo tarmog‘iga ham moslab bera olaman."),
            ],
            "izoh": "Skrinshotlar demo bazadan olingan; summalar, ismlar va filial nomlari yopilgan."},
     "en": {"nom": "Hamkor CRM", "tur": "Sales and installment system",
            "lid": "An installment-sales system that replaced 1C for a four-branch retail chain.",
            "holat": "In use",
            "alt": "Hamkor CRM home screen: cash, installment debt and a monthly profit chart; amounts hidden",
            "bloklar": [
                ("h", "The problem"),
                ("p", "The chain’s four stores ran on four separate 1C databases that couldn’t see each other. A customer blacklisted in one store could get new credit in the next, and any combined report meant collecting data from four places."),
                ("h", "What I built"),
                ("p", "One database and one system for every store: sales, installment contracts, payment schedules, cash, warehouse, payroll and reports. It syncs with 1C both ways, so the two ran side by side during the switch."),
                ("rasm", "crm-mijozlar", "Customer list: trust score, contracts and overdue debt."),
                ("ul", ["It works without internet: an encrypted local copy keeps every window usable, actions queue up and are sent when the connection returns.",
                        "Staff use a Windows app built with Tauri v2: receipts print silently and the app updates itself.",
                        "Before a release goes live, sales, contract, payment and report scenarios run against a throw-away PostgreSQL database.",
                        "Customers see their contracts and payments in a separate mobile app connected to the same database."]),
                ("rasm", "crm-qarz", "Overdue debt grouped by days late, with the collector’s call result."),
                ("rasm", "crm-kassa", "Cash balances by branch and payment type."),
                ("h", "Result"),
                ("p", "1,421 commits and 244 pages between 25 September and 26 October. I own the platform, so I can adapt it to another retail chain."),
            ],
            "izoh": "Screenshots come from a demo database; amounts, names and branch names are hidden."}},

    {"slug": "mijozlar-ilovasi", "boshi": (2026, 10), "oxiri": None, "kadr": ("tel", ["mobil-bosh", "mobil-katalog", "mobil-tolovlar"]),
     "stack": "Flutter, Dart, Riverpod",
     "uz": {"nom": "Hamkor mijozlar ilovasi", "tur": "Mobil ilova, Android va iPhone",
            "lid": "Muddatli to‘lov bilan xarid qilgan mijozlar uchun telefon ilovasi.",
            "holat": "Do‘konlarga chiqarishga tayyorlanmoqda",
            "alt": "Hamkor mijozlar ilovasi: bosh sahifa, katalog va to‘lovlar tarixi",
            "bloklar": [
                ("h", "Vazifa"),
                ("p", "Shartnomasi, keyingi to‘lovi yoki qolgan qarzini bilish uchun mijoz do‘konga borishi yoki qo‘ng‘iroq qilishi kerak edi. Do‘konda esa eslatma va aksiyalarni mijozga to‘g‘ridan-to‘g‘ri yetkazish yo‘li yo‘q edi."),
                ("h", "Yechim"),
                ("p", "Ilova Hamkor CRM’ning mijoz API’siga ulanadi. Kirish telefon raqami va SMS kod bilan; token telefonning xavfsiz xotirasida (iOS Keychain, Android Keystore) saqlanadi."),
                ("tel", [("mobil-bosh", "Bosh sahifa. Summalarni ilovaning o‘zi yashiradi."), ("mobil-katalog", "Katalog: narx oylik to‘lov bilan."), ("mobil-tolovlar", "To‘lovlar tarixi oylar bo‘yicha.")]),
                ("ul", ["Har bo‘lim to‘rt qatlamda: model, ma’lumot, holat va ekran. Ekran API’ga to‘g‘ridan-to‘g‘ri murojaat qilmaydi.",
                        "Testlar internetsiz ishlaydi: server o‘rniga namuna javoblar beriladi.",
                        "Birinchi versiya Expo (React Native) da yozilgan edi; 7-oktabrda ekranlar va API o‘zgarmagan holda Flutter’ga ko‘chirildi.",
                        "O‘zbek (kirill va lotin) va rus tilida, yorug‘ va qorong‘i mavzu."]),
                ("h", "Natija"),
                ("p", "Android, iPhone va web uchun bitta kod. Ilova hozir do‘konlarga chiqarishga tayyorlanmoqda."),
            ],
            "izoh": "Demo mijoz; ism va summalar yopilgan."},
     "en": {"nom": "Hamkor customer app", "tur": "Mobile app, Android and iPhone",
            "lid": "A phone app for customers who bought on installments.",
            "holat": "Being prepared for the stores",
            "alt": "Hamkor customer app: home, catalog and payment history",
            "bloklar": [
                ("h", "The problem"),
                ("p", "To check their contract, next payment or remaining debt, customers had to visit the store or call. The store had no direct way to send them reminders and offers."),
                ("h", "What I built"),
                ("p", "The app talks to Hamkor CRM’s customer API. Sign-in is a phone number and an SMS code; the token lives in the phone’s secure storage (iOS Keychain, Android Keystore)."),
                ("tel", [("mobil-bosh", "Home. The app hides amounts itself."), ("mobil-katalog", "Catalog priced by monthly payment."), ("mobil-tolovlar", "Payment history by month.")]),
                ("ul", ["Each feature has four layers: model, data, state and screen. Screens never call the API directly.",
                        "Tests run offline against sample responses instead of a server.",
                        "The first version was written in Expo (React Native); on 7 October it moved to Flutter with the same screens and API.",
                        "Uzbek (Cyrillic and Latin) and Russian, light and dark themes."]),
                ("h", "Result"),
                ("p", "One codebase for Android, iPhone and web. The app is now being prepared for the stores."),
            ],
            "izoh": "Demo customer; name and amounts are hidden."}},

    {"slug": "kino-tv", "boshi": (2026, 10), "oxiri": (2026, 10), "kadr": ("tel", ["kino-bosh", "kino-serial"]),
     "stack": "Python, aiogram 3, SQLite, Cloudflare Pages",
     "havola": ("https://t.me/linvkino_bot", "@linvkino_bot"),
     "uz": {"nom": "KINO TV", "tur": "Telegram bot va mini app",
            "lid": "Seriallar va kinolar uchun Telegram bot va mini app.",
            "alt": "KINO TV mini app: bosh sahifa va serial sahifasi",
            "bloklar": [
                ("h", "Vazifa"),
                ("p", "Ko‘p qismli serialni Telegram’da ko‘rish noqulay: kerakli qismni topish qiyin, qayerda to‘xtaganingiz esdan chiqadi. Admin uchun esa har bir yangi qism qo‘l ishi edi."),
                ("h", "Yechim"),
                ("p", "Admin yopiq ombor kanalga video joylaydi, bot postni o‘zi o‘qib katalogga yozadi va kod beradi. Video foydalanuvchiga nusxa sifatida yuboriladi, shuning uchun hajm chegarasi yo‘q."),
                ("tel", [("kino-bosh", "Mini app bosh sahifasi."), ("kino-serial", "Serial sahifasi va qismlar.")]),
                ("ul", ["Mini app yig‘ishsiz HTML, CSS va JavaScript; Cloudflare Pages’da turadi, katalog chekkada 60 soniya keshlanadi.",
                        "Qaysi qismda to‘xtaganingizni eslab qoladi va keyingisidan davom ettiradi; saqlanganlar ro‘yxati bor.",
                        "Bot va mini app bitta API’dan foydalanadi."]),
                ("h", "Natija"),
                ("p", "Katalogda 158 ta serial va 543 ta kino, 8 ta bo‘lim."),
            ]},
     "en": {"nom": "KINO TV", "tur": "Telegram bot and mini app",
            "lid": "A Telegram bot and mini app for series and films.",
            "alt": "KINO TV mini app: home and a series page",
            "bloklar": [
                ("h", "The problem"),
                ("p", "Watching a long series in Telegram is awkward: the right episode is hard to find and you lose where you stopped. For the admin, every new episode was manual work."),
                ("h", "What I built"),
                ("p", "The admin posts a video to a private storage channel; the bot reads the post, adds it to the catalog and assigns a code. Videos are sent to users as copies, so there is no size limit."),
                ("tel", [("kino-bosh", "Mini app home."), ("kino-serial", "Series page with episodes.")]),
                ("ul", ["The mini app is plain HTML, CSS and JavaScript on Cloudflare Pages, with the catalog cached at the edge for 60 seconds.",
                        "It remembers where you stopped and continues from the next episode; there is a saved list.",
                        "The bot and the mini app share one API."]),
                ("h", "Result"),
                ("p", "158 series and 543 films in 8 sections."),
            ]}},

    {"slug": "qogoz-bino", "boshi": (2026, 10), "oxiri": (2026, 10), "kadr": ("tel", ["qogoz-bosh", "qogoz-serial"]),
     "stack": "HTML, CSS, JavaScript, Python",
     "havola": ("https://qogoz-bino.pages.dev/", "qogoz-bino.pages.dev"),
     "uz": {"nom": "Qog‘oz Bino", "tur": "Telegram mini app",
            "lid": "Do‘stimning @QogozBinoTVbot boti uchun posterli katalog.",
            "alt": "Qog‘oz Bino mini app: yangi qismlar va serial sahifasi",
            "bloklar": [
                ("h", "Vazifa"),
                ("p", "Botda serial ko‘p, lekin ularni ko‘rib tanlash uchun katalog yo‘q edi. Shart: botning kodiga tegmaslik va uning tokenini ishlatmaslik."),
                ("h", "Yechim"),
                ("p", "Katalogni botning o‘zidan yig‘adigan skript yozdim: u har bir kodga /start yuboradi va javobni o‘qiydi. Mini app shu katalog bilan ishlaydi; serial tanlansa, kartani va qismlarni botning o‘zi beradi."),
                ("tel", [("qogoz-bosh", "Yangi qismlar va haftaning eng ko‘p ko‘rilganlari."), ("qogoz-serial", "Serial sahifasi.")]),
                ("ul", ["Kirill va lotinda jonli qidiruv, bo‘lim va janr bo‘yicha saralash.",
                        "To‘liq yig‘ish taxminan 10 daqiqa; yangi kodlar alohida tez qo‘shiladi."]),
                ("h", "Natija"),
                ("p", "Mini app BotFather’dagi menyu tugmasi orqali ochiladi; botning o‘z kodiga hech narsa qo‘shilmagan."),
            ]},
     "en": {"nom": "Qog‘oz Bino", "tur": "Telegram mini app",
            "lid": "A poster catalog for my friend’s bot, @QogozBinoTVbot.",
            "alt": "Qog‘oz Bino mini app: new episodes and a series page",
            "bloklar": [
                ("h", "The problem"),
                ("p", "The bot had plenty of series but no catalog to browse them. The constraint: don’t touch the bot’s code and don’t use its token."),
                ("h", "What I built"),
                ("p", "A script builds the catalog from the bot itself: it sends /start for each code and reads the reply. The mini app runs on that catalog; picking a series hands over to the bot, which sends the card and episodes."),
                ("tel", [("qogoz-bosh", "New episodes and the week’s most watched."), ("qogoz-serial", "Series page.")]),
                ("ul", ["Live search in Cyrillic and Latin, filters by section and genre.",
                        "A full rebuild takes about 10 minutes; new codes can be added quickly on their own."]),
                ("h", "Result"),
                ("p", "The mini app opens from the bot’s menu button in BotFather; nothing was added to the bot’s own code."),
            ]}},

    {"slug": "hamkor-savdo", "boshi": (2026, 8), "oxiri": None, "kadr": ("uzun", "uzun-hamkor"),
     "stack": "Next.js 16, React 19, TypeScript, Tailwind CSS v4",
     "havola": ("https://hamkorsavdo.uz/", "hamkorsavdo.uz"),
     "uz": {"nom": "Hamkor Savdo", "tur": "Brend sayti",
            "lid": "To‘rt filialli savdo tarmog‘ining brend sayti, narx kuzatuvi va bosma materiallar.",
            "holat": "Ishlab turibdi",
            "alt": "Hamkor Savdo sayti, bosh sahifa",
            "bloklar": [
                ("h", "Vazifa"),
                ("p", "Kompaniyani, uning taklifini, har bir filialni va bog‘lanish yo‘llarini bitta saytda ko‘rsatish. Asosiy shart: sekin mobil internetda ham tez ochilsin."),
                ("h", "Yechim"),
                ("p", "Animatsiya kutubxonasi ishlatilmadi: barcha harakat CSS va taxminan 1 KB JavaScript. Sahifa JavaScript yetib kelmasdan ham to‘liq o‘qiladi va ishlaydi: mobil menyu oddiy <details> elementida, telefon va manzillar oddiy havolalar."),
                ("ul", ["Ranglar, shriftlar va logotip brendbukdan olingan; logotip rasmdan vektorga o‘tkazilgan.",
                        "Matn kontrasti hamma joyda kamida 4.5:1.",
                        "E’lon qilinmagan ma’lumot, masalan ish vaqti yoki kafolat muddati, to‘qib qo‘yilmagan."]),
                ("butun", "uzun-hamkor", "Bosh sahifa to‘liq; ramka ichida aylantirib ko‘ring."),
                ("h", "Yonidagi ishlar"),
                ("p", "Narx kuzatuvi: raqobatchilarning Telegram guruhlaridagi e’lonlaridan narxlar ajratib olinadi, har bir do‘konga kunlik PDF faqat yangi va o‘zgargan narxlar bilan boradi."),
                ("rasm", "buklet", "Yevrobuklet, A4, uch buklama; bosmaga tayyor vektor fayl."),
                ("h", "Natija"),
                ("p", "O‘qiladigan sahifa (HTML va CSS) gzip bilan 35 KB."),
            ]},
     "en": {"nom": "Hamkor Savdo", "tur": "Brand website",
            "lid": "The brand site for a four-branch retail chain, plus price watching and print.",
            "holat": "Live",
            "alt": "Hamkor Savdo website, home page",
            "bloklar": [
                ("h", "The problem"),
                ("p", "Show the company, its offer, every branch and every way to reach it on one site. The main constraint: fast on slow mobile connections."),
                ("h", "What I built"),
                ("p", "No animation library: all motion is CSS plus about 1 KB of JavaScript. The page is fully readable and usable before any JavaScript arrives: the mobile menu is a plain <details> element, phone numbers and addresses are plain links."),
                ("ul", ["Colours, fonts and the logo come from the brand book; the logo was traced to vector from the bitmap.",
                        "Every text pair has at least 4.5:1 contrast.",
                        "Unpublished facts such as opening hours or warranty length were not made up."]),
                ("butun", "uzun-hamkor", "The full home page; scroll inside the frame."),
                ("h", "Alongside"),
                ("p", "Price watching: prices are pulled from competitors’ posts in Telegram groups, and each store gets a daily PDF with only the new and changed prices."),
                ("rasm", "buklet", "Tri-fold A4 booklet, print-ready vector file."),
                ("h", "Result"),
                ("p", "The readable page (HTML and CSS) is 35 KB gzipped."),
            ]}},

    {"slug": "mini-ges", "boshi": (2026, 10), "oxiri": (2026, 10), "kadr": ("uzun", "uzun-minges"),
     "stack": "HTML, CSS, JavaScript, GSAP, GitHub Actions",
     "havola": ("https://linverno-tm.github.io/mini-ges-site/", "linverno-tm.github.io/mini-ges-site"),
     "uz": {"nom": "MINI GES", "tur": "Sayt",
            "lid": "Kichik gidroelektrostansiyalar va ularni qurish xizmati uchun sayt.",
            "alt": "MINI GES sayti, bosh sahifa",
            "bloklar": [
                ("h", "Vazifa"),
                ("p", "Ulug‘nor GES (600 kVt, ishlab turibdi) va Baliqchi GES (1 000 kVt) ni tanishtirish va mini-GES qurish xizmatini sotish."),
                ("h", "Yechim"),
                ("p", "Freymvorksiz statik sayt. «Qanday ishlaydi» bo‘limi 3D model o‘rniga generatsiya qilingan izometrik SVG (taxminan 53 KB), shuning uchun arzon telefonda ham silliq ishlaydi."),
                ("ul", ["Soha yangiliklari sahifa ochilganda emas, sayt yig‘ilayotganda yoziladi: begona saytga so‘rov ketmaydi.",
                        "Har bir o‘zgarishni CI tekshiradi va GitHub Pages’ga o‘zi chiqaradi.",
                        "O‘zbek va rus tilida."]),
                ("butun", "uzun-minges", "Bosh sahifa to‘liq; ramka ichida aylantirib ko‘ring."),
                ("h", "Natija"),
                ("p", "Telefonda birinchi ochilishda taxminan 170 KB (gzip), birorta rasm yuklanmaydi."),
            ]},
     "en": {"nom": "MINI GES", "tur": "Website",
            "lid": "A site for small hydro-power plants and the service of building them.",
            "alt": "MINI GES website, home page",
            "bloklar": [
                ("h", "The problem"),
                ("p", "Present Ulug‘nor GES (600 kW, running) and Baliqchi GES (1,000 kW), and sell the service of building small hydro plants."),
                ("h", "What I built"),
                ("p", "A static site without a framework. The “How it works” section is a generated isometric SVG (about 53 KB) instead of a 3D model, so it stays smooth on cheap phones."),
                ("ul", ["Industry news is written in at build time, not fetched when the page opens, so no request goes to a third-party site.",
                        "CI checks every change and publishes it to GitHub Pages.",
                        "Uzbek and Russian."]),
                ("butun", "uzun-minges", "The full home page; scroll inside the frame."),
                ("h", "Result"),
                ("p", "About 170 KB gzipped on a phone’s first visit, with no images loaded."),
            ]}},

    {"slug": "shuxrat-ogli", "boshi": (2026, 10), "oxiri": (2026, 10), "kadr": ("uzun", "uzun-shuxrat"), "konsept": True,
     "stack": "HTML, CSS, JavaScript, SVG, Veo",
     "havola": ("https://linverno-tm.github.io/shuxrat-ogli-v2/", "linverno-tm.github.io/shuxrat-ogli-v2"),
     "uz": {"nom": "Shuxrat o‘g‘li", "tur": "Brend sayti",
            "lid": "«Baraka hamkor parranda» XK markasi uchun uch tilli brend sayti.",
            "alt": "Shuxrat o‘g‘li sayti, bosh sahifa",
            "bloklar": [
                ("h", "Vazifa"),
                ("p", "Mahsulotlarni ko‘rsatish, ulgurji xaridorni ariza qoldirishga olib kelish va qayerdan sotib olish mumkinligini aniq aytish."),
                ("h", "Yechim"),
                ("p", "SVG logo animatsiyasi, mahsulotlar va assortiment jadvali, ulgurji buyurtma arizasi va xarita. Matn bitta faylda yoziladi, ruscha va inglizcha sahifalar skript bilan yasaladi."),
                ("video", "Bosh qismdagi jonli video Veo bilan yaratilgan."),
                ("butun", "uzun-shuxrat", "Bosh sahifa to‘liq; ramka ichida aylantirib ko‘ring."),
                ("h", "Natija"),
                ("p", "Namuna sifatida topshirilgan. Mijozdan keladigan ma’lumot joylari maxsus ko‘rish rejimida belgilangan; soxta sharh yoki raqam qo‘yilmagan."),
            ]},
     "en": {"nom": "Shuxrat o‘g‘li", "tur": "Brand website",
            "lid": "A three-language brand site for the “Baraka hamkor parranda” poultry brand.",
            "alt": "Shuxrat o‘g‘li website, home page",
            "bloklar": [
                ("h", "The problem"),
                ("p", "Show the products, bring wholesale buyers to the order form and say clearly where to buy."),
                ("h", "What I built"),
                ("p", "An SVG logo animation, products and a range table, a wholesale order form and a map. The text is written in one file; the Russian and English pages are generated by a script."),
                ("video", "The live video in the header was made with Veo."),
                ("butun", "uzun-shuxrat", "The full home page; scroll inside the frame."),
                ("h", "Result"),
                ("p", "Delivered as a concept. Places waiting for the client’s data are marked in a review mode; no fake reviews or numbers were added."),
            ]}},

    {"slug": "oltinkol", "boshi": (2026, 10), "oxiri": (2026, 10), "kadr": ("uzun", "uzun-oltinkol"), "konsept": True,
     "stack": "HTML, CSS, JavaScript",
     "havola": ("https://linverno-tm.github.io/oltinkol-zona/", "linverno-tm.github.io/oltinkol-zona"),
     "uz": {"nom": "Oltinko‘l charm-poyabzal zonasi", "tur": "Sayt va admin panel",
            "lid": "Charm-poyabzal kichik sanoat zonasi uchun sayt va admin panel.",
            "alt": "Oltinko‘l zonasi sayti, bosh sahifa",
            "bloklar": [
                ("h", "Vazifa"),
                ("p", "Zonadagi do‘konlarni sotish va investor jalb qilish."),
                ("h", "Yechim"),
                ("p", "Do‘konlar, kredit va to‘lov hisoblagichi, imtiyozlar, investorlar va rezidentlar uchun sahifalar. Arizalar, do‘konlar va foydalanuvchilarni boshqarish uchun admin panel."),
                ("butun", "uzun-oltinkol", "Bosh sahifa to‘liq; ramka ichida aylantirib ko‘ring."),
                ("h", "Natija"),
                ("p", "14 ta bo‘lim, o‘zbek, rus va ingliz tilida."),
            ]},
     "en": {"nom": "Oltinko‘l leather and footwear zone", "tur": "Website and admin panel",
            "lid": "A site and admin panel for a small leather and footwear industrial zone.",
            "alt": "Oltinko‘l zone website, home page",
            "bloklar": [
                ("h", "The problem"),
                ("p", "Sell the zone’s shops and attract investors."),
                ("h", "What I built"),
                ("p", "Pages for shops, a credit and payment calculator, incentives, investors and residents, plus an admin panel for applications, shops and users."),
                ("butun", "uzun-oltinkol", "The full home page; scroll inside the frame."),
                ("h", "Result"),
                ("p", "14 sections in Uzbek, Russian and English."),
            ]}},
]

BOSHQA = [
    {"sana": (2026, 9), "url": "https://github.com/linverno-tm/accounting-report",
     "uz": ("Kameral hisobot", "Hisob-faktura va kassa cheklaridan soliq tekshiruvi uchun hisobotni o‘zi yig‘adigan dastur."),
     "en": ("Tax audit report", "Builds the tax-audit report from invoices and cash receipts.")},
    {"sana": (2026, 2), "url": "https://github.com/linverno-tm/chatforge",
     "uz": ("ChatForge", "Flutter’da messenjer: shaxsiy yozishmalar, kerakli odamga push-xabarnoma."),
     "en": ("ChatForge", "A Flutter messenger: one-to-one chats, push notifications to the right person.")},
    {"sana": (2026, 2), "url": "https://github.com/linverno-tm/bulk-sms",
     "uz": ("Ommaviy SMS", "Android ilova: Excel yoki CSV ro‘yxatdan SMS yuboradi; telefon o‘chib yonsa ham navbat yo‘qolmaydi."),
     "en": ("Bulk SMS", "An Android app that sends SMS from an Excel or CSV list; the queue survives a restart.")},
    {"sana": (2026, 1), "url": "https://github.com/linverno-tm/task-manager",
     "uz": ("Vazifalar ilovasi", "Internetsiz ishlaydi, aloqa tiklanganda o‘zi sinxronlanadi."),
     "en": ("Task manager", "Works offline and syncs on its own when the connection returns.")},
    {"sana": None, "url": None,
     "uz": ("O‘z MCP serverlarim", "YouTube va Pinterest bilan ishlash uchun: kanal va kontent ishini sun’iy intellekt orqali bajarish."),
     "en": ("My MCP servers", "For YouTube and Pinterest, so channel and content work can be done through AI.")},
]


def e(s):
    return html.escape(s, quote=True)


def picture(name, alt, sizes, lazy=True, high=False):
    m = RASM[name]
    ws = sorted(m["widths"])
    def srcset(ext):
        return ", ".join(f"/img/{name}-{w}.{ext} {w}w" for w in ws)
    w0, h0 = ws[-1], round(m["h"] * ws[-1] / m["w"])
    attrs = f'width="{w0}" height="{h0}" alt="{e(alt)}" decoding="async"'
    attrs += ' loading="lazy"' if lazy else ""
    attrs += ' fetchpriority="high"' if high else ""
    return (f'<picture><source type="image/avif" srcset="{srcset("avif")}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{srcset("webp")}" sizes="{sizes}">'
            f'<img src="/img/{name}-{ws[0]}.webp" {attrs}></picture>')


def sana(til, ym):
    return f"{U[til]['oy'][ym[1] - 1]} {ym[0]}"


def davr(til, p):
    b = sana(til, p["boshi"])
    if p["oxiri"] is None:
        return f"{b} – {U[til]['hozir']}"
    return b if p["oxiri"] == p["boshi"] else f"{b} – {sana(til, p['oxiri'])}"


def kadr(p, til, sizes, lazy=True, high=False):
    tur, x = p["kadr"]
    vt = f' style="view-transition-name: kadr-{p["slug"]}"'
    alt = p[til]["alt"]
    if tur == "tel":
        ichki = "".join(picture(n, alt if i == 0 else "", "(min-width: 760px) 170px, 28vw", lazy, high and i == 0) for i, n in enumerate(x))
        return f'<div class="kadr tel"{vt}>{ichki}</div>'
    cls = "kadr uzun" if tur == "uzun" else "kadr"
    return f'<div class="{cls}"{vt}>{picture(x, alt, sizes, lazy, high)}</div>'


def yol(til, slug=None):
    b = "/" if til == "uz" else "/en/"
    return b if slug is None else f"{b}ishlar/{slug}/"


def sahifa(til, title, desc, url_yol, boshqa_yol, body):
    u = U[til]
    alt_uz = url_yol if til == "uz" else boshqa_yol
    alt_en = url_yol if til == "en" else boshqa_yol
    return f"""<!doctype html>
<html lang="{til}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#101113">
<link rel="canonical" href="{SAYT}{url_yol}">
<link rel="alternate" hreflang="uz" href="{SAYT}{alt_uz}">
<link rel="alternate" hreflang="en" href="{SAYT}{alt_en}">
<link rel="alternate" hreflang="x-default" href="{SAYT}{alt_uz}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SAYT}{url_yol}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SAYT}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/onest.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#asosiy">{e(u['skip'])}</a>
<header class="tepa"><div class="wrap">
  <a class="nom" href="{yol(til)}">Muhammadabdulloh<span class="familiya"> Tojiddinov</span></a>
  <nav aria-label="{'Asosiy menyu' if til == 'uz' else 'Main'}">
    <a href="{yol(til)}#ishlar">{e(u['ishlar'])}</a>
    <a href="{yol(til)}#aloqa">{e(u['aloqa'])}</a>
    <a href="{boshqa_yol}" hreflang="{u['til_kod']}" lang="{u['til_kod']}" aria-label="{e(u['til'])}">{u['til_qisqa']}</a>
  </nav>
</div></header>
<main id="asosiy">
{body}
</main>
<footer><div class="wrap"><span>© 2026 Muhammadabdulloh Tojiddinov</span>
<nav aria-label="{'Havolalar' if til == 'uz' else 'Links'}"><a href="{TG}">Telegram</a><a href="{GITHUB}">GitHub</a><a href="{MANBA}">{e(u['manba'])}</a></nav></div></footer>
<script>{JS}</script>
</body>
</html>
"""


def bosh(til):
    u = U[til]
    kartalar = []
    for i, p in enumerate(LOYIHALAR):
        t = p[til]
        keng = i < 2
        sizes = "(min-width: 1160px) 1120px, 100vw" if keng else "(min-width: 760px) 544px, 100vw"
        yil = str(p["boshi"][0])
        tur = t["tur"] + (f", {u['konsept'].lower()}" if p.get("konsept") else "")
        kartalar.append(
            f'<a class="ish{" birinchi" if keng else ""}" href="{yol(til, p["slug"])}">'
            f'{kadr(p, til, sizes, lazy=i > 2, high=i == 0)}'
            f'<div class="qator"><h3>{e(t["nom"])}</h3><span class="yil">{yil}</span></div><p>{e(tur)}</p></a>')
    boshqa = []
    for b in BOSHQA:
        nom, izoh = b[til]
        s = sana(til, b["sana"]) if b["sana"] else ""
        nom_html = f'<a href="{b["url"]}">{e(nom)}</a>' if b["url"] else f"<b>{e(nom)}</b>"
        boshqa.append(f'<li><span class="sana">{e(s)}</span><div>{nom_html}<span>{e(izoh)}</span></div></li>')
    body = f"""<section class="wrap kirish" aria-labelledby="h1">
  <div class="ustun">
    <h1 id="h1">Muhammadabdulloh Tojiddinov</h1>
    <p>{e(u['kirish_1'])}</p>
    <p>{u['kirish_2']}</p>
    <div class="amallar"><a class="btn" href="{TG}">{TG_ICON}{e(u['tg'])}</a><a href="https://hamkorcrm.uz/">hamkorcrm.uz</a><a href="{GITHUB}">GitHub</a></div>
  </div>
</section>
<section class="wrap bolim" id="ishlar" aria-labelledby="ishlar-h" style="padding-top:0">
  <h2 id="ishlar-h">{e(u['tanlangan'])}</h2>
  <div class="ishlar">{''.join(kartalar)}</div>
</section>
<section class="wrap bolim" aria-labelledby="boshqa-h">
  <h2 id="boshqa-h">{e(u['boshqa'])}</h2>
  <ul class="royxat">{''.join(boshqa)}</ul>
</section>
<section class="wrap bolim aloqa" id="aloqa" aria-labelledby="aloqa-h">
  <h2 id="aloqa-h">{e(u['aloqa'])}</h2>
  <div class="ustun">
    <div class="dastak-qator"><a class="dastak" href="{TG}">@m_tojiddinov7</a>
    <button class="nusxa" type="button" data-nusxa="@m_tojiddinov7" data-ok="{e(u['nusxa_ok'])}" data-xato="{e(u['nusxa_xato'])}" aria-describedby="nusxa-holat">{e(u['nusxa'])}</button>
    <span id="nusxa-holat" class="sr-holat" role="status"></span></div>
    <p>{e(u['aloqa_k'])}</p>
    <div class="amallar"><a class="btn" href="{TG}">{TG_ICON}{e(u['tg'])}</a></div></div>
</section>"""
    boshqa_til = "en" if til == "uz" else "uz"
    return sahifa(til, u["title"], u["desc"], yol(til), yol(boshqa_til), body)


def blok(til, b):
    k = b[0]
    if k == "h":
        return f"<h2>{e(b[1])}</h2>"
    if k == "p":
        return f"<p>{e(b[1])}</p>"
    if k == "ul":
        return "<ul>" + "".join(f"<li>{e(x)}</li>" for x in b[1]) + "</ul>"
    if k == "rasm":
        return (f'<figure><div class="ramka">{picture(b[1], b[2], "(min-width: 1160px) 1120px, 100vw")}</div>'
                f"<figcaption>{e(b[2])}</figcaption></figure>")
    if k == "tel":
        ich = "".join(f'<figure style="margin:0"><div class="ramka">{picture(n, c, "(min-width: 760px) 220px, 45vw")}</div><figcaption>{e(c)}</figcaption></figure>' for n, c in b[1])
        return f'<div class="telefonlar" style="margin:48px 0">{ich}</div>'
    if k == "butun":
        return (f'<figure><div class="ramka sahifa-butun" tabindex="0" role="region" aria-label="{e(b[2])}">'
                f'{picture(b[1], b[2], "(min-width: 1160px) 1100px, 100vw")}</div><figcaption>{e(b[2])}</figcaption></figure>')
    if k == "video":
        u = U[til]
        return (f'<figure><div class="ramka video-ramka"><video muted loop playsinline preload="none" poster="/img/veo-kadr-800.webp" '
                f'width="960" height="540" data-src="/media/veo-tovuq.mp4" aria-label="{e(b[1])}"></video>'
                f'<button class="pauza" type="button" hidden data-pauza="{e(u["pauza"])}" data-davom="{e(u["davom"])}" aria-label="{e(u["pauza"])}"></button></div>'
                f"<figcaption>{e(b[1])}</figcaption></figure>")
    raise ValueError(k)


def loyiha(til, i):
    u, p = U[til], LOYIHALAR[i]
    t = p[til]
    nxt = LOYIHALAR[(i + 1) % len(LOYIHALAR)]
    m1, m2, m3, m4 = u["meta"]
    holat = u["konsept"] if p.get("konsept") else t.get("holat")
    meta = (f"<div><dt>{m1}</dt><dd>{e(davr(til, p))}</dd></div>"
            f"<div><dt>{m2}</dt><dd>{e(u['rol'])}</dd></div>"
            f"<div><dt>{m3}</dt><dd>{e(p['stack'])}</dd></div>")
    if holat or p.get("havola"):
        h = e(holat) if holat else ""
        if p.get("havola"):
            h += ("<br>" if h else "") + f'<a href="{p["havola"][0]}">{e(p["havola"][1])}</a>'
        meta += f"<div><dt>{m4}</dt><dd>{h}</dd></div>"
    # maqola: matn ustunda, rasmlar keng
    qism, ustun = [], []
    for b in t["bloklar"]:
        if b[0] in ("h", "p", "ul"):
            ustun.append(blok(til, b))
        else:
            if ustun:
                qism.append(f'<div class="ustun">{"".join(ustun)}</div>'); ustun = []
            qism.append(blok(til, b))
    if t.get("izoh"):
        ustun.append(f'<p class="izoh">{e(t["izoh"])}</p>')
    if ustun:
        qism.append(f'<div class="ustun">{"".join(ustun)}</div>')
    nt = nxt[til]
    body = f"""<article>
<header class="wrap loyiha-bosh">
  <a class="orqaga" href="{yol(til)}#ishlar">{e(u['orqaga'])}</a>
  <div class="ustun"><h1>{e(t['nom'])}</h1><p class="lid">{e(t['lid'])}</p></div>
  <dl class="meta">{meta}</dl>
</header>
<div class="wrap bosh-kadr">{kadr(p, til, "(min-width: 1160px) 1120px, 100vw", lazy=False, high=True)}</div>
<div class="wrap maqola">{''.join(qism)}</div>
<nav class="wrap keyingi" aria-label="{e(u['keyingi'])}"><small>{e(u['keyingi'])}</small>
  <a href="{yol(til, nxt['slug'])}"><div><h2>{e(nt['nom'])}</h2><p>{e(nt['tur'])}</p></div>{kadr(nxt, til, "(min-width: 760px) 544px, 100vw")}</a>
</nav>
</article>"""
    boshqa_til = "en" if til == "uz" else "uz"
    return sahifa(til, f"{t['nom']} — Muhammadabdulloh Tojiddinov", t["lid"], yol(til, p["slug"]), yol(boshqa_til, p["slug"]), body)


def yoz(rel, matn):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p) or ROOT, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(matn)
    return p


fayllar = []
for til in ("uz", "en"):
    pre = "" if til == "uz" else "en/"
    fayllar.append(yoz(f"{pre}index.html", bosh(til)))
    for i, p in enumerate(LOYIHALAR):
        fayllar.append(yoz(f"{pre}ishlar/{p['slug']}/index.html", loyiha(til, i)))

def yoq():
    u = U["uz"]
    kartalar = "".join(
        f'<a class="ish" href="{yol("uz", p["slug"])}">{kadr(p, "uz", "(min-width: 760px) 544px, 100vw")}'
        f'<div class="qator"><h3>{e(p["uz"]["nom"])}</h3><span class="yil">{p["boshi"][0]}</span></div><p>{e(p["uz"]["tur"])}</p></a>'
        for p in LOYIHALAR[:4])
    body = f"""<section class="wrap yoq" aria-labelledby="h1">
  <div class="ustun"><div class="yoq-kod" aria-hidden="true">404</div>
  <h1 id="h1">{e(u['yoq_t'])}</h1><p>{e(u['yoq_p'])}</p>
  <div class="amallar"><a class="btn" href="/">{e(u['bosh_sahifa'])}</a><a href="/en/" lang="en">English</a></div></div>
</section>
<section class="wrap bolim" aria-label="{e(u['tanlangan'])}"><div class="ishlar">{kartalar}</div></section>"""
    h = sahifa("uz", u["yoq_t"] + " — Muhammadabdulloh Tojiddinov", u["yoq_p"], "/404.html", "/en/", body)
    return h.replace('<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"', 1)


fayllar.append(yoz("404.html", yoq()))

urls = [yol("uz")] + [yol("uz", p["slug"]) for p in LOYIHALAR]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for u_ in urls:
    en = "/en" + u_
    for a, b in ((u_, en), (en, u_)):
        sm.append(f'  <url><loc>{SAYT}{a}</loc><xhtml:link rel="alternate" hreflang="{"en" if b == en else "uz"}" href="{SAYT}{b}"/></url>')
sm.append("</urlset>")
yoz("sitemap.xml", "\n".join(sm) + "\n")
for f in fayllar:
    print(os.path.relpath(f, ROOT), os.path.getsize(f))
