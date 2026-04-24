"""
Apply Aurum Spa & Aesthetics content to kimbrandesign HTML.
Replaces all text content and swaps images with styled placeholders.
"""
import re

PLACEHOLDER = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='600'%3E%3Crect fill='%23c9a96e' width='800' height='600'/%3E%3Ctext x='50%25' y='50%25' text-anchor='middle' dy='.3em' fill='%23fff' font-family='Georgia%2C serif' font-size='22' letter-spacing='3'%3EAurum Spa %26 Aesthetics%3C/text%3E%3C/svg%3E"

content = open("D:/Claude/3kimbrandesign/index.html", encoding="utf-8").read()

# ── META / TITLE ─────────────────────────────────────────────────────────────
content = content.replace(
    "<title>Kimbrandesign</title>",
    "<title>Aurum Spa &amp; Aesthetics | Luxury Med Spa &amp; Day Spa — Beverly Hills, CA</title>"
)
content = re.sub(
    r'(<meta name="description" content=")[^"]*(")',
    r'\1Aurum Spa & Aesthetics is Beverly Hills\' premier luxury med spa and day spa, located at 9500 Wilshire Blvd. Expert injectables, laser treatments, gold facials, massage, and bespoke wellness experiences.\2',
    content
)
content = re.sub(
    r'(<meta property="og:title" content=")[^"]*(")',
    r"\1Aurum Spa \&amp; Aesthetics — Beverly Hills' Gold Standard in Luxury \&amp; Aesthetics\2",
    content
)
content = re.sub(
    r'(<meta property="og:description" content=")[^"]*(")',
    r"\1Where clinical precision meets restorative luxury. Beverly Hills' most exclusive med spa on Wilshire Blvd.\2",
    content
)

# ── BRAND NAME (header logo text) ────────────────────────────────────────────
content = content.replace(">Kimbrandesign<", ">Aurum Spa &amp; Aesthetics<")
content = content.replace(">KIMBRANDESIGN<", ">AURUM SPA &amp; AESTHETICS<")

# ── NAVIGATION ───────────────────────────────────────────────────────────────
nav_old = (
    '<li data-astro-cid-5rz5afgx><a href="#about" data-astro-cid-5rz5afgx>About</a></li> '
    '<li data-astro-cid-5rz5afgx><a href="#services" data-astro-cid-5rz5afgx>Services</a></li> '
    '<li data-astro-cid-5rz5afgx><a href="#works" data-astro-cid-5rz5afgx>Work</a></li> '
    '<li data-astro-cid-5rz5afgx><a href="#team" data-astro-cid-5rz5afgx>Team</a></li> '
    '<li data-astro-cid-5rz5afgx><a href="#club" data-astro-cid-5rz5afgx>Club</a></li> '
    '<li data-astro-cid-5rz5afgx><a href="#contact" data-astro-cid-5rz5afgx>Contact</a></li>'
)
nav_new = (
    '<li data-astro-cid-5rz5afgx><a href="#about" data-astro-cid-5rz5afgx>About</a></li> '
    '<li data-astro-cid-5rz5afgx><a href="#services" data-astro-cid-5rz5afgx>Aesthetics</a></li> '
    '<li data-astro-cid-5rz5afgx><a href="#works" data-astro-cid-5rz5afgx>Spa &amp; Wellness</a></li> '
    '<li data-astro-cid-5rz5afgx><a href="#team" data-astro-cid-5rz5afgx>Signature Experiences</a></li> '
    '<li data-astro-cid-5rz5afgx><a href="#club" data-astro-cid-5rz5afgx>Book a Visit</a></li> '
    '<li data-astro-cid-5rz5afgx><a href="#contact" data-astro-cid-5rz5afgx>Contact</a></li>'
)
content = content.replace(nav_old, nav_new)

