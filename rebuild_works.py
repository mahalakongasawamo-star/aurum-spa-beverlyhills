"""
Rebuild the corrupted works section from scratch:
- Pulls clean kim-work HTML structure from themenectar/index.html (original backup)
- Applies Aurum headings, tags, and 4-5 image pools
- Reconstructs the Ask Aurum footer
- Replaces the entire works section in index.html
"""
import re

# ── Load files ────────────────────────────────────────────────────────────────
content  = open("D:/Claude/3kimbrandesign/index.html", encoding="utf-8").read()
original = open("D:/Claude/3kimbrandesign/themenectar/index.html", encoding="utf-8").read()

P = "images/services/"

# ── Service data (headings, tags, 4-5 image pools) ───────────────────────────
SERVICES = [
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Botox &amp; Neurotoxins</strong> Expertly placed neuromodulators that smooth, refine, and prevent — without erasing what makes you distinctly you.",
        "tags": ["#botox", "#neurotoxin", "#injectables", "#antiaging", "#refinement"],
        "images": [P+"Botox_001.png", P+"SRV_Botox_001.png", P+"SRV_Botox_002.png",
                   P+"SRV_Botox_003.png", P+"SRV_Botox_004.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Dermal Fillers</strong> Restore volume, define architecture, and balance your proportions with premium hyaluronic acid fillers.",
        "tags": ["#fillers", "#volumization", "#lipfillers", "#jawline", "#youthful"],
        "images": [P+"DermalFillers_001.png", P+"LipFIllers_001.png",
                   P+"ChinJawline_001.png", P+"SRV_Dermal_001.png", P+"SRV_Dermal_002.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Laser Skin Resurfacing</strong> Medical-grade laser treatments targeting uneven tone, sun damage, fine lines, and textural concerns.",
        "tags": ["#laser", "#resurfacing", "#skintone", "#rejuvenation", "#precision"],
        "images": [P+"LaserHairRemoval_001.png", P+"IPL_001.png",
                   P+"PigmentRemoval_001.png", P+"SRV_Laser_001.png", P+"SRV_Laser_002.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Microneedling &amp; PRP</strong> A powerful regenerative treatment that stimulates collagen and restores a luminous, youthful complexion.",
        "tags": ["#microneedling", "#PRP", "#collagen", "#regenerative", "#glow"],
        "images": [P+"MicroneedlingWithPRP_001.png", P+"MicroNeedling_001.png",
                   P+"PRPFacial_001.png", P+"SRV_MicroNeedling_001.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Hydrafacial MD</strong> The globally recognized gold standard of facial cleansing — zero redness, zero downtime, immediate radiance.",
        "tags": ["#hydrafacial", "#deepcleanse", "#hydration", "#glow", "#nodowntime"],
        "images": [P+"HydraFacial_001.png", P+"SRV_Dermal_003.png",
                   P+"SRV_Laser_003.png", P+"SRV_Dermal_004.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Chemical Peels</strong> Custom-blended medical peels clinician-supervised for maximum efficacy across all skin tones and types.",
        "tags": ["#chemicalpeel", "#brightening", "#resurfacing", "#clarity", "#medical"],
        "images": [P+"ChemicalPeel_001.png", P+"SRV_Laser_004.png",
                   P+"SRV_Laser_005.png", P+"SRV_Dermal_005.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Dysport &amp; IPL</strong> Advanced neuromodulator and intense pulsed light treatments for refined, lasting skin clarity.",
        "tags": ["#dysport", "#IPL", "#skinclarity", "#photofacial", "#advanced"],
        "images": [P+"Dysport_001.png", P+"SRV_Botox_005.png",
                   P+"IPL_001.png", P+"SRV_Botox_004.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Precision Treatments</strong> Tailored aesthetic protocols designed around your unique anatomy, skin, and personal vision of beauty.",
        "tags": ["#precision", "#bespoke", "#aesthetics", "#skincare", "#gold"],
        "images": [P+"PrecisionTreatments_001.png", P+"SRV_Dermal_002.png",
                   P+"SRV_Laser_002.png", P+"SRV_Botox_003.png"],
    },
]

# ── Extract original 8 kim-work items from backup ────────────────────────────
orig_works_idx = original.find('id="works"')
orig_works_end = original.find('</section>', orig_works_idx)
orig_works_html = original[orig_works_idx:orig_works_end]
orig_items = list(re.finditer(r'<kim-work[^>]*>.*?</kim-work>', orig_works_html, re.DOTALL))
print(f"Backup has {len(orig_items)} kim-work items")

# ── Build new kim-work items by modifying originals ──────────────────────────
new_items = []
for i, (orig_match, svc) in enumerate(zip(orig_items, SERVICES)):
    item = orig_match.group()

    # Replace all img src with service images (cycling through pool)
    pool = svc["images"]
    imgs = list(re.finditer(r'<img [^>]*data-astro-cid-wkx7uqji[^>]*>', item))
    for j, img_m in enumerate(imgs):
        old_img = img_m.group()
        new_src = pool[j % len(pool)]
        new_img = re.sub(r'src="[^"]*"', f'src="{new_src}"', old_img)
        new_img = re.sub(r'srcset="[^"]*"', '', new_img)
        new_img = new_img.replace('--fit: contain;', '--fit: cover;')
        item = item.replace(old_img, new_img, 1)

    # Replace h3 heading
    item = re.sub(
        r'<h3[^>]*>.*?</h3>',
        f'<h3 pos="5+5" pos-m="7+5" pos-s="6.." data-astro-cid-wkx7uqji>{svc["heading"]}</h3>',
        item, flags=re.DOTALL
    )

    # Replace tags
    tags_html = "".join(f'<li data-astro-cid-wkx7uqji>{t}</li>' for t in svc["tags"])
    item = re.sub(
        r'<ul data-astro-cid-wkx7uqji>.*?</ul>',
        f'<ul data-astro-cid-wkx7uqji>{tags_html}</ul>',
        item, flags=re.DOTALL
    )

    new_items.append(item)
    print(f"  Item {i+1}: {len(pool)} imgs cycling — {svc['heading'][:40]}...")

# ── Extract works section header (h2 + decos) from backup ────────────────────
backup_works_section = orig_works_html
# h2
h2_match = re.search(r'<h2[^>]*>.*?</h2>', backup_works_section, re.DOTALL)
h2 = h2_match.group().replace(
    '>Our work<',  '>Our Services<'
).replace('>Our work<', '>Our Services<')
# Force "Our Services" as the h2 text
h2 = re.sub(r'<h2[^>]*>.*?</h2>',
            '<h2 data-astro-cid-n5ebmdgj>Our Services</h2>',
            h2, flags=re.DOTALL)

# decos div
decos_match = re.search(r'<div class="works__decos"[^>]*>.*?</div>(?=\s*<div)', backup_works_section, re.DOTALL)
decos = decos_match.group() if decos_match else ''

# ── Build Ask Aurum footer ────────────────────────────────────────────────────
ask_aurum = """<div class="works__more grid" data-astro-cid-n5ebmdgj>
  <a pos="11+4" pos-m="5+4" pos-s="3+8" href="mailto:hello@aurumspaBH.com" data-astro-cid-n5ebmdgj>
    <img src="images/logo-aurum.png" alt="Aurum Spa &amp; Aesthetics" data-astro-cid-n5ebmdgj="true"
      loading="lazy" decoding="async" style="display:block;width:220px;height:220px;border-radius:50%;object-fit:cover;object-position:center;border:0.5px solid #c9a96e;margin:0 auto;">
    <span data-astro-cid-n5ebmdgj></span>
    <svg viewBox="0 0 420 120" style="width:min(420px,90vw);margin:0 auto;display:block;overflow:visible">
      <text x="50%" y="90" text-anchor="middle"
        font-family="Testimonia-bbbb71b25a03f59a, cursive"
        font-size="80" font-weight="400" fill="#0f0f0f"
        transform="rotate(-8,210,60)">Ask Aurum</text>
    </svg>
  </a>
</div>"""

# ── Assemble new works section ────────────────────────────────────────────────
works_list_html = "\n".join(new_items)
new_works_section = f"""id="works" class="works" data-astro-cid-n5ebmdgj> {h2} {decos} <div class="works__list" data-astro-cid-n5ebmdgj> {works_list_html} </div> {ask_aurum}"""

# ── Replace in main HTML ──────────────────────────────────────────────────────
# Find works section boundaries in current corrupted HTML
section_open = content.rfind('<section', 0, content.find('id="works"'))
section_close_pos = 153072
new_section = f'<section {new_works_section}</section>'

content = content[:section_open] + new_section + content[section_close_pos + len('</section>'):]

open("D:/Claude/3kimbrandesign/index.html", "w", encoding="utf-8").write(content)
print("\nDone — works section fully rebuilt from clean backup structure.")
