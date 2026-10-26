(() => {
  const d = document;
  const kam = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Telegram manzilini nusxa olish
  d.querySelectorAll("[data-nusxa]").forEach((b) => {
    const asl = b.textContent, holat = d.getElementById(b.getAttribute("aria-describedby"));
    b.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(b.dataset.nusxa);
        b.textContent = b.dataset.ok; b.dataset.holat = "ok";
        if (holat) holat.textContent = b.dataset.ok;
      } catch {
        b.textContent = b.dataset.xato;
      }
      setTimeout(() => { b.textContent = asl; delete b.dataset.holat; if (holat) holat.textContent = ""; }, 2200);
    });
  });

  // Kompyuterda karta kursorga qarab og'adi
  if (!kam && matchMedia("(hover: hover) and (pointer: fine)").matches) {
    d.querySelectorAll(".ish, .keyingi a").forEach((el) => {
      const k = el.querySelector(".kadr");
      if (!k) return;
      el.addEventListener("pointermove", (e) => {
        const r = k.getBoundingClientRect();
        k.style.setProperty("--rx", ((e.clientX - r.left) / r.width * 2 - 1).toFixed(3));
        k.style.setProperty("--ry", ((e.clientY - r.top) / r.height * 2 - 1).toFixed(3));
      });
      el.addEventListener("pointerleave", () => { k.style.removeProperty("--rx"); k.style.removeProperty("--ry"); });
    });
  }

  // Video: ko'ringanda o'ynaydi, tugma bilan to'xtaydi
  const v = d.querySelector("video[data-src]");
  if (!v) return;
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
})();
