"""Saytni yig'adi.

    python tools/build.py

Chiqadi: index.html, ishlar/<slug>/index.html (o'zbekcha) va en/... (inglizcha), 404.html, sitemap.xml.
Matn shu faylda; uslub tools/uslub.css, skript tools/skript.js (ikkalasi sahifa ichiga qo'yiladi);
rasm o'lchamlari tools/rasmlar.json da (tools/rasm.py yozadi).

G'oya: «chizmadan jonli ekranga». Har ish skrinshoti avval ko'k qalam chizmasi bo'lib turadi va skroll
bilan haqiqiy ekranga aylanadi — egasi nima qilishini sahifaning o'zi ko'rsatadi.
"""
import base64
import hashlib
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RASM = json.load(open(os.path.join(ROOT, "tools", "rasmlar.json"), encoding="utf-8"))
CSS = open(os.path.join(ROOT, "tools", "uslub.css"), encoding="utf-8").read()
JS = open(os.path.join(ROOT, "tools", "skript.js"), encoding="utf-8").read()


_VER, _LQ = {}, {}


def ver(url):
    """Statik fayl manziliga mazmun xeshi: media 1 yil «immutable» keshlansa ham yangilanishi yetib boradi."""
    if url not in _VER:
        with open(os.path.join(ROOT, url.lstrip("/")), "rb") as f:
            _VER[url] = f"{url}?v={hashlib.md5(f.read()).hexdigest()[:8]}"
    return _VER[url]


def lqip(url):
    """Rasm/video posterining 16 px «xira nusxasi» (data URI) — asl fayl kelguncha joy bo'sh turmaydi."""
    if url not in _LQ:
        import io
        from PIL import Image
        im = Image.open(os.path.join(ROOT, url.lstrip("/"))).convert("RGB")
        im = im.resize((16, max(2, round(16 * im.height / im.width))), Image.LANCZOS)
        b = io.BytesIO(); im.save(b, "WEBP", quality=30)
        _LQ[url] = "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()
    return _LQ[url]


for _f in ("/unbounded.woff2", "/onest.woff2"):
    CSS = CSS.replace(f'url("{_f}")', f'url("{ver(_f)}")')

JS_XESH = "sha256-" + base64.b64encode(hashlib.sha256(JS.encode("utf-8")).digest()).decode()
SAYT = "https://linverno-tm.github.io"
TG = "https://t.me/m_tojiddinov7"
GITHUB = "https://github.com/linverno-tm"
MANBA = "https://github.com/linverno-tm/linverno-tm.github.io"

TG_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M21.4 4.2 2.9 11.3c-1.3.5-1.2 1.2-.2 1.5l4.7 1.5 1.8 5.6c.2.6.1.9.8.9.5 0 .7-.2 1-.5l2.3-2.2 4.8 3.5c.9.5 1.5.2 1.7-.8l3.1-14.8c.3-1.3-.5-1.9-1.5-1.8ZM8.6 14l9.3-5.9c.5-.3.9-.1.5.2l-7.9 7.2-.3 3.4L8.6 14Z"/></svg>'
TASHQI = '<svg class="tashqi" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3h8v8M13 3 3 13" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'

# --------------------------------------------------------------------------------------------
# Umumiy matn
# --------------------------------------------------------------------------------------------
U = {
    "uz": {
        "title": "Muhammadabdulloh Tojiddinov — sayt, CRM, bot va video",
        "desc": "Biznes uchun sayt, CRM, Telegram bot va video yasayman: chizmadan ishga tushirishgacha o‘zim. Hamkor CRM muallifi.",
        "skip": "Asosiy qismga o‘tish",
        "ishlar": "Ishlar", "aloqa": "Aloqa",
        "til": "English", "til_qisqa": "EN", "til_kod": "en",
        "h1": "Sayt, CRM, bot va video yasayman.",
        "kirish": "Muhammadabdulloh Tojiddinov. Chizmasidan serverga chiqarishgacha hammasini o‘zim qilaman.",
        "tg": "Telegram’da yozish",
        "korish": "Ishlarni ko‘rish",
        "jonli": "ishlab turibdi",
        "ishlar_h": "Tanlangan ishlar",
        "ishlar_p": "Har biri chizma bo‘lib boshlangan. Hozir ishlab turibdi.",
        "myn": ("Muammo", "Yechim", "Natija"),
        "batafsil": "Batafsil",
        "jarayon_h": "Qanday ishlayman",
        "jarayon_p": "Boshidan oxirigacha bir kishi javob beradi.",
        "qadamlar": [
            ("Chizma", "Biznesingizni so‘rab, ekranlarni chizaman."),
            ("Kod", "Dizayndan serverga, hammasini o‘zim yozaman."),
            ("Sinov", "Telefon, planshet va kompyuterda tekshiraman."),
            ("Ishga tushirish", "Domen, hosting, bot ulangan holda topshiraman."),
        ],
        "video_h": "Video",
        "video_p": "Reklama kadrlari va saytlar uchun jonli fon.",
        "kliplar": ("Veo bilan yaratilgan reklama kadri, Shuxrat o‘g‘li sayti uchun.", "Chelakdan oqayotgan shpaklyovka: PROMIX sayti uchun kinemagraf."),
        "yana_h": "Yana",
        "aloqa_h": "Loyihangiz bormi?",
        "aloqa_p": "Telegram’da qisqacha yozing: biznesingiz nima qiladi va nimani tezlashtirmoqchisiz.",
        "manba": "Sayt manbasi",
        "orqaga": "Barcha ishlar",
        "keyingi": "Keyingi loyiha",
        "meta": ("Davr", "Rol", "Texnologiyalar", "Holat"),
        "rol": "Muallif: dizayn va dasturlash",
        "konsept": "Konsept",
        "pauza": "Videoni to‘xtatish", "davom": "Videoni davom ettirish",
        "oy": ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"],
        "hozir": "hozir",
        "nusxa": "Nusxa olish", "nusxa_ok": "Nusxa olindi", "nusxa_xato": "Qo‘lda nusxa oling",
        "yoq_t": "Sahifa topilmadi", "yoq_p": "Havola eskirgan yoki xato yozilgan. Ishlardan birini oching yoki bosh sahifaga qayting.", "bosh_sahifa": "Bosh sahifa",
        "menyu": "Asosiy menyu", "havolalar": "Havolalar",
    },
    "en": {
        "title": "Muhammadabdulloh Tojiddinov — websites, CRM, bots, video",
        "desc": "I build websites, CRMs, Telegram bots and video for businesses, from the first sketch to launch. Author of Hamkor CRM.",
        "skip": "Skip to content",
        "ishlar": "Work", "aloqa": "Contact",
        "til": "O‘zbekcha", "til_qisqa": "UZ", "til_kod": "uz",
        "h1": "I build websites, CRMs, bots and video.",
        "kirish": "Muhammadabdulloh Tojiddinov. From the first sketch to the live server, I do it all myself.",
        "tg": "Message on Telegram",
        "korish": "See the work",
        "jonli": "live",
        "ishlar_h": "Selected work",
        "ishlar_p": "Each one started as a sketch. Each one is running now.",
        "myn": ("Problem", "Solution", "Result"),
        "batafsil": "Details",
        "jarayon_h": "How I work",
        "jarayon_p": "One person answers for all of it, from start to finish.",
        "qadamlar": [
            ("Sketch", "I ask about your business and draw the screens."),
            ("Code", "Design to server, I write all of it."),
            ("Testing", "Checked on phone, tablet and desktop."),
            ("Launch", "Handed over with domain, hosting and bot connected."),
        ],
        "video_h": "Video",
        "video_p": "Ad shots and living backgrounds for websites.",
        "kliplar": ("An ad shot made with Veo for the Shuxrat o‘g‘li site.", "Filler pouring from a bucket: a cinemagraph for the PROMIX site."),
        "yana_h": "More",
        "aloqa_h": "Have a project?",
        "aloqa_p": "Send a few lines on Telegram: what your business does and what you want to speed up.",
        "manba": "Site source",
        "orqaga": "All work",
        "keyingi": "Next project",
        "meta": ("Period", "Role", "Stack", "Status"),
        "rol": "Author: design and development",
        "konsept": "Concept",
        "pauza": "Pause video", "davom": "Play video",
        "oy": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "hozir": "present",
        "nusxa": "Copy", "nusxa_ok": "Copied", "nusxa_xato": "Copy it manually",
        "yoq_t": "Page not found", "yoq_p": "The link is outdated or mistyped. Open one of the projects or go back home.", "bosh_sahifa": "Home",
        "menyu": "Main", "havolalar": "Links",
    },
}

