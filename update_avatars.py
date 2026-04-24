"""Replace Aurum logo placeholders with minimalist initial avatars for each guest."""
import re
from urllib.parse import quote

content = open("D:/Claude/3kimbrandesign/index.html", encoding="utf-8").read()

def make_avatar(initials):
    """Minimalist circular avatar: cream background, thin gold ring, dark initials."""
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 80" width="80" height="80">
  <circle cx="40" cy="40" r="39" fill="#F7F3EE" stroke="#C9A96E" stroke-width="1"/>
  <text x="40" y="40" dominant-baseline="central" text-anchor="middle"
    font-family="Georgia, serif" font-size="20" font-weight="400"
    fill="#1A1A1A" letter-spacing="1">{initials}</text>
</svg>'''
    return "data:image/svg+xml," + quote(svg, safe="")

GUESTS = [
    ("M.L.", "ML"),
    ("R.A.", "RA"),
    ("C.T.", "CT"),
    ("J.W.", "JW"),
    ("S.M.", "SM"),
    ("A.K.", "AK"),
]

matches = list(re.finditer(r'<kim-testimony[^>]*>.*?</kim-testimony>', content, re.DOTALL))
print(f"Found {len(matches)} testimonials")

offset = 0
for i, (match, (name, initials)) in enumerate(zip(matches, GUESTS)):
    old_block = match.group()
    new_block = old_block

    # Replace src of the author__image img
    new_src = make_avatar(initials)
    new_block = re.sub(
        r'(<img [^>]+class="author__image"[^>]*)\bsrc="[^"]*"',
        lambda m, s=new_src: m.group(1) + f'src="{s}"',
        new_block
    )
    # Clear srcset (was already empty but ensure)
    new_block = re.sub(r'srcset="[^"]*"', 'srcset=""', new_block)

    start = match.start() + offset
    end   = match.end()   + offset
    content = content[:start] + new_block + content[end:]
    offset += len(new_block) - len(old_block)
    print(f"  {i+1}. {name} -> {initials} avatar")

open("D:/Claude/3kimbrandesign/index.html", "w", encoding="utf-8").write(content)
print("Done — minimalist avatars applied to all 6 testimonials.")
