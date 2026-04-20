import os
import re

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Retro Tech Life</title>
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg: #0d0c0c;
      --panel: rgba(255,255,255,0.04);
      --panel-strong: rgba(255,255,255,0.06);
      --text: #f3eadb;
      --muted: #cfbea4;
      --faint: #9d907d;
      --line: rgba(214, 181, 112, 0.25);
      --gold: #caa25e;
      --gold-soft: #e6c88e;
      --button-text: #15120d;
      --shadow: 0 18px 60px rgba(0, 0, 0, 0.35);
      --radius: 24px;
      --max: 800px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
    }}

    body {{
      font-family: "Inter", sans-serif;
      line-height: 1.7;
      letter-spacing: 0.01em;
      color: var(--text);
      background: #0d0c0c;
    }}

    a {{
      color: inherit;
      text-decoration: none;
    }}

    .container {{
      width: min(92%, var(--max));
      margin: 0 auto;
    }}

    .topbar {{
      position: sticky;
      top: 0;
      z-index: 50;
      border-bottom: 1px solid var(--line);
      background: rgba(13, 12, 12, 0.82);
      backdrop-filter: blur(12px);
    }}

    .topbar-inner {{
      min-height: 78px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 20px;
      flex-wrap: wrap;
      width: min(92%, 1220px);
      margin: 0 auto;
    }}

    .brand {{
      font-family: "Cormorant Garamond", serif;
      font-size: 2rem;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--gold-soft);
      white-space: nowrap;
    }}

    .nav {{
      display: flex;
      gap: 24px;
      flex-wrap: wrap;
    }}

    .nav a {{
      color: var(--muted);
      font-size: 0.95rem;
      transition: 0.25s ease;
    }}

    .nav a:hover {{
      color: var(--gold-soft);
    }}
    
    .content-section {{
        padding: 80px 0;
    }}

    h1 {{
      font-family: "Cormorant Garamond", serif;
      font-size: clamp(2.5rem, 6vw, 4rem);
      font-weight: 600;
      line-height: 1.1;
      margin-bottom: 30px;
      color: var(--gold-soft);
    }}

    h2, h3, h4 {{
      font-family: "Cormorant Garamond", serif;
      font-weight: 600;
      color: var(--gold-soft);
      margin-top: 40px;
      margin-bottom: 15px;
    }}
    
    h3 {{ font-size: 2rem; }}
    h4 {{ font-size: 1.5rem; }}

    p, ul {{
      margin-bottom: 20px;
      color: var(--muted);
      font-size: 1.1rem;
    }}
    
    ul {{
        padding-left: 20px;
    }}
    
    li {{
        margin-bottom: 10px;
    }}

    .btn {{
      display: inline-flex;
      justify-content: center;
      align-items: center;
      min-height: 50px;
      padding: 0 30px;
      border-radius: 999px;
      border: 1px solid var(--gold);
      font-weight: 500;
      transition: 0.25s ease;
      cursor: pointer;
      font-size: 1.1rem;
    }}

    .btn-primary {{
      background: var(--gold);
      color: var(--button-text);
      box-shadow: var(--shadow);
    }}

    .btn-primary:hover {{
      background: var(--gold-soft);
      transform: translateY(-2px);
    }}

    .product-header-img {{
        width: 100%;
        border-radius: 18px;
        border: 1px solid var(--line);
        margin-bottom: 40px;
    }}

    .cta-box {{
        margin-top: 60px;
        padding: 40px;
        border: 1px solid var(--line);
        border-radius: var(--radius);
        background: var(--panel);
        text-align: center;
    }}

    @media (max-width: 640px) {{
      .topbar-inner {{
        padding: 14px 0;
      }}
      .brand {{
        font-size: 1.45rem;
      }}
    }}
  </style>
</head>
<body>

  <header class="topbar">
    <div class="topbar-inner">
      <a href="../" class="brand">Retro Tech Life</a>
      <nav class="nav">
        <a href="../#home">Home</a>
        <a href="../#shop">Shop</a>
        <a href="../#journal">Journal</a>
      </nav>
    </div>
  </header>

  <main class="content-section">
    <div class="container">
      <a href="../#shop" style="color: var(--gold); margin-bottom: 20px; display: inline-block;">&larr; Back to Shop</a>
      
      {img_html}
      
      {content_html}

      <div class="cta-box">
        <h3 style="margin-top: 0;">Pronto per l'acquisto?</h3>
        <p style="margin-bottom: 30px;">Scegli la versione che preferisci su Gumroad.</p>
        <a class="btn btn-primary" href="{gumroad_link}" target="_blank" rel="noopener noreferrer">Acquista Ora su Gumroad</a>
      </div>

    </div>
  </main>

</body>
</html>
"""

products = [
    {
        "file": "vampire-subscription-tracker.html",
        "title": "Vampire Subscription Tracker",
        "img": "https://public-files.gumroad.com/tl7cdvyde1v2um7s7hwr4dzednlp",
        "link": "https://retotechlife.gumroad.com/l/SubscriptionTracker_____",
        "html": """
      <h1>Vampire Subscription Tracker: Smetti di perdere soldi per abbonamenti che hai dimenticato</h1>
      <p>Quanti abbonamenti stai pagando in questo esatto momento? Software che non usi più, periodi di prova (free trial) che ti sei dimenticato di disdire, servizi di streaming che guardi una volta all'anno. Questi sono i "Vampiri": piccole spese ricorrenti che, silenziose, prosciugano il tuo conto in banca mese dopo mese.</p>
      <p>Il <strong>Vampire Subscription Tracker</strong> è stato creato per darti il controllo immediato sulle tue finanze personali o aziendali.</p>
      <h3>Cos'è e come funziona?</h3>
      <p>È un foglio di calcolo (spreadsheet) estremamente semplice e adatto anche ai principianti, progettato per aiutarti a individuare a colpo d'occhio tutti gli addebiti ricorrenti nascosti tra le tue spese mensili.</p>
      <p>Il processo è banale ma potente:</p>
      <ul>
        <li>Copia e incolla le tue transazioni recenti.</li>
        <li>Controlla i pagamenti ricorrenti che il foglio evidenzierà.</li>
        <li>Scopri esattamente quanti soldi stai sprecando in abbonamenti inutili, trial dimenticati e servizi a basso utilizzo.</li>
      </ul>
      <h3>Perché scaricarlo?</h3>
      <p>Se vuoi fare un <em>audit</em> rapido e spietato delle tue uscite ma non hai tempo né voglia di costruire un file Excel o Notion da zero, questo strumento fa esattamente al caso tuo.</p>
      <p><strong>Il vantaggio migliore?</strong> È un prodotto standalone <strong>100% gratuito</strong>. Scaricalo oggi, usalo in 5 minuti e inizia a recuperare i soldi che stavi letteralmente regalando.</p>
