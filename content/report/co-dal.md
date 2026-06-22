---
title: "6. Co dál: doporučení"
type: report
tags: [report, doporučení]
updated: 2026-06-21
publish: true
---
**Doporučení pro vydavatele, obor a veřejné instituce.**

Předchozí kapitoly ukazují, že generativní AI nepřináší médiím jednu izolovanou hrozbu, ale souběh
několika tlaků: oslabení distribuce, reputační rizika, právní nejistotu a proměnu redakční práce.
Doporučení v této kapitole míří k tomu, co lze v takovém prostředí dělat prakticky. Jejich strukturovaný
přehled podle síly opory drží i stránka [[doporuceni|Doporučení]].

Doporučení však nemají stejnou váhu. První skupina má poměrně silnou oporu v datech a reaguje na již
doložené problémy, například na chybovost AI, potřebu lidského gatekeepingu nebo roztříštěnost rozhodování
uvnitř redakcí. Druhá skupina představuje spíše strategické sázky na budoucnost: kolektivní licencování,
nové standardy pro AI vyhledávání nebo posun k některým formátům. Tyto kroky mohou být racionální, ale
zatím nejsou empiricky potvrzeným řešením.

Liší se i náročnost jejich provedení. Menší a lokální redakce často nemají kapacity na vlastní AI tým,
důsledný [[human-in-the-loop|human-in-the-loop]] u každého typu obsahu ani na rychlé produktové experimenty.
Proto kapitola vedle plného seznamu uvádí i minimální balíček kroků, s nimiž mohou začít i menší redakce.

## Čemu se vyhnout

Než přijdou konkrétní doporučení, stojí za to pojmenovat dva kroky, kterým by se média měla vyhnout:

**Plošné uzamčení všech AI robotů bez rozlišení jejich role.**
Dostupná data, včetně working paperu Zhaoa a Bermana, naznačují, že úplné odstřižení všech botů může snížit
nejen strojovou citovanost, ale i návštěvnost od lidských uživatelů, protože médium ztrácí viditelnost
v nových vyhledávacích rozhraních ([[zhao-berman-2025]]). Smysl proto dává [[crawler-separation-opt-out|diferencovaný
přístup]], který rozlišuje mezi roboty pro trénink modelů a roboty používanými pro vyhledávání nebo citaci.

**Skryté používání AI při tvorbě publikovaného obsahu.**
Případy CNET nebo Sports Illustrated ukazují, že nepřiznané nasazení AI může mít reputační i obchodní dopad
([[futurism-2023]]). [[transparentnost-deklarace-ai|Transparentnost]] sama o sobě negarantuje důvěru, její
absence ji však může poškodit velmi rychle. Experimentální studie Khatiwady a kol. tento obraz zpřesňuje:
přiznání, že se na textu podílela AI, důvěryhodnost nesnižuje, v experimentu ji dokonce mírně zvyšovalo,
zatímco mnohem víc škodí extrémní tón samotného obsahu ([[khatiwada-2026]]). Jde o experiment na malém
americkém vzorku (zhruba 180 respondentů), takže výsledek je třeba brát jako indicii, nikoli jako robustní
důkaz. Co bylo dosud jen indicie, podpírá teď silnější důkaz: předregistrovaný conjoint experiment v Chile na více než dvou tisících respondentů ukázal, že **deklarace i lidský dohled patří k nejsilnějším pozitivním prediktorům** vnímané důvěryhodnosti — publikum reaguje méně na přítomnost AI než na strukturu odpovědnosti kolem ní ([[valenzuela-2026]]); kvalitativní výzkum doplňuje, že čtenáři chtějí hlavně viditelný lidský dohled a formulaci „AI-assisted", ne „vytvořeno AI" ([[zier-diakopoulos-2026]]). Z toho plyne praktické doporučení, které ovšem sama studie head-to-head netestovala: účinnější než
pouhý odznak „vytvořeno AI" je nejspíš procesní deklarace, která říká, co AI změnila a kdo výstup ověřil,
například „AI upravila styl, fakta ověřil editor".

## A. Doporučení pro vydavatele

### Minimum pro menší redakci

Pokud redakce nemá kapacitu řešit celý seznam doporučení, dává smysl začít čtyřmi kroky:

- revidovat přístup robotů a neblokovat plošně vše bez rozlišení účelu,
- přijmout stručná interní pravidla pro používání AI,
- nepouštět k publiku nic bez dohledatelné lidské odpovědnosti,
- stručně a veřejně popsat, jak redakce AI používá.

