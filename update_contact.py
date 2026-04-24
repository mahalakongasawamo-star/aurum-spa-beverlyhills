"""Replace contact section + add footer with Aurum content from screenshot."""

content = open("D:/Claude/3kimbrandesign/index.html", encoding="utf-8").read()

# ── Find the existing contact section ────────────────────────────────────────
section_start = content.rfind('<section', 0, content.find('id="contact"'))
section_end_tag = '</section>'
section_end = content.find(section_end_tag, content.find('id="contact"')) + len(section_end_tag)

print(f"Contact section: {section_start} to {section_end}")

NEW_CONTACT = '''<section id="contact" class="contact grid" data-astro-cid-sraju53i style="
  background:#0F0F0F;
  color:#FFFFFF;
  padding:8rem 0 6rem;
  text-align:center;
  position:relative;
">
<style>
#contact .contact__label {
  font-family: var(--font-primary);
  font-size: 0.7rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.5);
  margin-bottom: 2rem;
}
#contact .contact__heading {
  font-family: var(--font-secondary);
  font-size: clamp(3rem, 7vw, 6rem);
  font-weight: 400;
  line-height: 1.1;
  color: #FFFFFF;
  margin: 0 auto 3.5rem;
  max-width: 700px;
}
#contact .contact__address {
  font-family: var(--font-primary);
  font-size: 0.95rem;
  line-height: 2;
  color: rgba(255,255,255,0.75);
  margin-bottom: 3rem;
}
#contact .contact__hours {
  display: inline-grid;
  grid-template-columns: 1fr auto;
  gap: 0.25rem 3rem;
  font-family: var(--font-primary);
  font-size: 0.9rem;
  color: rgba(255,255,255,0.75);
  text-align: left;
  margin: 0 auto 3rem;
}
#contact .contact__hours span:nth-child(odd) {
  color: rgba(255,255,255,0.5);
}
#contact .contact__hours span:nth-child(even) {
  text-align: right;
}
#contact .contact__tel,
#contact .contact__email-text {
  font-family: var(--font-primary);
  font-size: 1rem;
  color: rgba(255,255,255,0.75);
  display: block;
  margin-bottom: 0.5rem;
  text-decoration: none;
}
#contact .contact__tel:hover,
#contact .contact__email-text:hover {
  color: #C9A96E;
}
#contact .contact__desc {
  font-family: var(--font-primary);
  font-size: 0.9rem;
  line-height: 1.8;
  color: rgba(255,255,255,0.5);
  max-width: 640px;
  margin: 2.5rem auto 3rem;
}
#contact .contact__cta {
  display: inline-block;
  border: 1px solid rgba(255,255,255,0.35);
  border-radius: 100px;
  padding: 1.1rem 2.5rem;
  font-family: var(--font-primary);
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #FFFFFF;
  text-decoration: none;
  transition: border-color 0.3s, color 0.3s, background 0.3s;
  margin-bottom: 5rem;
}
#contact .contact__cta:hover {
  border-color: #C9A96E;
  color: #C9A96E;
  background: rgba(201,169,110,0.07);
}
#contact .contact__footer {
  border-top: 1px solid rgba(255,255,255,0.12);
  padding-top: 2.5rem;
  font-family: var(--font-primary);
  font-size: 0.75rem;
  color: rgba(255,255,255,0.35);
  line-height: 1.7;
  max-width: 700px;
  margin: 0 auto 2.5rem;
}
#contact .contact__nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.5rem 1.5rem;
  font-family: var(--font-primary);
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}
#contact .contact__nav a {
  color: rgba(255,255,255,0.4);
  text-decoration: none;
  transition: color 0.2s;
}
#contact .contact__nav a:hover {
  color: #C9A96E;
}
</style>

<div pos="row" data-astro-cid-sraju53i>
  <p class="contact__label">Visit Aurum</p>
  <h2 class="contact__heading">Find Us on<br>Wilshire Boulevard.</h2>

  <div class="contact__address">
    Aurum Spa &amp; Aesthetics<br>
    9500 Wilshire Blvd<br>
    Beverly Hills, CA 90212<br>
    United States
  </div>

  <div class="contact__hours">
    <span>Monday &ndash; Friday</span><span>9:00 AM &ndash; 8:00 PM</span>
    <span>Saturday</span><span>9:00 AM &ndash; 7:00 PM</span>
    <span>Sunday</span><span>10:00 AM &ndash; 6:00 PM</span>
  </div>

  <a href="tel:+13103857023" class="contact__tel">(310) 385-7023</a>
  <a href="mailto:hello@aurumspaBH.com" class="contact__email-text">hello@aurumspaBH.com</a>

  <p class="contact__desc">
    Aurum is located on Wilshire Boulevard in the heart of Beverly Hills &mdash; one of the world&rsquo;s most prestigious addresses. Easily accessible from Rodeo Drive, the 405 and 10 freeways, with valet parking available and street parking on Wilshire Boulevard.
  </p>

  <a href="mailto:hello@aurumspaBH.com" class="contact__cta contact__link" data-astro-cid-vnzlvqnm>
    HELLO@AURUMSPABH.COM
  </a>

  <div class="contact__footer">
    &copy; 2025 Aurum Spa &amp; Aesthetics. All rights reserved. 9500 Wilshire Blvd, Beverly Hills, CA 90212.
    Medical aesthetic services are performed or supervised by licensed medical professionals. Individual results may vary.
  </div>

  <nav class="contact__nav">
    <a href="#">Home</a>
    <a href="#">About</a>
    <a href="#">Aesthetics</a>
    <a href="#">Spa &amp; Wellness</a>
    <a href="#">Signature Experiences</a>
    <a href="#">Book</a>
    <a href="#">Contact</a>
    <a href="#">Privacy Policy</a>
    <a href="#">Terms of Service</a>
  </nav>
</div>
</section>'''

content = content[:section_start] + NEW_CONTACT + content[section_end:]
open("D:/Claude/3kimbrandesign/index.html", "w", encoding="utf-8").write(content)
print("Done.")
