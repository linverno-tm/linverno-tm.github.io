"""Saytni yig'adi: index.html (o'zbekcha) va en/index.html (inglizcha).

    python tools/build.py

Matn shu faylda, uslub tools/style.css da (sahifaga ichiga qo'yiladi), rasmlar img/ da
(o'lchamlari tools/rasmlar.json da).
"""
import html
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RASM = json.load(open(os.path.join(ROOT, "tools", "rasmlar.json"), encoding="utf-8"))
CSS = open(os.path.join(ROOT, "tools", "style.css"), encoding="utf-8").read() + open(os.path.join(ROOT, "tools", "harakat.css"), encoding="utf-8").read()
JS = open(os.path.join(ROOT, "tools", "harakat.js"), encoding="utf-8").read()
SAYT = "https://linverno-tm.github.io/"
TG = "https://t.me/m_tojiddinov7"

T = {
    "uz": {
        "lang": "uz",
        "title": "Muhammadabdulloh Tojiddinov — CRM, Telegram bot, mini app va mobil ilovalar",
        "desc": "Biznes uchun CRM, Telegram bot, mini app, mobil ilova va sayt yarataman. Hamkor CRM muallifi: to‘rtta filialning 1C bazasini bitta tizimga birlashtirgan muddatli to‘lov savdo tizimi.",
        "skip": "Asosiy qismga o‘tish",
        "nav": [("#ishlar", "Ishlar"), ("#xizmatlar", "Xizmatlar"), ("#aloqa", "Aloqa")],
        "til_link": "en/", "til_label": "EN", "til_aria": "English version",
        "tg_btn": "Telegram’da yozish",
        "h1_bosh": "Biznesingiz uchun", "h1_oxir": "yarataman.",
        "h1_sozlar": ["CRM", "mobil ilova", "Telegram bot", "mini app", "sayt"],
        "h1_statik": "CRM, mobil ilova, Telegram bot, mini app va sayt",
        "lenta": ["Hamkor CRM", "Mijozlar ilovasi", "KINO TV", "Qog‘oz Bino", "Hamkor Savdo", "Shuxrat o‘g‘li", "Oltinko‘l", "MINI GES", "ChatForge"],
        "lead": "<strong>Hamkor CRM muallifiman.</strong> To‘rtta filialning alohida 1C bazalarini bitta tizimga birlashtirdim: savdo, nasiya, kassa va ombor endi bir joyda va internet uzilsa ham ishlaydi.",
        "cta2": "Ishlarni ko‘rish",
        "hero_alt": "Hamkor CRM bosh sahifasi: kassalardagi pul, nasiya qarzi, muddati o‘tgan qarz, oylik foyda grafigi",
        "hero_izoh": "Hamkor CRM bosh sahifasi. Summalar, ismlar va filial nomlari yopilgan.",
        "crm_h2": "Hamkor CRM",
        "crm_tagi": "1C o‘rnini bosgan muddatli to‘lov savdo tizimi. Sentabr 2026 dan ishlab chiqyapman, platforma meniki.",
        "crm_p1": "To‘rtta do‘kon to‘rtta alohida 1C bazasida ishlardi va bir-birini ko‘rmasdi. Bir do‘konda qora ro‘yxatga tushgan mijoz keyingisida yana nasiyaga tovar olishi mumkin edi.",
        "crm_p2": "Hammasi uchun bitta tizim qurdim: savdo, nasiya shartnomalari, to‘lovlar, kassa, ombor, ish haqi va hisobotlar. 1C bilan ikki tomonlama sinxronlanadi, shuning uchun o‘tish davrida ikkalasi yonma-yon ishladi.",
        "faktlar": [
            ("Internet uzilsa ham ishlaydi", "Kompyuterdagi shifrlangan nusxa bilan har bir oyna ochilaveradi. Amallar navbatga yoziladi va aloqa tiklanganda o‘zi yuboriladi."),
            ("Windows dasturi", "Chekni so‘ramasdan chop etadi va o‘zi yangilanadi. Xodimlar brauzer emas, dastur bilan ishlaydi."),
            ("Har bir yangilanish oldin sinovdan o‘tadi", "Savdo, shartnoma, to‘lov va hisobotlar vaqtinchalik bazada tekshiriladi, keyin ishga chiqadi."),
            ("Mijoz telefonida ham", "Shartnoma, to‘lov grafigi va qolgan qarzni mijoz o‘z ilovasida ko‘radi. Ilova pastda, «Mobil ilovalar» bo‘limida."),
        ],
        "ekranlar": [
            ("crm-mijozlar", "Mijozlar ro‘yxati: har bir mijozning ishonch bahosi, shartnomalari va muddati o‘tgan qarzi", "Mijozlar va ularning ishonch bahosi"),
            ("crm-qarz", "Muddati o‘tgan qarzlar ro‘yxati, kechikish kunlari bo‘yicha guruhlangan", "Muddati o‘tgan qarzlar"),
            ("crm-kassa", "Kassalardagi pul qoldig‘i filiallar kesimida: naqd, terminal, Click, Payme", "Kassalar filiallar kesimida"),
        ],
        "crm_oxir": "Bir oyda <span class=\"raqam\" data-son=\"1373\">1 373</span> ta o‘zgarish, <span class=\"raqam\" data-son=\"230\">230</span> dan ortiq ekran, <span class=\"raqam\" data-son=\"65\">65</span> ta hisobot. Shu platformani sizning savdongizga ham moslab beraman.",
        "crm_link": "hamkorcrm.uz",
        "toliq": "To‘liq o‘lchamda ochish",
        "mob_h2": "Mobil ilovalar",
        "mob_tagi": "Android va iPhone uchun bitta koddan yozaman (Flutter): bitta ilova ikkala do‘konga chiqadi.",
        "mob_alt": ("Hamkor ilovasi, bosh sahifa: o‘z mablag‘i, muddatli to‘lov limiti, o‘tkazma, to‘ldirish, to‘lash va karta tugmalari",
                    "Hamkor ilovasi, katalog: telefonlar va oylik to‘lov narxi",
                    "Hamkor ilovasi, to‘lovlar tarixi oylar bo‘yicha: Payme, naqd, Click"),
        "mob_h3": "Hamkor — mijozlar ilovasi",
        "mob_p": "Muddatli to‘lov bilan xarid qilgan mijoz uchun: shartnomalar, qolgan qarz, keyingi to‘lov va to‘lov tarixi telefonda. Katalogdan muddatli to‘lovga buyurtma beradi, do‘kon bilan chatda yozishadi.",
        "mob_fakt": [
            ("Hamkor CRM bilan bitta tizimda", "Do‘konda qilingan to‘lov ilovada ham ko‘rinadi, qo‘shimcha kiritish yo‘q."),
            ("Kirish oson, qulf ishonchli", "Telefon raqami va SMS kod bilan kiriladi; keyin ilova PIN yoki barmoq izi bilan ochiladi."),
            ("Uch tilda, ikki mavzuda", "O‘zbek (kirill va lotin) va rus tilida; yorug‘ va qorong‘i ko‘rinish."),
        ],
        "mob_izoh": "Demo mijoz. Ism va summalar yopilgan; ilova do‘konlarga chiqarishga tayyorlanmoqda.",
        "mob_boshqa_h3": "Boshqa ilovalarim",
        "mob_boshqa": [
            ("ChatForge", "Flutter’da messenjer: shaxsiy yozishmalar, kerakli odamga push-xabarnoma.", "https://github.com/linverno-tm/chatforge"),
            ("Ommaviy SMS", "Android ilova: Excel yoki CSV ro‘yxatdan SMS yuboradi; telefon o‘chib yonsa ham navbat yo‘qolmaydi.", "https://github.com/linverno-tm/bulk-sms"),
            ("Vazifalar ilovasi", "Internet yo‘qda ham ishlaydi, aloqa tiklanganda o‘zi sinxronlanadi.", "https://github.com/linverno-tm/task-manager"),
        ],
        "kod": "Kodi",
        "batafsil": "Batafsil",
        "case": {
            "mijoz": [
                ("Maqsad", "Muddatli to‘lov bilan xarid qilgan mijoz shartnomasi, keyingi to‘lovi va limitini do‘konga bormasdan ko‘rsin; do‘kon esa unga xabar va aksiyani to‘g‘ridan-to‘g‘ri yuborsin."),
                ("Yechim", "Flutter va Riverpod; har bo‘lim to‘rt qatlamda (model, ma’lumot, holat, ekran). Kirish SMS kod bilan, token telefonning xavfsiz xotirasida. Ma’lumot Hamkor CRM’ning mijoz API’sidan keladi. Avval Expo (React Native) da yozilgan edi, 7-oktabrda to‘liq Flutter’ga ko‘chirildi."),
                ("Natija", "Android, iPhone va web uchun bitta kod. Testlar internetsiz ishlaydi: server o‘rniga namuna javoblar. Ilova do‘konlarga chiqarishga tayyorlanmoqda."),
            ],
            "kino": [
                ("Maqsad", "Ko‘p qismli serialni Telegram’da qulay ko‘rish: kerakli qismni tez topish va qayerda to‘xtaganini yo‘qotmaslik."),
                ("Yechim", "Bot (Python, aiogram 3, SQLite) yopiq ombor kanaldagi postlarni o‘zi katalogga yozadi: admin faqat video joylaydi, kodni bot beradi. Video foydalanuvchiga nusxa sifatida yuboriladi, hajm chegarasi yo‘q. Mini app yig‘ishsiz HTML/CSS/JS, Cloudflare Pages’da, katalog chekkada keshlanadi."),
                ("Natija", "Katalogda 701 ta serial va kino, 8 ta bo‘lim. Mini app keyingi qismdan davom ettiradi va saqlanganlar ro‘yxatini yuritadi."),
            ],
            "qogoz": [
                ("Maqsad", "Do‘stning @QogozBinoTVbot boti uchun posterli katalog — botning kodiga tegmasdan va tokenisiz."),
                ("Yechim", "Katalogni botning o‘zidan yig‘adigan skript: har kodga /start yuboradi va javobni o‘qiydi. Mini app kirill va lotinda jonli qidiradi, bo‘lim va janr bo‘yicha saralaydi; serial bosilsa botning o‘zi ochiladi."),
                ("Natija", "Bot tokeni ishlatilmaydi. To‘liq yig‘ish taxminan 10 daqiqa, yangi kodlar alohida tez qo‘shiladi."),
            ],
            "sayt-hamkor": [
                ("Maqsad", "To‘rt filialli tarmoqni tanishtirish: kompaniya, taklif, har filial va bog‘lanish yo‘llari. Asosiy shart: sekin internetda ham tez ochilsin."),
                ("Yechim", "Next.js 16, React 19, Tailwind v4, animatsiya kutubxonasisiz: hamma harakat CSS va taxminan 1 KB JavaScript. Logotip brendbukdagi rasmdan vektorga o‘tkazilgan."),
                ("Natija", "O‘qiladigan sahifa (HTML va CSS) 35 KB gzip. JavaScript yuklanmasa ham ishlaydi. Matn kontrasti hamma joyda 4.5:1 dan yuqori; to‘qima sharh va ma’lumot yo‘q."),
            ],
            "sayt-shuxrat": [
                ("Maqsad", "«Baraka hamkor parranda» XK markasi uchun uch tilli brend sayti: mahsulot, ulgurji savdo va qayerdan sotib olish."),
                ("Yechim", "SVG logo animatsiyasi, mahsulotlar va assortiment jadvali, ulgurji buyurtma arizasi, xarita, Veo bilan jonli video. Matn bitta faylda; ruscha va inglizcha sahifalar skript bilan yasaladi."),
                ("Natija", "Namuna holatida topshirilgan: mijozdan keladigan ma’lumot joylari maxsus rejimda belgilanadi, soxta sharh qo‘yilmagan."),
            ],
            "sayt-oltinkol": [
                ("Maqsad", "Charm-poyabzal kichik sanoat zonasida do‘kon sotish va investor jalb qilish."),
                ("Yechim", "Do‘konlar, kredit va to‘lov hisoblagichi, imtiyozlar, investorlar va rezidentlar sahifalari. Arizalar, do‘konlar va foydalanuvchilarni boshqaradigan admin panel."),
                ("Natija", "14 ta bo‘lim, o‘zbek, rus va ingliz tilida."),
            ],
            "sayt-minges": [
                ("Maqsad", "Ulug‘nor GES (600 kVt, ishlab turibdi) va Baliqchi GES (1 000 kVt) ni tanishtirish va mini-GES qurish xizmatini sotish."),
                ("Yechim", "Freymvorksiz statik sayt. «Qanday ishlaydi» bo‘limi 3D model o‘rniga generatsiya qilingan izometrik SVG (~53 KB). Soha yangiliklari sayt yig‘ilayotganda yoziladi; o‘zbek va rus tilida."),
                ("Natija", "Telefonda birinchi ochilishda taxminan 170 KB (gzip), rasm yuklanmaydi. Har o‘zgarishni CI tekshirib, o‘zi chiqaradi."),
            ],
        },
        "tg_h2": "Telegram bot va mini app",
        "tg_tagi": "Mijoz alohida ilova o‘rnatmaydi: katalog, qidiruv va ro‘yxat Telegram ichida ochiladi.",
        "kino_alt": ("KINO TV mini app bosh sahifasi: tanlangan serial va bo‘limlar", "KINO TV: serial sahifasi, qismlar ro‘yxati"),
        "kino_p": "Seriallar va kinolar uchun bot va mini app. Bo‘limlar, qidiruv, qismlar ro‘yxati; qaysi qismda to‘xtaganingizni eslab qoladi va keyingisidan davom ettiradi.",
        "qogoz_alt": ("Qog‘oz Bino mini app: yangi qismlar va eng ko‘p ko‘rilganlar", "Qog‘oz Bino: serial sahifasi va qismlar"),
        "qogoz_p": "Telegram kanal uchun mini app: yangi chiqqan qismlar, haftaning eng ko‘p ko‘rilganlari, qidiruv va «Mening ro‘yxatim».",
        "sayt_h2": "Saytlar",
        "sayt_tagi": "Har biri o‘z brendi uchun noldan chizilgan, shablonsiz.",
        "saytlar": [
            ("sayt-hamkor", "Hamkor Savdo", "", "To‘rt filialli savdo tarmog‘i sayti: katalog, filiallar va muddatli to‘lovga ariza.", "https://hamkorsavdo.uz/", "hamkorsavdo.uz", "Hamkor Savdo sayti: «Oilangiz uchun ishonchli hamkor» sarlavhasi va ariza shakli"),
            ("sayt-shuxrat", "Shuxrat o‘g‘li", "konsept", "Parranda brendi uchun sayt: mahsulotlar, ulgurji buyurtma, Veo bilan yaratilgan jonli video. Uch tilda.", "https://linverno-tm.github.io/shuxrat-ogli-v2/", "Saytni ochish", "Shuxrat o‘g‘li sayti: brend belgisi va xo‘roz surati"),
            ("sayt-oltinkol", "Oltinko‘l charm-poyabzal zonasi", "konsept", "Kichik sanoat zonasi sayti: do‘konlar, to‘lov hisoblagichi, investorlar va rezidentlar uchun bo‘limlar.", "https://linverno-tm.github.io/oltinkol-zona/", "Saytni ochish", "Oltinko‘l zonasi sayti: «O‘z do‘koningiz — atigi 20% to‘lov bilan»"),
            ("sayt-minges", "MINI GES", "", "Kichik gidroelektrostansiyalar sayti: loyihalar, qanday ishlashi, xizmatlar va ariza.", "https://linverno-tm.github.io/mini-ges-site/", "Saytni ochish", "MINI GES sayti: «O‘z yeringizdagi suvdan elektr ishlab chiqaring»"),
        ],
        "media_h2": "Reklama videosi va bosma dizayn",
        "media_tagi": "Sayt yonida kerak bo‘ladigan narsalar ham: jonli video, motion roliklar, buklet.",
        "veo_h3": "Veo bilan jonli video",
        "veo_p": "Shuxrat o‘g‘li sayti uchun. Remotion’da esa matn va raqamli motion roliklar yig‘aman.",
        "veo_pauza": "Videoni to‘xtatish", "veo_davom": "Videoni davom ettirish",
        "buklet_h3": "Yevrobuklet, Hamkor Savdo",
        "buklet_p": "A4, uch buklama, bosmaga tayyor vektor fayl. Tashqi tomoni.",
        "buklet_alt": "Hamkor Savdo yevrobukleti: «24 oygacha muddatli to‘lov», tovarlar va oylik to‘lovlar",
        "boshqa_h2": "Avtomatlashtirish",
        "boshqa": [
            ("Narx kuzatuvi", "Raqobatchilarning Telegram guruhlaridagi e’lonlari narxlarga aylanadi; har do‘kon uchun kunlik PDF faqat yangi va o‘zgargan narxlar bilan keladi."),
            ("Kameral hisobot", "Hisob-faktura va kassa cheklaridan soliq tekshiruvi uchun hisobotni o‘zi yig‘adigan dastur."),
            ("O‘z ulagichlarim", "YouTube va Pinterest bilan ishlaydigan MCP serverlar: kanal va kontent ishini sun’iy intellekt orqali bajarish uchun."),
        ],
        "xiz_h2": "Nima qila olaman",
        "xiz_tagi": "CRM’dan mobil ilovagacha: biznesga kerak dasturning hammasini o‘zim yozaman.",
        "xizmatlar": [
            ("Savdo va nasiya uchun CRM", "1C o‘rniga yoki yonida ishlaydigan tizim: shartnoma, to‘lov grafigi, kassa, ombor, hisobotlar. Internet bo‘lmasa ham ishlaydi."),
            ("Telegram bot va mini app", "Katalog, buyurtma, ariza va mijoz bilan aloqa Telegram ichida. Mijoz hech narsa o‘rnatmaydi."),
            ("Mobil ilovalar", "Android va iPhone uchun bitta koddan: mijoz ilovasi, xodimlar ilovasi, oflayn ishlaydigan ilova."),
            ("Saytlar", "Brend sayti, katalog, ariza shakllari. Telefonda tez ochiladi, bir necha tilda."),
            ("Avtomatlashtirish", "1C, Telegram, Excel va PDF bilan bog‘lash: hisobotlar, narx kuzatuvi, takrorlanadigan qo‘l ishini dasturga topshirish."),
            ("Video va bosma dizayn", "Veo va Remotion bilan reklama roliklari, flayer va yevrobuklet."),
        ],
        "aloqa_h2": "Loyihangizni Telegram’da yozing",
        "aloqa_p": "Qisqacha yozing: biznesingiz nima bilan shug‘ullanadi va nimani tezlashtirmoqchisiz. O‘zim javob beraman.",
        "github": "GitHub",
        "footer": "Muhammadabdulloh Tojiddinov",
    },
    "en": {
        "lang": "en",
        "title": "Muhammadabdulloh Tojiddinov — CRM, Telegram bots, mini apps and mobile apps",
        "desc": "I build CRMs, Telegram bots, mini apps, mobile apps and websites for businesses. Author of Hamkor CRM, an installment-sales system that joined four stores’ 1C databases into one.",
        "skip": "Skip to content",
        "nav": [("#ishlar", "Work"), ("#xizmatlar", "Services"), ("#aloqa", "Contact")],
        "til_link": "../", "til_label": "UZ", "til_aria": "O‘zbekcha versiya",
        "tg_btn": "Message on Telegram",
        "h1_bosh": "I build", "h1_oxir": "for businesses.",
        "h1_sozlar": ["CRMs", "mobile apps", "Telegram bots", "mini apps", "websites"],
        "h1_statik": "CRMs, mobile apps, Telegram bots, mini apps and websites",
        "lenta": ["Hamkor CRM", "Customer app", "KINO TV", "Qog‘oz Bino", "Hamkor Savdo", "Shuxrat o‘g‘li", "Oltinko‘l", "MINI GES", "ChatForge"],
        "lead": "<strong>I wrote Hamkor CRM.</strong> It joined four stores’ separate 1C databases into one system: sales, installments, cash and stock now live in one place and keep working when the internet drops.",
        "cta2": "See the work",
        "hero_alt": "Hamkor CRM home screen: cash on hand, installment debt, overdue debt, monthly profit chart",
        "hero_izoh": "Hamkor CRM home screen. Amounts, names and branch names are hidden.",
        "crm_h2": "Hamkor CRM",
        "crm_tagi": "An installment-sales system that replaced 1C. In development since September 2026; I own the platform.",
        "crm_p1": "Four stores ran on four separate 1C databases that couldn’t see each other. A customer blacklisted in one store could get new credit in the next.",
        "crm_p2": "I built one system for all of them: sales, installment contracts, payments, cash, warehouse, payroll and reports. It syncs with 1C both ways, so the two ran side by side during the switch.",
        "faktlar": [
            ("Works without internet", "An encrypted local copy keeps every window usable. Actions queue up and sync back on their own when the line returns."),
            ("Windows app", "Prints receipts silently and updates itself. Staff work in an app, not a browser tab."),
            ("Every release is tested first", "Sales, contracts, payments and reports run on a throw-away database before a build goes live."),
            ("On the customer’s phone too", "Customers see their contract, payment schedule and remaining debt in their own app, shown below under “Mobile apps”."),
        ],
        "ekranlar": [
            ("crm-mijozlar", "Customer list: each customer’s trust score, contracts and overdue debt", "Customers and their trust score"),
            ("crm-qarz", "Overdue debt list grouped by days late", "Overdue debt"),
            ("crm-kassa", "Cash balance per branch: cash, card terminal, Click, Payme", "Cash by branch"),
        ],
        "crm_oxir": "In one month: <span class=\"raqam\" data-son=\"1373\">1,373</span> changes, <span class=\"raqam\" data-son=\"230\">230</span>+ screens, <span class=\"raqam\" data-son=\"65\">65</span> reports. I can adapt the same platform to your business.",
        "crm_link": "hamkorcrm.uz",
        "toliq": "Open full size",
        "mob_h2": "Mobile apps",
        "mob_tagi": "Android and iPhone from one codebase (Flutter): one app, published to both stores.",
        "mob_alt": ("Hamkor app home: own funds, installment limit, transfer, top-up, pay and card buttons",
                    "Hamkor app catalog: phones with the monthly payment",
                    "Hamkor app payment history by month: Payme, cash, Click"),
        "mob_h3": "Hamkor — the customer app",
        "mob_p": "For customers who bought on installments: contracts, remaining debt, next payment and payment history on the phone. They order from the catalog on installments and chat with the store.",
        "mob_fakt": [
            ("One system with Hamkor CRM", "A payment made in the store shows up in the app too, nothing to enter twice."),
            ("Easy sign-in, solid lock", "Sign in with a phone number and an SMS code; after that the app opens with a PIN or a fingerprint."),
            ("Three languages, two themes", "Uzbek (Cyrillic and Latin) and Russian; light and dark."),
        ],
        "mob_izoh": "Demo customer. Name and amounts are hidden; the app is being prepared for the stores.",
        "mob_boshqa_h3": "Other apps I built",
        "mob_boshqa": [
            ("ChatForge", "A Flutter messenger: one-to-one chats, push notifications to the right person.", "https://github.com/linverno-tm/chatforge"),
            ("Bulk SMS", "An Android app that sends SMS from an Excel or CSV list; the queue survives a phone restart.", "https://github.com/linverno-tm/bulk-sms"),
            ("Task app", "Works offline and syncs on its own when the connection returns.", "https://github.com/linverno-tm/task-manager"),
        ],
        "kod": "Code",
        "batafsil": "Details",
        "case": {
            "mijoz": [
                ("Goal", "Customers who bought on installments see their contract, next payment and limit without visiting the store, and the store can send them notices and offers directly."),
                ("Solution", "Flutter and Riverpod, each feature in four layers (model, data, state, screen). Sign-in with an SMS code, the token kept in the phone’s secure storage. Data comes from Hamkor CRM’s customer API. First written in Expo (React Native), fully moved to Flutter on 7 October."),
                ("Result", "One codebase for Android, iPhone and web. Tests run offline against sample responses. The app is being prepared for the stores."),
            ],
            "kino": [
                ("Goal", "Watching long series in Telegram comfortably: find the right episode fast and never lose where you stopped."),
                ("Solution", "The bot (Python, aiogram 3, SQLite) turns posts in a private storage channel into the catalog on its own: the admin only uploads videos, the bot assigns codes. Videos are sent as copies, with no size limit. The mini app is plain HTML/CSS/JS on Cloudflare Pages, with the catalog cached at the edge."),
                ("Result", "701 series and films in 8 sections. The mini app continues from the next episode and keeps a saved list."),
            ],
            "qogoz": [
                ("Goal", "A poster catalog for a friend’s bot, @QogozBinoTVbot, without touching its code or using its token."),
                ("Solution", "A script builds the catalog from the bot itself: it sends /start for each code and reads the reply. The mini app searches live in Cyrillic and Latin, filters by section and genre, and opens the bot for the chosen series."),
                ("Result", "No bot token needed. A full rebuild takes about 10 minutes; new codes are added quickly on their own."),
            ],
            "sayt-hamkor": [
                ("Goal", "Introduce a four-branch chain: the company, the offer, each branch and every way to reach it. The main constraint: fast on slow connections."),
                ("Solution", "Next.js 16, React 19, Tailwind v4 and no animation library: all motion is CSS plus about 1 KB of JavaScript. The logo was traced to vector from the brand book artwork."),
                ("Result", "The readable page (HTML and CSS) is 35 KB gzipped and works without JavaScript. Every text pair is above 4.5:1 contrast; no invented reviews or facts."),
            ],
            "sayt-shuxrat": [
                ("Goal", "A three-language brand site for the “Baraka hamkor parranda” poultry brand: products, wholesale and where to buy."),
                ("Solution", "SVG logo animation, products and a full range table, a wholesale order form, a map and a live video made with Veo. The text lives in one file; Russian and English pages are generated by a script."),
                ("Result", "Delivered as a concept: places waiting for the client’s data are marked in a review mode, and no fake reviews were added."),
            ],
            "sayt-oltinkol": [
                ("Goal", "Sell shops and attract investors for a small leather and footwear industrial zone."),
                ("Solution", "Pages for shops, a credit and payment calculator, incentives, investors and residents, plus an admin panel for applications, shops and users."),
                ("Result", "14 sections in Uzbek, Russian and English."),
            ],
            "sayt-minges": [
                ("Goal", "Present Ulug‘nor GES (600 kW, running) and Baliqchi GES (1,000 kW) and sell the service of building small hydro plants."),
                ("Solution", "A static site without a framework. The “How it works” section is a generated isometric SVG (~53 KB) instead of a 3D model. Industry news is written in at build time; Uzbek and Russian."),
                ("Result", "About 170 KB gzipped on a phone’s first visit, with no images loaded. CI checks and publishes every change."),
            ],
        },
        "tg_h2": "Telegram bots and mini apps",
        "tg_tagi": "Nothing to install: the catalog, search and lists open right inside Telegram.",
        "kino_alt": ("KINO TV mini app home: featured series and sections", "KINO TV: series page with the episode list"),
        "kino_p": "A bot and mini app for series and films. Sections, search, episode lists; it remembers where you stopped and continues from the next episode.",
        "qogoz_alt": ("Qog‘oz Bino mini app: new episodes and most watched", "Qog‘oz Bino: series page and episodes"),
        "qogoz_p": "A mini app for a Telegram channel: new episodes, this week’s most watched, search and a personal list.",
        "sayt_h2": "Websites",
        "sayt_tagi": "Each one drawn from scratch for its brand, no templates.",
        "saytlar": [
            ("sayt-hamkor", "Hamkor Savdo", "", "Site for a four-branch retail chain: catalog, branches and an installment application form.", "https://hamkorsavdo.uz/", "hamkorsavdo.uz", "Hamkor Savdo site: headline “A partner your family can trust” and the application form"),
            ("sayt-shuxrat", "Shuxrat o‘g‘li", "concept", "Site for a poultry brand: products, wholesale orders and a live video made with Veo. In three languages.", "https://linverno-tm.github.io/shuxrat-ogli-v2/", "Open the site", "Shuxrat o‘g‘li site: brand mark and a rooster photo"),
            ("sayt-oltinkol", "Oltinko‘l leather and footwear zone", "concept", "Site for a small industrial zone: shops, a payment calculator, pages for investors and residents.", "https://linverno-tm.github.io/oltinkol-zona/", "Open the site", "Oltinko‘l zone site: “Your own shop with just 20% down”"),
            ("sayt-minges", "MINI GES", "", "Site for small hydro-power plants: projects, how it works, services and an application form.", "https://linverno-tm.github.io/mini-ges-site/", "Open the site", "MINI GES site: “Make electricity from the water on your land”"),
        ],
        "media_h2": "Ad video and print design",
        "media_tagi": "The things a site usually needs next to it: live video, motion clips, a booklet.",
        "veo_h3": "Live video made with Veo",
        "veo_p": "For the Shuxrat o‘g‘li site. For type and number driven motion clips I use Remotion.",
        "veo_pauza": "Pause video", "veo_davom": "Play video",
        "buklet_h3": "Tri-fold booklet, Hamkor Savdo",
        "buklet_p": "A4, three panels, print-ready vector file. Outer side.",
        "buklet_alt": "Hamkor Savdo tri-fold booklet: “installments up to 24 months”, products and monthly payments",
        "boshqa_h2": "Automation",
        "boshqa": [
            ("Price watch", "Competitors’ posts in Telegram groups become prices; each store gets a daily PDF with only the new and changed prices."),
            ("Tax audit report", "A program that builds the tax-audit report from invoices and cash receipts on its own."),
            ("My own connectors", "MCP servers for YouTube and Pinterest, so channel and content work can be done through AI."),
        ],
        "xiz_h2": "What I can do for you",
        "xiz_tagi": "From a CRM to a mobile app: I write all the software a business needs myself.",
        "xizmatlar": [
            ("CRM for sales and installments", "A system that replaces 1C or runs next to it: contracts, payment schedules, cash, stock, reports. Works offline."),
            ("Telegram bots and mini apps", "Catalog, orders, applications and customer contact inside Telegram. Your customer installs nothing."),
            ("Mobile apps", "Android and iPhone from one codebase: customer apps, staff apps, apps that work offline."),
            ("Websites", "Brand sites, catalogs, application forms. Fast on phones, in several languages."),
            ("Automation", "Connecting 1C, Telegram, Excel and PDF: reports, price watching, handing repetitive manual work to software."),
            ("Video and print design", "Ad clips made with Veo and Remotion, flyers and tri-fold booklets."),
        ],
        "aloqa_h2": "Tell me about your project on Telegram",
        "aloqa_p": "A few lines are enough: what your business does and what you want to speed up. I answer myself.",
        "github": "GitHub",
        "footer": "Muhammadabdulloh Tojiddinov",
    },
}