### Krátkodobě

**1. Revidovat technické nastavení přístupu k obsahu.** Vydavatelé by měli zkontrolovat, které typy robotů
mají na webu přístup a jaké jsou důsledky tohoto nastavení pro trénink modelů, citovanost i návštěvnost.
Smyslem není plošný zákaz, ale selektivní režim: omezovat roboty určené pro sběr tréninkových dat a zároveň
pečlivě zvažovat, zda neblokovat ty, kteří ovlivňují viditelnost média v odpovídacích rozhraních.

**2. Přijmout interní redakční rámec pro používání AI.** Každá redakce by měla mít srozumitelná pravidla pro
to, kde lze AI použít a kde nikoli. Inspirací mohou být pravidla [[seznam|Seznam Zpráv]] nebo
[[cesky-rozhlas|Českého rozhlasu]]. Základní rámec má obsahovat zákaz vydávat AI-generovaný text za autorský
novinářský výkon, zákaz používat AI bez kontroly v citlivých zpravodajských formátech a jasné určení lidské
odpovědnosti za finální publikovaný výstup.

**3. Zveřejňovat vůči publiku, jak redakce AI používá.** Transparentnost vůči publiku bude s nástupem AI Actu
i dalších regulatorních požadavků důležitější. Vydavatelé by měli srozumitelně vysvětlit, k čemu AI využívají,
jaké typy výstupů označují a kde trvají na čistě lidské práci.

**4. Udržet člověka ve smyčce u všeho, co míří k publiku.** Výzkumy newsroomů i testy chybovosti AI ukazují,
že princip human-in-the-loop není doplňková opatrnost, ale základní obranná linie. Každý obsah směřující
k publiku má mít dohledatelného lidského autora, editora nebo odpovědnou redakční roli.

### Střednědobě

**5. Přesunout investice od komoditního obsahu k původní tvorbě.** Data naznačují, že největší ztráty dopadají
na jednoduše shrnutelný obsah, zatímco vyšší odolnost si drží původní reportáže, investigativa, odborný
kontext a autorsky rozpoznatelné texty.

**6. Posilovat důvěryhodnost konkrétních autorů a značek.** V prostředí, kde AI rozhraní stírají rozdíl mezi
zdroji, roste význam rozpoznatelné redakční a autorské identity — systematická práce s autory, editory,
newslettery, podcasty a dalšími formáty, které budují vztah mezi médiem a publikem napřímo.

**7. Chránit nejhodnotnější obsah chytrým paywallem a produktovou strategií.** Původní a obtížně nahraditelný
obsah má mít vyšší ochranu i vyšší ekonomickou hodnotu. Pro menší trhy dává smysl kombinace otevřeného
servisního obsahu a placené vrstvy postavené na exkluzivitě, interpretaci nebo komunitní vazbě.

**8. Přizpůsobit technickou infrastrukturu AI vyhledávání.** Vedle tradičního SEO je třeba věnovat pozornost
i tomu, jak jsou články čitelné pro odpovídací systémy: kvalitní strukturovaná metadata, jasné označení
autora, zdroje, data publikace a logickou stavbu textu. Pojmy typu [[generativni-optimalizace|AEO, GEO]] nebo
standardy jako `llms.txt` je však zatím přesnější chápat jako experimentální strategii, ne jako ověřené řešení.

**9. Využívat AI jako nástroj podpory, ne jako náhradu autorství.** AI může pomáhat s přepisy, tříděním
dokumentů, rešeršní přípravou nebo identifikací slabých míst v textu. Nemá však přebírat roli autora, editora
ani ověřovatele faktů. Redakce by měly sledovat i riziko postupné homogenizace stylu.

**10. Budovat mezioborové AI týmy, ne izolované experimenty.** Významnou bariérou inovací nejsou jen finance,
ale i soupeřící sila mezi redakcí, produktem, technologií a byznysem. Vydavatelé proto potřebují smíšené
pracovní skupiny.

### Dlouhodobě

**11. Žádat od technologických platforem data o citovanosti, proklikovosti a chybovosti.** Bez těchto dat
nelze vyhodnotit ekonomický ani reputační dopad AI distribuce.

