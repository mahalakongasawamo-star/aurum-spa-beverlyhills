"""
Redistribute service images — 4-5 unique images per item, cycling to fill 7 slots.
"""
import re

content = open("D:/Claude/3kimbrandesign/index.html", encoding="utf-8").read()

P = "images/services/"

# 4-5 unique images per item — cycle fills remaining slots up to 7
ITEM_POOLS = [
    # 1  Botox & Neurotoxins  (5 unique)
    [P+"Botox_001.png", P+"SRV_Botox_001.png", P+"SRV_Botox_002.png",
     P+"SRV_Botox_003.png", P+"SRV_Botox_004.png"],

    # 2  Dermal Fillers  (5 unique)
    [P+"DermalFillers_001.png", P+"LipFIllers_001.png", P+"ChinJawline_001.png",
     P+"SRV_Dermal_001.png", P+"SRV_Dermal_002.png"],

    # 3  Laser Skin Resurfacing  (5 unique)
    [P+"LaserHairRemoval_001.png", P+"IPL_001.png", P+"PigmentRemoval_001.png",
     P+"SRV_Laser_001.png", P+"SRV_Laser_002.png"],

    # 4  Microneedling & PRP  (4 unique)
    [P+"MicroneedlingWithPRP_001.png", P+"MicroNeedling_001.png",
     P+"PRPFacial_001.png", P+"SRV_MicroNeedling_001.png"],

    # 5  Hydrafacial MD  (4 unique)
    [P+"HydraFacial_001.png", P+"SRV_Dermal_003.png",
     P+"SRV_Laser_003.png", P+"SRV_Dermal_004.png"],

    # 6  Chemical Peels  (4 unique)
    [P+"ChemicalPeel_001.png", P+"SRV_Laser_004.png",
     P+"SRV_Laser_005.png", P+"SRV_Dermal_005.png"],

    # 7  Dysport & IPL  (4 unique)
    [P+"Dysport_001.png", P+"SRV_Botox_005.png",
     P+"IPL_001.png", P+"SRV_Botox_004.png"],

    # 8  Precision Treatments  (4 unique)
    [P+"PrecisionTreatments_001.png", P+"SRV_Dermal_002.png",
     P+"SRV_Laser_002.png", P+"SRV_Botox_003.png"],
]

# ── Locate works section ─────────────────────────────────────────────────────
works_idx  = content.find('id="works"')
works_end  = content.find('</section>', works_idx)
works_html = content[works_idx:works_end]
work_items = list(re.finditer(r'<kim-work[^>]*>.*?</kim-work>', works_html, re.DOTALL))

print(f"Found {len(work_items)} work items")

new_works_html = works_html
offset = 0

for i, (match, pool) in enumerate(zip(work_items, ITEM_POOLS)):
    old_item = match.group()
    new_item = old_item

    imgs = list(re.finditer(r'<img [^>]*data-astro-cid-wkx7uqji[^>]*>', new_item))
    for j, img_match in enumerate(imgs):
        old_img = img_match.group()
        new_src = pool[j % len(pool)]
        new_img = re.sub(r'src="[^"]*"', f'src="{new_src}"', old_img)
        new_img = re.sub(r'srcset="[^"]*"', '', new_img)
        new_item = new_item.replace(old_img, new_img, 1)

    rel_start = match.start() - works_idx + offset
    rel_end   = match.end()   - works_idx + offset
    new_works_html = new_works_html[:rel_start] + new_item + new_works_html[rel_end:]
    offset += len(new_item) - len(old_item)

    label = re.search(r'<strong[^>]*>(.*?)</strong>', new_item)
    print(f"  Item {i+1} ({label.group(1) if label else '?'}): "
          f"{len(pool)} unique imgs cycling across 7 slots")

content = content[:works_idx] + new_works_html + content[works_end:]
open("D:/Claude/3kimbrandesign/index.html", "w", encoding="utf-8").write(content)
print("\nDone.")
