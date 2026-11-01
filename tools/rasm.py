"""Rasmlarni sayt uchun tayyorlaydi va tools/rasmlar.json ni yangilaydi.

    python tools/rasm.py rasm   <manba.png> <nom> <kenglik,kenglik> [--nisbat 16:10] [--max-h 5400]
    python tools/rasm.py chizma <manba.png> <nom> [--nisbat 16:10] [--kenglik 1200]

rasm   — AVIF va WebP, berilgan kengliklarda (/img/<nom>-<w>.avif|webp). --nisbat bo'lsa tepadan kesiladi.
chizma — skrinshotdan ko'k qalam chizmasi (qirralar, shaffof fon): /img/<nom>.webp. Bezak qatlami.
"""
import json
import os
import sys

import cv2
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON = os.path.join(ROOT, "tools", "rasmlar.json")
IMG = os.path.join(ROOT, "img")
QALAM = (36, 66, 208)


def opt(nom, default=None):
    if nom in sys.argv:
        return sys.argv[sys.argv.index(nom) + 1]
    return default


def kes(im, nisbat, max_h):
    w, h = im.size
    if nisbat:
        a, b = (int(x) for x in nisbat.split(":"))
        h2 = round(w * b / a)
        if h2 <= h:
            im = im.crop((0, 0, w, h2))
    if max_h and im.size[1] > int(max_h):
        im = im.crop((0, 0, w, int(max_h)))
    return im


def yoz_json(nom, w, h, widths=None):
    d = json.load(open(JSON, encoding="utf-8")) if os.path.exists(JSON) else {}
    d[nom] = {"w": w, "h": h, **({"widths": widths} if widths else {})}
    json.dump(d, open(JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def rasm(manba, nom, widths):
    im = Image.open(manba).convert("RGB")
    im = kes(im, opt("--nisbat"), opt("--max-h"))
    w, h = im.size
    for kw in widths:
        kw = min(kw, w)
        r = im.resize((kw, round(h * kw / w)), Image.LANCZOS)
        r.save(os.path.join(IMG, f"{nom}-{kw}.webp"), "WEBP", quality=78, method=6)
        r.save(os.path.join(IMG, f"{nom}-{kw}.avif"), "AVIF", quality=58, speed=4)
    yoz_json(nom, w, h, sorted({min(k, w) for k in widths}, reverse=True))
    print(nom, w, h, widths)


def chizma(manba, nom):
    im = Image.open(manba).convert("RGB")
    im = kes(im, opt("--nisbat"), None)
    kw = int(opt("--kenglik", 1200))
    w, h = im.size
    im = im.resize((kw, round(h * kw / w)), Image.LANCZOS)
    g = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY)
    g = cv2.GaussianBlur(g, (3, 3), 0)
    q = cv2.Canny(g, 40, 120)
    q = cv2.dilate(q, np.ones((2, 2), np.uint8), iterations=1)
    H, W = q.shape
    # 24 px to'r (kalka qog'ozidagidek), juda xira
    tor = np.zeros_like(q)
    tor[::24, :] = 1
    tor[:, ::24] = 1
    a = np.where(q > 0, 235, np.where(tor > 0, 34, 0)).astype(np.uint8)
    rgba = np.dstack([np.full((H, W), c, np.uint8) for c in QALAM] + [a])
    Image.fromarray(rgba, "RGBA").save(os.path.join(IMG, f"{nom}.webp"), "WEBP", quality=70, method=6, alpha_quality=60)
    yoz_json(nom, W, H)
    print(nom, W, H, os.path.getsize(os.path.join(IMG, f"{nom}.webp")))


if __name__ == "__main__":
    ish, manba, nom = sys.argv[1], sys.argv[2], sys.argv[3]
    if ish == "rasm":
        rasm(manba, nom, [int(x) for x in sys.argv[4].split(",")])
    elif ish == "chizma":
        chizma(manba, nom)
