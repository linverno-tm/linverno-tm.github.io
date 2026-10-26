(() => {
  const d = document, html = d.documentElement;
  const kam = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const sichqon = matchMedia("(hover: hover) and (pointer: fine)").matches;

  // Tepa panel scroll qilinganda qorayadi
  const tepa = d.querySelector(".tepa");
  const belgila = () => tepa.classList.toggle("yopishgan", scrollY > 16);
  addEventListener("scroll", belgila, { passive: true });
  belgila();

  // Loyiha oynalari: tugma, plitkani bosish, Esc, fon
  const och = (id) => { const o = d.getElementById(id); if (o && !o.open) o.showModal(); };
  d.querySelectorAll("[data-oyna]").forEach((el) => {
    el.addEventListener("click", (e) => {
      if (e.target.closest("a, video, .pauza")) return;
      och(el.dataset.oyna);
    });
  });
  d.querySelectorAll("dialog.oyna").forEach((o) => {
    o.querySelector(".yop").addEventListener("click", () => o.close());
    o.addEventListener("click", (e) => { if (e.target === o) o.close(); });
  });
  if (location.hash.startsWith("#ish-")) och("oyna-" + location.hash.slice(5));

  // Video: ko'ringanda o'ynaydi, tugma bilan to'xtaydi
  const v = d.querySelector("video[data-src]");
  if (v) {
    const b = v.parentElement.querySelector(".pauza");
    const PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M8 5.5v13l10.5-6.5z"/></svg>';
    const PAUZA = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>';
    let qolda = false, yuklandi = false;
    const yukla = () => { if (!yuklandi) { v.src = v.dataset.src; yuklandi = true; } };
    const ikon = () => { b.innerHTML = v.paused ? PLAY : PAUZA; b.setAttribute("aria-label", v.paused ? b.dataset.davom : b.dataset.pauza); };
    b.hidden = false;
    v.addEventListener("play", ikon); v.addEventListener("pause", ikon); ikon();
    b.addEventListener("click", () => { qolda = true; yukla(); v.paused ? v.play() : v.pause(); });
    if (!kam) new IntersectionObserver(([x]) => {
      if (qolda) return;
      if (x.isIntersecting) { yukla(); v.play().catch(() => {}); } else v.pause();
    }, { rootMargin: "200px 0px" }).observe(v);
  }

  if (kam) return;

  // Plitkalar ketma-ket chiqadi
  d.querySelectorAll(".bento").forEach((g) => [...g.children].forEach((el, i) => el.style.setProperty("--i", i % 6)));
  const fmt = new Intl.NumberFormat(html.lang === "uz" ? "ru-RU" : "en-US");
  const sana = (el) => {
    const oxir = +el.dataset.son, t0 = performance.now();
    const q = (t) => {
      const p = Math.min(1, (t - t0) / 1500);
      el.textContent = fmt.format(Math.round(oxir * (1 - Math.pow(1 - p, 3))));
      if (p < 1) requestAnimationFrame(q);
    };
    requestAnimationFrame(q);
  };
  const kuzat = new IntersectionObserver((xs) => {
    for (const x of xs) {
      if (!x.isIntersecting) continue;
      x.target.classList.add("korindi");
      x.target.querySelectorAll("[data-son]").forEach(sana);
      kuzat.unobserve(x.target);
    }
  }, { rootMargin: "0px 0px -10% 0px", threshold: 0.1 });
  d.querySelectorAll(".plitka, .bolim-sarlavha").forEach((el) => kuzat.observe(el));

  if (!sichqon) return;
  // Kursor ortidan rangli yorug'lik
  d.querySelectorAll(".plitka").forEach((el) => {
    el.addEventListener("pointermove", (e) => {
      const r = el.getBoundingClientRect();
      el.style.setProperty("--mx", e.clientX - r.left + "px");
      el.style.setProperty("--my", e.clientY - r.top + "px");
    });
  });
  // Oq tugma kursorga ozgina tortiladi
  d.querySelectorAll(".btn-oq").forEach((el) => {
    el.addEventListener("pointermove", (e) => {
      const r = el.getBoundingClientRect();
      el.style.translate = ((e.clientX - r.left) / r.width - 0.5) * 8 + "px " + ((e.clientY - r.top) / r.height - 0.5) * 6 + "px";
    });
    el.addEventListener("pointerleave", () => { el.style.translate = ""; });
  });
})();
