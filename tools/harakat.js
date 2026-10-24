(() => {
  const d = document, html = d.documentElement;
  const kam = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const sichqon = matchMedia("(hover: hover) and (pointer: fine)").matches;

  // Yopishqoq header: scroll qilinganda foni qorayadi
  const tepa = d.querySelector(".tepa");
  const tepaBelgi = () => tepa.classList.toggle("yopishgan", scrollY > 24);
  addEventListener("scroll", tepaBelgi, { passive: true });
  tepaBelgi();

  // Video: ko'ringanda o'ynaydi, tugma bilan to'xtatiladi
  const v = d.querySelector("video[data-src]");
  if (v) {
    const b = v.parentElement.querySelector(".pauza");
    const PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M8 5.5v13l10.5-6.5z"/></svg>';
    const PAUZA = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>';
    let qolda = false, yuklandi = false;
    const yukla = () => { if (!yuklandi) { v.src = v.dataset.src; yuklandi = true; } };
    const ikon = () => {
      b.innerHTML = v.paused ? PLAY : PAUZA;
      b.setAttribute("aria-label", v.paused ? b.dataset.davom : b.dataset.pauza);
    };
    b.hidden = false;
    v.addEventListener("play", ikon); v.addEventListener("pause", ikon); ikon();
    b.addEventListener("click", () => { qolda = true; yukla(); v.paused ? v.play() : v.pause(); });
    if (!kam) new IntersectionObserver(([x]) => {
      if (qolda) return;
      if (x.isIntersecting) { yukla(); v.play().catch(() => {}); } else v.pause();
    }, { rootMargin: "200px 0px" }).observe(v);
  }

  if (kam) return;

  // Ko'ringanda chiqib kelish (CSS: html.harakat ... / .korindi)
  d.querySelectorAll(".bolim-bosh h2").forEach((h) => { h.innerHTML = '<span class="ich">' + h.innerHTML + "</span>"; });
  const SEL = ".bolim-bosh h2, .bolim-bosh > .tagi, .crm-chap > *, .ekranlar figure, .mobil-matn > *, .uch-telefon, " +
    ".mobil-rasmlar figcaption, .mobil-boshqa h3, .royxat li, .ish, .sayt, .media-ishlar figure, .xizmat, .aloqa > *";
  const elar = [...d.querySelectorAll(SEL)];
  const sana = new Map();
  for (const el of elar) {
    const n = sana.get(el.parentElement) || 0;
    sana.set(el.parentElement, n + 1);
    el.style.setProperty("--i", Math.min(n, 6));
  }
  const kuzat = new IntersectionObserver((xs) => {
    for (const x of xs) {
      if (!x.isIntersecting) continue;
      x.target.classList.add("korindi");
      kuzat.unobserve(x.target);
      x.target.querySelectorAll("[data-son]").forEach(sana_);
    }
  }, { rootMargin: "0px 0px -12% 0px", threshold: 0.08 });
  elar.forEach((el) => kuzat.observe(el));

  // Raqamlar sanab chiqadi
  const fmt = new Intl.NumberFormat(html.lang === "uz" ? "ru-RU" : "en-US");
  function sana_(el) {
    const oxir = +el.dataset.son, t0 = performance.now(), dav = 1400;
    const qadam = (t) => {
      const p = Math.min(1, (t - t0) / dav), q = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt.format(Math.round(oxir * q));
      if (p < 1) requestAnimationFrame(qadam);
    };
    requestAnimationFrame(qadam);
  }

  // Birinchi ekran: CRM ekrani scroll bilan tekislanadi, sichqonchaga ergashadi
  const hero = d.querySelector(".hero-rasm");
  let kutish = false;
  const egil = () => {
    kutish = false;
    hero.style.setProperty("--egil", Math.max(0, 1 - scrollY / (innerHeight * 0.65)).toFixed(3));
  };
  addEventListener("scroll", () => { if (!kutish) { kutish = true; requestAnimationFrame(egil); } }, { passive: true });
  egil();

  if (!sichqon) return;
  const heroBolim = d.querySelector(".hero");
  heroBolim.addEventListener("pointermove", (e) => {
    const r = heroBolim.getBoundingClientRect();
    hero.style.setProperty("--px", ((e.clientX - r.left) / r.width * 2 - 1).toFixed(3));
    hero.style.setProperty("--py", ((e.clientY - r.top) / r.height * 2 - 1).toFixed(3));
  });
  heroBolim.addEventListener("pointerleave", () => { hero.style.setProperty("--px", 0); hero.style.setProperty("--py", 0); });

  // Kursor ortidan yorug'lik
  d.querySelectorAll("[data-nur]").forEach((el) => {
    el.addEventListener("pointermove", (e) => {
      const r = el.getBoundingClientRect();
      el.style.setProperty("--mx", e.clientX - r.left + "px");
      el.style.setProperty("--my", e.clientY - r.top + "px");
    });
  });

  // Tugmalar kursorga ozgina tortiladi
  d.querySelectorAll(".btn-asosiy").forEach((el) => {
    el.addEventListener("pointermove", (e) => {
      const r = el.getBoundingClientRect();
      el.style.translate = ((e.clientX - r.left) / r.width - 0.5) * 8 + "px " + ((e.clientY - r.top) / r.height - 0.5) * 6 + "px";
    });
    el.addEventListener("pointerleave", () => { el.style.translate = ""; });
  });
})();