"""
    },
    {
        "file": "irl-event-engine.html",
        "title": "IRL Event Engine",
        "img": "https://public-files.gumroad.com/0mgsflg74fts94w7gf0byk03yc9y",
        "link": "https://retotechlife.gumroad.com/l/irl-event-engine",
        "html": """
      <h1>IRL Event Engine: Il Motore per i tuoi Eventi dal Vivo (In Real Life)</h1>
      <p>Riunire le persone in una stanza fa molto di più che riempire dei posti a sedere. Un evento dal vivo ben riuscito costruisce fiducia, trasforma i semplici follower in una vera community e offre un'esperienza tangibile ed esclusiva del tuo brand.</p>
      <p>Ma organizzare tutto questo da zero può diventare rapidamente un incubo fatto di budget sforati, location sbagliate e logistica disastrosa.</p>
      <p>L'<strong>IRL Event Engine</strong> è il sistema "plug-and-play" per <em>pianificare, finanziare, ospitare e riutilizzare (repurpose)</em> un evento locale premium, eliminando completamente l'ansia dell'improvvisazione. Che si tratti di un raduno privato, un pop-up brandizzato, un workshop o un meetup della tua community, questo toolkit strutturato ti guida dall'idea all'esecuzione con massima chiarezza e zero tempo sprecato.</p>
      <h3>A chi si rivolge?</h3>
      <p>È lo strumento perfetto per:</p>
      <ul>
        <li>Creator che vogliono monetizzare un'audience locale.</li>
        <li>Coach ed educatori che vogliono posizionarsi come brand "Premium".</li>
        <li>Community builder alla ricerca di un coinvolgimento (engagement) reale offline.</li>
        <li>Freelance, agenzie e piccoli brand che creano esperienze locali indimenticabili.</li>
      </ul>
      <h3>Come è strutturato? Scegli il tuo livello:</h3>
      <p><strong>🎯 Starter: Pianifica il tuo evento senza caos</strong><br>La struttura fondamentale per organizzare la logistica e non perdere soldi.<br><em>Cosa include:</em> Dashboard di pianificazione, calcolatori di budget e di punto di pareggio (break-even), checklist per la selezione della location, timeline dell'evento, task tracker e template per la scaletta (run-of-show).</p>
      <p><strong>💰 Pro: Finanzia l'evento con Sponsor e Partner locali</strong><br>Tutto ciò che c'è nello Starter, più gli strumenti per far pagare l'evento ad altri.<br><em>Cosa include:</em> Playbook per il contatto degli sponsor, template per il Pitch Deck, script esatti per email e DM da inviare ai partner, modelli per le offerte di sponsorizzazione e tracker delle partnership.</p>
      <p><strong>🚀 Professional: Trasforma un singolo evento in ROI a lungo termine</strong><br>Tutto ciò che c'è nel Pro, più la strategia per amplificare l'evento online.<br><em>Cosa include:</em> Piano per la cattura dei contenuti (shot list per video/foto), flusso di lavoro per i video brevi (short-form), framework di "repurposing", calendario dei contenuti post-evento e il playbook per massimizzare il Ritorno sull'Investimento.</p>
      <h3>Perché questo sistema funziona?</h3>
      <p>L'IRL Event Engine non ti dà semplice "ispirazione astratta". Ti fornisce i fogli di calcolo, gli script e i framework operativi reali. E soprattutto, ti insegna che l'evento non finisce quando gli ospiti se ne vanno: se documentato e riutilizzato correttamente, diventerà un generatore di contenuti e attenzione per i mesi a venire.</p>
