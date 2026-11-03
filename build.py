import os, shutil, json
SITE_URL = "https://TWOJA-DOMENA.pl"   # <- troque pela sua domínio
ADSENSE = ""                            # <- ex: "ca-pub-1234567890123456"
NAME = "Skarbnik"
TAG = "Podatki i pieniądze po ludzku"
OUT = "public"

def svg(kind):
    g = {
 "skala": '<rect width="400" height="220" fill="#14213D"/><rect x="40" y="90" width="210" height="90" fill="#0F9D8A"/><rect x="250" y="40" width="110" height="140" fill="#F2B134"/><text x="60" y="145" font-size="34" fill="#fff" font-family="sans-serif" font-weight="700">12%</text><text x="270" y="120" font-size="34" fill="#14213D" font-family="sans-serif" font-weight="700">32%</text>',
 "pit": '<rect width="400" height="220" fill="#0F9D8A"/><rect x="110" y="30" width="180" height="160" rx="6" fill="#fff"/><rect x="130" y="55" width="100" height="10" fill="#14213D"/><rect x="130" y="80" width="140" height="8" fill="#cfd8dc"/><rect x="130" y="100" width="140" height="8" fill="#cfd8dc"/><rect x="130" y="120" width="90" height="8" fill="#cfd8dc"/><circle cx="260" cy="160" r="22" fill="#F2B134"/><path d="M250 160l7 7 13-15" stroke="#14213D" stroke-width="5" fill="none"/>',
 "ike": '<rect width="400" height="220" fill="#F2B134"/><path d="M40 180 Q120 170 170 130 T360 40" stroke="#14213D" stroke-width="8" fill="none"/><circle cx="360" cy="40" r="12" fill="#14213D"/><rect x="60" y="150" width="30" height="30" fill="#0F9D8A"/><rect x="120" y="130" width="30" height="50" fill="#0F9D8A"/><rect x="180" y="100" width="30" height="80" fill="#0F9D8A"/><rect x="240" y="75" width="30" height="105" fill="#0F9D8A"/>',
 "belka": '<rect width="400" height="220" fill="#14213D"/><circle cx="150" cy="110" r="70" fill="#F2B134"/><path d="M150 110 L150 40 A70 70 0 0 1 211 75 Z" fill="#0F9D8A"/><text x="250" y="105" font-size="44" fill="#fff" font-family="sans-serif" font-weight="700">19%</text><text x="250" y="135" font-size="16" fill="#9fb3c8" font-family="sans-serif">podatek od zysków</text>',
 "jdg": '<rect width="400" height="220" fill="#EEF2F6"/><rect x="50" y="50" width="90" height="120" rx="6" fill="#14213D"/><rect x="155" y="50" width="90" height="120" rx="6" fill="#0F9D8A"/><rect x="260" y="50" width="90" height="120" rx="6" fill="#F2B134"/><text x="70" y="118" font-size="20" fill="#fff" font-family="sans-serif" font-weight="700">skala</text><text x="170" y="118" font-size="20" fill="#fff" font-family="sans-serif" font-weight="700">19%</text><text x="268" y="118" font-size="18" fill="#14213D" font-family="sans-serif" font-weight="700">ryczałt</text>'}[kind]
    return f'<svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true" preserveAspectRatio="xMidYMid slice">{g}</svg>'

