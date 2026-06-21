---
title: Doporučení (podle síly opory)
type: koncept
tags: [doporučení, strategie, redakce, regulace]
updated: 2026-06-21
zdroje: [zhao-berman-2025, futurism-2023, khatiwada-2026, fletcher-verckist-2025, wu-2024, cools-diakopoulos-2024, doshi-hauser-2024, aov-2025, newman-2026, rsl-collective-2025, slpv-2026, deck-2025, palmieri-hufnagel-2026, prchal-2024, gerlich-2025, barcaui-2025]
publish: true
---
# Doporučení (podle síly opory)

Závěrečná doporučení reportu („Co dál"). Klíčový rozdíl: **doporučení nemají stejnou váhu.**
Část reaguje na **už doložené problémy** (chybovost AI, potřeba lidského gatekeepingu, náklady
plošné blokace) a má oporu v datech. Část jsou **strategické sázky** na budoucnost (kolektivní
licencování, nové standardy pro AI vyhledávání, přesun k formátům) — mohou být racionální, ale
zatím nejsou empiricky potvrzeným řešením. Tahle stránka body přerovnává podle té osy, ne podle
adresáta. Adresát značen: **[V]** vydavatelé · **[O]** obor a instituce · **[Š]** školy a veřejnost.

## Čemu se vyhnout (doložené anti-vzory)
- **Plošné uzamčení všech AI robotů bez rozlišení role.** Odstřižení všech botů sníží nejen
  strojovou citovanost, ale i návštěvnost od lidských uživatelů — médium ztratí viditelnost
  v nových rozhraních ([[zhao-berman-2025]] — working paper; [[crawler-separation-opt-out]]). [V]
- **Skryté používání AI v publikovaném obsahu.** Případy [[futurism-2023|CNET a Sports
  Illustrated]] ukázaly reputační i obchodní dopad. Účinnější než odznak „vytvořeno AI" je
  procesní deklarace „co AI změnila a kdo ověřil" ([[khatiwada-2026]] — ⚠️ malý US vzorek;
  [[transparentnost-deklarace-ai]]). [V]

## Doložené (silná opora)
Reagují na doložené problémy; report je řadí mezi nejpevněji podložené.

- **(4) Udržet člověka ve smyčce u všeho, co míří k publiku.** Každý výstup má mít dohledatelného
  lidského autora/editora — testy chybovosti to staví jako základní obrannou linii, ne doplňkovou
  opatrnost (BBC/EBU ~45 % zkreslení, [[fletcher-verckist-2025]]; [[human-in-the-loop]],
  [[halucinace-falesne-atribuce]]). [V]
- **(1) Revidovat přístup robotů — selektivní, ne plošný režim.** Omezit roboty pro trénink, ale
  zvážit ponechání těch, kteří ovlivňují citovanost a viditelnost ([[crawler-separation-opt-out]],
  [[aov-2025]] — ⚠️ oborové doporučení). [V][O]
- **(2) Přijmout interní redakční rámec pro AI.** Srozumitelná pravidla kde ano/ne; zákaz vydávat
  AI text za autorský výkon, jasná lidská odpovědnost za výstup. Inspirace [[seznam|Seznam Zprávy]]
  a [[cesky-rozhlas|Český rozhlas]]. [V]
- **(3) Zveřejnit vůči publiku, jak redakce AI používá.** Skryté nasazení škodí ([[futurism-2023]]);
  s AI Actem poroste i regulatorní tlak ([[transparentnost-deklarace-ai]], [[regulace-eu-ai-act-dsa]]). [V]
- **(9) Využívat AI jako podporu, ne náhradu autorství.** Bezpečná asistenční zóna (přepisy,
  rešerše, testování protiargumentů) vs. jádro odpovědnosti; sledovat homogenizaci ([[wu-2024]],
  [[cools-diakopoulos-2024]], [[exo-zurnalistika]], [[doshi-hauser-2024]]). [V]

## Strategické sázky (racionální, zatím nepotvrzené)
Report je označuje za směr, který musí projít praktickým testem.

- **(5) Přesunout investice od komoditního obsahu k původní tvorbě** a **(6) posilovat
  důvěryhodnost autorů a značek.** Směr má dílčí oporu (nejzranitelnější je snadno shrnutelný
  obsah → [[ai-overviews-zero-click]]; priority lídrů → [[newman-2026]]), ale je to sázka na
  formát. [V]
