#!/usr/bin/env bash
# Cloudflare Pages'ga chiqarish: sayt fayllari (tools/, git'siz) + _headers/_redirects → tojiddinov-portfolio.pages.dev
# GitHub Pages (linverno-tm.github.io) asosiy manba bo'lib qoladi; bu — tezroq nusxa.
set -e
cd "$(dirname "$0")/.."
D="${TMPDIR:-/tmp}/portfolio-cf"
rm -rf "$D"; mkdir -p "$D"
cp -r index.html 404.html en ishlar img media favicon.svg apple-touch-icon.png og.png robots.txt sitemap.xml *.woff2 OFL-*.txt "$D"/
cp tools/cloudflare/_headers tools/cloudflare/_redirects "$D"/
npx -y wrangler@4 pages deploy "$D" --project-name tojiddinov-portfolio --branch main --commit-dirty=true