# ── HERO ─────────────────────────────────────────────────────────────────────
content = content.replace(
    "<h1 data-astro-cid-7sflhgxc>Branding with soul, strategy &amp; impact</h1>",
    "<h1 data-astro-cid-7sflhgxc>The Finest Version<br>of You Awaits.</h1>"
)
# eyebrow / deco spans in hero — add pre-headline
content = content.replace(
    '<span class="hero__deco" data-astro-cid-7sflhgxc></span> <span class="hero__deco" data-astro-cid-7sflhgxc></span> <span class="hero__deco" data-astro-cid-7sflhgxc></span>',
    '<span class="hero__deco" data-astro-cid-7sflhgxc></span> <span class="hero__deco" data-astro-cid-7sflhgxc></span> <span class="hero__deco" data-astro-cid-7sflhgxc></span><p style="font-size:0.75rem;letter-spacing:0.2em;text-transform:uppercase;margin-bottom:1rem;opacity:0.8;">Beverly Hills\' Gold Standard in Luxury Aesthetics &amp; Wellness</p>'
)

# ── ABOUT SECTION ────────────────────────────────────────────────────────────
content = content.replace(
    "<h2 pos=\"5+5\" pos-m=\"row\" pos-s=\"3+8\" data-astro-cid-3cggfioh>Shaping the beauty of everyday brands</h2>",
    "<h2 pos=\"5+5\" pos-m=\"row\" pos-s=\"3+8\" data-astro-cid-3cggfioh>Beverly Hills\' Gold Standard.<br>Built Intentionally.</h2>"
)
content = content.replace(
    "KIMBRANDESIGN is a strategic brand transformation studio led by Kim Sentis.",
    "AURUM SPA &amp; AESTHETICS was founded on a single, non-negotiable belief: that Beverly Hills deserved a spa and aesthetics destination that matched the caliber of the city itself."
)
content = content.replace(
    "With over 15 years of experience in cosmetics, branding and marketing, Kim partners with brand leaders to clarify vision, unlock new positioning and guide meaningful transformation.",
    "Our team is composed of board-certified medical professionals, licensed master estheticians, certified massage therapists, and wellness practitioners — each selected for both their technical mastery and their ability to make every guest feel genuinely cared for."
)
content = content.replace(
    "Combining strategic clarity, emotional intelligence and creative leadership, KBD helps brands express who they truly are - clearly, consistently and beautifully.",
    "The name Aurum is Latin for gold — and it reflects everything we stand for. Gold is not a marketing word. It is the standard to which we hold every treatment, every interaction, and every result we deliver."
)
content = content.replace(
    "We often work with brands at pivotal moments - when they need to redefine who they are and where they are going.",
    "We chose Wilshire Boulevard deliberately. The heart of Beverly Hills is one of the world\'s most storied addresses — and Aurum belongs here."
)
content = content.replace(
    "Our hybrid model allows us to assemble tailor-made teams around each project, delivering the strategic depth of a consultancy with the creative impact of a leading agency.",
    "Whether you are a long-time Beverly Hills resident, a Hollywood professional, a visiting executive, or a discerning traveler, our doors are open — and our standard is always gold."
)

# ── SERVICES HEADINGS ────────────────────────────────────────────────────────
content = content.replace(">Brand strategy<", ">Aurum Aesthetics<")
content = content.replace(">Brand creation<", ">Aurum Spa<")
content = content.replace(">Brand activation<", ">Signature Journeys<")

# Service descriptions (look for the <p> tags under each service heading)
content = content.replace(
    "Clarify your brand&#39;s identity, define its purpose, and build the strategic foundation that guides every decision.",
    "World-class aesthetic medicine — Botox, fillers, laser resurfacing, PRP, chemical peels, IV therapy, and body contouring — performed by licensed medical professionals."
)
content = content.replace(
    "Bring your brand to life with a cohesive visual identity system — logo, typography, color, and all the elements that make your brand instantly recognizable.",
    "Deeply restorative spa rituals — gold facials, Swedish and deep tissue massage, hot stone, body wraps, and couples retreats — in a private sanctuary of warmth and stillness."
)
content = content.replace(
    "Launch campaigns that move people, build communities, and make your brand felt across every channel and touchpoint.",
    "Choreographed half-day and full-day retreats that combine medical aesthetics and luxury spa — thoughtfully sequenced so each element prepares and enhances the next."
)

