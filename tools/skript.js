(() => {
  // Video: ko'ringanda o'ynaydi, tugma bilan to'xtaydi; kam harakat so'ralgan bo'lsa o'zi o'ynamaydi
  const v = document.querySelector("video[data-src]");
  if (!v) return;
  const b = v.parentElement.querySelector(".pauza");
  const kam = matchMedia("(prefers-reduced-motion: reduce)").matches;
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