"""
    },
    {
        "file": "micro-saas-in-a-box.html",
        "title": "Micro-SaaS In A Box",
        "img": "https://public-files.gumroad.com/9od3gwi3cwkjn1c9lbupk70iixn1",
        "link": "https://retotechlife.gumroad.com/l/micro-saas-in-a-box",
        "html": """
      <h1>Micro-SaaS In A Box: Lancia e monetizza il tuo Software senza scrivere una riga di codice</h1>
      <p>Hai una grande idea per un software o uno strumento digitale, ma ti blocchi davanti alla complessità tecnica? Oppure non hai i capitali (e il tempo) per assumere un team di sviluppatori?</p>
      <p>Non sei il solo. Oggi, i creator e gli indie hacker di maggior successo non passano mesi a programmare: usano ecosistemi no-code intelligenti.</p>
      <p>Il <strong>Micro-SaaS In A Box</strong> è l'acceleratore definitivo. Ti fornisce i sistemi collaudati, i template e gli asset necessari per passare da una semplice idea a un prodotto "live" e profittevole nel minor tempo possibile. Niente tentativi alla cieca, niente mesi sprecati in sviluppo: lanci in giorni, non in mesi.</p>
      <h3>I Benefici Principali</h3>
      <ul>
        <li><strong>Zero Codice, Zero Barriere:</strong> Salta l'ostacolo tecnico sfruttando infrastrutture no-code già testate.</li>
        <li><strong>Esecuzione Immediata:</strong> Usa un framework passo-passo che elimina le congetture. Segui il processo, lancia il prodotto e inizia a incassare.</li>
        <li><strong>Sistemi Reali:</strong> Basato su flussi di lavoro (workflow) di veri SaaS, adattati per essere gestiti da una sola persona.</li>
        <li><strong>Unico Pagamento:</strong> Accesso immediato, nessun abbonamento mensile. Paghi una volta e costruisci il tuo SaaS.</li>
      </ul>
      <h3>Quale versione si adatta meglio alle tue esigenze?</h3>
      <p><strong>📦 Starter — La fondazione strategica (Perfetto per validare l'idea)</strong><br>Tutto ciò che ti serve per strutturare un'offerta che si vende da sola.<br><em>Include:</em> Framework per l'offerta e il posizionamento, architettura del prodotto a livelli, template per la strategia di prezzo e roadmap di lancio.</p>
      <p><strong>🚀 Premium — Il pacchetto per costruire e lanciare (Consigliato)</strong><br>I tuoi asset di vendita e costruzione pronti all'uso.<br><em>Include tutto ciò che c'è nello Starter, più:</em> Template per landing page e funnel, sequenze email, template di database, setup della struttura no-code e playbook per casi d'uso reali.</p>
      <p><strong>💼 Pro — Il business-in-a-box completo per scalare (Per professionisti)</strong><br>Il pacchetto definitivo "Publish-Ready".<br><em>Include tutto ciò che c'è nel Premium, più:</em> File del sistema di delivery, tutti gli asset grafici editabili, template legali di base, impostazione avanzata del checkout e la checklist finale di lancio.</p>
"""
    },
    {
        "file": "ghost-mode-sabbatical-protocol.html",
        "title": "Ghost-Mode Sabbatical Protocol",
        "img": "https://public-files.gumroad.com/rktiyc5tfrtz62hh8u92w7blr3fe",
        "link": "https://retotechlife.gumroad.com/l/Ghost-Mode",
        "html": """
      <h1>Ghost-Mode Sabbatical Protocol: Il tuo Reset Digitale di 30 Giorni</h1>
      <p>Senti di essere a un passo dal <em>burnout</em> digitale? Sei un professionista del web, un freelancer o un manager che sogna di staccare completamente per 30 giorni, ma il terrore di vedere il proprio business crollare te lo impedisce?</p>
      <p>La verità è che nel mondo moderno spegnere il telefono non basta: se non prepari il terreno, passerai la vacanza a preoccuparti delle email accumulate o dei clienti in attesa.</p>
      <p>Il <strong>Ghost-Mode Sabbatical Protocol</strong> è il sistema definitivo per premere il tasto "Pausa" senza distruggere ciò che hai costruito. Attraverso un piano meticolosamente strutturato e sistemi automatizzati, questo protocollo garantisce che la tua vita digitale (e il tuo business) continuino a funzionare senza intoppi mentre tu ti concentri sull'unica cosa che conta: ricaricare la mente.</p>
      <h3>Cos'è e perché è indispensabile?</h3>
      <p>Il protocollo è il tuo "pulsante di reset digitale". È stato progettato per chi ha la necessità vitale di recuperare energie, ma non può permettersi di perdere il controllo operativo. Ti permette di assentarti in totale "Ghost-Mode", delegando e automatizzando tutto il necessario affinché, al tuo ritorno, non ci sia nessun incendio da spegnere.</p>
      <h3>I Benefici Principali</h3>
      <ul>
        <li><strong>Libertà senza sensi di colpa:</strong> Prenditi 30 giorni di stacco totale con la certezza matematica che il tuo ecosistema aziendale è al sicuro.</li>
        <li><strong>Transizione perfetta:</strong> Impara come uscire di scena senza traumi per te e per i tuoi clienti, grazie a un piano di avvicinamento guidato.</li>
        <li><strong>Rientro Zero-Stress:</strong> La vera paura delle ferie è il ritorno. Con questo sistema, il tuo rientro sarà fluido e gestito dall'intelligenza artificiale, senza l'ansia di mille email non lette.</li>
      </ul>
      <h3>Cosa include il Protocollo?</h3>
      <p>Riceverai immediatamente l'accesso a tutti gli strumenti operativi:</p>
      <ul>
        <li><strong>60-Day Planner:</strong> La tua mappa esatta per preparare il terreno in vista del reset digitale. Non si spegne tutto da un giorno all'altro, si pianifica l'uscita.</li>
        <li><strong>Delegation OS:</strong> Sistemi operativi pronti all'uso per permettere al tuo team (o ai tuoi collaboratori) di gestire in autonomia le urgenze senza mai doverti contattare.</li>
        <li><strong>AI Re-Entry System:</strong> Un potente strumento basato sull'Intelligenza Artificiale che, al tuo rientro, smaltirà rapidamente email, aggiornamenti e trend accumulati durante la pausa.</li>
        <li><strong>Bonus Pack:</strong> Strumenti e template extra per potenziare il tuo benessere digitale quotidiano, non solo in vacanza.</li>
      </ul>
"""
    },
    {
        "file": "digital-heirloom-protocol.html",
        "title": "Digital Heirloom Protocol",
        "img": "https://public-files.gumroad.com/w0b4p2qdumqjwt8j87skl71z92dm",
        "link": "https://retotechlife.gumroad.com/l/DigitalHeirloom",
        "html": """
      <h1>Digital Heirloom Protocol: Metti al sicuro la tua eredità digitale</h1>
      <p>Passiamo anni della nostra vita a costruire patrimoni, aziende e routine nel mondo digitale, ma raramente ci fermiamo a pensare a cosa accadrebbe se improvvisamente non potessimo più gestirli.</p>
      <p>Il risultato di questa mancanza di preparazione è purtroppo prevedibile: account perduti per sempre, fondi o crypto congelati, abbonamenti aziendali che continuano a scalare soldi, sistemi inaccessibili e familiari costretti a ricostruire tutto da zero, in momenti di forte stress emotivo.</p>
      <p>Il <strong>Digital Heirloom Protocol</strong> è il sistema premium per prevenire tutto questo: ti aiuta a mettere in sicurezza la tua eredità digitale, prima che sia la vita a costringere qualcun altro a dover tirare a indovinare.</p>
      <h3>Cos'è e perché è indispensabile?</h3>
      <p>Questo Protocollo non è un servizio cloud in abbonamento, né un servizio di custodia. <strong>Tu mantieni il 100% del controllo sui tuoi dati, sui tuoi account e sulle tue chiavi private.</strong></p>
      <p>È un framework strutturato e privato che ti guida nel documentare ciò che conta davvero, proteggendolo in modo adeguato, e garantendo che le persone giuste possano agire al momento giusto senza confusione o panico.</p>
      <h3>I Benefici Principali</h3>
      <ul>
        <li><strong>Zero Custodia, Massima Privacy:</strong> I tuoi dati sensibili rimangono sotto il tuo esclusivo controllo (Privacy-first).</li>
        <li><strong>Oltre le semplici password:</strong> Progettato per asset reali (portafogli crypto, accessi aziendali, documenti familiari), non è un semplice password manager.</li>
        <li><strong>Porta ordine nel caos:</strong> Elimina l'ansia del "cosa succederebbe se..." lasciando a chi ami chiarezza e non confusione.</li>
      </ul>
      <h3>Cosa ti aiuta a organizzare?</h3>
      <ul>
        <li>Account digitali e abbonamenti attivi.</li>
        <li>Portafogli di criptovalute e istruzioni per l'accesso (self-custody).</li>
        <li>Asset aziendali e account operativi.</li>
        <li>Archivi digitali personali e familiari.</li>
        <li>Istruzioni per l'accesso in caso di emergenza e deleghe.</li>
      </ul>
      <h3>Cosa è incluso?</h3>
      <ul>
        <li><strong>The Digital Heirloom Protocol Manual:</strong> La guida passo-passo per strutturare la tua legacy in modo chiaro e sicuro.</li>
        <li><strong>The Vault Workbook:</strong> Un documento operativo di accompagnamento per fare l'inventario dei tuoi asset.</li>
        <li><strong>Implementation Framework:</strong> Il sistema per completare il setup in modo veloce e mirato.</li>
        <li><strong>Bonus Video Esclusivo.</strong></li>
      </ul>
"""
    },
    {
        "file": "agentic-seo-os.html",
        "title": "Agentic SEO OS",
        "img": "https://public-files.gumroad.com/qi52ffy61jmyfg47685rgox1xgn0",
        "link": "https://retotechlife.gumroad.com/l/AgenticSEOOS",
        "html": """
      <h1>Agentic SEO OS™: Struttura i tuoi dati per dominare il mercato AI</h1>
      <p>La maggior parte dei brand ha un problema enorme che non sa ancora di avere: <strong>i loro siti web sono ottimizzati solo per gli esseri umani</strong>.</p>
      <p>Strumenti come ChatGPT, Perplexity o i nuovi agenti di shopping basati su AI non vengono sedotti da un bel layout grafico. Hanno bisogno di informazioni strutturate, specifiche e affidabili per capire cos'è un prodotto, a chi serve, come si paragona alle alternative e se il tuo brand è una scelta commerciale sicura. <strong>Se il tuo catalogo è confuso, il tuo brand diventerà invisibile.</strong></p>
      <h3>Cos'è e perché è indispensabile?</h3>
      <p><strong>Agentic SEO OS™</strong> non è la solita guida generica alla SEO tradizionale. È un <strong>sistema operativo e digitale professionale</strong> ideato per aiutarti a ristrutturare il tuo catalogo per renderlo "AI-ready" (pronto per essere scoperto dall'Intelligenza Artificiale).</p>
      <p>Ti fornisce un framework estremamente pratico per trasformare elementi come: descrizioni dei prodotti, specifiche tecniche, logiche di prezzo, politiche di reso e segnali di fiducia in asset cristallini e <strong>leggibili dalle macchine (machine-readable)</strong>.</p>
      <h3>I Benefici Principali</h3>
      <ul>
        <li><strong>Visibilità nel nuovo web:</strong> Fai in modo che i motori di intelligenza artificiale raccomandino i tuoi prodotti rispetto a quelli della concorrenza.</li>
        <li><strong>Dalla teoria alla pratica:</strong> Niente concetti astratti. Ti offre un meccanismo concreto per ristrutturare i tuoi dati affinché le AI possano valutarli con sicurezza.</li>
        <li><strong>La Promessa Centrale:</strong> In soli 7 giorni puoi ristrutturare la logica di base del tuo catalogo, rendendolo più chiaro, più facilmente paragonabile e perfettamente leggibile dall'AI.</li>
      </ul>
      <h3>Cosa otterrai all'interno del sistema?</h3>
      <p>A seconda della versione scelta, avrai accesso a: documenti strategici di framework, linee guida pratiche per l'implementazione, sistemi di prompt avanzati, protocolli per testare la risposta dell'AI (AI testing), e logiche strutturate per migliorare radicalmente la tua visibilità tecnica.</p>
"""
    },
    {
        "file": "dpp-readiness-system.html",
        "title": "DPP Readiness System",
        "img": "https://public-files.gumroad.com/vnfu6ge2o9ge9znjeb3kntnk86qf",
        "link": "https://retotechlife.gumroad.com/l/dpp-readiness-system",
        "html": """
      <h1>DPP Readiness System: Prepara il tuo Brand all'era del Passaporto Digitale</h1>
      <p>Il mercato europeo sta cambiando e la trasparenza non è più solo una parola di marketing: sta diventando un requisito. Con l'avvento imminente del <em>Digital Product Passport (DPP)</em>, la vera sfida per i brand non è solo produrre bene, ma saper tracciare e documentare come lo si fa.</p>
      <p>Sei circondato da confusione legale, fogli Excel disordinati e comunicazioni frammentate con i fornitori? Il <strong>DPP Readiness System</strong> è la bussola operativa di cui hai bisogno per mettere in ordine i tuoi dati prima che diventi un'emergenza.</p>
      <h3>Cos'è e perché è indispensabile?</h3>
      <p>Questo non è un noioso manuale legale. È un <strong>kit di implementazione pratico</strong> progettato specificamente per piccoli brand di moda, artigiani e business e-commerce D2C. Il suo scopo è aiutarti a creare un flusso di lavoro pulito e strutturato per raccogliere, organizzare e documentare i dati dei tuoi prodotti e della tua filiera.</p>
      <p>Invece di partire da zero e perderti nel "caos dei fornitori", avrai un sistema operativo pronto all'uso (adattabile facilmente a Notion o Airtable) che ti permetterà di trasformare l'obbligo della tracciabilità in un vero e proprio <strong>asset di valore per il tuo brand</strong>.</p>
      <h3>I Benefici Principali</h3>
      <ul>
        <li><strong>Tutto in un unico posto:</strong> Dì addio ai dati sparsi. Centralizza le informazioni sui prodotti e ottimizza il flusso di comunicazione con i fornitori.</li>
        <li><strong>Mappa la tua Supply Chain:</strong> Ottieni una visione chiara e mappata degli elementi essenziali della tua filiera produttiva.</li>
        <li><strong>Crea il tuo "DPP Pilota":</strong> Struttura un primo modello funzionante di Passaporto Digitale del Prodotto per essere pronto per le future normative.</li>
        <li><strong>Trasparenza come Marketing:</strong> Migliora la documentazione interna e trasforma la tracciabilità in una storia potente da raccontare ai tuoi clienti.</li>
      </ul>
      <h3>Quale versione scegliere?</h3>
      <p>Scegli il livello di profondità più adatto alla fase attuale del tuo business:</p>
      <ol>
        <li><strong>Starter:</strong> L'essenziale per un primo setup rapido e pulito.</li>
        <li><strong>Pro:</strong> Un sistema interno molto più completo e dettagliato.</li>
        <li><strong>Guided Implementation:</strong> Una struttura guidata per chi vuole un supporto più strutturato nell'implementazione.</li>
      </ol>
"""
    },
    {
        "file": "phygital-community-creator-asset-kit.html",
        "title": "Phygital Community & Creator Asset Kit",
        "img": "https://public-files.gumroad.com/9rkyfuuoocrpqb8m5vpk3qyp62xt",
        "link": "https://retotechlife.gumroad.com/l/phygital-community-creator-asset-kit",
        "html": """
      <h1>Phygital Community & Creator Asset Kit: Costruisci una lealtà reale, fuori dagli schermi</h1>
      <p>La tua audience può anche seguirti assiduamente online, ma c'è una verità innegabile: <strong>la vera lealtà si costruisce nel mondo reale (In Real Life).</strong></p>
      <p>I like e i commenti sono metriche superficiali. Se vuoi trasformare i tuoi follower in una vera e propria community o in clienti fedeli, devi superare la barriera digitale. Il <strong>Phygital Community & Creator Asset Kit</strong> è il sistema pratico per pianificare, organizzare e gestire un evento dal vivo senza dover improvvisare la logistica, la comunicazione o le fasi successive all'evento.</p>
      <h3>Perché è indispensabile oggi?</h3>
      <p>Il mercato digitale è saturo e l'algoritmo dei social network cambia continuamente le regole del gioco. Questo kit non serve semplicemente a "organizzare un meetup", ma è un asset strategico per <strong>creare un ecosistema proprietario che non dipende dai social media</strong>.</p>
      <h3>I Benefici Principali</h3>
      <ul>
        <li><strong>Zero improvvisazione:</strong> Saprai esattamente cosa fare, quando farlo e come gestire ogni aspetto operativo senza stress.</li>
        <li><strong>Monetizzazione intelligente:</strong> Avrai gli strumenti per trovare sponsor locali che coprano i costi (o generino profitto) fin dal giorno zero.</li>
        <li><strong>Effetto leva (Phygital):</strong> Imparerai a trasformare quell'unica esperienza dal vivo in settimane di contenuti brevi (short-form) perfetti per i tuoi canali online.</li>
        <li><strong>Relazioni a lungo termine:</strong> Un pubblico che ti stringe la mano e vive un'esperienza dal vivo si trasforma nella risorsa più forte del tuo brand.</li>
      </ul>
      <h3>Cosa troverai all'interno della versione Starter?</h3>
      <ul>
        <li><strong>Practical Event Playbook:</strong> La guida tattica passo-passo per strutturare il tuo evento.</li>
        <li><strong>Operations Dashboard Template:</strong> Un cruscotto per avere ogni singolo dettaglio logistico sempre sotto controllo.</li>
        <li><strong>Local Sponsorship Scripts:</strong> I testi esatti da usare per approcciare e chiudere accordi con gli sponsor locali.</li>
        <li><strong>Short-Form Repurposing System:</strong> Il sistema per estrarre contenuti virali dai video e dalle foto dell'evento.</li>
        <li><strong>30-Day Post-Event Follow-Up Plan:</strong> Il piano strategico per mantenere alta l'attenzione e convertire l'entusiasmo dei partecipanti.</li>
      </ul>
"""
    },
    {
        "file": "omnichannel-ai-content-dashboard.html",
        "title": "Omnichannel AI Content Dashboard",
        "img": "https://public-files.gumroad.com/b4w3gw4yf4xq6w7kxonn4cc39g8r",
        "link": "https://retotechlife.gumroad.com/l/qeimj",
        "html": """
      <h1>Omnichannel AI Content Dashboard: Moltiplica i tuoi contenuti in una frazione del tempo</h1>
      <p>Sei un content creator, un podcaster o un'agenzia? Allora sai benissimo che registrare un video lungo o un podcast è solo il 20% del lavoro. Il vero ostacolo è la distribuzione: prendere quel contenuto e trasformarlo in reel, post per LinkedIn, thread per X e newsletter, senza dover passare ore intere a riscrivere e tagliare.</p>
      <p>L'<strong>Omnichannel AI Content Dashboard</strong> è la soluzione definitiva per smettere di rincorrere le scadenze editoriali e iniziare a dominare ogni piattaforma.</p>
      <h3>Cos'è e perché è indispensabile?</h3>
      <p>Creare contenuti da zero per ogni singolo social network è insostenibile. Questo sistema ti permette di prendere <em>un singolo pezzo di contenuto lungo</em> (come un video YouTube o un episodio di un podcast) e trasformarlo in molteplici asset pronti per i social, sfruttando in modo strategico e ordinato l'Intelligenza Artificiale.</p>
      <p>Non si tratta di semplici prompt disordinati, ma di un flusso di lavoro (workflow) professionale e testato, costruito per farti risparmiare decine di ore ogni settimana e per garantire che la tua voce rimanga coerente su tutti i canali.</p>
      <h3>I Benefici Principali</h3>
      <ul>
        <li><strong>Massima Efficienza:</strong> Trasforma 1 contenuto lungo in 15+ post social in meno di un'ora.</li>
        <li><strong>Flusso di Lavoro Standardizzato:</strong> Elimina il blocco dello scrittore e la confusione grazie alle SOP (Standard Operating Procedures) incluse.</li>
        <li><strong>Pronto all'uso su Notion:</strong> Non dovrai costruire nulla da zero. Ti basta importare i file e iniziare a lavorare in un ambiente già strutturato e ottimizzato.</li>
        <li><strong>Scalabilità per Agenzie:</strong> Perfetto non solo per i singoli creator, ma anche per i team che gestiscono i contenuti di più clienti.</li>
      </ul>
      <h3>Cosa include l'Edizione Base?</h3>
      <p>Un kit completo pronto per l'importazione: AI Content Dashboard Blueprint, SOP Repurposing System, Libreria di Prompt AI, Guida al Setup su Notion, e File CSV preimpostati.</p>
      <h3>Fai il salto di livello con il "Complete Bundle"</h3>
      <p>Se vuoi eliminare anche il lavoro manuale di copia-incolla, il <em>Complete Bundle</em> include l'infrastruttura per automatizzare l'intero processo con Zapier Automation Setups, Advanced Workflow Guide e Automation Field Map.</p>
"""
    },
    {
        "file": "subscription-revenue-blueprint.html",
        "title": "Subscription Revenue Blueprint",
        "img": "https://public-files.gumroad.com/oyj6qswudxivmgxrxqjany1yzvkj",
        "link": "https://retotechlife.gumroad.com/l/isxrfk",
        "html": """
      <h1>Subscription Revenue Blueprint: Come trasformare i tuoi clienti in entrate ricorrenti</h1>
      <p>Se hai un brand nei settori <strong>Home, Pet o Beauty</strong>, sai bene quanto sia frustrante la continua rincorsa per acquisire nuovi clienti. L'advertising costa sempre di più e vendere prodotti fisici singolarmente significa che ogni mese il tuo fatturato riparte da zero.</p>
      <p>Ma cosa succederebbe se potessi aggiungere un livello di abbonamento <em>digitale</em> ai tuoi prodotti fisici, stabilizzando le entrate e fidelizzando la tua clientela, il tutto in soli 14 giorni?</p>
      <h3>Cos'è il Subscription Revenue Blueprint?</h3>
      <p>È il sistema definitivo progettato per i brand di e-commerce che vogliono creare entrate ricorrenti <strong>senza aggiungere nemmeno un briciolo di complessità logistica</strong>. Niente nuove spedizioni complesse, niente gestione del magazzino extra: solo una strategia mirata per massimizzare il valore nel tempo di chi ha già acquistato da te (Customer Lifetime Value o CLTV).</p>
      <h3>Perché è indispensabile per il tuo Brand?</h3>
      <p>Il mercato attuale punisce chi si affida esclusivamente agli acquisti una tantum. Se non costruisci un sistema per trattenere i clienti (Retention), stai letteralmente lasciando soldi sul tavolo. Avere un "layer" di abbonamento ti permette di:</p>
      <ul>
        <li><strong>Azzerare l'ansia del primo del mese</strong>, potendo contare su una base di fatturato (MRR) prevedibile e garantita.</li>
        <li><strong>Aumentare drasticamente il Lifetime Value</strong>, trasformando acquirenti casuali in veri e propri membri della tua community.</li>
        <li><strong>Evitare i classici incubi logistici</strong> tipici delle classiche "subscription box" fisiche, sfruttando invece leve digitali ad alto margine.</li>
      </ul>
      <h3>Cosa troverai all'interno del Bundle?</h3>
      <p>Non si tratta solo di teoria, ma di un kit pratico e pronto all'uso. Acquistando il Blueprint riceverai un download digitale immediato contenente:</p>
      <ul>
        <li>Il Blueprint Principale: La guida passo-passo per implementare il tuo sistema in 14 giorni.</li>
        <li>3 Case Studies Verticali: Esempi reali applicati.</li>
        <li>Retention Email Vault.</li>
        <li>Libreria degli "Offer Hook".</li>
        <li>Recurring Revenue Copy Pack.</li>
        <li>Checklist di Lancio.</li>
        <li>Calcolatore CLTV (Worksheet & Excel).</li>
      </ul>
"""
    },
    {
        "file": "branching-course-kit.html",
        "title": "Branching Course Kit",
        "img": "https://public-files.gumroad.com/fcjrjh7lbm6btpj3aa7e7e711a7c",
        "link": "https://retotechlife.gumroad.com/l/BranchingCourseKit",
        "html": """
      <h1>Branching Course Kit: Trasforma i tuoi corsi da noiosi a interattivi</h1>
      <p>La maggior parte dei corsi online segue una struttura terribilmente prevedibile: lezione 1, lezione 2, lezione 3... fino alla fine. Il risultato? L'attenzione cala e gli studenti si annoiano.</p>
      <p>Il <strong>Branching Course Kit</strong> è progettato per creator, coach e formatori che vogliono rivoluzionare questa dinamica, trasformando corsi lineari in esperienze di apprendimento interattive e dinamiche. Questo kit ti offre un metodo pratico per introdurre percorsi "a bivi" (branching logic), scelte significative per l'utente e percorsi formativi personalizzati, il tutto senza complicare eccessivamente il processo di creazione.</p>
      <p>Che tu voglia un semplice punto di partenza o un sistema avanzato e completo, questo kit ti fornirà la struttura esatta per creare corsi non lineari molto più coinvolgenti.</p>
      <h3>Cosa troverai all'interno?</h3>
      <p>Il pacchetto contiene tutto il necessario per progettare l'esperienza visiva e logica del corso:</p>
      <ul>
        <li>Guide in PDF passo-passo</li>
        <li>Template pronti all'uso</li>
        <li>Esempi di diagrammi di flusso (flowchart)</li>
        <li>Strutture a bivi preimpostate</li>
        <li>Script per accompagnare i passaggi</li>
        <li>Casi d'uso pratici</li>
        <li>Strumenti di implementazione</li>
      </ul>
      <h3>Quale versione scegliere?</h3>
      <ul>
        <li><strong>Starter:</strong> L'essenziale per costruire il tuo primo corso a bivi con un kit semplice, chiaro e super pratico.</li>
        <li><strong>Creator:</strong> Il pacchetto intermedio per costruire corsi ramificati strutturati, arricchiti con template, script e casi d'uso concreti per veri prodotti formativi.</li>
        <li><strong>Pro:</strong> Il sistema definitivo. Ottieni l'intero ecosistema con asset avanzati, strutture più profonde e strumenti di implementazione premium.</li>
      </ul>
"""
    },
    {
        "file": "cognito-ui.html",
        "title": "Cognito UI",
        "img": "https://public-files.gumroad.com/izxq3awpdjqqu5u7wnc8rpoz9cfs",
        "link": "https://retotechlife.gumroad.com/l/CognitoUI",
        "html": """
      <h1>Cognito UI: Il React UI Kit progettato per il comfort visivo</h1>
      <p>Le interfacce moderne sono spesso caotiche, dense e faticose per gli occhi. Il risultato? L'utente si stanca prima. <strong>Cognito UI</strong> è un kit di interfaccia utente per React focalizzato sul <em>comfort</em>, ideato per i team di sviluppo che vogliono costruire esperienze digitali più calme, chiare e adattive.</p>
      <p>Il vero fiore all'occhiello di questo kit è l'introduzione di un vero e proprio <strong>Comfort Mode</strong> con preferenze utente persistenti. Potrai offrire ai tuoi utenti opzioni per ridurre le animazioni (reduced motion), aumentare il contrasto, ingrandire la tipografia e creare spaziature più "traspiranti".</p>
      <p>Sviluppato con <strong>React, Next.js, Tailwind CSS e Framer Motion</strong>, Cognito UI aiuta gli sviluppatori a trasformare l'Accessibilità (Accessibility) da una noiosa checklist dell'ultimo minuto a una vera e propria <em>feature premium</em> del prodotto.</p>
      <p>È l'infrastruttura ideale per dashboard SaaS, pannelli di amministrazione, prodotti educativi, strumenti interni e qualsiasi interfaccia in cui la leggibilità e la riduzione dell'attrito visivo siano fondamentali.</p>
      <h3>Cosa include il sistema?</h3>
      <ul>
        <li>Provider per il Comfort Mode</li>
        <li>Gestione delle preferenze utente persistenti</li>
        <li>Logica avanzata per la riduzione delle animazioni</li>
        <li>Controlli per contrasto e leggibilità</li>
        <li>Componenti UI adattivi e reattivi</li>
        <li>Un'interfaccia Demo di esempio</li>
        <li>Documentazione completa e guide al setup</li>
      </ul>
      <h3>Scegli il tuo livello:</h3>
      <p><strong>🛠️ Foundation — €29</strong><br>Il nucleo del sistema Comfort Mode per React e Next.js.</p>
      <p><strong>✨ Refined — €49</strong><br>Un kit UI adattivo più elegante e rifinito per un'esperienza di comfort superiore.</p>
      <p><strong>🚀 Commercial — €69</strong><br>Il pacchetto completo Cognito UI, pronto per il lancio e per l'utilizzo in progetti commerciali.</p>
"""
    },
    {
        "file": "aura-sdk.html",
        "title": "Aura SDK",
        "img": "https://public-files.gumroad.com/r1xp0r88r2ez0gbjuc6lu3ox2x4n",
        "link": "https://retotechlife.gumroad.com/l/AuraSDK",
        "html": """
      <h1>Aura SDK: Intelligenza Audio e Analisi Emotiva in Python</h1>
      <p>Se sviluppi software, gestisci l'assistenza clienti o analizzi conversazioni, sai che una trascrizione nuda e cruda cattura solo una minima parte del reale significato di una frase. Per capire davvero un'interazione, devi poter "leggere" tra le righe.</p>
      <p><strong>Aura SDK</strong> è un toolkit basato su Python progettato specificamente per sviluppatori, analisti e team tecnici che vogliono estrarre segnali conversazionali (conversation signals) da audio multilingua, attraverso una pipeline moderna e pronta all'uso.</p>
      <p>Questa applicazione ti permette di caricare (o registrare) un file audio, trascriverlo automaticamente utilizzando il modello <em>Whisper</em>, rilevarne la lingua parlata e infine analizzare il testo con modelli basati su <em>Transformer</em> per produrre un'analisi di sentiment, emozioni e un "Empathy Score" finale.</p>
      <h3>A chi si rivolge?</h3>
      <p>È un punto di partenza tecnico ideale (una "foundation") per sviluppatori, analisti di conversazioni, team di customer support, software house e creator che stanno costruendo o esplorando l'ambito dell'Audio Intelligence.</p>
      <h3>Cosa include il Toolkit?</h3>
      <p>Riceverai un progetto pronto per essere esteso e personalizzato:</p>
      <ul>
        <li>Interfaccia visiva pronta all'uso sviluppata in Gradio.</li>
        <li>Trascrizione audio ad alta precisione alimentata da Whisper.</li>
        <li>Rilevamento automatico della lingua (Language detection).</li>
        <li>Analisi testuale di base per emozioni e sentiment.</li>
        <li>Calcolo dell'Empathy Score con alert visivi pensati per gli operatori.</li>
        <li>Codice sorgente Python completamente modulare e documentazione tecnica.</li>
      </ul>
      <p><em>Nota Importante: Aura SDK è uno strumento di supporto analitico. I risultati forniti dai modelli sono probabilistici e puramente indicativi. Non devono mai essere considerati come una "verità emotiva definitiva" o come un sostituto del giudizio critico umano.</em></p>
"""
    },
    {
        "file": "ethos-pro-suite.html",
        "title": "Ethos Pro Suite",
        "img": "https://public-files.gumroad.com/ags79hqvh2nvil9gpkzfcik7x44a",
        "link": "https://retotechlife.gumroad.com/l/EthosProSuite",
        "html": """
      <h1>Ethos Pro Suite: Il Toolkit per un'Intelligenza Artificiale più etica e sicura</h1>
      <p>Costruire prodotti basati sull'Intelligenza Artificiale significa gestire un potere enorme. Tuttavia, con questo potere arriva anche il rischio di bias cognitivi, interfacce troppo complesse e dataset compromessi.</p>
      <p>La <strong>Ethos Pro Suite</strong> è un toolkit modulare ideato per sviluppatori, team di prodotto AI, startup, agenzie e software house che vogliono costruire prodotti più equi, sicuri e adattivi, implementando solidi flussi di lavoro di "Responsible AI", senza mai sacrificare l'usabilità o la qualità del codice.</p>
      <p>Il pacchetto combina due sistemi premium in un'unica suite definitiva:</p>
      <h3>1. Morph Core (Interfacce Adattive)</h3>
      <p>Un set di componenti per <strong>React, Tailwind e Framer Motion</strong> progettato per creare interfacce "consapevoli del contesto". Morph Core permette alle tue dashboard e alle tue app di semplificarsi fluidamente in una modalità più sicura e a "basso carico cognitivo", adattandosi alle reali esigenze e allo stato dell'utente.</p>
      <h3>2. Atlas Audit Kit (Analisi dei Dataset)</h3>
      <p>Un framework pratico per l'auditing dei bias nei dataset testuali. L'obiettivo? Rilevare i problemi <em>prima</em> del lancio. Il kit include uno spazio di lavoro strutturato per l'audit, template per la reportistica e uno scanner in <strong>Python</strong> in grado di rilevare "red flags" (campanelli d'allarme) legati a pregiudizi di genere, lingua o differenze culturali all'interno dei tuoi dati.</p>
      <h3>Scegli la licenza adatta a te:</h3>
      <ul>
        <li><strong>Personal:</strong> Ideale per creatori singoli, sviluppatori indipendenti e uso puramente individuale.</li>
        <li><strong>Studio:</strong> La scelta perfetta per piccoli team e flussi di lavoro collaborativi interni.</li>
        <li><strong>Team / Commercial:</strong> Per aziende strutturate che desiderano utilizzare la suite per i propri prodotti interni e in ambienti di produzione su vasta scala.</li>
        <li><strong>Agency / Client Work:</strong> La licenza definitiva per agenzie, consulenti e team di sviluppo che utilizzano la suite in lavori commerciali consegnati direttamente ai loro clienti finali.</li>
      </ul>
"""
    },
    {
        "file": "sentient-ux-auditor.html",
        "title": "Sentient UX Auditor",
        "img": "https://public-files.gumroad.com/5lgsiolh1rd5dqg17naqn42y7mg2",
        "link": "https://retotechlife.gumroad.com/l/SentientUXAuditor",
        "html": """
      <h1>Sentient UX Auditor: Trova e correggi i "Dark Pattern" prima del lancio</h1>
      <p>Oggi, i team di sviluppo revisionano sistematicamente il codice per scovare bug, errori di accessibilità o incongruenze visive. Eppure, quasi nessuno analizza le interfacce per scovare linguaggio coercitivo, finte urgenze (FOMO) o percorsi decisionali manipolatori.</p>
      <p>Il risultato? La fiducia degli utenti crolla e il brand ne risente.</p>
      <p><strong>Sentient UX Auditor</strong> è una CLI (Command Line Interface) professionale in Node.js costruita proprio per colmare questa lacuna. Esegue una scansione dei tuoi file HTML e React/JSX per rilevare <em>Dark Pattern</em>, copy manipolatorio e altre forme di quello che chiamiamo <strong>Debito Tecnico Etico (Ethical Technical Debt)</strong>.</p>
      <h3>Cosa rileva esattamente lo scanner?</h3>
      <p>Sentient UX Auditor analizza il tuo codice e segnala pattern come:</p>
      <ul>
        <li><em>Confirmshaming</em> (manipolazione tramite il senso di colpa durante una disiscrizione).</li>
        <li>Falsa urgenza e linguaggio basato sulla FOMO (Fear Of Missing Out).</li>
        <li>Call to Action (CTA) coercitive o manipolatorie.</li>
        <li>Scelte di parole che riducono l'autonomia dell'utente.</li>
        <li>Segnali sospetti legati all'accessibilità cognitiva e pattern ARIA ambigui.</li>
      </ul>
      <p>Ogni problema trovato non si limita a essere segnalato: viene affiancato da un suggerimento pratico di riscrittura (in un linguaggio più chiaro) focalizzato sull'autonomia e la comprensione dell'utente.</p>
      <h3>Cosa otterrai dall'Audit?</h3>
      <p>Invece del classico commento soggettivo "questo testo non mi convince", otterrai dati rigorosi e strutturati: risultati categorizzati in base alla gravità, punteggio etico a livello di progetto, fasce di rischio e report pronti per essere esportati.</p>
      <h3>A chi si rivolge?</h3>
      <p>È lo strumento definitivo per UX/UI Designer, Sviluppatori Frontend, Team SaaS e agenzie che revisionano landing page, funnel di vendita e flussi di checkout.</p>
"""
    },
    {
        "file": "boardforge.html",
        "title": "BoardForge",
        "img": "", # Nessuna immagine fornita
        "link": "https://retotechlife.gumroad.com/l/BoardForge",
        "html": """
      <h1>BoardForge: Il tuo Consiglio di Amministrazione Virtuale</h1>
      <p>Prendere decisioni di business ad alto rischio completamente da soli è pericoloso, stressante e spesso molto costoso. Eppure, per molti founder e solopreneur, è l'unica via. Fino ad oggi.</p>
      <p><strong>BoardForge: Virtual Board of Directors Simulator</strong> è il sistema che trasforma ChatGPT o Claude nel tuo Consiglio di Amministrazione "sintetico", composto da 5 consiglieri iper-specializzati:</p>
      <ul>
        <li><strong>CFO Implacabile:</strong> per analizzare flussi di cassa, ROI e tasso di bruciatura dei fondi (burn rate).</li>
        <li><strong>CMO Aggressivo:</strong> per testare posizionamento, offerte e canali di crescita.</li>
        <li><strong>Consulente Legale Paranoico:</strong> per scovare rischi, analizzare contratti e compliance.</li>
        <li><strong>COO Operativo:</strong> per ottimizzare sistemi, trovare colli di bottiglia e valutare la scalabilità.</li>
        <li><strong>CEO Strategico:</strong> per soppesare i pro e i contro e prendere la decisione finale.</li>
      </ul>
      <h3>Molto più di un "Prompt"</h3>
      <p>Questo non è l'ennesimo comando copia-incolla. È un vero e proprio sistema di <em>Decision-Making</em> progettato non per darti risposte compiacenti, ma per sfidare le tue convinzioni, testare sotto pressione le tue idee da 5 angolazioni diverse e forzarti alla chiarezza. Invece di chiedere un singolo parere a un'AI generica, assisterai a un realistico dibattito esecutivo che si consoliderà in una raccomandazione strategica finale.</p>
      <h3>Cosa otterrai da una singola sessione?</h3>
      <p>Con un solo setup, BoardForge ti aiuterà a generare: Executive Summary, Analisi SWOT, Proiezioni Finanziarie a 3 anni, Registro dei Rischi, Piano d'azione a 90 giorni e un Verdetto Strategico finale (Go / Pivot / Delay / No-Go).</p>
      <h3>Nessuna barriera tecnica</h3>
      <p>Niente codice. Nessuna API da configurare. Nessun software da installare. Ti basterà importare i file forniti nel tuo account ChatGPT o Claude, incollare la tua idea di business e lasciare che il Consiglio inizi a lavorare.</p>
"""
    },
    {
        "file": "creator-ma-valuation-vault.html",
        "title": "Creator M&A Valuation Vault",
        "img": "", # Nessuna immagine fornita
        "link": "https://retotechlife.gumroad.com/l/MandA",
        "html": """
      <h1>The Money and the Power: La "Cassaforte" per la Valutazione e l'Acquisizione di Asset Digitali</h1>
      <p>La Creator Economy sta cambiando rapidamente e le regole del gioco si stanno evolvendo. Il prossimo livello non è più la semplice "crescita" dei follower, ma la <strong>Proprietà (Ownership)</strong>.</p>
      <p><em>The Money and the Power: Creator M&A Valuation Vault</em> è il toolkit digitale premium costruito per founder, creator, operatori di newsletter e media builders che vogliono comprendere il <em>vero</em> valore degli asset digitali e muoversi con sicurezza nel mondo delle acquisizioni, delle exit e delle partnership strategiche.</p>
      <p>Non si tratta di teoria, ma di un sistema pratico per valutare newsletter, canali YouTube e community, utilizzando logiche e metriche specifiche per i creator, non noiosi e inadatti template aziendali.</p>
      <h3>Scegli il tuo livello di ambizione:</h3>
      <p><strong>1) The Observer ($49) – Il toolkit esplorativo</strong><br>Ideale se vuoi esplorare il mondo delle acquisizioni per la prima volta e capire se un target vale la pena di essere analizzato.</p>
      <p><strong>2) The Dealmaker ($149) – L'arsenale operativo (Il più scelto)</strong><br>Il pacchetto principale per operatori seri e agenzie che vogliono valutare un asset e avviare veri e propri negoziati. Include Modelli di valutazione specifici (Newsletter, YouTube, Community).</p>
      <p><strong>3) The Empire Builder ($349) – Il sistema per chi pensa in grande</strong><br>Il bundle premium completo per compratori esperti, roll-up operator e founder che preparano exit strutturate.</p>
      <h3>Cosa rende questo Vault diverso dagli altri?</h3>
      <p>La maggior parte dei modelli di M&A è generica. Questo vault è stato progettato basandosi sulle metriche che contano davvero in questo ecosistema: Qualità dell'audience, Rischio di dipendenza dalla piattaforma, Concentrazione delle entrate, Tasso d'abbandono (Churn), Proprietà intellettuale (IP) e Reale trasferibilità dell'asset.</p>