# ── WORKS / PORTFOLIO SECTION ────────────────────────────────────────────────
content = content.replace(
    ">Our work<",
    ">Our Results<"
)
# Replace portfolio project names with Aurum service spotlights
replacements = [
    ("The Power of Algae When the sensorial richness of algae meets the living force of the ocean, for the", "The Aurum Executive Half-Day | 3.5 Hours | $625"),
    ("L&#39;Art de Nourrir les Peaux Where rich care blends with gourmand textures and sensorial fragrances, n", "The Gold Standard Journey Half-Day | 4 Hours | $825"),
    ("The Symbiocene Where breakthrough biotechnology opens the path to a new symbiosis between humans, fo", "The Aurum Full Day Retreat Full Day | 6 Hours | $1,350"),
    ("Iconic since 1963 Where timeless simplicity meets the confidence of an iconic blue, celebrating the", "Botox &amp; Neurotoxin Treatments Expertly placed neuromodulators — polished, never frozen"),
    ("The Art of the Journey Where retail and spa experiences become moments of discovery, connection and", "Gold Body Ritual Full-body exfoliation with 24k gold-infused body wrap | 90 min | $365"),
    ("Protection You Can Trust Where expert care, natural protection and gentle design come together to sa", "Aurum Signature Facial Bespoke 90-minute facial | Gold-infused serum | $295"),
    ("The Guccification of Beauty Where self-expression, eclectic beauty and bold aesthetics redefine the", "Microneedling with PRP Collagen-stimulating regenerative treatment | Series of 3–6"),
    ("Give the Gift of Time Where the simple gesture of offering a watch becomes a symbol of connection, e", "Hydrafacial MD The globally recognized gold standard of facial cleansing | $199–$285"),
]
for old, new in replacements:
    content = content.replace(old, new)

# ── TESTIMONIALS ─────────────────────────────────────────────────────────────
content = content.replace(">In their words<", ">The Aurum Experience, In Their Words.<")

old_testimonials = [
    (
        "Lidia Mola",
        "M.L., Bel Air"
    ),
    (
        "Delphine Logereau",
        "R.A., West Hollywood"
    ),
    (
        "Jerome Goarnisson",
        "C.T., Brentwood"
    ),
    (
        "Stephanie Eyherabide",
        "J.W., Malibu"
    ),
    (
        "Frederic Chivrac",
        "Additional Guest"
    ),
    (
        "Florence Bauduin",
        "Additional Guest"
    ),
]

testimonial_quotes = [
    "Aurum has completely redefined what I expect from a spa. The level of clinical expertise paired with genuine luxury — there is simply nothing else like it in Beverly Hills.",
    "I came in for the full-day retreat and left feeling like the best version of myself. Every single person on that team was exceptional. I have already booked my next three visits.",
    "The combination of medical aesthetics and world-class spa treatments under one roof is exactly what Beverly Hills has been missing. Aurum fills that gap perfectly.",
    "I have visited premier spas in New York, Paris, and Dubai. Aurum is in that conversation. This is what the gold standard actually looks like.",
    "From the moment I walked in to the moment I left, every detail was considered. Aurum is extraordinary.",
    "The Gold Body Ritual alone is worth the trip. The entire experience is unlike anything else in the city.",
]

# Replace testimonial names
for i, (old_name, new_name) in enumerate(old_testimonials):
    content = content.replace(f">{old_name}<", f">{new_name}<")
    content = content.replace(f'alt="{old_name}"', f'alt="Aurum Guest"')