TG_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M21.4 4.2 2.9 11.3c-1.3.5-1.2 1.2-.2 1.5l4.7 1.5 1.8 5.6c.2.6.1.9.8.9.5 0 .7-.2 1-.5l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.1-14.8c.3-1.3-.5-1.9-1.5-1.8ZM8.6 14l9.3-5.9c.5-.3.9-.1.5.2l-7.9 7.2-.3 3.4L8.6 14Z"/></svg>'
PAUZA = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>'


def e(s):
    return html.escape(s, quote=True)


def picture(root, name, alt, sizes, cls="", lazy=True, high=False):
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
    c = f' class="{cls}"' if cls else ""
    return (f'<picture><source type="image/avif" srcset="{srcset("avif")}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{srcset("webp")}" sizes="{sizes}">'
            f'<img{c} src="{root}img/{name}-{ws[0]}.webp" {attrs}></picture>')


def page(k):
    t = T[k]
    root = "" if k == "uz" else "../"
    url = SAYT if k == "uz" else SAYT + "en/"
    css = CSS.replace("{ROOT}", root)
    nav = "".join(f'<a class="bolim" href="{h}">{e(l)}</a>' for h, l in t["nav"])
    sozlar = t["h1_sozlar"] + t["h1_sozlar"][:1]
    h1 = (f'<span class="q">{e(t["h1_bosh"])}</span>'
          f'<span class="q aylan" aria-hidden="true"><span class="aylan-ichi">'
          + "".join(f"<span>{e(x)}</span>" for x in sozlar) +
          f'</span></span><span class="statik">{e(t["h1_statik"])}</span>'
          f'<span class="q">{e(t["h1_oxir"])}</span>')
    yulduz = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 0c.9 6.6 5.4 11.1 12 12-6.6.9-11.1 5.4-12 12-.9-6.6-5.4-11.1-12-12C6.6 11.1 11.1 6.6 12 0Z"/></svg>'
    lenta_bir = "".join(f'<span class="soz{" kontur" if i % 2 else ""}">{e(x)}</span>{yulduz}' for i, x in enumerate(t["lenta"]))
    suzuvchi = picture(root, "mobil-bosh", "", "(min-width: 900px) 15vw, 34vw", lazy=False)
    harflar = "".join(f'<span style="--i:{i}">{ch}</span>' for i, ch in enumerate("@m_tojiddinov7"))
    hero_img = picture(root, "crm-bosh", t["hero_alt"], "(min-width: 900px) 64vw, 160vw", lazy=False, high=True)

    fakt = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in t["faktlar"])
    ekr = []
    for i, (n, alt, cap) in enumerate(t["ekranlar"]):
        ekr.append(f'<figure><a class="ramka" href="{root}img/{n}-1600.webp" aria-label="{e(t["toliq"])}: {e(cap)}">'
                   f'{picture(root, n, alt, "(min-width: 1100px) 58vw, 150vw")}</a><figcaption class="izoh">{e(cap)}</figcaption></figure>')

    PLYUS = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2" stroke-linecap="round" fill="none"/></svg>'

    def batafsil(slug):
        q = "".join(f'<div><h4>{e(a)}</h4><p>{e(b)}</p></div>' for a, b in t["case"][slug])
        return f'<details class="batafsil"><summary>{e(t["batafsil"])}{PLYUS}</summary><div class="batafsil-ichi">{q}</div></details>'

    def tg_ish(slug, nom, matn, alts, href, link):
        tel = "".join(f'<figure><div class="telefon">{picture(root, f"{slug}-{s}", a, "(min-width: 900px) 21vw, 46vw")}</div></figure>'
                      for s, a in zip(("bosh", "serial"), alts))
        return (f'<article class="ish"><div class="telefonlar">{tel}</div><h3>{e(nom)}</h3><p>{e(matn)}</p>'
                f'<a class="havola" href="{href}" rel="noopener">{e(link)}</a>{batafsil(slug)}</article>')

    saytlar = []
    for n, nom, belgi, matn, href, link, alt in t["saytlar"]:
        b = f'<span class="belgi">{e(belgi)}</span>' if belgi else ""
        uzun = n.replace("sayt-", "uzun-")
        rasm = f'<div class="ramka oqim" data-nur>{picture(root, uzun, alt, "(min-width: 700px) 48vw, 100vw")}</div>'
        if href:
            rasm = f'<a href="{href}" rel="noopener" tabindex="-1" aria-hidden="true">{rasm}</a>'
        havola = f'<a class="havola" href="{href}" rel="noopener">{e(link)}</a>' if href else ""
        saytlar.append(f'<article class="sayt">{rasm}'
                       f'<h3>{e(nom)}{b}</h3><p>{e(matn)}</p>{havola}{batafsil(n)}</article>')

    mob_tel = "".join(f'<figure><div class="telefon">{picture(root, n, a, "(min-width: 1000px) 19vw, 64vw")}</div></figure>'
                      for n, a in zip(("mobil-bosh", "mobil-katalog", "mobil-tolovlar"), t["mob_alt"]))
    mob_fakt = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in t["mob_fakt"])
    mob_boshqa = "".join(f'<li><b>{e(a)}</b><span>{e(b)}</span><a class="havola" href="{h}" rel="noopener">{e(t["kod"])}: {e(a)}</a></li>'
                         for a, b, h in t["mob_boshqa"])
    boshqa = "".join(f"<li><b>{e(a)}</b><span>{e(b)}</span></li>" for a, b in t["boshqa"])
    xiz = "".join(f'<div class="xizmat" data-nur><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in t["xizmatlar"])
    poster = f"{root}img/veo-kadr-800.webp"
    other = SAYT + ("en/" if k == "uz" else "")

    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<meta name="theme-color" content="#0b1416">
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
<link rel="preload" href="{root}geologica.woff2" as="font" type="font/woff2" crossorigin>
<style>{css}</style>
<script>if (!matchMedia("(prefers-reduced-motion: reduce)").matches) document.documentElement.classList.add("harakat");</script>
</head>
<body>
<a class="skip" href="#asosiy">{e(t['skip'])}</a>
<div class="progress" aria-hidden="true"></div>
<header class="tepa"><div class="wrap top">
  <a class="nom" href="{root or './'}"><span class="toliq">Muhammadabdulloh Tojiddinov</span><span class="qisqa">M. Tojiddinov</span></a>
  <nav aria-label="{'Bo‘limlar' if k == 'uz' else 'Sections'}">{nav}<a class="til" href="{t['til_link']}" hreflang="{'en' if k == 'uz' else 'uz'}" lang="{'en' if k == 'uz' else 'uz'}" aria-label="{e(t['til_aria'])}">{t['til_label']}</a>
  <a class="btn btn-asosiy" href="{TG}" rel="noopener" aria-label="{e(t['tg_btn'])}">{TG_ICON}<span>{e(t['tg_btn'])}</span></a></nav>
</div></header>
<main id="asosiy">
<section class="wrap hero" aria-labelledby="h1">
  <h1 id="h1">{h1}</h1>
  <div class="hero-pastki">
    <div class="hero-matn">
      <p>{t['lead']}</p>
      <div class="tugmalar">
        <a class="btn btn-asosiy" href="{TG}" rel="noopener">{TG_ICON}{e(t['tg_btn'])}</a>
        <a class="btn btn-ikkinchi" href="#ishlar">{e(t['cta2'])}</a>
      </div>
    </div>
    <figure class="hero-rasm">
      <div class="plast">{hero_img}</div>
      <div class="suzuvchi" aria-hidden="true">{suzuvchi}</div>
      <figcaption class="izoh">{e(t['hero_izoh'])}</figcaption>
    </figure>
  </div>
</section>
<div class="lenta" aria-hidden="true"><div class="lenta-ichi">{lenta_bir}{lenta_bir}</div></div>

<section class="wrap bolim-bosh" id="ishlar" aria-labelledby="crm">
  <h2 id="crm">{e(t['crm_h2'])}</h2>
  <div class="crm-ichi">
    <div class="crm-chap">
      <p class="tagi">{e(t['crm_tagi'])}</p>
      <div class="crm-yozuv"><p>{e(t['crm_p1'])}</p><p>{e(t['crm_p2'])}</p></div>
      <dl class="faktlar">{fakt}</dl>
      <div class="crm-oxir"><p>{t['crm_oxir']}</p><a class="havola" href="https://hamkorcrm.uz/" rel="noopener">{e(t['crm_link'])}</a></div>
    </div>
    <div class="ekranlar">{''.join(ekr)}</div>
  </div>
</section>

<section class="wrap bolim-bosh" id="mobil" aria-labelledby="mb">
  <h2 id="mb">{e(t['mob_h2'])}</h2>
  <p class="tagi">{e(t['mob_tagi'])}</p>
  <div class="mobil-ichi">
    <figure class="mobil-rasmlar">
      <div class="uch-telefon">{mob_tel}</div>
      <figcaption class="izoh">{e(t['mob_izoh'])}</figcaption>
    </figure>
    <div class="mobil-matn">
      <h3>{e(t['mob_h3'])}</h3>
      <p>{e(t['mob_p'])}</p>
      <dl class="faktlar">{mob_fakt}</dl>
      {batafsil("mijoz")}
    </div>
  </div>
  <div class="mobil-boshqa">
    <h3>{e(t['mob_boshqa_h3'])}</h3>
    <ul class="royxat uchta">{mob_boshqa}</ul>
  </div>
</section>

<section class="wrap bolim-bosh" id="telegram" aria-labelledby="tg">
  <h2 id="tg">{e(t['tg_h2'])}</h2>
  <p class="tagi">{e(t['tg_tagi'])}</p>
  <div class="tg-ishlar">
    {tg_ish('kino', 'KINO TV', t['kino_p'], t['kino_alt'], 'https://t.me/linvkino_bot', '@linvkino_bot')}
    {tg_ish('qogoz', 'Qog‘oz Bino', t['qogoz_p'], t['qogoz_alt'], 'https://qogoz-bino.pages.dev/', 'qogoz-bino.pages.dev')}
  </div>
</section>

<section class="wrap bolim-bosh" id="saytlar" aria-labelledby="sy">
  <h2 id="sy">{e(t['sayt_h2'])}</h2>
  <p class="tagi">{e(t['sayt_tagi'])}</p>
  <div class="saytlar">{''.join(saytlar)}</div>
</section>

<section class="wrap bolim-bosh" id="media" aria-labelledby="md">
  <h2 id="md">{e(t['media_h2'])}</h2>
  <p class="tagi">{e(t['media_tagi'])}</p>
  <div class="media-ishlar">
    <figure>
      <div class="ramka video-ramka">
        <video muted loop playsinline preload="none" poster="{poster}" width="960" height="540" data-src="{root}media/veo-tovuq.mp4" aria-label="{e(t['veo_h3'])}"></video>
        <button class="pauza" type="button" hidden data-pauza="{e(t['veo_pauza'])}" data-davom="{e(t['veo_davom'])}" aria-label="{e(t['veo_pauza'])}">{PAUZA}</button>
      </div>
      <h3>{e(t['veo_h3'])}</h3><p>{e(t['veo_p'])}</p>
    </figure>
    <figure class="buklet">
      <div class="ramka">{picture(root, 'buklet', t['buklet_alt'], '(min-width: 900px) 56vw, 100vw')}</div>
      <h3>{e(t['buklet_h3'])}</h3><p>{e(t['buklet_p'])}</p>
    </figure>
  </div>
</section>

<section class="wrap bolim-bosh" id="boshqa" aria-labelledby="bq">
  <h2 id="bq">{e(t['boshqa_h2'])}</h2>
  <ul class="royxat">{boshqa}</ul>
</section>

<section class="wrap bolim-bosh" id="xizmatlar" aria-labelledby="xz">
  <h2 id="xz">{e(t['xiz_h2'])}</h2>
  <p class="tagi">{e(t['xiz_tagi'])}</p>
  <div class="xizmatlar">{xiz}</div>
</section>

<section class="wrap aloqa" id="aloqa" aria-labelledby="al">
  <h2 id="al" class="tagi">{e(t['aloqa_h2'])}</h2>
  <a class="katta-havola" href="{TG}" rel="noopener" aria-label="Telegram: @m_tojiddinov7"><span class="harflar" aria-hidden="true">{harflar}</span></a>
  <p class="tagi" style="margin-top:28px">{e(t['aloqa_p'])}</p>
  <div class="aloqa-boshqa">
    <a class="havola" href="https://hamkorcrm.uz/" rel="noopener">hamkorcrm.uz</a>
    <a class="havola" href="https://github.com/linverno-tm" rel="noopener">{e(t['github'])}</a>
  </div>
</section>
</main>
<footer><div class="wrap"><span>© 2026 {e(t['footer'])}</span><a href="{t['til_link']}" hreflang="{'en' if k == 'uz' else 'uz'}">{'English' if k == 'uz' else 'O‘zbekcha'}</a></div></footer>
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