"""
    }
]

for p in products:
    filepath = os.path.join("products", p["file"])
    img_html = f'<img src="{p["img"]}" alt="{p["title"]}" class="product-header-img">' if p["img"] else ''
    content = TEMPLATE.format(
        title=p["title"],
        img_html=img_html,
        content_html=p["html"],
        cta_title="Pronto per l'acquisto?",
        cta_desc="Scegli la versione che preferisci su Gumroad.",
        gumroad_link=p["link"]
    )
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(products)} files.")

# Update index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# I will use a simple find and replace for the buttons in index.html to add the Info Product button.
# Since the HTML structure is somewhat consistent but varies, let's just do a smart regex or replace loop based on the links.

replacements = {
    "https://retotechlife.gumroad.com/l/SubscriptionTracker_____": "vampire-subscription-tracker.html",
    "https://retotechlife.gumroad.com/l/irl-event-engine": "irl-event-engine.html",
    "https://retotechlife.gumroad.com/l/micro-saas-in-a-box": "micro-saas-in-a-box.html",
    "https://retotechlife.gumroad.com/l/Ghost-Mode": "ghost-mode-sabbatical-protocol.html",
    "https://retotechlife.gumroad.com/l/DigitalHeirloom": "digital-heirloom-protocol.html",
    "https://retotechlife.gumroad.com/l/AgenticSEOOS": "agentic-seo-os.html",
    "https://retotechlife.gumroad.com/l/dpp-readiness-system": "dpp-readiness-system.html",
    "https://retotechlife.gumroad.com/l/phygital-community-creator-asset-kit": "phygital-community-creator-asset-kit.html",
    "https://retotechlife.gumroad.com/l/qeimj": "omnichannel-ai-content-dashboard.html",
    "https://retotechlife.gumroad.com/l/isxrfk": "subscription-revenue-blueprint.html",
    "https://retotechlife.gumroad.com/l/BranchingCourseKit": "branching-course-kit.html",
    "https://retotechlife.gumroad.com/l/CognitoUI": "cognito-ui.html",
    "https://retotechlife.gumroad.com/l/AuraSDK": "aura-sdk.html",
    "https://retotechlife.gumroad.com/l/EthosProSuite": "ethos-pro-suite.html",
    "https://retotechlife.gumroad.com/l/SentientUXAuditor": "sentient-ux-auditor.html"
}

# Find <div style="margin-top:20px;"><a class="btn btn-primary" href="{link}" target="_blank" rel="noopener noreferrer">TEXT</a></div>
# Or just <a class="btn btn-primary" href="{link}" target="_blank" rel="noopener noreferrer">TEXT</a>

for link, file in replacements.items():
    # Attempt 1: with wrapping div
    pattern1 = f'<div style="margin-top:20px;"><a class="btn btn-primary" href="{link}" target="_blank" rel="noopener noreferrer">(.*?)</a></div>'
    replacement1 = f'<div class="cta-row" style="margin-top:20px; flex-wrap: nowrap;">\\n              <a class="btn btn-secondary" style="flex:1" href="products/{file}">Info Product</a>\\n              <a class="btn btn-primary" style="flex:1" href="{link}" target="_blank" rel="noopener noreferrer">\\1</a>\\n            </div>'
    html = re.sub(pattern1, replacement1, html)
    
    # Attempt 2: without wrapping div (like Product 03 / 04 / 08 / 13)
    # Be careful not to replace it if it already got replaced by pattern1, but pattern1 has the div.
    pattern2 = f'(<div class="price">.*?</div>\\s*)<a class="btn btn-primary" href="{link}" target="_blank" rel="noopener noreferrer">(.*?)</a>'
    replacement2 = f'\\1<div class="cta-row" style="margin-top:20px; flex-wrap: nowrap;">\\n              <a class="btn btn-secondary" style="flex:1" href="products/{file}">Info Product</a>\\n              <a class="btn btn-primary" style="flex:1" href="{link}" target="_blank" rel="noopener noreferrer">\\2</a>\\n            </div>'
    html = re.sub(pattern2, replacement2, html)

# Add BoardForge and M&A Vault to the end of the products grid
new_products = """
          <article class="card">
            <div class="product-badge">Product 19</div>
            <div class="product-title">BoardForge</div>
            <div class="mini-line"></div>
            <p class="product-desc">Il tuo Consiglio di Amministrazione Virtuale in ChatGPT o Claude.</p>
            <div class="cta-row" style="margin-top:20px; flex-wrap: nowrap;">
              <a class="btn btn-secondary" style="flex:1" href="products/boardforge.html">Info Product</a>
              <a class="btn btn-primary" style="flex:1" href="https://retotechlife.gumroad.com/l/BoardForge" target="_blank" rel="noopener noreferrer">Choose your version</a>
            </div>
          </article>

          <article class="card">
            <div class="product-badge">Product 20</div>
            <div class="product-title">Creator M&A Valuation Vault</div>
            <div class="mini-line"></div>
            <p class="product-desc">Modelli di valutazione e acquisizione per i creator.</p>
            <div class="cta-row" style="margin-top:20px; flex-wrap: nowrap;">
              <a class="btn btn-secondary" style="flex:1" href="products/creator-ma-valuation-vault.html">Info Product</a>
              <a class="btn btn-primary" style="flex:1" href="https://retotechlife.gumroad.com/l/MandA" target="_blank" rel="noopener noreferrer">Choose your version</a>
            </div>
          </article>
"""

html = html.replace('        </div></div>\n      </div>\n    </section>', new_products + '\n        </div></div>\n      </div>\n    </section>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html")
