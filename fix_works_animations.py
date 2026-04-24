"""
Fix works section:
1. Add missing Work.astro scroll-animation script
2. Restore 'Discover more' span + 'Ask Aurum' em in works__more
3. Make logo circle border 0.5px thinner (remove solid border, use box-shadow ring)
"""
import re

content = open("D:/Claude/3kimbrandesign/index.html", encoding="utf-8").read()

# ── 1. Restore works__more with Discover more + Ask Aurum ────────────────────
OLD_MORE = content[content.find('class="works__more'):content.find('</section>', content.find('class="works__more')) - 50]

NEW_MORE = '''<div class="works__more grid" data-astro-cid-n5ebmdgj>
  <span pos="11+4" pos-m="5+4" pos-s="3+8" data-astro-cid-n5ebmdgj>Discover more</span>
  <a pos="11+4" pos-m="5+4" pos-s="3+8" href="mailto:hello@aurumspaBH.com" data-astro-cid-n5ebmdgj>
    <img src="images/logo-aurum.png" alt="Aurum Spa &amp; Aesthetics"
      data-astro-cid-n5ebmdgj="true"
      loading="lazy" decoding="async"
      style="display:block;width:220px;height:220px;border-radius:50%;object-fit:cover;object-position:center;margin:0 auto;">
    <em data-astro-cid-n5ebmdgj>Ask Aurum</em>
  </a>
</div>'''

# Find exact start/end of works__more div
more_start = content.find('<div class="works__more')
if more_start == -1:
    print("ERROR: works__more not found")
else:
    # Find its closing </div>
    depth = 0
    pos = more_start
    more_end = -1
    while pos < len(content):
        o = content.find('<div', pos + 1)
        c = content.find('</div>', pos)
        if c == -1:
            break
        if o != -1 and o < c:
            depth += 1
            pos = o
        else:
            if depth == 0:
                more_end = c + len('</div>')
                break
            depth -= 1
            pos = c + 1

    print(f"works__more: {more_start} to {more_end}")
    content = content[:more_start] + NEW_MORE + content[more_end:]
    print("  works__more replaced with Discover more + Ask Aurum")

# ── 2. Add Work.astro scroll script before Works.astro script ─────────────────
WORK_SCRIPT = '<script type="module" src="_astro/Work.astro_astro_type_script_index_0_lang.C00Wt-TI.js"></script>'
WORKS_SCRIPT = '<script type="module" src="_astro/Works.astro_astro_type_script_index_0_lang.uzYmAIDQ.js"></script>'

if WORK_SCRIPT not in content:
    content = content.replace(WORKS_SCRIPT, WORK_SCRIPT + ' ' + WORKS_SCRIPT, 1)
    print("  Work.astro scroll script added")
else:
    print("  Work.astro script already present")

# ── 3. Thin the logo circle border via CSS (box-shadow instead of solid border) ──
# Update aurum-logo-circle style block
OLD_LOGO_CSS = '''.works__more[data-astro-cid-n5ebmdgj] a[data-astro-cid-n5ebmdgj] img[data-astro-cid-n5ebmdgj] {
  object-fit: contain !important;
  background-color: #0f0f0f;
  padding: 1rem;
}'''
NEW_LOGO_CSS = '''.works__more[data-astro-cid-n5ebmdgj] a[data-astro-cid-n5ebmdgj] img[data-astro-cid-n5ebmdgj] {
  object-fit: cover !important;
  box-shadow: 0 0 0 0.5px rgba(201,169,110,0.55);
}'''

if OLD_LOGO_CSS in content:
    content = content.replace(OLD_LOGO_CSS, NEW_LOGO_CSS, 1)
    print("  Logo circle border thinned to 0.5px box-shadow ring")
else:
    print("  WARNING: aurum-logo-circle CSS not found exactly — check manually")

open("D:/Claude/3kimbrandesign/index.html", "w", encoding="utf-8").write(content)
print("\nDone.")