A = [
dict(slug="skala-podatkowa-pit-jak-liczyc-podatek", cover="skala", cat="PIT", date="2026-11-03", min=4,
 title="Skala podatkowa PIT: jak naprawdę liczy się podatek dochodowy",
 desc="12% i 32%, kwota wolna 30 000 zł i próg 120 000 zł. Prosty przykład, jak działa skala podatkowa i ile podatku zapłacisz.",
 body="""<p>Skala podatkowa to najpopularniejsza forma rozliczania PIT w Polsce. Mają ją osoby na etacie, zleceniu i wielu przedsiębiorców. Zasady są proste, ale wokół progów narosło sporo mitów.</p>
<h2>Dwa progi, dwie stawki</h2>
<p>Do 120 000 zł dochodu rocznie płacisz <strong>12%</strong>. Od nadwyżki ponad tę kwotę płacisz <strong>32%</strong>. Nie jest tak, że po przekroczeniu progu cały dochód opodatkowany jest wyższą stawką. Wyższa stawka dotyczy wyłącznie nadwyżki.</p>
<h2>Kwota wolna od podatku</h2>
<p>Kwota wolna wynosi 30 000 zł. W praktyce działa to tak, że podatek obliczony od dochodu zmniejszasz o 3 600 zł (czyli 12% z 30 000 zł). Dlatego przy niskich dochodach podatek wynosi zero.</p>
<h2>Przykład</h2>
<p>Dochód roczny 150 000 zł: od pierwszych 120 000 zł podatek wynosi 14 400 zł, od pozostałych 30 000 zł wynosi 9 600 zł. Razem 24 000 zł, minus 3 600 zł kwoty zmniejszającej, czyli <strong>20 400 zł</strong> podatku.</p>
<div class="ad">AD</div>
<div class="callout"><strong>Pamiętaj:</strong> do podatku dochodowego dochodzi jeszcze składka zdrowotna (9% podstawy przy skali) i składki ZUS. Nie są one częścią PIT, ale wpływają na to, ile zostaje Ci w kieszeni.</div>
<h2>Jak legalnie zapłacić mniej?</h2>
<p>Skorzystaj z ulg i odliczeń, o których piszemy w osobnym artykule, oraz z kont emerytalnych IKZE. Małżonkowie mogą też w niektórych sytuacjach rozliczyć się wspólnie, co bywa korzystne przy dużej różnicy dochodów.</p>"""),
dict(slug="pit-37-ulgi-i-odliczenia", cover="pit", cat="PIT", date="2026-10-28", min=4,
 title="PIT-37: najważniejsze ulgi i odliczenia, o których łatwo zapomnieć",
 desc="Ulga na dzieci, IKZE, termomodernizacja, darowizny. Sprawdź, co możesz odliczyć w rocznym rozliczeniu PIT-37.",
 body="""<p>Roczne rozliczenie PIT-37 składasz najpóźniej do <strong>30 kwietnia</strong> następnego roku. Wielu podatników traci pieniądze tylko dlatego, że nie wie o dostępnych ulgach. Oto te najczęstsze.</p>
<h2>Ulga na dzieci</h2>
<p>Przysługuje rodzicom małoletnich dzieci, a kwota zależy od liczby dzieci. Obowiązują limity dochodowe, więc sprawdź warunki dla swojej sytuacji. Ulga obniża podatek bezpośrednio.</p>
<h2>IKZE</h2>
<p>Wpłaty na Indywidualne Konto Zabezpieczenia Emerytalnego odliczasz od dochodu, w granicach rocznego limitu. Im wyższy próg podatkowy, tym większa korzyść.</p>
<h2>Ulga termomodernizacyjna</h2>
<p>Dla właścicieli domów jednorodzinnych: wydatki na ocieplenie, wymianę okien czy źródła ciepła można odliczyć od dochodu. Zachowaj faktury, bo urząd może poprosić o dokumenty.</p>
<div class="ad">AD</div>
<h2>Darowizny i ulga rehabilitacyjna</h2>
<p>Darowizny na cele pożytku publicznego i kultu religijnego odliczysz od dochodu w określonym limicie. Osoby z niepełnosprawnością i ich opiekunowie mogą skorzystać z ulgi rehabilitacyjnej.</p>
<div class="callout"><strong>Wskazówka:</strong> przepisy i limity zmieniają się niemal co roku. Przed złożeniem zeznania sprawdź aktualne zasady na podatki.gov.pl lub w usłudze Twój e-PIT.</div>"""),
dict(slug="ike-i-ikze-czym-sie-roznia", cover="ike", cat="Oszczędzanie", date="2026-10-21", min=4,
 title="IKE czy IKZE? Różnice, zalety i dla kogo które konto",
 desc="Porównanie IKE i IKZE: ulga podatkowa, zwolnienie z podatku Belki, limity wpłat i zasady wypłaty.",
 body="""<p>IKE i IKZE to dwa konta, które pozwalają oszczędzać na emeryturę z preferencjami podatkowymi. Wyglądają podobnie, ale korzyści podatkowe pojawiają się w innym momencie.</p>
<h2>IKE: zysk bez podatku na końcu</h2>
<p>Wpłaty na IKE nie obniżają podatku dziś. Za to po spełnieniu warunków (m.in. ukończenie 60 lat) wypłacasz środki <strong>bez 19% podatku od zysków</strong>. Dobrze działa, gdy inwestujesz długoterminowo i liczysz na wysokie zyski.</p>
<h2>IKZE: ulga na starcie</h2>
<p>Wpłaty na IKZE odliczasz od dochodu w PIT, więc od razu płacisz niższy podatek. Przy wypłacie po 65. roku życia płacisz zryczałtowany podatek 10% od całości wypłaty.</p>
<div class="ad">AD</div>
<h2>Które wybrać?</h2>
<ul><li><strong>Wyższe dochody (stawka 32%):</strong> IKZE daje większą ulgę.</li><li><strong>Dochody w pierwszym progu:</strong> zwykle warto rozważyć IKE albo oba konta.</li><li><strong>Przedsiębiorcy:</strong> mają wyższy limit wpłat na IKZE.</li></ul>
<p>Limity wpłat są ustalane co roku i zależą od przeciętnego wynagrodzenia. Aktualne kwoty znajdziesz u instytucji prowadzącej konto lub na gov.pl.</p>
<div class="callout"><strong>Uwaga:</strong> przy wypłacie przed czasem tracisz preferencje podatkowe, więc traktuj to jako pieniądze zamrożone do emerytury.</div>"""),
dict(slug="podatek-belki-jak-dziala", cover="belka", cat="Oszczędzanie", date="2026-10-14", min=3,
 title="Podatek Belki: ile wynosi i jak go legalnie ograniczyć",
 desc="Podatek od zysków kapitałowych wynosi 19%. Wyjaśniamy, kogo dotyczy i jak go uniknąć dzięki IKE, IKZE i obligacjom.",
 body="""<p>Podatek Belki to popularna nazwa 19% podatku od dochodów z kapitału. Płacisz go od zysków z lokat, kont oszczędnościowych, obligacji, funduszy i akcji.</p>
<h2>Jak jest naliczany?</h2>
<p>Podatek dotyczy <strong>zysku</strong>, nie całej kwoty. Jeśli wpłacisz 10 000 zł na lokatę i zarobisz 500 zł odsetek, podatek wyniesie 95 zł, a w kieszeni zostanie 405 zł. Bank zwykle pobiera go automatycznie.</p>
<div class="ad">AD</div>
<h2>Jak go ograniczyć?</h2>
<ul><li><strong>IKE i IKZE:</strong> zyski rosną bez corocznego opodatkowania.</li><li><strong>Dłuższe okresy lokat:</strong> mniej wypłat odsetek to mniej momentów poboru podatku.</li><li><strong>Obligacje skarbowe:</strong> podatek płacisz przy wypłacie odsetek, a nie co roku.</li></ul>
<h2>Inflacja a realny zysk</h2>
<p>Przy ocenie oszczędzania porównuj oprocentowanie po podatku z inflacją. Jeśli zysk netto jest niższy od inflacji, Twoje oszczędności realnie tracą na wartości.</p>
<div class="callout"><strong>Pamiętaj:</strong> zyski z zagranicznych brokerów wymagają samodzielnego rozliczenia w PIT-38.</div>"""),
dict(slug="jdg-skala-liniowy-ryczalt", cover="jdg", cat="Firma", date="2026-10-07", min=5,
 title="JDG: skala, podatek liniowy czy ryczałt? Jak wybrać formę opodatkowania",
 desc="Porównanie trzech form opodatkowania działalności gospodarczej: skala 12/32%, liniowy 19% i ryczałt od przychodów.",
 body="""<p>Zakładając jednoosobową działalność, wybierasz sposób płacenia podatku dochodowego. Decyzja wpływa na Twoje obciążenia przez cały rok, więc warto ją przeliczyć.</p>
<h2>Skala podatkowa (12% i 32%)</h2>
<p>Daje kwotę wolną i możliwość wspólnego rozliczenia z małżonkiem. Sprawdza się przy niższych dochodach i gdy korzystasz z ulg. Składka zdrowotna wynosi 9% dochodu.</p>
<h2>Podatek liniowy (19%)</h2>
<p>Jedna stawka niezależnie od dochodu. Opłaca się zwykle przy wysokich zarobkach, bo nie ma progu 32%. Nie masz kwoty wolnej ani wspólnego rozliczenia. Składka zdrowotna wynosi 4,9% dochodu.</p>
<div class="ad">AD</div>
<h2>Ryczałt od przychodów ewidencjonowanych</h2>
<p>Płacisz procent od <strong>przychodu</strong>, a nie od dochodu, a stawka zależy od rodzaju działalności. Nie odliczasz kosztów, więc ryczałt bywa korzystny przy niskich kosztach, na przykład w usługach i pracy umysłowej.</p>
<h2>Jak wybrać?</h2>
<p>Zrób symulację: porównaj prognozowany przychód, koszty i ulgi w każdej z form. Formę możesz zwykle zmienić raz w roku, w terminie określonym w przepisach.</p>
<div class="callout"><strong>Uwaga:</strong> przy wyborze formy skonsultuj się z księgowym. Przepisy dotyczące składki zdrowotnej i ZUS zmieniały się w ostatnich latach.</div>"""),
]