- **(7) Chránit nejhodnotnější obsah paywallem a produktovou strategií.** [V]
- **(8) Přizpůsobit infrastrukturu AI vyhledávání** — AEO, GEO, `llms.txt`. ⚠️ Explicitně
  experimentální, ne ověřené řešení ([[generativni-optimalizace]]). [V]
- **(10) Budovat mezioborové AI týmy místo izolovaných experimentů.** Bariérou inovací nejsou
  jen finance, ale soupeřící sila redakce/produkt/technologie/byznys. [V]
- **(11) Žádat od platforem data o citovanosti, proklikovosti a chybovosti.** Aspirativní — bez
  nich nelze vyhodnotit ekonomický ani reputační dopad AI distribuce. [V][O]
- **(12) Diverzifikovat příjmy mimo platformní distribuci** (předplatné, eventy, B2B, členské
  modely) — nenahrazovat závislost na Googlu závislostí na AI platformách. [V]
- **(13) Posílit kolektivní vyjednávání o licencích** a **(16) zapojit ČR do mezinárodních
  iniciativ** ([[rsl-collective-2025]] — ⚠️ oborový standard se zájmem). Zatím spíš obranný
  mechanismus než ověřený model: 49 % manažerů čeká jen minoritní příjem, 20 % žádný
  ([[newman-2026]]; [[licencovani-trzni-asymetrie]]). [O]
- **(14) Sjednotit doporučení k TDM opt-outu a přístupu robotů** a **(15) kolektivně řešit
  i ochranu integrity značek.** Opt-out je bez vymahatelnosti omezený ([[prchal-2024]]); odtud
  tlak na oddělení crawlerů podle účelu ([[deck-2025]], [[palmieri-hufnagel-2026]] — ⚠️ Cloudflare). [O]
- **(17) Důsledně vymáhat regulatorní rámec** — AI Act, DSA, soutěžní rovina (UK CMA).
  Vymahatelnost se teprve ukáže ([[regulace-eu-ai-act-dsa]]). [O]

## Školy a veřejnost (slabší důkazní základ)
Report sám přiznává, že tahle část má slabší oporu než doporučení mířená na vydavatele — stojí na
obecnějších studiích o kognitivním offloadingu.

- **(20) Posílit mediální a AI gramotnost** — učit nejen že AI chybuje, ale i jak plynulá forma
  oslabuje obezřetnost. [Š]
- **(21) Zavádět princip AI-after-attempt** — student řeší úkol nejdřív sám, pak AI jako zpětná
  vazba ([[kognitivni-offloading]], [[barcaui-2025]], [[gerlich-2025]] — korelace, ne kauzalita). [Š]
- **(22) Ekonomicky podporovat média investující do původní práce** (granty, institucionální
  podpora, ochota publika platit). [Š][O]
- **(23) Vést uživatele k vědomému ověřování AI odpovědí** — ověřit ve více zdrojích, nepřijímat
  odpověď chatbota jako konečné stanovisko. [Š]

## Minimum pro menší redakce
Když redakce nemá kapacitu na celý seznam, čtyři kroky (vesměs z doložené skupiny):
- revidovat přístup robotů a neblokovat plošně vše bez rozlišení účelu,
- přijmout stručná interní pravidla pro používání AI,
- nepustit k publiku nic bez dohledatelné lidské odpovědnosti,
- stručně a veřejně popsat, jak redakce AI používá.

## České specifikum
Rámec [[slpv|SLPV]] pro kolektivní vyjednávání; **(18)** financovat domácí výzkum dopadů AI na
informační chování (datová mezera → [[otevrene-otazky]]); **(19)** využít specifika dvou silných
vyhledávacích bran Google + [[seznam|Seznam]] k silnějšímu domácímu vyjednávání. Viz [[cesky-trh]].

## Výhrady a otevřené otázky
- Hranice doložené × strategické není ostrá; řada doporučení má dílčí oporu i otevřené konce.
  Klasifikace vychází z rámce reportu (úvod „Co dál" a závěr), ne z nezávislého měření.
- **Doložené ≠ dořešené:** i u lidského dohledu chybí dlouhodobé měření dopadu na důvěru.

## Zdroje
- Silná opora: [[fletcher-verckist-2025]], [[zhao-berman-2025]], [[wu-2024]], [[cools-diakopoulos-2024]], [[futurism-2023]]
- Strategické / advokační: [[newman-2026]], [[rsl-collective-2025]], [[deck-2025]], [[palmieri-hufnagel-2026]], [[aov-2025]]
- Slabší (offloading): [[gerlich-2025]], [[barcaui-2025]], [[khatiwada-2026]]
