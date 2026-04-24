"""
Replace all work item images with Aurum service photos.
Distributes 19 images across 8 work items (each item gets a themed collage).
Updates headings and tags to match Aurum services.
"""
import re

content = open("D:/Claude/3kimbrandesign/index.html", encoding="utf-8").read()

# ── Service data ──────────────────────────────────────────────────────────────
services = [
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Botox &amp; Neurotoxins</strong> Expertly placed neuromodulators that smooth, refine, and prevent — without erasing what makes you distinctly you.",
        "tags": ["#botox", "#neurotoxin", "#injectables", "#antiaging", "#refinement"],
        "images": ["Botox_001.png", "SRV_Botox_001.png", "SRV_Botox_002.png", "SRV_Botox_003.png", "SRV_Botox_004.png", "SRV_Botox_005.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Dermal Fillers</strong> Restore volume, define architecture, and balance your proportions with premium hyaluronic acid fillers.",
        "tags": ["#fillers", "#volumization", "#lipfillers", "#jawline", "#youthful"],
        "images": ["DermalFillers_001.png", "LipFIllers_001.png", "ChinJawline_001.png", "DermalFillers_001.png", "LipFIllers_001.png", "ChinJawline_001.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Laser Skin Resurfacing</strong> Medical-grade laser treatments targeting uneven tone, sun damage, fine lines, and textural concerns.",
        "tags": ["#laser", "#resurfacing", "#skintone", "#rejuvenation", "#precision"],
        "images": ["LaserHairRemoval_001.png", "IPL_001.png", "PigmentRemoval_001.png", "LaserHairRemoval_001.png", "IPL_001.png", "PigmentRemoval_001.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Microneedling &amp; PRP</strong> A powerful regenerative treatment that stimulates collagen and restores a luminous, youthful complexion.",
        "tags": ["#microneedling", "#PRP", "#collagen", "#regenerative", "#glow"],
        "images": ["MicroneedlingWithPRP_001.png", "MicroNeedling_001.png", "PRPFacial_001.png", "MicroneedlingWithPRP_001.png", "MicroNeedling_001.png", "PRPFacial_001.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Hydrafacial MD</strong> The globally recognized gold standard of facial cleansing — zero redness, zero downtime, immediate radiance.",
        "tags": ["#hydrafacial", "#deepcleanse", "#hydration", "#glow", "#nodowntime"],
        "images": ["HydraFacial_001.png", "ChemicalPeel_001.png", "HydraFacial_001.png", "ChemicalPeel_001.png", "HydraFacial_001.png", "ChemicalPeel_001.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Chemical Peels</strong> Custom-blended medical peels clinician-supervised for maximum efficacy across all skin tones and types.",
        "tags": ["#chemicalpeel", "#brightening", "#resurfacing", "#clarity", "#medical"],
        "images": ["ChemicalPeel_001.png", "PigmentRemoval_001.png", "ChemicalPeel_001.png", "PigmentRemoval_001.png", "ChemicalPeel_001.png", "PigmentRemoval_001.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Dysport &amp; IPL</strong> Advanced neuromodulator and intense pulsed light treatments for refined, lasting skin clarity.",
        "tags": ["#dysport", "#IPL", "#skinclarity", "#photofacial", "#advanced"],
        "images": ["Dysport_001.png", "IPL_001.png", "Dysport_001.png", "IPL_001.png", "Dysport_001.png", "IPL_001.png"],
    },
    {
        "heading": "<strong data-astro-cid-wkx7uqji>Precision Treatments</strong> Tailored aesthetic protocols designed around your unique anatomy, skin, and personal vision of beauty.",
        "tags": ["#precision", "#bespoke", "#aesthetics", "#skincare", "#gold"],
        "images": ["PrecisionTreatments_001.png", "SRV_Botox_001.png", "PrecisionTreatments_001.png", "SRV_Botox_002.png", "PrecisionTreatments_001.png", "SRV_Botox_003.png"],
    },
]

# ── Locate works section ──────────────────────────────────────────────────────
works_idx  = content.find('id="works"')
works_end  = content.find('</section>', works_idx)
works_html = content[works_idx:works_end]

work_items = list(re.finditer(r'<kim-work[^>]*>.*?</kim-work>', works_html, re.DOTALL))

new_works_html = works_html
offset = 0

for i, (match, svc) in enumerate(zip(work_items, services)):
    old_item = match.group()
    new_item = old_item

    # Replace all img src with cycling service images
    imgs = list(re.finditer(r'<img [^>]*data-astro-cid-wkx7uqji[^>]*>', new_item))
    pool = svc["images"]
    for j, img_match in enumerate(imgs):
        old_img = img_match.group()
        new_src = f'images/services/{pool[j % len(pool)]}'
        new_img = re.sub(r'src="[^"]*"', f'src="{new_src}"', old_img)
        new_img = re.sub(r'srcset="[^"]*"', '', new_img)
        # Remove astro constrained sizing so object-fit handles it
        new_img = new_img.replace('--fit: contain;', '--fit: cover;')
        new_item = new_item.replace(old_img, new_img, 1)

    # Replace heading
    new_item = re.sub(
        r'<h3[^>]*>.*?</h3>',
        f'<h3 pos="5+5" pos-m="7+5" pos-s="6.." data-astro-cid-wkx7uqji>{svc["heading"]}</h3>',
        new_item, flags=re.DOTALL
    )

    # Replace tags
    tags_html = "".join(f'<li data-astro-cid-wkx7uqji>{t}</li>' for t in svc["tags"])
    new_item = re.sub(
        r'<ul data-astro-cid-wkx7uqji>.*?</ul>',
        f'<ul data-astro-cid-wkx7uqji>{tags_html}</ul>',
        new_item, flags=re.DOTALL
    )

    new_works_html = new_works_html.replace(old_item, new_item, 1)

content = content[:works_idx] + new_works_html + content[works_end:]

# Ensure service images also use object-fit cover (not constrained sizing)
content = content.replace(
    "</style>",
    """.work__image[data-astro-cid-wkx7uqji] img { object-fit: cover !important; width: 100% !important; height: 100% !important; }
</style>""",
    1  # only first occurrence
)

open("D:/Claude/3kimbrandesign/index.html", "w", encoding="utf-8").write(content)
print("Done — works section updated with all service images.")
