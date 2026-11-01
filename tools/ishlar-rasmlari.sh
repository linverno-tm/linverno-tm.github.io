#!/usr/bin/env bash
# Ishlar skrinshotlaridan sayt rasmlarini yasaydi. Manba papkasi: $1 (suratlar.py --ishlar natijasi)
set -e
X="$1"
cd "$(dirname "$0")/.."
python tools/rasm.py rasm "$X/charm-kom.png" charm-kom 1600,960,640
python tools/rasm.py rasm "$X/promix-kom.png" promix-kom 1600,960,640
for k in charm promix ges; do python tools/rasm.py rasm "$X/$k-tel.png" $k-tel 520,390; done
python tools/rasm.py rasm "$X/hamkorsavdo-tel.png" savdo-tel 520,390
python tools/rasm.py rasm "$X/hamkorsavdo-uzun.png" uzun-savdo 1100,640 --max-h 10000
python tools/rasm.py rasm "$X/ges-uzun.png" uzun-ges 1100,640 --max-h 8200
python tools/rasm.py rasm "$X/charm-uzun.png" uzun-charm 1100,640 --max-h 8600
python tools/rasm.py chizma "$X/charm-kom.png" chizma-charm --nisbat 16:10
python tools/rasm.py chizma "$X/promix-kom.png" chizma-promix --nisbat 16:10
python tools/rasm.py chizma "$X/hamkorsavdo-kom.png" chizma-savdo --nisbat 16:10
python tools/rasm.py chizma "$X/ges-kom.png" chizma-ges --nisbat 16:10
