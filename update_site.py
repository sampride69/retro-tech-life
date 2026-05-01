import os
import re

# 1. UPDATE GENERATE_PAGES.PY
with open("generate_pages.py", "r", encoding="utf-8") as f:
    gen_content = f.read()

# Update images for BoardForge and M&A
gen_content = gen_content.replace(
    '"img": "", # Nessuna immagine fornita\n        "link": "https://retotechlife.gumroad.com/l/BoardForge"',
    '"img": "https://public-files.gumroad.com/pkhtlhprkjbggdc5p3vznm7bdh1s",\n        "link": "https://retotechlife.gumroad.com/l/BoardForge"'
)
gen_content = gen_content.replace(
    '"img": "", # Nessuna immagine fornita\n        "link": "https://retotechlife.gumroad.com/l/MandA"',
    '"img": "https://public-files.gumroad.com/4pkwhaqj2gdtrt4megnixraob5n2",\n        "link": "https://retotechlife.gumroad.com/l/MandA"'
)

# New products for generate_pages.py
new_gen_products = """    {
        "file": "ai-receptionist-agency-playbook.html",
        "title": "AI-Receptionist Agency Playbook",
        "img": "https://public-files.gumroad.com/upm06nxg1pous5otq2jhcvvq0m60",
        "link": "https://retotechlife.gumroad.com/l/AIReceptionistAgencyPlaybook",
        "html": '''
      <h1>AI-Receptionist Agency Playbook</h1>
      <p>A complete step-by-step playbook for building and selling AI receptionist services to local businesses.</p>
      <p>Every local business has the same invisible problem:<br>The phone rings while they are busy.</p>
      <p>A dentist is with a patient.<br>A plumber is on a job.<br>A beauty salon is serving a client.<br>A restaurant is in the middle of lunch service.<br>An auto repair shop is dealing with a customer at the counter.</p>
      <p>And in that moment, a potential customer may simply hang up and call someone else.</p>
      <p>That missed call could have been an appointment, a quote request, a booking, a new patient, or a repeat customer.</p>
      <p>This is exactly where the AI receptionist opportunity begins.</p>
      <p>AI-Receptionist Agency Playbook is a complete operational toolkit that shows you how to build and sell AI receptionist services to local businesses — without starting from a blank page.</p>
      <p>This is not a generic AI prompt pack.</p>
      <p>It is a practical agency playbook designed to help you understand the opportunity, package the service, contact potential clients, create a simple demo, onboard businesses, price your offer, and launch your first local AI receptionist service.</p>
      <p>Instead of wondering what to say, what to offer, how to explain the service, how to structure the bot, or how much to charge, you get a ready-to-use system you can adapt and put into action.</p>
'''
    },
    {
        "file": "culinaryroots.html",
        "title": "CulinaryRoots – Family Recipe Memory Kit ITA + ENG",
        "img": "https://public-files.gumroad.com/hjtno2tb27qg7fr9ij9go3rn9o7y",
        "link": "https://retotechlife.gumroad.com/l/CulinaryRoots",
        "html": '''
      <h1>CulinaryRoots – Family Recipe Memory Kit</h1>
      <p>A bilingual English + Italian digital kit to preserve family recipes, memories, gestures, and cooking secrets before they disappear.</p>
      <p>Some family recipes were never written down. They live in someone’s hands, in a grandmother’s memory, in a parent’s instinct.</p>
      <p>CulinaryRoots is a bilingual digital kit, available in English and Italian, created to help you collect, document, and preserve your own family recipes before they disappear.</p>
      <p>This kit guides you step by step through the process of recording a recipe from someone you love: the ingredients, approximate quantities, gestures, timing, memories, photos, cooking secrets, and the story behind the dish.</p>
'''
    },
    {
        "file": "purehome-suite.html",
        "title": "PureHome Suite",
        "img": "https://public-files.gumroad.com/zd8iyizosbhep7qhflqog70dd5qb",
        "link": "https://retotechlife.gumroad.com/l/PureHomeSuite",
        "html": '''
      <h1>PureHome Suite</h1>
      <p>PureHome Suite includes two local-first wellness software editions:</p>
      <p>PureHome Legacy — Personal Edition is designed for private homes, families and personal use. It helps users organize a guided home wellness journey, track progress, generate printable reports, create symbolic milestone certificates, and keep their data locally on their device.</p>
      <p>PureSpace Pro — Property Edition is designed for hotels, B&Bs, apartments, offices, condominiums, campsites, hostels, property managers and managed spaces. It helps users manage multiple rooms or properties, run a structured audit journey, generate space wellness reports, create printable certificates, and maintain a local vault of profiles and progress.</p>
      <p>Both editions include English and Italian support, local vault export/import, printable reports, printable certificates, and no cloud account requirement.</p>
'''
    },
    {
        "file": "hero-tale-english.html",
        "title": "Hero-Tale English — Screen-Free Audio Adventures for Kids",
        "img": "https://public-files.gumroad.com/l664dr31lu8b3gobqyk93mle7odn",
        "link": "https://retotechlife.gumroad.com/l/HeroTaleEnglish",
        "html": '''
      <h1>Hero-Tale English — Screen-Free Audio Adventures for Kids</h1>
      <p>5 gentle audio stories, calm routines, and printable magic cards to help children face everyday challenges without screens.</p>
      <p>Hero-Tale English is a screen-free storytelling kit for families with young children. Inside, you’ll find 5 gentle audio adventures where children become the heroes of everyday challenges: fear of the dark, the first day of school, big feelings, sleeping in their own bed, and missing a parent or caregiver.</p>
'''
    },
    {
        "file": "hero-tale-italiano.html",
        "title": "Hero-Tale Italiano — Avventure Audio Senza Schermi per Bambini",
        "img": "https://public-files.gumroad.com/7dx9b0e6hli1klr9yy0ps77hu71v",
        "link": "https://retotechlife.gumroad.com/l/HeroTaleItaliano",
        "html": '''
      <h1>Hero-Tale Italiano — Avventure Audio Senza Schermi per Bambini</h1>
      <p>5 avventure audio senza schermi per bambini, con mini routine calmanti, carte magiche stampabili, guide per genitori e certificati finali.</p>
      <p>Hero-Tale Italiano è un kit narrativo senza schermi pensato per famiglie con bambini piccoli. All’interno troverai 5 avventure audio dolci e coinvolgenti, dove il bambino diventa l’eroe di piccole sfide quotidiane.</p>
'''
    },
    {
        "file": "ai-contract-review.html",
        "title": "AI Contract Review Starter Kit",
        "img": "https://public-files.gumroad.com/10pka83g0pmn7mqafs4t3ntbpsna",
        "link": "https://retotechlife.gumroad.com/l/AIContractReview",
        "html": '''
      <h1>AI Contract Review Starter Kit</h1>
      <p>Prompt, checklist e template per leggere, riassumere e organizzare contratti con l’aiuto dell’AI, mantenendo controllo umano e fonti verificabili.</p>
      <p>L’AI Contract Review Starter Kit è un pacchetto digitale pensato per aiutarti a organizzare la lettura di contratti, accordi, NDA, documenti commerciali e materiali contrattuali con il supporto dell’AI, senza affidarti ciecamente alle risposte generate.</p>
'''
    },
    {
        "file": "aegis-pm.html",
        "title": "Aegis PM — Privacy-First AI Project Management",
        "img": "https://public-files.gumroad.com/zbgdxxoe90msvewya9y4ao3bydux",
        "link": "https://retotechlife.gumroad.com/l/AegisPM",
        "html": '''
      <h1>Aegis PM — Privacy-First AI Project Management</h1>
      <p>A full-stack prototype and sales kit for privacy-first AI project management workflows.</p>
      <p>Aegis PM is a complete enterprise-oriented demo kit for building, presenting, and validating privacy-first AI workflows for project and product management teams.</p>
      <p>The local backend redacts sensitive entities before AI processing, sends only tokenized content to the AI workflow, and reconstructs the final business output locally.</p>
'''
    }
]
"""
# Insert new products into the list
gen_content = gen_content.replace('    }\n]\n', '    },\n' + new_gen_products)