**12. Diverzifikovat příjmy mimo platformní distribuci.** Média by neměla nahrazovat závislost na Googlu
závislostí na nových AI platformách. Potřebují předplatné, eventy, školení, B2B produkty i členské modely.

## B. Doporučení pro oborová sdružení a veřejné instituce

### Krátkodobě

**13. Posílit kolektivní vyjednávání o licencích.** Menší jazykové trhy mají omezenou vyjednávací sílu.
Institucionální rámec [[slpv|Správce licenčních práv vydavatelů]], který se v březnu 2025 stal kolektivním
správcem majetkových práv vydavatelů tiskových publikací, proto může pomoci, aby český trh nevyjednával
roztříštěně, ale koordinovaně ([[slpv-2026]]).

**14. Sjednotit doporučení k TDM opt-outu a přístupu robotů.** Oborová sdružení by měla vydavatelům nabídnout
jasný a technicky srozumitelný standard, jak pracovat s `robots.txt`, s TDM opt-outem i s dalšími mechanismy
ochrany obsahu. Součástí má být i tlak na to, aby dominantní platformy oddělily crawlery podle účelu.

**15. Kolektivně řešit i ochranu integrity značek, nejen autorská práva.** Pokud AI systémy vytvářejí falešné
atribuce nebo poškozují nestrannost médií, měla by oborová agenda zahrnovat i pravidla pro citaci, nápravu
chyb a ochranu redakční integrity.

### Střednědobě

**16. Zapojit český trh do širších mezinárodních licenčních iniciativ.** Platformy typu [[rsl-collective|RSL
Collective]] nebo další vznikající standardy mohou být důležité zejména pro menší a střední vydavatele. Česká
média by neměla čekat, až budou pravidla hotová jinde.

**17. Důsledně vymáhat regulatorní rámec.** Veřejné instituce by měly trvat na tom, aby
[[regulace-eu-ai-act-dsa|AI Act i další evropská pravidla]] byly v praxi vymahatelné, zejména v oblasti
označování syntetického obsahu, transparentnosti a ochrany práv. Britská debata kolem CMA ukazuje, že tato
agenda nebude jen autorskoprávní, ale i soutěžní.

### Dlouhodobě

**18. Financovat český výzkum dopadů AI na informační chování.** Českému prostředí chybí systematická data
o tom, jak lidé důvěřují AI odpovědím, jak je ověřují a jak AI mění jejich vztah ke zpravodajství.

**19. Využít specifika [[cesky-trh|českého trhu]] se dvěma silnými vyhledávacími branami.** To zvyšuje tlak
na vydavatele, ale zároveň vytváří prostor pro silnější domácí vyjednávání a testování alternativních modelů.

## Dovětek: Doporučení pro školy a veřejnost

Tato část přesahuje hlavní osu reportu zaměřenou na média. Nejde o rovnocennou třetí část, ale o stručný
dovětek opřený o obecnější studie o [[kognitivni-offloading|kognitivním offloadingu]] a AI gramotnosti; jeho
důkazní základ je slabší než u doporučení mířených přímo na vydavatele.

**20. Posílit mediální a AI gramotnost.** Součástí mediální výchovy má být rozpoznávání syntetického obsahu,
práce se zdroji a základní zásady ověřování AI výstupů — a také to, jak samotná forma plynulé odpovědi
oslabuje kritickou obezřetnost.

**21. Zavádět princip AI-after-attempt ve vzdělávání.** Smysl dává model, v němž student nejprve řeší úkol sám
a teprve poté využije AI jako nástroj zpětné vazby nebo kontroly.

**22. Podporovat ekonomicky média, která investují do původní práce.** Investigativa a terénní reportáž
potřebují ekonomickou oporu — granty, institucionální podporu i ochotu publika platit.

**23. Vést uživatele k vědomému ověřování AI odpovědí.** Základním návykem by mělo být ověření v několika
důvěryhodných zdrojích a schopnost rozlišit mezi pohodlnou odpovědí a skutečně doloženou informací.

---

Tato doporučení nejsou definitivním návodem pro každý typ média. Nejpevněji podložené jsou kroky související
s redakčními pravidly, lidským dohledem a algoritmickou gramotností. Licenční koalice, nové standardy pro AI
vyhledávání nebo přesun k některým formátům je přesnější chápat jako strategický směr, který bude muset projít
praktickým testem.

Pokračovat: [[zdroje|Použitá literatura →]] · zpět na [[index|úvod reportu]]