CSS = """:root{--ink:#14213D;--bg:#F6F8FA;--card:#fff;--teal:#0F9D8A;--amber:#F2B134;--mut:#5b6b7f;--line:#dde3ea}
@media(prefers-color-scheme:dark){:root{--ink:#e8eef5;--bg:#0e1522;--card:#16203a;--mut:#9fb0c4;--line:#27344f}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:18px/1.7 'Source Serif 4',Georgia,serif}
h1,h2,h3,.brand,nav,.meta,.btn{font-family:'Bricolage Grotesque',system-ui,sans-serif}
a{color:var(--teal)}a:focus-visible,button:focus-visible{outline:3px solid var(--amber);outline-offset:2px}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
header.top{border-bottom:1px solid var(--line);background:var(--card)}
header.top .wrap{display:flex;justify-content:space-between;align-items:center;gap:16px;padding-top:14px;padding-bottom:14px;flex-wrap:wrap}
.brand{font-weight:800;font-size:1.5rem;text-decoration:none;color:var(--ink);letter-spacing:-.02em}
.brand span{color:var(--teal)}
nav a{margin-left:18px;color:var(--ink);text-decoration:none;font-weight:500;font-size:.95rem}nav a:hover{color:var(--teal)}
.hero{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center;padding:56px 0 40px}
.hero h1{font-size:clamp(2rem,5vw,3.4rem);line-height:1.08;margin:0 0 16px;letter-spacing:-.03em;font-weight:800}
.hero p{color:var(--mut);margin:0 0 22px;max-width:46ch}
.btn{display:inline-block;background:var(--ink);color:var(--bg);padding:12px 22px;border-radius:6px;text-decoration:none;font-weight:600}
.hero svg{width:100%;height:auto;border-radius:10px}
.feat{display:grid;grid-template-columns:1fr 1fr;gap:28px;background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden;margin-bottom:28px}
.feat svg{width:100%;height:100%;min-height:220px;display:block}.feat .t{padding:28px}
.list{display:grid;gap:0}
.row{display:grid;grid-template-columns:200px 1fr;gap:22px;padding:22px 0;border-top:1px solid var(--line);align-items:center}
.row svg{width:100%;height:auto;border-radius:6px;display:block}
.meta{color:var(--mut);font-size:.85rem}
.row h3,.feat h2{margin:4px 0 6px;font-size:1.35rem;line-height:1.25;letter-spacing:-.01em}
.row h3 a,.feat h2 a{color:var(--ink);text-decoration:none}.row h3 a:hover,.feat h2 a:hover{color:var(--teal)}
.row p,.feat p{margin:0;color:var(--mut);font-size:.98rem;line-height:1.55}
.sec{font-size:1.1rem;font-weight:700;margin:36px 0 8px}
article{max-width:700px;margin:0 auto;padding:36px 0 20px}
article h1{font-size:clamp(1.9rem,4.5vw,2.8rem);line-height:1.12;letter-spacing:-.025em;margin:6px 0 14px;font-weight:800}
article h2{font-size:1.55rem;margin:36px 0 6px;letter-spacing:-.01em}
article .cover{margin:24px 0}article .cover svg{width:100%;height:auto;border-radius:10px;display:block}
.callout{border-left:4px solid var(--amber);background:var(--card);padding:14px 18px;margin:26px 0;border-radius:0 8px 8px 0;font-size:.97rem;line-height:1.6}
.ad{margin:30px 0;min-height:110px;display:flex;align-items:center;justify-content:center;color:var(--mut);font:12px sans-serif;border:1px dashed var(--line);border-radius:6px}
.ad.live{border:0}
.disc{font-size:.85rem;color:var(--mut);border-top:1px solid var(--line);margin-top:36px;padding-top:14px;line-height:1.5}
footer{border-top:1px solid var(--line);margin-top:50px;background:var(--card);font-family:'Bricolage Grotesque',sans-serif;font-size:.9rem;color:var(--mut)}
footer .wrap{padding-top:26px;padding-bottom:26px;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
footer a{color:var(--mut);margin-right:14px}
.page{max-width:700px;margin:0 auto;padding:40px 0}.page h1{font-family:'Bricolage Grotesque',sans-serif;letter-spacing:-.02em}
@media(max-width:720px){.hero,.feat{grid-template-columns:1fr}.row{grid-template-columns:110px 1fr;gap:14px}nav a{margin-left:12px}body{font-size:17px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;600;800&family=Source+Serif+4:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">'
ADS = f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE}" crossorigin="anonymous"></script>' if ADSENSE else ""
ADUNIT = ('<div class="ad live"><ins class="adsbygoogle" style="display:block" data-ad-client="%s" data-ad-slot="SEU_SLOT" data-ad-format="auto" data-full-width-responsive="true"></ins><script>(adsbygoogle=window.adsbygoogle||[]).push({});</script></div>' % ADSENSE) if ADSENSE else '<div class="ad">Miejsce na reklamę</div>'

def page(title, desc, path, main, extra=""):
    return f'''<!doctype html><html lang="pl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{SITE_URL}{path}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:locale" content="pl_PL">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%2314213D'/%3E%3Ctext x='16' y='23' font-size='20' text-anchor='middle' fill='%23F2B134' font-family='sans-serif' font-weight='700'%3Ez%C5%82%3C/text%3E%3C/svg%3E">
{FONTS}<link rel="stylesheet" href="/style.css">{ADS}{extra}</head><body>
<header class="top"><div class="wrap"><a class="brand" href="/">{NAME}<span>.</span></a><nav><a href="/#artykuly">Artykuły</a><a href="/o-nas/">O nas</a><a href="/kontakt/">Kontakt</a></nav></div></header>
<main class="wrap">{main}</main>
<footer><div class="wrap"><div><strong>{NAME}</strong> · {TAG}</div><div><a href="/o-nas/">O nas</a><a href="/kontakt/">Kontakt</a><a href="/polityka-prywatnosci/">Polityka prywatności</a></div></div>
<div class="wrap" style="padding-top:0"><small>Treści mają charakter informacyjny i nie stanowią porady podatkowej ani finansowej.</small></div></footer></body></html>'''

def w(path, s):
    p = os.path.join(OUT, path.lstrip("/")); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(s)

MONTHS = ["stycznia","lutego","marca","kwietnia","maja","czerwca","lipca","sierpnia","września","października","listopada","grudnia"]
def pl(d): y,m,dd = d.split("-"); return f"{int(dd)} {MONTHS[int(m)-1]} {y}"

if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(OUT); open(f"{OUT}/style.css","w").write(CSS)

hero_svg = '<svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Skala podatkowa: 12% do 120 000 zł, 32% powyżej"><rect width="400" height="300" rx="10" fill="#14213D"/><rect x="30" y="150" width="230" height="100" fill="#0F9D8A"/><rect x="260" y="70" width="110" height="180" fill="#F2B134"/><text x="46" y="210" font-size="42" font-weight="800" fill="#fff" font-family="sans-serif">12%</text><text x="276" y="150" font-size="42" font-weight="800" fill="#14213D" font-family="sans-serif">32%</text><line x1="260" y1="40" x2="260" y2="268" stroke="#fff" stroke-dasharray="4 4"/><text x="268" y="40" font-size="14" fill="#fff" font-family="sans-serif">120 000 zł</text><text x="30" y="280" font-size="13" fill="#9fb3c8" font-family="sans-serif">dochód roczny →</text></svg>'
f = A[0]
feat = f'<div class="feat"><a href="/{f["slug"]}/" aria-hidden="true" tabindex="-1">{svg(f["cover"])}</a><div class="t"><div class="meta">{f["cat"]} · {pl(f["date"])}</div><h2><a href="/{f["slug"]}/">{f["title"]}</a></h2><p>{f["desc"]}</p></div></div>'
rows = "".join(f'<div class="row"><a href="/{a["slug"]}/" aria-hidden="true" tabindex="-1">{svg(a["cover"])}</a><div><div class="meta">{a["cat"]} · {pl(a["date"])} · {a["min"]} min czytania</div><h3><a href="/{a["slug"]}/">{a["title"]}</a></h3><p>{a["desc"]}</p></div></div>' for a in A[1:])
home = f'''<section class="hero"><div><h1>Podatki i pieniądze, wyjaśnione bez żargonu.</h1><p>Praktyczne poradniki o PIT, ulgach, oszczędzaniu i prowadzeniu firmy. Z przykładami liczbowymi, które możesz przenieść na własną sytuację.</p><a class="btn" href="#artykuly">Czytaj poradniki</a></div>{hero_svg}</section>
<h2 class="sec" id="artykuly">Najnowsze artykuły</h2>{feat}{ADUNIT}<div class="list">{rows}</div>'''
w("index.html", page(f"{NAME}: podatki i finanse osobiste po polsku", "Poradniki o podatku PIT, ulgach podatkowych, oszczędzaniu i formach opodatkowania firmy. Proste wyjaśnienia z przykładami.", "/", home))

for a in A:
    rel = "".join([f'<div class="row"><a href="/{b["slug"]}/" aria-hidden="true" tabindex="-1">{svg(b["cover"])}</a><div><div class="meta">{b["cat"]}</div><h3><a href="/{b["slug"]}/">{b["title"]}</a></h3></div></div>' for b in A if b is not a][:3])
    body = a["body"].replace('<div class="ad">AD</div>', ADUNIT)
    ld = json.dumps({"@context":"https://schema.org","@type":"Article","headline":a["title"],"datePublished":a["date"],"inLanguage":"pl","author":{"@type":"Organization","name":NAME}}, ensure_ascii=False)
    main = f'''<article><div class="meta">{a["cat"]} · {pl(a["date"])} · {a["min"]} min czytania</div><h1>{a["title"]}</h1><div class="cover">{svg(a["cover"])}</div>{body}
<p class="disc">Artykuł ma charakter wyłącznie informacyjny i nie jest poradą podatkową. Przepisy i limity się zmieniają, więc przed podjęciem decyzji sprawdź aktualne regulacje na gov.pl lub skonsultuj się z doradcą podatkowym.</p></article>
<h2 class="sec">Czytaj dalej</h2><div class="list">{rel}</div>'''
    w(f"{a['slug']}/index.html", page(f'{a["title"]} | {NAME}', a["desc"], f'/{a["slug"]}/', main, f'<script type="application/ld+json">{ld}</script>'))

w("o-nas/index.html", page(f"O nas | {NAME}", "Kim jesteśmy i jak tworzymy poradniki podatkowe.", "/o-nas/", f'<div class="page"><h1>O nas</h1><p>{NAME} to blog o podatkach i finansach osobistych pisany prostym językiem. Chcemy, żeby każdy mógł zrozumieć swoje rozliczenia i podejmować lepsze decyzje o pieniądzach.</p><p>Każdy artykuł opieramy na obowiązujących przepisach i opatrujemy przykładami liczbowymi. Przepisy podatkowe się zmieniają, dlatego zachęcamy do weryfikacji szczegółów na stronach urzędowych.</p><p>Nie jesteśmy doradcami podatkowymi. Publikowane treści mają charakter informacyjny.</p></div>'))
w("kontakt/index.html", page(f"Kontakt | {NAME}", "Skontaktuj się z redakcją.", "/kontakt/", '<div class="page"><h1>Kontakt</h1><p>Masz pytanie, uwagę albo chcesz zgłosić błąd w artykule? Napisz do nas:</p><p><a href="mailto:kontakt@TWOJA-DOMENA.pl">kontakt@TWOJA-DOMENA.pl</a></p><p>Odpowiadamy zwykle w ciągu kilku dni roboczych. Nie udzielamy indywidualnych porad podatkowych.</p></div>'))
w("polityka-prywatnosci/index.html", page(f"Polityka prywatności | {NAME}", "Informacje o plikach cookie, reklamach i przetwarzaniu danych.", "/polityka-prywatnosci/", f'<div class="page"><h1>Polityka prywatności</h1><p>Serwis {NAME} szanuje prywatność odwiedzających. Poniżej opisujemy, jakie dane mogą być przetwarzane.</p><h2>Pliki cookie i reklamy</h2><p>Serwis może korzystać z usług reklamowych Google AdSense. Google i jego partnerzy mogą używać plików cookie do wyświetlania reklam dopasowanych do wcześniejszych wizyt. Możesz zarządzać personalizacją reklam w ustawieniach Google (adssettings.google.com).</p><h2>Dane analityczne</h2><p>Możemy zbierać anonimowe statystyki ruchu, aby poprawiać zawartość serwisu.</p><h2>Twoje prawa</h2><p>Na podstawie RODO masz prawo dostępu do swoich danych, ich sprostowania i usunięcia. Skontaktuj się z nami przez stronę Kontakt.</p><p>Data ostatniej aktualizacji: {pl("2026-11-03")}.</p></div>'))

urls = ["/","/o-nas/","/kontakt/","/polityka-prywatnosci/"]+[f"/{a['slug']}/" for a in A]
w("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{SITE_URL}{u}</loc></url>" for u in urls)+"</urlset>")
w("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
if ADSENSE: w("ads.txt", f"google.com, pub-{ADSENSE.split('pub-')[-1]}, DIRECT, f08c47fec0942fa0\n")
w("404.html", page(f"Nie znaleziono | {NAME}", "Strona nie istnieje.", "/404", '<div class="page"><h1>Nie znaleziono strony</h1><p>Adres może być nieaktualny. <a href="/">Wróć na stronę główną</a>.</p></div>'))
open(f"{OUT}/../vercel.json","w").write('{"cleanUrls":true,"trailingSlash":true}')
print("ok", len(urls))