# Also fix the `new_products` append in generate_pages.py to not mess up things, we can just comment out the index.html update logic since we are updating it manually here.
gen_content = gen_content.replace('html = html.replace(\'        </div></div>\\n      </div>\\n    </section>\', new_products + \'\\n        </div></div>\\n      </div>\\n    </section>\')', 
                                  '# html = html.replace(...)')

with open("generate_pages.py", "w", encoding="utf-8") as f:
    f.write(gen_content)

# 2. UPDATE INDEX.HTML
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

# Update Product 19 Image
idx_content = re.sub(
    r'<article class="card">\s*<div class="product-badge">Product 19</div>\s*<div class="product-title">BoardForge</div>',
    '<article class="card">\\n            <div class="product-badge">Product 19</div>\\n            <div class="product-image-wrap"><img class="product-image" src="https://public-files.gumroad.com/pkhtlhprkjbggdc5p3vznm7bdh1s" alt="BoardForge"></div>\\n            <div class="product-title">BoardForge</div>',
    idx_content
)

# Update Product 20 Image
idx_content = re.sub(
    r'<article class="card">\s*<div class="product-badge">Product 20</div>\s*<div class="product-title">Creator M&A Valuation Vault</div>',
    '<article class="card">\\n            <div class="product-badge">Product 20</div>\\n            <div class="product-image-wrap"><img class="product-image" src="https://public-files.gumroad.com/4pkwhaqj2gdtrt4megnixraob5n2" alt="Creator M&A Valuation Vault"></div>\\n            <div class="product-title">Creator M&A Valuation Vault</div>',
    idx_content
)

