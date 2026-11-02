# Muhammadabdulloh Tojiddinov — portfolio

Shaxsiy sayt: https://linverno-tm.github.io/ (o‘zbekcha) va https://linverno-tm.github.io/en/ (inglizcha).

G‘oya: **chizmadan jonli ekranga.** Har ish skrinshoti avval ko‘k qalam chizmasi bo‘lib turadi va skroll bilan
haqiqiy ekranga aylanadi. Och kalka qog‘ozi, ko‘k qalam, siyoh; Unbounded (sarlavha) + Onest (matn).

- Freymvorksiz statik sayt: bosh sahifa va har loyiha uchun alohida sahifa (`/ishlar/<loyiha>/`).
- Harakat faqat CSS (scroll-driven animations, view transitions); qo‘llamaydigan brauzer va
  `prefers-reduced-motion` da oxirgi holat darhol ko‘rinadi. Matn va asosiy rasm hech qachon yashirin boshlanmaydi.
- Shriftlar (SIL Open Font License) lotin belgilarigacha kichraytirilgan: `onest.woff2`, `unbounded.woff2`.
- Hamkor CRM va mijozlar ilovasi ekranlari demo bazadan olingan: ismlar, raqamlar va summalar yopilgan.

Matnni o‘zgartirish: `tools/build.py` → `python tools/build.py`. Uslub: `tools/uslub.css`, skript: `tools/skript.js`.

Rasmlar: `tools/rasm.py` (AVIF/WebP o‘lchamlari va ko‘k chizma qatlami), ishlar skrinshotlaridan hammasini yasash —
`bash tools/ishlar-rasmlari.sh <skrinshotlar papkasi>`.

## Cloudflare nusxasi

`bash tools/cloudflare.sh` — sayt fayllarini `tojiddinov-portfolio.pages.dev` ga chiqaradi (`tools/cloudflare/_headers`: rasm/video/shrift 1 yil `immutable`, manzillarda `?v=<xesh>`; `_redirects`: `/promix-uz/` va boshqa alohida repo'lar GitHub Pages'ga). Videolar AV1 WebM (+ MP4 zaxira): `ffmpeg -c:v libaom-av1 -crf 38`.