# Replace testimonial quote text — find <blockquote> or <q> tags
# The testimonial text appears in <p> tags with specific patterns; do targeted replacements
testimony_texts = [
    ("Kim has a rare talent for understanding the essence of a brand and translating it into something tangible and powerful.",
     "Aurum has completely redefined what I expect from a spa. The level of clinical expertise paired with genuine luxury — there is simply nothing else like it in Beverly Hills."),
    ("Working with KBD was transformative. Kim helped us clarify our brand identity in a way that resonated deeply with our customers.",
     "I came in for the full-day retreat and left feeling like the best version of myself. Every single person was exceptional. I have already booked my next three visits."),
    ("The strategic depth combined with creative execution is exceptional. KBD delivered beyond our expectations.",
     "The combination of medical aesthetics and world-class spa under one roof is exactly what Beverly Hills has been missing. Aurum fills that gap perfectly."),
    ("KBD's approach to brand strategy is both rigorous and inspired. The results speak for themselves.",
     "I have visited premier spas in New York, Paris, and Dubai. Aurum is in that conversation. This is what the gold standard actually looks like."),
    ("Kim's ability to see what a brand could become, and then help you get there, is truly exceptional.",
     "From the moment I walked in, every detail was considered. Aurum is extraordinary."),
    ("The transformation of our brand under KBD's guidance exceeded all our expectations.",
     "The Gold Body Ritual alone is worth the trip. The entire experience is unlike anything else in the city."),
]
for old_q, new_q in testimony_texts:
    content = content.replace(old_q, new_q)

# ── TEAM SECTION ─────────────────────────────────────────────────────────────
content = content.replace(
    ">A tailored team for each project.<",
    ">Our Expert Team.<"
)
# Replace team role labels
team_roles = [
    ("Brand Strategist", "Medical Director"),
    ("Creative Director", "Lead Esthetician"),
    ("Art Director", "Massage Therapist"),
    ("Copywriter", "Wellness Consultant"),
    ("Brand Designer", "Aesthetic Injector"),
    ("Motion Designer", "Client Experience"),
]
for old_r, new_r in team_roles:
    content = content.replace(f">{old_r}<", f">{new_r}<")

# ── CLUB / CTA SECTION ───────────────────────────────────────────────────────
content = content.replace(">Providence club<", ">The Aurum Inner Circle<")
content = content.replace(
    "Providence",
    "Aurum Inner Circle"
)
# Book section
content = content.replace(
    ">Book a call<",
    ">Reserve Your Experience<"
)
content = content.replace(
    "book a call",
    "Reserve Your Experience"
)

# ── FAQ SECTION ──────────────────────────────────────────────────────────────
content = content.replace(
    ">FAQ Our approach<",
    ">FAQ Your Questions Answered.<"
)

# ── CONTACT SECTION ──────────────────────────────────────────────────────────
content = content.replace(
    'href="mailto:ksentis@kimbrandesign.com"',
    'href="mailto:hello@aurumspaBH.com"'
)
content = content.replace(
    "Contact Us",
    "Book Your Appointment"
)
content = content.replace(
    ">Legals<",
    ">(310) 385-7023<"
)
content = content.replace(
    'href="Legals.pdf"',
    'href="tel:+13103857023"'
)
content = content.replace(
    'href="https://ocitocine.com"',
    'href="https://aurumspaBH.com"'
)
content = content.replace(
    "> Site by Ocitocine <",
    "> 9500 Wilshire Blvd, Beverly Hills <"
)

# ── FOOTER BRAND NAME ────────────────────────────────────────────────────────
content = content.replace(
    "Kimbrandesign",
    "Aurum Spa &amp; Aesthetics"
)
content = content.replace(
    "kimbrandesign.com",
    "aurumspaBH.com"
)

# ── IMAGE PLACEHOLDERS ───────────────────────────────────────────────────────
# Replace all img src and srcset with placeholder
def replace_img(m):
    full = m.group(0)
    # Replace src="..."
    full = re.sub(r'src="[^"]*(_astro|webp|jpg|jpeg|png|gif)[^"]*"', f'src="{PLACEHOLDER}"', full)
    # Remove srcset entirely (too complex with placeholder)
    full = re.sub(r'srcset="[^"]*"', 'srcset=""', full)
    # Update alt text
    full = re.sub(r'alt="[^"]*"', 'alt="Aurum Spa &amp; Aesthetics"', full)
    return full

content = re.sub(r'<img [^>]+>', replace_img, content)

# ── WRITE OUTPUT ─────────────────────────────────────────────────────────────
open("D:/Claude/3kimbrandesign/index.html", "w", encoding="utf-8").write(content)
print("Done! Aurum Spa content applied to index.html")