new_cards = """
          <article class="card">
            <div class="product-badge">Product 22</div>
            <div class="product-image-wrap"><img class="product-image" src="https://public-files.gumroad.com/upm06nxg1pous5otq2jhcvvq0m60" alt="AI-Receptionist Agency Playbook"></div>
            <div class="product-title">AI-Receptionist Agency Playbook</div>
            <div class="mini-line"></div>
            <p class="product-desc">A complete operational toolkit that shows you how to build and sell AI receptionist services to local businesses.</p>
            <div class="price">€99</div>
            <div class="cta-row" style="margin-top:20px; flex-wrap: nowrap;">
              <a class="btn btn-secondary" style="flex:1" href="products/ai-receptionist-agency-playbook.html">Info Product</a>
              <a class="btn btn-primary" style="flex:1" href="https://retotechlife.gumroad.com/l/AIReceptionistAgencyPlaybook" target="_blank" rel="noopener noreferrer">Buy now</a>
            </div>
          </article>

          <article class="card">
            <div class="product-badge">Product 23</div>
            <div class="product-image-wrap"><img class="product-image" src="https://public-files.gumroad.com/hjtno2tb27qg7fr9ij9go3rn9o7y" alt="CulinaryRoots"></div>
            <div class="product-title">CulinaryRoots</div>
            <div class="mini-line"></div>
            <p class="product-desc">A bilingual English + Italian digital kit to preserve family recipes, memories, gestures, and cooking secrets before they disappear.</p>
            <div class="price">€29</div>
            <div class="cta-row" style="margin-top:20px; flex-wrap: nowrap;">
              <a class="btn btn-secondary" style="flex:1" href="products/culinaryroots.html">Info Product</a>
              <a class="btn btn-primary" style="flex:1" href="https://retotechlife.gumroad.com/l/CulinaryRoots" target="_blank" rel="noopener noreferrer">Buy now</a>
            </div>
          </article>

          <article class="card">
            <div class="product-badge">Product 24</div>
            <div class="product-image-wrap"><img class="product-image" src="https://public-files.gumroad.com/zd8iyizosbhep7qhflqog70dd5qb" alt="PureHome Suite"></div>
            <div class="product-title">PureHome Suite</div>
            <div class="mini-line"></div>
            <p class="product-desc">Local-first wellness software editions: PureHome Legacy (Personal Edition) and PureSpace Pro (Property Edition).</p>
            <div class="plan-box">
              <div class="plan-row"><div><div class="plan-name">Personal</div><div class="plan-text">PureHome Legacy</div></div><div class="plan-price">€59</div></div>
              <div class="plan-row"><div><div class="plan-name">Property</div><div class="plan-text">PureSpace Pro</div></div><div class="plan-price">€299</div></div>
            </div>
            <div class="cta-row" style="margin-top:20px; flex-wrap: nowrap;">
              <a class="btn btn-secondary" style="flex:1" href="products/purehome-suite.html">Info Product</a>
              <a class="btn btn-primary" style="flex:1" href="https://retotechlife.gumroad.com/l/PureHomeSuite" target="_blank" rel="noopener noreferrer">Choose your version</a>
            </div>
          </article>

          <article class="card">
            <div class="product-badge">Product 25</div>
            <div class="product-image-wrap"><img class="product-image" src="https://public-files.gumroad.com/l664dr31lu8b3gobqyk93mle7odn" alt="Hero-Tale English"></div>
            <div class="product-title">Hero-Tale English</div>
            <div class="mini-line"></div>
            <p class="product-desc">5 screen-free audio adventures for kids, with calm routines, printable magic cards, parent guides, and certificates.</p>
            <div class="price">€49</div>
            <div class="cta-row" style="margin-top:20px; flex-wrap: nowrap;">
              <a class="btn btn-secondary" style="flex:1" href="products/hero-tale-english.html">Info Product</a>
              <a class="btn btn-primary" style="flex:1" href="https://retotechlife.gumroad.com/l/HeroTaleEnglish" target="_blank" rel="noopener noreferrer">Buy now</a>
            </div>
          </article>

          <article class="card">
            <div class="product-badge">Product 26</div>
            <div class="product-image-wrap"><img class="product-image" src="https://public-files.gumroad.com/7dx9b0e6hli1klr9yy0ps77hu71v" alt="Hero-Tale Italiano"></div>
            <div class="product-title">Hero-Tale Italiano</div>
            <div class="mini-line"></div>
            <p class="product-desc">5 avventure audio senza schermi per bambini, con mini routine calmanti, carte magiche stampabili, guide per genitori e certificati finali.</p>
            <div class="price">€39</div>
            <div class="cta-row" style="margin-top:20px; flex-wrap: nowrap;">
              <a class="btn btn-secondary" style="flex:1" href="products/hero-tale-italiano.html">Info Product</a>
              <a class="btn btn-primary" style="flex:1" href="https://retotechlife.gumroad.com/l/HeroTaleItaliano" target="_blank" rel="noopener noreferrer">Buy now</a>
            </div>
          </article>

          <article class="card">
            <div class="product-badge">Product 27</div>
            <div class="product-image-wrap"><img class="product-image" src="https://public-files.gumroad.com/10pka83g0pmn7mqafs4t3ntbpsna" alt="AI Contract Review Starter Kit"></div>
            <div class="product-title">AI Contract Review Starter Kit</div>
            <div class="mini-line"></div>
            <p class="product-desc">Prompt, checklist e template per leggere, riassumere e organizzare contratti con l’aiuto dell’AI, mantenendo controllo umano.</p>
            <div class="plan-box">
              <div class="plan-row"><div><div class="plan-name">Starter</div></div><div class="plan-price">€97</div></div>
              <div class="plan-row featured-plan"><div><div class="plan-name">Pro</div></div><div class="plan-price">€197</div></div>
              <div class="plan-row"><div><div class="plan-name">Premium</div></div><div class="plan-price">€497</div></div>
            </div>
            <div class="cta-row" style="margin-top:20px; flex-wrap: nowrap;">
              <a class="btn btn-secondary" style="flex:1" href="products/ai-contract-review.html">Info Product</a>
              <a class="btn btn-primary" style="flex:1" href="https://retotechlife.gumroad.com/l/AIContractReview" target="_blank" rel="noopener noreferrer">Choose your version</a>
            </div>
          </article>

          <article class="card">
            <div class="product-badge">Product 28</div>
            <div class="product-image-wrap"><img class="product-image" src="https://public-files.gumroad.com/zbgdxxoe90msvewya9y4ao3bydux" alt="Aegis PM"></div>
            <div class="product-title">Aegis PM</div>
            <div class="mini-line"></div>
            <p class="product-desc">A full-stack prototype and sales kit for privacy-first AI project management workflows.</p>
            <div class="plan-box">
              <div class="plan-row"><div><div class="plan-name">Starter</div></div><div class="plan-price">€299</div></div>
              <div class="plan-row featured-plan"><div><div class="plan-name">Commercial</div></div><div class="plan-price">€599</div></div>
              <div class="plan-row"><div><div class="plan-name">Agency</div></div><div class="plan-price">€1499</div></div>
            </div>
            <div class="cta-row" style="margin-top:20px; flex-wrap: nowrap;">
              <a class="btn btn-secondary" style="flex:1" href="products/aegis-pm.html">Info Product</a>
              <a class="btn btn-primary" style="flex:1" href="https://retotechlife.gumroad.com/l/AegisPM" target="_blank" rel="noopener noreferrer">Choose your version</a>
            </div>
          </article>
"""

idx_content = idx_content.replace(
    '        </div></div>\n      </div>\n    </section>',
    new_cards + '\n        </div></div>\n      </div>\n    </section>'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)
