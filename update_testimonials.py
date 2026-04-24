"""Replace testimonial content with Aurum quotes and add gold hover effect."""
import re

content = open("D:/Claude/3kimbrandesign/index.html", encoding="utf-8").read()

AURUM_TESTIMONIALS = [
    {
        "quote": "Aurum has completely redefined what I expect from a spa. The level of clinical expertise paired with genuine luxury — there is simply nothing else like it in Beverly Hills.",
        "name": "M.L.",
        "role": "Aurum Guest — Bel Air",
    },
    {
        "quote": "I came in for the full-day retreat and left feeling like the best version of myself. Every single person on that team was exceptional. I have already booked my next three visits.",
        "name": "R.A.",
        "role": "Aurum Guest — West Hollywood",
    },
    {
        "quote": "The combination of medical aesthetics and world-class spa treatments under one roof is exactly what Beverly Hills has been missing. Aurum fills that gap perfectly.",
        "name": "C.T.",
        "role": "Aurum Guest — Brentwood",
    },
    {
        "quote": "I have visited premier spas in New York, Paris, and Dubai. Aurum is in that conversation. This is what the gold standard actually looks like.",
        "name": "J.W.",
        "role": "Aurum Guest — Malibu",
    },
    {
        "quote": "From the moment I walked in to the moment I left, every detail was considered. The team's dedication to excellence is unlike anything I've encountered. Aurum is extraordinary.",
        "name": "S.M.",
        "role": "Aurum Guest — Beverly Hills",
    },
    {
        "quote": "The Gold Body Ritual alone is worth the trip. But the entire experience — the space, the team, the results — is unlike anything else in the city.",
        "name": "A.K.",
        "role": "Aurum Guest — Pacific Palisades",
    },
]

matches = list(re.finditer(r'<kim-testimony[^>]*>.*?</kim-testimony>', content, re.DOTALL))
print(f"Found {len(matches)} testimonials")

offset = 0
for i, (match, aurum) in enumerate(zip(matches, AURUM_TESTIMONIALS)):
    old = match.group()
    new = old

    # Replace blockquote paragraph text
    new = re.sub(
        r'(<blockquote[^>]*>)\s*<p>.*?</p>\s*(</blockquote>)',
        lambda m, q=aurum["quote"]: f'{m.group(1)}<p>{q}</p>{m.group(2)}',
        new, flags=re.DOTALL
    )

    # Replace author name
    new = re.sub(
        r'(<span class="author__name"[^>]*>)[^<]*(</span>)',
        rf'\g<1>{aurum["name"]}\g<2>',
        new
    )

    # Replace author role
    new = re.sub(
        r'(<span class="author__role"[^>]*>)[^<]*(</span>)',
        rf'\g<1>{aurum["role"]}\g<2>',
        new
    )

    start = match.start() + offset
    end   = match.end()   + offset
    content = content[:start] + new + content[end:]
    offset += len(new) - len(old)

# Inject hover style block after existing testimonial styles (before </head> if no better anchor)
HOVER_CSS = """<style id="testimony-gold-hover">
/* Gold glow + lift on testimony card hover */
kim-testimony[data-astro-cid-7bgby7vy] {
  transition: transform 0.35s cubic-bezier(0.34,1.56,0.64,1),
              box-shadow 0.35s ease,
              background-color 0.35s ease;
  border-radius: 16px;
  position: relative;
  cursor: default;
}
kim-testimony[data-astro-cid-7bgby7vy]:hover {
  transform: translateY(-8px) scale(1.015);
  box-shadow:
    0 16px 48px rgba(201,169,110,0.30),
    0 4px 16px rgba(201,169,110,0.20),
    0 0 0 1.5px rgba(201,169,110,0.35);
  background-color: rgba(201,169,110,0.07);
  z-index: 10;
}
/* Gold accent on blockquote text on hover */
kim-testimony[data-astro-cid-7bgby7vy]:hover blockquote p {
  color: #0F0F0F;
}
/* Avatar circle gold ring on hover */
kim-testimony[data-astro-cid-7bgby7vy]:hover .author__image {
  box-shadow: 0 0 0 2px #c9a96e;
}
</style>"""

# Insert before </head>
content = content.replace("</head>", HOVER_CSS + "\n</head>", 1)

open("D:/Claude/3kimbrandesign/index.html", "w", encoding="utf-8").write(content)
print("Done — testimonials updated with Aurum quotes + gold hover effect.")