# --------------------------------------------------------------------------------------------
# Loyihalar
# vizual (bosh sahifa va loyiha boshi): kom — kompyuter ekrani, uzun — kom uzun sahifa (ramkada skroll),
#   chizma — ko'k chizma qatlami, tel — telefon ekrani, tellar — faqat telefonlar.
# bosh=True — bosh sahifadagi tanlangan ishlar. qisqa — muammo, yechim, natija (har biri 1 qator).
# Bloklar: ("h", matn) | ("p", matn) | ("ul", [..]) | ("rasm", nom, izoh) | ("tel", [(nom, izoh)])
#          | ("butun", nom, izoh) | ("video", izoh)
# --------------------------------------------------------------------------------------------
LOYIHALAR = [
    {"slug": "hamkor-crm", "boshi": (2026, 9), "oxiri": None, "bosh": True,
     "vizual": {"kom": "crm-bosh", "chizma": "chizma-crm", "tel": "mobil-bosh", "manzil": "hamkorcrm.uz"},
     "stack": "Next.js, TypeScript, PostgreSQL 16, Tauri v2",
     "havola": ("https://hamkorcrm.uz/", "hamkorcrm.uz"),
     "uz": {"nom": "Hamkor CRM", "tur": "Savdo va nasiya tizimi",
            "lid": "To‘rt filialli savdo tarmog‘i uchun 1C o‘rnini bosgan muddatli to‘lov savdo tizimi.",
            "qisqa": ("To‘rt do‘kon to‘rtta alohida 1C bazasida ishlardi va bir-birini ko‘rmasdi.",
                      "Bitta baza: savdo, nasiya, kassa, ombor va hisobot; internetsiz ham ishlaydi, mijozga mobil ilova.",
                      "Bir oyda 244 sahifa; to‘rt filial bitta tizimda ishlayapti."),
            "holat": "Ishlatilmoqda",
            "alt": "Hamkor CRM bosh sahifasi: kassalar, nasiya qarzi va oylik foyda grafigi; summalar yopilgan",
            "tel_alt": "Hamkor mijozlar ilovasi, bosh sahifa; summalar yopilgan",
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
            "qisqa": ("Four stores ran on four separate 1C databases that couldn’t see each other.",
                      "One database for sales, installments, cash, stock and reports; works offline, with a customer app.",
                      "244 pages in one month; all four branches now run on one system."),
            "holat": "In use",
            "alt": "Hamkor CRM home screen: cash, installment debt and a monthly profit chart; amounts hidden",
            "tel_alt": "Hamkor customer app, home screen; amounts hidden",
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

    {"slug": "hamkor-savdo", "boshi": (2026, 8), "oxiri": None, "bosh": True,
     "vizual": {"kom": "uzun-savdo", "uzun": True, "chizma": "chizma-savdo", "tel": "savdo-tel", "manzil": "hamkorsavdo.uz"},
     "stack": "Next.js 16, React 19, TypeScript, Tailwind CSS v4",
     "havola": ("https://hamkorsavdo.uz/", "hamkorsavdo.uz"),
     "uz": {"nom": "Hamkor Savdo", "tur": "Brend sayti",
            "lid": "To‘rt filialli savdo tarmog‘ining brend sayti, narx kuzatuvi va bosma materiallar.",
            "qisqa": ("Kompaniya, to‘rt filial va bog‘lanish yo‘llari bitta joyda yo‘q edi.",
                      "Brendbuk asosida sayt: logotip vektorga o‘tkazilgan, mahsulot 3D ko‘rinishda, har filialga sahifa.",
                      "To‘rt filial, 7 000+ mahsulot va muddatli to‘lov sharti bitta saytda."),
            "holat": "Ishlab turibdi",
            "alt": "Hamkor Savdo sayti, bosh sahifa",
            "tel_alt": "Hamkor Savdo sayti telefonda",
            "bloklar": [
                ("h", "Vazifa"),
                ("p", "Kompaniyani, uning taklifini, har bir filialni va bog‘lanish yo‘llarini bitta saytda ko‘rsatish. Asosiy shart: sekin mobil internetda ham tez ochilsin."),
                ("h", "Yechim"),
                ("p", "Sayt Next.js’dan statik sahifalar sifatida chiqariladi. Mahsulotni har tomondan ko‘rsatadigan 3D qism sahifa ochilib bo‘lgach, bo‘sh paytda yuklanadi, shuning uchun matn birinchi chiqadi; telefon va manzillar oddiy havolalar."),
                ("ul", ["Ranglar, shriftlar va logotip brendbukdan olingan; logotip rasmdan vektorga o‘tkazilgan.",
                        "Matn kontrasti hamma joyda kamida 4.5:1.",
                        "E’lon qilinmagan ma’lumot, masalan ish vaqti yoki kafolat muddati, to‘qib qo‘yilmagan."]),
                ("butun", "uzun-savdo", "Bosh sahifa to‘liq; ramka ichida aylantirib ko‘ring."),
                ("h", "Yonidagi ishlar"),
                ("p", "Narx kuzatuvi: raqobatchilarning Telegram guruhlaridagi e’lonlaridan narxlar ajratib olinadi, har bir do‘konga kunlik PDF faqat yangi va o‘zgargan narxlar bilan boradi."),
                ("rasm", "buklet", "Yevrobuklet, A4, uch buklama; bosmaga tayyor vektor fayl."),
            ]},
     "en": {"nom": "Hamkor Savdo", "tur": "Brand website",
            "lid": "The brand site for a four-branch retail chain, plus price watching and print.",
            "qisqa": ("The company, its four branches and its contacts were never in one place.",
                      "A site built from the brand book: logo traced to vector, products in 3D, a page for every branch.",
                      "Four branches, 7,000+ products and installment terms on one site."),
            "holat": "Live",
            "alt": "Hamkor Savdo website, home page",
            "tel_alt": "Hamkor Savdo website on a phone",
            "bloklar": [
                ("h", "The problem"),
                ("p", "Show the company, its offer, every branch and every way to reach it on one site. The main constraint: fast on slow mobile connections."),
                ("h", "What I built"),
                ("p", "The site is exported from Next.js as static pages. The 3D part that shows a product from every side loads only after the page is up and the browser is idle, so the text comes first; phone numbers and addresses are plain links."),
                ("ul", ["Colours, fonts and the logo come from the brand book; the logo was traced to vector from the bitmap.",
                        "Every text pair has at least 4.5:1 contrast.",
                        "Unpublished facts such as opening hours or warranty length were not made up."]),
                ("butun", "uzun-savdo", "The full home page; scroll inside the frame."),
                ("h", "Alongside"),
                ("p", "Price watching: prices are pulled from competitors’ posts in Telegram groups, and each store gets a daily PDF with only the new and changed prices."),
                ("rasm", "buklet", "Tri-fold A4 booklet, print-ready vector file."),
            ]}},

    {"slug": "oltinkol", "boshi": (2026, 10), "oxiri": None, "bosh": True,
     "vizual": {"kom": "charm-kom", "chizma": "chizma-charm", "tel": "charm-tel", "manzil": "linverno-tm.github.io/oltinkol-zona"},
     "stack": "HTML, CSS, JavaScript, Cloudflare Workers, D1",
     "havola": ("https://linverno-tm.github.io/oltinkol-zona/", "linverno-tm.github.io/oltinkol-zona"),
     "uz": {"nom": "Andijon Charm-Poyabzal Markazi", "tur": "Sayt, admin panel va Telegram bot",
            "lid": "Oltinko‘l tumanidagi charm-poyabzal zonasi uchun sayt, admin panel va arizalar boti.",
            "qisqa": ("Zonadagi do‘konlarni sotish va investor topish kerak edi.",
                      "Uch tilli sayt: teridan poyabzalgacha hikoya, zonaning 3D xaritasi; arizalar direksiya botiga karta bo‘lib tushadi.",
                      "14 bo‘lim, o‘zbek, rus va ingliz tilida; har arizani kim qabul qilgani ko‘rinib turadi."),
            "holat": "Ishlab turibdi",
            "alt": "Andijon Charm-Poyabzal Markazi sayti, bosh sahifa",
            "tel_alt": "Andijon Charm-Poyabzal Markazi sayti telefonda",
            "bloklar": [
                ("h", "Vazifa"),
                ("p", "Zonadagi do‘konlarni sotish, poyabzal va charm ishlab chiqaruvchilarni hamda investorlarni jalb qilish."),
                ("h", "Yechim"),
                ("p", "Do‘konlar, kredit shartlari, imtiyozlar, investorlar va rezidentlar uchun sahifalar. Arizalar, do‘konlar va foydalanuvchilarni boshqarish uchun admin panel."),
                ("ul", ["Teridan poyabzalgacha hikoya va zonaning 3D xaritasi: og‘ir 3D qism faqat foydalanuvchi harakatidan keyin yuklanadi.",
                        "Sayt va mijozlar botidan kelgan ariza direksiya guruhiga karta bo‘lib tushadi: qabul qilindi, qo‘ng‘iroq qilindi, yopildi.",
                        "Instagram izohlari va xabarlari ham botga keladi, har kuni 20:00 da kunlik hisobot."]),
                ("butun", "uzun-charm", "Bosh sahifa to‘liq; ramka ichida aylantirib ko‘ring."),
                ("h", "Natija"),
                ("p", "14 ta bo‘lim, o‘zbek, rus va ingliz tilida; arizalar yo‘qolmaydi, kim qachon javob bergani kartada yozilib boradi."),
            ]},
     "en": {"nom": "Andijan Leather & Footwear Centre", "tur": "Website, admin panel and Telegram bot",
            "lid": "A site, admin panel and lead bot for a leather and footwear zone in Oltinko‘l district.",
            "qisqa": ("The zone needed to sell its shops and find investors.",
                      "A three-language site: the leather-to-shoe story and a 3D zone map; every lead lands in the board’s bot as a card.",
                      "14 sections in Uzbek, Russian and English; each lead shows who picked it up."),
            "holat": "Live",
            "alt": "Andijan Leather & Footwear Centre website, home page",
            "tel_alt": "Andijan Leather & Footwear Centre website on a phone",
            "bloklar": [
                ("h", "The problem"),
                ("p", "Sell the zone’s shops and attract footwear and leather makers and investors."),
                ("h", "What I built"),
                ("p", "Pages for shops, credit terms, incentives, investors and residents, plus an admin panel for applications, shops and users."),
                ("ul", ["The leather-to-shoe story and a 3D map of the zone: the heavy 3D part loads only after the visitor interacts.",
                        "Leads from the site and the customer bot arrive in the board’s group as cards: accepted, called, closed.",
                        "Instagram comments and messages come to the bot too, with a daily report at 20:00."]),
                ("butun", "uzun-charm", "The full home page; scroll inside the frame."),
                ("h", "Result"),
                ("p", "14 sections in Uzbek, Russian and English; no lead gets lost, and each card records who answered and when."),
            ]}},

    {"slug": "promix", "boshi": (2026, 10), "oxiri": (2026, 10), "bosh": True, "konsept": True,
     "vizual": {"kom": "promix-kom", "chizma": "chizma-promix", "tel": "promix-tel", "manzil": "linverno-tm.github.io/promix-uz"},
     "stack": "Python, Jinja2, HTML, CSS, JavaScript, ffmpeg",
     "havola": ("https://linverno-tm.github.io/promix-uz/", "linverno-tm.github.io/promix-uz"),
     "uz": {"nom": "PROMIX", "tur": "Pardoz materiallari sayti",
            "lid": "Rossiyalik pardoz materiallari ishlab chiqaruvchisi uchun o‘zbekcha sayt namunasi.",
            "qisqa": ("Ishlab chiqaruvchining O‘zbekiston uchun o‘zbekcha sayti yo‘q edi.",
                      "Texnik tavsiflardan 30 mahsulotli katalog; chelakdan oqayotgan shpaklyovka kinemagrafi.",
                      "O‘zbek va rus tilida tayyor namuna; ochiq chiqarish ishlab chiqaruvchi roziligi bilan."),
            "alt": "PROMIX sayti, bosh sahifa",
            "tel_alt": "PROMIX sayti telefonda",
            "bloklar": [
                ("h", "Vazifa"),
                ("p", "Pardoz materiallarini O‘zbekistondagi ustalar va do‘konlarga o‘z tilida tanishtirish: nima, qayerga, qancha sarflanadi."),
                ("h", "Yechim"),
                ("p", "Sayt Python va Jinja2 shablonlaridan yig‘iladi. 30 ta mahsulot ma’lumoti (sarf, qurish vaqti, qadoq) ishlab chiqaruvchining texnik tavsifidan olingan."),
                ("ul", ["Bosh qismdagi jonli fon: chelakdan oqayotgan shpaklyovka kinemagrafi, ffmpeg bilan siqilgan.",
                        "Harakatni kamaytirish so‘ralgan yoki trafik tejash rejimida video yuklanmaydi, oddiy surat turadi.",
                        "O‘zbek va rus tilida."]),
                ("video2", "PROMIX sayti uchun kinemagraf."),
                ("h", "Natija"),
                ("p", "Namuna sifatida tayyor. Savdo belgisi va qadoq suratlari ishlab chiqaruvchiniki, shuning uchun ochiq chiqarish ularning roziligi bilan."),
            ]},
     "en": {"nom": "PROMIX", "tur": "Finishing materials website",
            "lid": "A concept Uzbek-language site for a Russian maker of finishing materials.",
            "qisqa": ("The maker had no Uzbek-language site for Uzbekistan.",
                      "A 30-product catalog built from the spec sheets; a cinemagraph of filler pouring from a bucket.",
                      "A finished concept in Uzbek and Russian; going public needs the maker’s consent."),
            "alt": "PROMIX website, home page",
            "tel_alt": "PROMIX website on a phone",
            "bloklar": [
                ("h", "The problem"),
                ("p", "Introduce the finishing materials to builders and shops in Uzbekistan in their own language: what each product is, where it goes and how much you need."),
                ("h", "What I built"),
                ("p", "The site is generated from Python and Jinja2 templates. Data for 30 products (coverage, drying time, packaging) comes from the maker’s spec sheets."),
                ("ul", ["The living header background is a cinemagraph of filler pouring from a bucket, compressed with ffmpeg.",
                        "With reduced motion or data saver on, the video is not loaded and a still image is shown.",
                        "Uzbek and Russian."]),
                ("video2", "A cinemagraph for the PROMIX site."),
                ("h", "Result"),
                ("p", "Ready as a concept. The trademark and pack photos belong to the maker, so going public needs their consent."),
            ]}},

    {"slug": "mini-ges", "boshi": (2026, 10), "oxiri": None, "bosh": True,
     "vizual": {"kom": "uzun-ges", "uzun": True, "chizma": "chizma-ges", "tel": "ges-tel", "manzil": "linverno-tm.github.io/mini-ges-site"},
     "stack": "HTML, CSS, JavaScript, GitHub Actions",
     "havola": ("https://linverno-tm.github.io/mini-ges-site/", "linverno-tm.github.io/mini-ges-site"),
     "uz": {"nom": "MINI GES", "tur": "Sayt",
            "lid": "Kichik gidroelektrostansiyalar va ularni qurish xizmati uchun sayt.",
            "qisqa": ("Ulug‘nor (600 kVt) va Baliqchi (1 000 kVt) GES’larini tanitib, qurish xizmatini sotish kerak edi.",
                      "Freymvorksiz sayt: kanal videosi, ishlash sxemasi va 3D turbina; harakat CSS’da, JavaScript 16 KB.",
                      "Uch tilda; har o‘zgarishni CI tekshirib, o‘zi chiqaradi."),
            "alt": "MINI GES sayti, bosh sahifa",
            "tel_alt": "MINI GES sayti telefonda",
            "bloklar": [
                ("h", "Vazifa"),
                ("p", "Ulug‘nor GES (600 kVt, ishlab turibdi) va Baliqchi GES (1 000 kVt) ni tanishtirish va mini-GES qurish xizmatini sotish."),
                ("h", "Yechim"),
                ("p", "Freymvorksiz statik sayt, g‘oyasi: sahifa — kanal. Suv turbinadan o‘tib tokka aylanadi: haqiqiy kanal videosi, ishlash sxemasi, 3D turbina (Sketchfab, CC BY) va ikki obyekt."),
                ("ul", ["Soha yangiliklari sahifa ochilganda emas, sayt yig‘ilayotganda yoziladi: begona saytga so‘rov ketmaydi.",
                        "Har bir o‘zgarishni CI tekshiradi va GitHub Pages’ga o‘zi chiqaradi.",
                        "Animatsiya kutubxonasi olib tashlangan: harakat CSS’da, telefonda sarlavha darhol ko‘rinadi.",
                        "O‘zbek, rus va ingliz tilida."]),
                ("butun", "uzun-ges", "Bosh sahifa to‘liq; ramka ichida aylantirib ko‘ring."),
                ("h", "Natija"),
                ("p", "Uch tilli sayt; yangilash uchun faqat o‘zgarishni yuborish kifoya, qolganini CI qiladi."),
            ]},
     "en": {"nom": "MINI GES", "tur": "Website",
            "lid": "A site for small hydro-power plants and the service of building them.",
            "qisqa": ("Present the Ulug‘nor (600 kW) and Baliqchi (1,000 kW) plants and sell the build service.",
                      "A framework-free site: canal video, a how-it-works diagram and a 3D turbine; motion in CSS, 16 KB of JavaScript.",
                      "Three languages; CI checks and publishes every change."),
            "alt": "MINI GES website, home page",
            "tel_alt": "MINI GES website on a phone",
            "bloklar": [
                ("h", "The problem"),
                ("p", "Present Ulug‘nor GES (600 kW, running) and Baliqchi GES (1,000 kW), and sell the service of building small hydro plants."),
                ("h", "What I built"),
                ("p", "A static site without a framework, built on one idea: the page is a canal. Water passes the turbine and becomes power: real canal video, a how-it-works diagram, a 3D turbine (Sketchfab, CC BY) and the two plants."),
                ("ul", ["Industry news is written in at build time, not fetched when the page opens, so no request goes to a third-party site.",
                        "CI checks every change and publishes it to GitHub Pages.",
                        "The animation library is gone: motion is CSS, and the headline shows at once on phones.",
                        "Uzbek, Russian and English."]),
                ("butun", "uzun-ges", "The full home page; scroll inside the frame."),
                ("h", "Result"),
                ("p", "A three-language site; an update is just a push, CI does the rest."),
            ]}},

    {"slug": "qogoz-bino", "boshi": (2026, 10), "oxiri": None, "bosh": True,
     "vizual": {"tellar": ["qogoz-bosh", "qogoz-serial"], "chizma": "chizma-qogoz"},
     "stack": "Python, aiogram 3, Telethon, HTML, CSS, JavaScript",
     "havola": ("https://t.me/QogozBinoTVbot", "@QogozBinoTVbot"),
     "uz": {"nom": "Qog‘oz Bino", "tur": "Telegram bot va mini app",
            "lid": "Do‘stimning @QogozBinoTVbot boti: Manybot o‘rniga o‘z bot va posterli mini app.",
            "qisqa": ("Botda serial ko‘p edi, lekin u Manybot’ga bog‘liq va tanlash uchun katalog yo‘q edi.",
                      "O‘z bot (aiogram 3): menyu daraxti, ombor kanaldan yuborish, muqovalar; posterli mini app.",
                      "Mini app bot menyusidan ochiladi; kirill va lotinda jonli qidiruv."),
            "alt": "Qog‘oz Bino mini app: yangi qismlar",
            "tel_alt": "Qog‘oz Bino mini app: serial sahifasi",
            "bloklar": [
                ("h", "Vazifa"),
                ("p", "Botda serial ko‘p, lekin u Manybot konstruktorida ishlardi va ularni ko‘rib tanlash uchun katalog yo‘q edi."),
                ("h", "Yechim"),
                ("p", "Manybot o‘rniga o‘z bot: menyu daraxti, video ombor kanaldan nusxa sifatida yuboriladi, har serialga muqova. Katalogni botning o‘zidan yig‘adigan skript va shu katalog bilan ishlaydigan mini app."),
                ("tel", [("qogoz-bosh", "Yangi qismlar va haftaning eng ko‘p ko‘rilganlari."), ("qogoz-serial", "Serial sahifasi.")]),
                ("ul", ["Kirill va lotinda jonli qidiruv, bo‘lim va janr bo‘yicha saralash.",
                        "Serial tanlansa, kartani va qismlarni botning o‘zi beradi.",
                        "Har qism kamida 480p; vertikal va sifatsiz videolar olinmaydi."]),
                ("h", "Natija"),
                ("p", "Mini app BotFather’dagi menyu tugmasi orqali ochiladi; bot o‘z serverida ishlaydi."),
            ]},
     "en": {"nom": "Qog‘oz Bino", "tur": "Telegram bot and mini app",
            "lid": "My friend’s @QogozBinoTVbot: an own bot in place of Manybot, plus a poster mini app.",
            "qisqa": ("The bot had plenty of series, but it depended on Manybot and had no catalog to browse.",
                      "An own bot (aiogram 3): menu tree, sending from a storage channel, covers; a poster mini app.",
                      "The mini app opens from the bot menu; live search in Cyrillic and Latin."),
            "alt": "Qog‘oz Bino mini app: new episodes",
            "tel_alt": "Qog‘oz Bino mini app: a series page",
            "bloklar": [
                ("h", "The problem"),
                ("p", "The bot had plenty of series, but it ran on the Manybot builder and had no catalog to browse them."),
                ("h", "What I built"),
                ("p", "An own bot in place of Manybot: a menu tree, videos sent as copies from a storage channel, a cover for every series. A script builds the catalog from the bot itself, and a mini app runs on that catalog."),
                ("tel", [("qogoz-bosh", "New episodes and the week’s most watched."), ("qogoz-serial", "Series page.")]),
                ("ul", ["Live search in Cyrillic and Latin, filters by section and genre.",
                        "Picking a series hands over to the bot, which sends the card and episodes.",
                        "Every episode is at least 480p; vertical and low-quality videos are rejected."]),
                ("h", "Result"),
                ("p", "The mini app opens from the bot’s menu button in BotFather; the bot runs on its own server."),
            ]}},

    {"slug": "mijozlar-ilovasi", "boshi": (2026, 10), "oxiri": None,
     "vizual": {"tellar": ["mobil-bosh", "mobil-katalog", "mobil-tolovlar"]},
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

    {"slug": "kino-tv", "boshi": (2026, 10), "oxiri": (2026, 10),
     "vizual": {"tellar": ["kino-bosh", "kino-serial"]},
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

    {"slug": "shuxrat-ogli", "boshi": (2026, 10), "oxiri": (2026, 10), "konsept": True,
     "vizual": {"kom": "uzun-shuxrat", "uzun": True, "manzil": "linverno-tm.github.io/shuxrat-ogli-v2"},
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
]

BOSHQA = [
    {"sana": (2026, 9), "url": "https://github.com/linverno-tm/accounting-report",
     "uz": ("Kameral hisobot", "Hisob-faktura va kassa cheklaridan soliq tekshiruvi uchun hisobotni o‘zi yig‘adi."),
     "en": ("Tax audit report", "Builds the tax-audit report from invoices and cash receipts.")},
    {"sana": (2026, 2), "url": "https://github.com/linverno-tm/chatforge",
     "uz": ("ChatForge", "Flutter’da messenjer: shaxsiy yozishmalar va push-xabarnoma."),
     "en": ("ChatForge", "A Flutter messenger: one-to-one chats and push notifications.")},
    {"sana": (2026, 2), "url": "https://github.com/linverno-tm/bulk-sms",
     "uz": ("Ommaviy SMS", "Excel yoki CSV ro‘yxatdan SMS yuboradigan Android ilova."),
     "en": ("Bulk SMS", "An Android app that sends SMS from an Excel or CSV list.")},
    {"sana": (2026, 1), "url": "https://github.com/linverno-tm/task-manager",
     "uz": ("Vazifalar ilovasi", "Internetsiz ishlaydi, aloqa tiklanganda o‘zi sinxronlanadi."),
     "en": ("Task manager", "Works offline and syncs on its own when the connection returns.")},
]

# Jarayon rasmlari: ko'k qalam chiziqlari (pathLength=1 — chizilish animatsiyasi uchun)
QADAM_SVG = [
    '<rect x="6" y="8" width="108" height="76" rx="4"/><path d="M6 22h108"/><rect x="16" y="32" width="52" height="20" rx="2"/><path d="M16 62h40M16 70h28"/><rect x="78" y="32" width="26" height="42" rx="2"/>',
    '<path d="M38 26 18 46l20 20M82 26l20 20-20 20M68 18 52 74"/>',
    '<rect x="6" y="14" width="66" height="46" rx="3"/><path d="M28 72h22M39 60v12"/><rect x="62" y="30" width="34" height="48" rx="3"/><rect x="98" y="40" width="18" height="36" rx="3"/>',
    '<rect x="6" y="16" width="108" height="62" rx="4"/><path d="M6 30h108"/><circle cx="18" cy="23" r="2.5"/><path d="M40 54l12 12 26-28"/>',
]


def e(s):
    return html.escape(s, quote=True)


def picture(name, alt, sizes, lazy=True, high=False, cls=""):
    m = RASM[name]
    ws = sorted(m["widths"])
    def srcset(ext):
        return ", ".join(f"{ver(f'/img/{name}-{w}.{ext}')} {w}w" for w in ws)
    w0, h0 = ws[-1], round(m["h"] * ws[-1] / m["w"])
    attrs = f'width="{w0}" height="{h0}" alt="{e(alt)}"'
    attrs += ' loading="lazy" decoding="async"' if lazy else ""
    attrs += ' fetchpriority="high"' if high else ""
    attrs += f' class="{(cls + " lq").strip()}" style="background-image: url({lqip(f'/img/{name}-{ws[0]}.webp')})"'
    return (f'<picture><source type="image/avif" srcset="{srcset("avif")}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{srcset("webp")}" sizes="{sizes}">'
            f'<img src="{ver(f"/img/{name}-{ws[0]}.webp")}" {attrs}></picture>')


def chizma(name, lazy=True):
    """Ko'k chizma qatlami: faqat bezak, skroll bilan yo'qoladi (CSS)."""
    if not name or name not in RASM:
        return ""
    m = RASM[name]
    return (f'<img class="chizma" src="{ver(f'/img/{name}.webp')}" alt="" width="{m["w"]}" height="{m["h"]}"{' loading="lazy"' if lazy else ''} decoding="async">'
            '<span class="skaner" aria-hidden="true"></span>')


def sana(til, ym):
    return f"{U[til]['oy'][ym[1] - 1]} {ym[0]}"


def davr(til, p):
    b = sana(til, p["boshi"])
    if p["oxiri"] is None:
        return f"{b} – {U[til]['hozir']}"
    return b if p["oxiri"] == p["boshi"] else f"{b} – {sana(til, p['oxiri'])}"


def yol(til, slug=None):
    b = "/" if til == "uz" else "/en/"
    return b if slug is None else f"{b}ishlar/{slug}/"


def oyna(nom, alt, manzil, sizes, uzun=False, chz=None, lazy=True, high=False, vt=None):
    """Brauzer oynasi ichidagi kompyuter ekrani."""
    st = f' style="view-transition-name: {vt}"' if vt else ""
    sl = ""
    if uzun:  # ramka (16:10) ichida sahifa oxirigacha siljish, rasm balandligiga nisbatan
        m = RASM[nom]
        sl = f' style="--siljish: -{(1 - (10 / 16) / (m["h"] / m["w"])) * 100:.1f}%"'
    return (f'<div class="oyna{" oyna--uzun" if uzun else ""}"{st}>'
            f'<div class="oyna__bar" aria-hidden="true"><i></i><i></i><i></i><span>{e(manzil)}</span></div>'
            f'<div class="oyna__ekran"{sl}>{picture(nom, alt, sizes, lazy, high)}{chizma(chz) if chz else ""}</div></div>')


def tel(nom, alt, sizes, lazy=True, chz=None, cls="", high=False):
    return f'<div class="tel {cls}"><div class="tel__ekran">{picture(nom, alt, sizes, lazy, high)}{chizma(chz, lazy) if chz else ""}</div></div>'


def vizual(p, til, lazy=True, high=False, chizmali=True, vt=True):
    """Loyihaning asosiy kompozitsiyasi: kompyuter + telefon yoki telefonlar."""
    v, t = p["vizual"], p[til]
    vtn = f"kadr-{p['slug']}" if vt else None
    if "tellar" in v:
        ichki = "".join(tel(n, t["alt"] if i == 0 else t.get("tel_alt", ""), "(min-width: 960px) 260px, 42vw", lazy,
                            v.get("chizma") if (chizmali and i == 0) else None, high=high and i == 0)
                        for i, n in enumerate(v["tellar"]))
        st = f' style="view-transition-name: {vtn}"' if vtn else ""
        return f'<div class="kompozitsiya kompozitsiya--tellar n{len(v["tellar"])}"{st}>{ichki}</div>'
    k = oyna(v["kom"], t["alt"], v.get("manzil", ""), "(min-width: 1200px) 760px, (min-width: 960px) 62vw, 92vw",
             v.get("uzun"), v.get("chizma") if chizmali else None, lazy, high, vtn)
    tl = tel(v["tel"], t.get("tel_alt", ""), "(min-width: 960px) 200px, 30vw", True, cls="tel--yon") if v.get("tel") else ""
    return f'<div class="kompozitsiya">{k}{tl}</div>'


def sahifa(til, title, desc, url_yol, boshqa_yol, body, preload_img=None):
    u = U[til]
    ld = ""
    if url_yol in ("/", "/en/"):
        ld = '<script type="application/ld+json">' + json.dumps({
            "@context": "https://schema.org", "@type": "Person", "name": "Muhammadabdulloh Tojiddinov",
            "url": SAYT + url_yol, "jobTitle": "Software developer", "sameAs": [TG, GITHUB]}, ensure_ascii=False) + "</script>\n"
    alt_uz = url_yol if til == "uz" else boshqa_yol
    alt_en = url_yol if til == "en" else boshqa_yol
    return f"""<!doctype html>
<html lang="{til}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src 'self' data:; media-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' '{JS_XESH}'; font-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="theme-color" content="#eceeea">
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
<link rel="preload" href="{ver('/unbounded.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{ver('/onest.woff2')}" as="font" type="font/woff2" crossorigin>
<style>{CSS}</style>
{ld}</head>
<body>
<a class="skip" href="#asosiy">{e(u['skip'])}</a>
<div class="progress" aria-hidden="true"></div>
<header class="tepa"><div class="wrap">
  <a class="nom" href="{yol(til)}"><span class="belgi" aria-hidden="true">MT</span><span class="nom__matn">Muhammadabdulloh<span class="familiya"> Tojiddinov</span></span></a>
  <nav aria-label="{e(u['menyu'])}">
    <a href="{yol(til)}#ishlar">{e(u['ishlar'])}</a>
    <a href="{yol(til)}#aloqa">{e(u['aloqa'])}</a>
    <a href="{boshqa_yol}" hreflang="{u['til_kod']}" lang="{u['til_kod']}" aria-label="{u['til_qisqa']}, {e(u['til'])}">{u['til_qisqa']}</a>
  </nav>
</div></header>
<main id="asosiy">
{body}
</main>
<footer class="pastki"><div class="wrap"><span>© 2026 Muhammadabdulloh Tojiddinov</span>
<nav aria-label="{e(u['havolalar'])}"><a href="{TG}">Telegram</a><a href="{GITHUB}">GitHub</a><a href="{MANBA}">{e(u['manba'])}</a></nav></div></footer>
<script>{JS}</script>
</body>
</html>
"""


def ish_karta(til, p, i):
    """Bosh sahifadagi bitta ish: kompozitsiya + muammo/yechim/natija."""
    u, t = U[til], p[til]
    tur = t["tur"] + (f", {u['konsept'].lower()}" if p.get("konsept") else "")  # konsept — halol belgi
    myn = "".join(f"<div><dt>{e(n)}</dt><dd>{e(m)}</dd></div>" for n, m in zip(u["myn"], t["qisqa"]))
    havola = ""
    if p.get("havola"):
        havola = f'<a class="tashqi-havola" href="{p["havola"][0]}">{e(p["havola"][1])}{TASHQI}</a>'
    return f"""<article class="ish{' ish--teskari' if i % 2 else ''}" aria-labelledby="ish-{p['slug']}">
  <a class="ish__vizual" href="{yol(til, p['slug'])}" tabindex="-1" aria-hidden="true">{vizual(p, til)}</a>
  <div class="ish__matn">
    <p class="ish__tur"><span>{p['boshi'][0]}</span>{e(tur)}</p>
    <h3 id="ish-{p['slug']}"><a href="{yol(til, p['slug'])}">{e(t['nom'])}</a></h3>
    <dl class="myn">{myn}</dl>
    <p class="ish__havolalar"><a class="btn btn--chiziq" href="{yol(til, p['slug'])}">{e(u['batafsil'])}<span class="sr"> — {e(t['nom'])}</span></a>{havola}</p>
  </div>
</article>"""


def yana_kartalar(til, slugs):
    out = []
    for p in LOYIHALAR:
        if p["slug"] not in slugs:
            continue
        t = p[til]
        v = p["vizual"]
        n = v["tellar"][0] if "tellar" in v else v["kom"]
        cls = "yana__rasm yana__rasm--tel" if "tellar" in v else "yana__rasm"
        out.append(f'<li><a href="{yol(til, p["slug"])}"><div class="{cls}">{picture(n, t["alt"], "(min-width: 960px) 360px, 80vw")}</div>'
                   f'<span class="yana__nom">{e(t["nom"])}</span><span class="yana__tur">{e(t["tur"])}, {p["boshi"][0]}</span></a></li>')
    return "".join(out)


def bosh(til):
    u = U[til]
    tanlangan = [p for p in LOYIHALAR if p.get("bosh")]
    ishlar = "\n".join(ish_karta(til, p, i) for i, p in enumerate(tanlangan))
    qadamlar = "".join(
        f'<li><svg viewBox="0 0 120 92" aria-hidden="true">{re.sub(r"<(path|rect|circle) ", r'<\1 pathLength="1" ', s)}</svg><h3>{e(n)}</h3><p>{e(m)}</p></li>'
        for (n, m), s in zip(u["qadamlar"], QADAM_SVG))
    qatorlar = []
    for b in BOSHQA:
        nom, izoh = b[til]
        qatorlar.append(f'<li><span class="sana">{e(sana(til, b["sana"]))}</span><a href="{b["url"]}">{e(nom)}</a><span>{e(izoh)}</span></li>')
    crm = LOYIHALAR[0]
    k1, k2 = u["kliplar"]
    body = f"""<section class="kirish" aria-labelledby="h1">
  <div class="wrap">
    <h1 id="h1">{e(u['h1'])}</h1>
    <div class="kirish__past">
      <p>{e(u['kirish'])}</p>
      <div class="amallar"><a class="btn" href="{TG}">{TG_ICON}{e(u['tg'])}</a><a class="btn btn--chiziq" href="#ishlar">{e(u['korish'])}</a></div>
    </div>
  </div>
  <div class="wrap stol">
    <div class="stol__olcham stol__olcham--x" aria-hidden="true"><span>1440</span></div>
    {oyna("crm-bosh", crm[til]["alt"], "hamkorcrm.uz", "(min-width: 1200px) 860px, 88vw", lazy=False, high=True)}
    <div class="stol__tel">
      <div class="stol__olcham stol__olcham--y" aria-hidden="true"><span>844</span></div>
      {tel("mobil-bosh", crm[til]["tel_alt"], "(min-width: 960px) 220px, 34vw", lazy=False, chz="chizma-mobil", cls="tel--stol")}
    </div>
    <p class="stol__belgi"><span class="nuqta" aria-hidden="true"></span>hamkorcrm.uz, {e(u['jonli'])}</p>
  </div>
</section>
<section class="bolim ishlar" id="ishlar" aria-labelledby="ishlar-h">
  <div class="wrap bolim__bosh"><h2 id="ishlar-h">{e(u['ishlar_h'])}</h2><p>{e(u['ishlar_p'])}</p></div>
  <div class="wrap ishlar__royxat">
{ishlar}
  </div>
</section>
<section class="bolim jarayon" aria-labelledby="jarayon-h">
  <div class="wrap bolim__bosh"><h2 id="jarayon-h">{e(u['jarayon_h'])}</h2><p>{e(u['jarayon_p'])}</p></div>
  <div class="wrap"><ol class="qadamlar">{qadamlar}</ol></div>
</section>
<section class="bolim video" aria-labelledby="video-h">
  <div class="wrap bolim__bosh"><h2 id="video-h">{e(u['video_h'])}</h2><p>{e(u['video_p'])}</p></div>
  <div class="wrap kliplar">
    {klip(til, "/media/veo-tovuq.mp4", "/img/veo-kadr-800.webp", k1)}
    {klip(til, "/media/promix-oqim.mp4", "/img/promix-kadr-800.webp", k2)}
  </div>
</section>
<section class="bolim yana" aria-labelledby="yana-h">
  <div class="wrap bolim__bosh"><h2 id="yana-h">{e(u['yana_h'])}</h2></div>
  <div class="wrap">
    <ul class="yana__kartalar">{yana_kartalar(til, ("mijozlar-ilovasi", "kino-tv", "shuxrat-ogli"))}</ul>
    <ul class="royxat">{''.join(qatorlar)}</ul>
  </div>
</section>
{aloqa(til)}"""
    boshqa_til = "en" if til == "uz" else "uz"
    return sahifa(til, u["title"], u["desc"], yol(til), yol(boshqa_til), body)


def aloqa(til):
    u = U[til]
    return f"""<section class="bolim aloqa" id="aloqa" aria-labelledby="aloqa-h">
  <div class="wrap">
    <h2 id="aloqa-h">{e(u['aloqa_h'])}</h2>
    <p>{e(u['aloqa_p'])}</p>
    <div class="aloqa__qator"><a class="dastak" href="{TG}">@m_tojiddinov7</a>
    <button class="nusxa" type="button" data-nusxa="@m_tojiddinov7" data-ok="{e(u['nusxa_ok'])}" data-xato="{e(u['nusxa_xato'])}" aria-describedby="nusxa-holat">{e(u['nusxa'])}</button>
    <span id="nusxa-holat" class="sr" role="status"></span></div>
    <div class="amallar"><a class="btn btn--katta" href="{TG}">{TG_ICON}{e(u['tg'])}</a></div>
  </div>
</section>"""


def klip(til, src, poster, izoh):
    u = U[til]
    webm = src.rsplit(".", 1)[0] + ".webm"
    av1 = f' data-av1="{ver(webm)}"' if os.path.exists(os.path.join(ROOT, webm.lstrip("/"))) else ""
    return (f'<figure class="klip"><div class="klip__ramka"><video muted loop playsinline preload="none" poster="{ver(poster)}" width="960" height="540" '
            f'style="background-image: url({lqip(poster)})" data-src="{ver(src)}"{av1} aria-label="{e(izoh)}"></video>'
            f'<button class="pauza" type="button" hidden data-pauza="{e(u["pauza"])}" data-davom="{e(u["davom"])}" aria-label="{e(u["davom"])}"></button></div>'
            f'<figcaption>{e(izoh)}</figcaption></figure>')


def blok(til, b):
    k = b[0]
    if k == "h":
        return f"<h2>{e(b[1])}</h2>"
    if k == "p":
        return f"<p>{e(b[1])}</p>"
    if k == "ul":
        return "<ul>" + "".join(f"<li>{e(x)}</li>" for x in b[1]) + "</ul>"
    if k == "rasm":
        return (f'<figure class="keng"><div class="ramka">{picture(b[1], b[2], "(min-width: 1200px) 1120px, 100vw")}</div>'
                f"<figcaption>{e(b[2])}</figcaption></figure>")
    if k == "tel":
        ich = "".join(f'<figure>{tel(n, c, "(min-width: 760px) 240px, 45vw")}<figcaption>{e(c)}</figcaption></figure>' for n, c in b[1])
        return f'<div class="telefonlar keng">{ich}</div>'
    if k == "butun":
        return (f'<figure class="keng"><div class="ramka sahifa-butun" tabindex="0" role="region" aria-label="{e(b[2])}">'
                f'{picture(b[1], b[2], "(min-width: 1200px) 1100px, 100vw")}</div><figcaption>{e(b[2])}</figcaption></figure>')
    if k == "video":
        return klip(til, "/media/veo-tovuq.mp4", "/img/veo-kadr-800.webp", b[1]).replace('class="klip"', 'class="klip keng"', 1)
    if k == "video2":
        return klip(til, "/media/promix-oqim.mp4", "/img/promix-kadr-800.webp", b[1]).replace('class="klip"', 'class="klip keng"', 1)
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
  <h1>{e(t['nom'])}</h1><p class="lid">{e(t['lid'])}</p>
  <dl class="meta">{meta}</dl>
</header>
<div class="wrap bosh-kadr">{vizual(p, til, lazy=False, high=True, chizmali=False)}</div>
<div class="wrap maqola">{''.join(qism)}</div>
<nav class="wrap keyingi" aria-label="{e(u['keyingi'])}"><p class="keyingi__yorliq">{e(u['keyingi'])}</p>
  <a href="{yol(til, nxt['slug'])}"><div><h2>{e(nt['nom'])}</h2><p>{e(nt['tur'])}</p></div>{vizual(nxt, til, chizmali=False)}</a>
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


def yoq():
    u = U["uz"]
    body = f"""<section class="wrap yoq" aria-labelledby="h1">
  <div class="yoq-kod" aria-hidden="true">404</div>
  <h1 id="h1">{e(u['yoq_t'])}</h1><p>{e(u['yoq_p'])}</p>
  <div class="amallar"><a class="btn" href="/">{e(u['bosh_sahifa'])}</a><a class="btn btn--chiziq" href="/en/" lang="en">English</a></div>
</section>
<section class="bolim yana" aria-label="{e(u['ishlar_h'])}"><div class="wrap">
  <ul class="yana__kartalar">{yana_kartalar("uz", ("hamkor-crm", "hamkor-savdo", "oltinkol"))}</ul></div></section>"""
    h = sahifa("uz", u["yoq_t"] + " — Muhammadabdulloh Tojiddinov", u["yoq_p"], "/404.html", "/en/", body)
    return h.replace('<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"', 1)


if __name__ == "__main__":
    fayllar = []
    for til in ("uz", "en"):
        pre = "" if til == "uz" else "en/"
        fayllar.append(yoz(f"{pre}index.html", bosh(til)))
        for i, p in enumerate(LOYIHALAR):
            fayllar.append(yoz(f"{pre}ishlar/{p['slug']}/index.html", loyiha(til, i)))
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
