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

  // Yuklanish holati: idish ustida nur + chiziq (foiz ma'lum bo'lsa — haqiqiy), tayyor bo'lgach so'nadi.
  const yukl = (idish) => {
    if (idish._yukl) return idish._yukl;
    const q = d.createElement("span"), chiziq = d.createElement("i"), raqam = d.createElement("b");
    q.className = "yukl-qatlam"; q.setAttribute("aria-hidden", "true"); q.append(chiziq, raqam);
    if (getComputedStyle(idish).position === "static") idish.style.position = "relative";
    idish.append(q);
    const h = {
      foiz(p) {
        if (h.bitdi || !(p >= 0)) return;
        p = Math.min(1, p); q.classList.add("foizli");
        q.style.setProperty("--p", p.toFixed(3)); raqam.textContent = Math.round(p * 100) + "%";
      },
      tayyor() {
        if (h.bitdi) return; h.bitdi = true; q.classList.add("bitdi");
        setTimeout(() => { q.remove(); idish._yukl = null; }, kam ? 0 : 480);
      },
    };
    return (idish._yukl = h);
  };

  // Rasmlar (skrinshotlar): ekranga yaqinlashganda hali kelmagan bo'lsa — holat, kelgach yo'qoladi.
  const idishi = (i) => i.closest(".oyna__ekran, .tel__ekran, .ramka") || i.parentElement.parentElement;
  const rasmKut = (i) => {
    if (i.complete && i.naturalWidth) return;
    const h = yukl(idishi(i));
    i.addEventListener("load", h.tayyor, { once: true });
    i.addEventListener("error", h.tayyor, { once: true });
    if (i.complete && i.naturalWidth) h.tayyor();
  };
  const rasmlar = [...d.querySelectorAll("main img.lq")].filter((i) => !(i.complete && i.naturalWidth));
  if (rasmlar.length) {
    const io = new IntersectionObserver((es) => es.forEach((x) => {
      if (x.isIntersecting) { io.unobserve(x.target); rasmKut(x.target); }
    }), { rootMargin: "200px 0px" });
    rasmlar.forEach((i) => io.observe(i));
  }

  // Videolar: ko'ringanda o'ynaydi (kam harakat / trafik tejashda — faqat tugma bilan), tugma bilan to'xtaydi.
  // AV1 WebM qo'llasa — o'sha (2–3 barobar yengil), bo'lmasa MP4. Yuklanayotganda foizli chiziq.
  const PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M8 5.5v13l10.5-6.5z"/></svg>';
  const PAUZA = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>';
  d.querySelectorAll("video[data-src]").forEach((v) => {
    const idish = v.parentElement, b = idish.querySelector(".pauza");
    let qolda = false, yuklandi = false;
    const yukla = () => {
      if (yuklandi) return; yuklandi = true;
      const h = yukl(idish);
      const foiz = () => { if (v.duration && v.buffered.length) h.foiz(v.buffered.end(v.buffered.length - 1) / v.duration); };
      v.addEventListener("progress", foiz); v.addEventListener("loadedmetadata", foiz);
      v.addEventListener("playing", h.tayyor, { once: true });
      v.addEventListener("canplaythrough", () => { if (v.paused) h.tayyor(); }, { once: true });
      v.addEventListener("error", h.tayyor, { once: true });
      const av1 = v.dataset.av1 && v.canPlayType('video/webm; codecs="av01.0.05M.08"') === "probably";
      v.src = av1 ? v.dataset.av1 : v.dataset.src;
    };
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
