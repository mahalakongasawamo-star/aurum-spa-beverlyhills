"""Replace all testimony author__image src with the real Aurum logo."""
import re

content = open("D:/Claude/3kimbrandesign/index.html", encoding="utf-8").read()

LOGO = "images/logo-aurum.png"

def replace_author_img(m):
    tag = m.group()
    # Replace src (appears before class in this HTML)
    tag = re.sub(r'src="[^"]*"', f'src="{LOGO}"', tag)
    tag = re.sub(r'srcset="[^"]*"', 'srcset=""', tag)
    tag = re.sub(r'alt="[^"]*"', 'alt="Aurum Spa &amp; Aesthetics"', tag)
    return tag

# Match any <img> that contains class="author__image"
new_content = re.sub(
    r'<img [^>]*class="author__image"[^>]*>',
    replace_author_img,
    content
)

count = content.count('class="author__image"')
print(f"Replaced {count} author__image tags with logo-aurum.png")

open("D:/Claude/3kimbrandesign/index.html", "w", encoding="utf-8").write(new_content)
print("Done.")
