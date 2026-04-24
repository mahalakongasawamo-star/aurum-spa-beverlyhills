"""
Convert all PNG images to WebP (quality 82) and update index.html references.
Also patches image loading attributes and adds preload hint for hero.
"""
import os, re, glob
from PIL import Image

BASE = "D:/Claude/3kimbrandesign"

# ── 1. Convert all PNGs to WebP ──────────────────────────────────────────────
pngs = (
    glob.glob(f"{BASE}/images/*.png") +
    glob.glob(f"{BASE}/images/services/*.png")
)

savings = 0
converted = 0
skipped = 0

for png_path in sorted(pngs):
    webp_path = png_path[:-4] + ".webp"
    png_size = os.path.getsize(png_path)

    if os.path.exists(webp_path):
        webp_size = os.path.getsize(webp_path)
        saved = png_size - webp_size
        savings += saved
        skipped += 1
        print(f"  SKIP (exists) {os.path.basename(png_path)} -> {webp_size//1024}KB (saved {saved//1024}KB)")
        continue

    try:
        img = Image.open(png_path)
        # Preserve RGBA for logo; use RGB for photos
        if img.mode in ("RGBA", "LA") and "logo" in png_path.lower():
            img.save(webp_path, "WEBP", quality=90, method=6, lossless=False)
        else:
            if img.mode in ("RGBA", "LA", "P"):
                img = img.convert("RGB")
            img.save(webp_path, "WEBP", quality=82, method=6)

        webp_size = os.path.getsize(webp_path)
        saved = png_size - webp_size
        savings += saved
        converted += 1
        print(f"  {os.path.basename(png_path):45s} {png_size//1024:>5}KB -> {webp_size//1024:>4}KB  (-{saved//1024}KB)")
    except Exception as e:
        print(f"  ERROR {png_path}: {e}")

print(f"\nConverted: {converted}  Skipped (already exist): {skipped}")
print(f"Total savings: {savings//1024} KB  ({savings//1024//1024} MB)")

# ── 2. Update index.html ──────────────────────────────────────────────────────
html_path = f"{BASE}/index.html"
content = open(html_path, encoding="utf-8").read()
original = content

# 2a. Replace all .png -> .webp in src= and srcset= for images/... paths
#     (only our local images, not favicon or other assets)
content = re.sub(
    r'((?:src|srcset)=")(images/[^"]+)\.png(")',
    lambda m: m.group(1) + m.group(2) + ".webp" + m.group(3),
    content
)

# 2b. Also fix CSS background-image url() references if any
content = re.sub(
    r"(url\(['\"]?)(images/[^'\")\s]+)\.png(['\"]?\))",
    lambda m: m.group(1) + m.group(2) + ".webp" + m.group(3),
    content
)

# 2c. Add loading="lazy" where missing on non-hero images
#     Hero image: hero2.webp gets fetchpriority="high" loading="eager"
def patch_img(m):
    tag = m.group()
    src_m = re.search(r'src="([^"]*)"', tag)
    if not src_m:
        return tag
    src = src_m.group(1)

    is_hero = "hero2" in src
    is_logo = "logo-aurum" in src

    # fetchpriority
    if is_hero:
        if 'fetchpriority' not in tag:
            tag = tag.rstrip('>').rstrip('/') + ' fetchpriority="high">'
        tag = re.sub(r'fetchpriority="[^"]*"', 'fetchpriority="high"', tag)
        tag = re.sub(r'loading="[^"]*"', 'loading="eager"', tag)
    else:
        if 'loading=' not in tag:
            tag = tag.rstrip('>').rstrip('/') + ' loading="lazy">'
        elif 'loading="auto"' in tag or 'loading="none"' in tag:
            tag = re.sub(r'loading="[^"]*"', 'loading="lazy"', tag)
        if 'fetchpriority="high"' in tag and not is_hero:
            tag = re.sub(r'fetchpriority="high"', 'fetchpriority="auto"', tag)

    # decoding="async" everywhere
    if 'decoding=' not in tag:
        tag = tag.rstrip('>').rstrip('/') + ' decoding="async">'

    return tag

content = re.sub(r'<img [^>]+>', patch_img, content)

# 2d. Add <link rel="preload"> for hero image right after the CSS preload
HERO_PRELOAD = '<link rel="preload" as="image" href="images/hero2.webp" fetchpriority="high">'
CSS_LINK = '<link rel="stylesheet" href="_astro/index.DsvAy34u.css">'
if HERO_PRELOAD not in content:
    content = content.replace(CSS_LINK, HERO_PRELOAD + "\n  " + CSS_LINK, 1)
    print("  Hero preload link added")

# 2e. Defer non-critical module scripts that can load after page is interactive
#     Layout.js is the heaviest (17KB) — already type="module" (deferred)
#     Add explicit defer to the inline contact snackbar script
content = content.replace(
    '<script type="module">document.addEventListener',
    '<script type="module" defer>document.addEventListener',
    1
)

replacements = content.count(".webp") - original.count(".webp")
print(f"\n  .png -> .webp replacements in HTML: {replacements}")
open(html_path, "w", encoding="utf-8").write(content)
print("  index.html updated")
print("\nDone.")
