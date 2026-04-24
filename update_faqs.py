"""Replace FAQ section with Aurum-specific Q&A content."""
import re

content = open("D:/Claude/3kimbrandesign/index.html", encoding="utf-8").read()

SVG_ICON = '''<svg viewBox="0 0 13 16" fill="none" xmlns="http://www.w3.org/2000/svg" data-astro-cid-z6gx6xcw> <path d="M6.35156 0.25C6.50921 0.247103 6.68178 0.301017 6.87402 0.435547C7.02152 0.53877 7.11012 0.696817 7.11523 0.956055C7.13826 2.13731 7.13287 3.31967 7.10059 4.50195C7.0681 5.69191 7.06374 6.88137 7.08691 8.07031L7.09082 8.25195L7.26465 8.30469C8.10682 8.56013 8.94867 8.78889 9.79004 8.99023L9.79785 8.99219L9.80469 8.99316C10.6289 9.13751 11.4268 9.33561 12.1973 9.58691L12.2021 9.58789C12.4747 9.67059 12.6308 9.80837 12.7139 9.9873C12.7547 10.1452 12.761 10.3301 12.7246 10.5479C12.637 10.7145 12.5074 10.8676 12.3262 11.0049C12.1723 11.1214 11.9675 11.1743 11.6836 11.1338C11.1963 11.0641 10.691 10.9506 10.168 10.792L9.63965 10.6182C8.85469 10.3087 8.12444 10.0515 7.44922 9.84668L7.12012 9.74609L7.12598 10.0908C7.14187 10.9052 7.21405 11.7445 7.3418 12.6084H7.34277C7.41419 13.4589 7.42977 14.2828 7.39062 15.0801V15.0977C7.39422 15.2851 7.32533 15.4275 7.16895 15.5459C6.98228 15.6872 6.81187 15.7471 6.6543 15.75C6.42928 15.7541 6.23007 15.6932 6.04883 15.5664C5.88764 15.4536 5.81325 15.3136 5.80957 15.126C5.79172 14.2103 5.77371 13.2946 5.75586 12.3789V12.3711L5.75488 12.3633C5.68195 11.4536 5.6369 10.5435 5.61914 9.63281L5.61621 9.45508L5.44629 9.39941C4.65455 9.14121 3.86299 8.93745 3.07227 8.78809C2.30332 8.64282 1.53287 8.4442 0.760742 8.19238L0.755859 8.19141L0.651367 8.15527C0.430387 8.07007 0.354549 7.96958 0.332031 7.88867L0.327148 7.87207L0.320312 7.85645L0.268555 7.7041C0.234179 7.5608 0.249888 7.44255 0.300781 7.33887L0.316406 7.30859L0.322266 7.27441C0.361128 7.06533 0.462062 6.90236 0.630859 6.77441C0.783782 6.65861 0.987364 6.60538 1.26855 6.64453C1.92674 6.79185 2.58552 6.96596 3.24512 7.16602C3.92103 7.37104 4.59723 7.54943 5.27246 7.7002L5.56738 7.76562L5.57617 7.46387C5.6108 6.38115 5.61777 5.2985 5.59668 4.2168C5.57568 3.13948 5.55518 2.06169 5.53418 0.984375C5.52923 0.725224 5.61086 0.564384 5.75391 0.456055C5.93 0.322705 6.12643 0.254153 6.35156 0.25Z" fill="white" stroke="#0F0F0F" stroke-width="0.5" data-astro-cid-z6gx6xcw></path> </svg>'''

FAQS = [
    {
        "q": "Do I need a consultation before my first treatment?",
        "a": "Every new guest begins with a private consultation with one of our licensed medical aestheticians or nurse practitioners. We take the time to understand your goals, assess your skin, and recommend a personalised treatment plan before anything is scheduled.",
    },
    {
        "q": "Are your aesthetic treatments medically supervised?",
        "a": "Yes. Every medical aesthetic treatment at Aurum is performed or directly supervised by a licensed healthcare professional. We do not delegate clinical decisions — your safety and results are our highest priority.",
    },
    {
        "q": "Do you offer treatments for men?",
        "a": "Of course. Aurum welcomes all guests. Many of our clients are men seeking natural-looking refinement, skin health, and anti-aging treatments tailored to their anatomy and aesthetic goals.",
    },
    {
        "q": "What is the cancellation policy?",
        "a": "We kindly request 24 hours' notice for cancellations or rescheduling. Late cancellations or no-shows may be subject to a service fee. We understand life happens — please reach out as soon as possible and we will do our best to accommodate.",
    },
    {
        "q": "Do you offer gift cards?",
        "a": "Yes. Aurum gift cards are available in any amount and can be redeemed for any service. They make a thoughtful and elevated gift for any occasion. Contact us directly to arrange one.",
    },
    {
        "q": "Where is Aurum located?",
        "a": "We are at 9500 Wilshire Blvd, Beverly Hills, CA 90212 — in the heart of the Golden Triangle. Complimentary valet and validated parking are available. We recommend arriving 10 minutes early for your first visit.",
    },
]

def make_faq(q, a, include_script=False):
    script = ' <script type="module" src="_astro/Faq.astro_astro_type_script_index_0_lang.GFtsrRxB.js"></script>' if include_script else ''
    return (
        f'{script}<kim-faq class="faq" name="faq" data-astro-cid-z6gx6xcw="true">'
        f' <summary data-astro-cid-z6gx6xcw> {q} '
        f'<span data-astro-cid-z6gx6xcw> {SVG_ICON} </span>'
        f' </summary>'
        f' <div col="20" class="faq__container" data-astro-cid-z6gx6xcw>'
        f' <div class="faq__content grid" data-astro-cid-z6gx6xcw>'
        f' <div pos="1-12" pos-s="row" data-astro-cid-z6gx6xcw>'
        f' <p>{a}</p>'
        f' </div> </div> </div> </kim-faq>'
    )

# Replace h2 subtitle
content = content.replace(
    '>FAQ <span data-astro-cid-ewl3b5dn>Our approach</span></h2>',
    '>FAQ <span data-astro-cid-ewl3b5dn>Your questions answered</span></h2>',
    1
)

# Find the faqs__list div and replace all kim-faq items inside it
list_start = content.find('<div pos="2+22" pos-m="row" class="faqs__list"')
if list_start == -1:
    print("ERROR: faqs__list not found")
    exit()

# Find its closing </div> by depth tracking
depth = 0
pos = list_start
list_end = -1
while pos < len(content):
    o = content.find('<div', pos + 1)
    c = content.find('</div>', pos + 1)
    if c == -1:
        break
    if o != -1 and o < c:
        depth += 1
        pos = o
    else:
        if depth == 0:
            list_end = c + len('</div>')
            break
        depth -= 1
        pos = c + 1

print(f"faqs__list: {list_start} to {list_end}")

# Build new list content
new_items = ""
for i, faq in enumerate(FAQS):
    new_items += make_faq(faq["q"], faq["a"], include_script=(i == 0))
    print(f"  FAQ {i+1}: {faq['q'][:50]}")

new_list = (
    '<div pos="2+22" pos-m="row" class="faqs__list" data-astro-cid-ewl3b5dn>'
    + new_items +
    '</div>'
)

content = content[:list_start] + new_list + content[list_end:]
open("D:/Claude/3kimbrandesign/index.html", "w", encoding="utf-8").write(content)
print("\nDone.")
