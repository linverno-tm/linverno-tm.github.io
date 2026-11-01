(() => {
  const d = document;
  const kam = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const tejash = navigator.connection && navigator.connection.saveData;

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

  // Videolar: ko'ringanda o'ynaydi (kam harakat / trafik tejashda — faqat tugma bilan), tugma bilan to'xtaydi
  const PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M8 5.5v13l10.5-6.5z"/></svg>';
  const PAUZA = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>';
  d.querySelectorAll("video[data-src]").forEach((v) => {
    const b = v.parentElement.querySelector(".pauza");
    let qolda = false, yuklandi = false;
    const yukla = () => { if (!yuklandi) { v.src = v.dataset.src; yuklandi = true; } };
    const ikon = () => { b.innerHTML = v.paused ? PLAY : PAUZA; b.setAttribute("aria-label", v.paused ? b.dataset.davom : b.dataset.pauza); };
    b.hidden = false;
    v.addEventListener("play", ikon); v.addEventListener("pause", ikon); ikon();
    b.addEventListener("click", () => { qolda = true; yukla(); v.paused ? v.play().catch(() => {}) : v.pause(); });
    if (kam || tejash) return;
    new IntersectionObserver(([x]) => {
      if (qolda) return;
      if (x.isIntersecting) { yukla(); v.play().catch(() => {}); } else v.pause();
    }, { rootMargin: "120px 0px" }).observe(v);
  });
})();
