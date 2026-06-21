---
title: "3. Hodnota dat"
type: report
tags: [report, licencování, data]
updated: 2026-06-21
publish: true
---
**Jak AI průmysl využívá novinářský obsah.**

Generativní AI byla od počátku závislá na rozsáhlých textových korpusech, jejichž součástí byla
i profesionální žurnalistika. Novinářské texty modelům poskytují jazykovou pestrost, popisy reálných
událostí a průběžně aktualizované zachycení veřejného dění. Pro mediální sektor z toho plynou dvě
otázky: jak velkou roli tento obsah v datovém řetězci AI skutečně hraje a jak je za jeho využití
kompenzován vydavatel.

[[licencovani-trzni-asymetrie|Debata má dvě roviny]]. První je právní spor o legitimitu dat: zda
a za jakých podmínek smějí technologické firmy trénovat modely na mediálním obsahu. Druhá je
ekonomický problém asymetrie trhu. I pokud se licenční režim postupně ustálí, nemusí z něj profitovat
všichni vydavatelé stejně.

## Zpravodajská data byla pro trénink modelů významná

Význam žurnalistiky v trénovacích datech ukazují zjištění o sadě C4 a dalších rozsáhlých webových
korpusech používaných při vývoji starších generací velkých jazykových modelů. Analýza The Washington
Post a Allenova institutu pro umělou inteligenci ukázala, že mezi významnými zdroji této datové sady
byly velké mediální domy včetně The New York Times, The Guardian nebo Forbes ([[schaul-2023]]). Další
analytické texty upozorňují, že zpravodajské a mediální weby tvořily v těchto korpusech důležitou
složku, i když přesné podíly se liší podle metodiky ([[radsch-2024]]; [[fletcher-2024]]).

Profesionální žurnalistika tedy nebyla pro raný vývoj LLM okrajovým vstupem. Silnější teze, že bez
novinářských dat by současné modely nemohly fungovat nebo že kvalitní žurnalistika představuje jejich
jediný nenahraditelný zdroj, už zůstává plauzibilním strategickým závěrem, nikoli exaktně změřeným
faktem.

Spory kolem [[common-crawl|Common Crawl]] a dalších datových sběrů zároveň ukazují, že transparentnost
původu trénovacích dat zůstává omezená. Vydavatelé často jen částečně vědí, v jakém rozsahu a za jakých
podmínek byl jejich obsah použit. Tato netransparentnost se stala jedním ze zdrojů napětí mezi
mediálním a technologickým sektorem ([[reisner-2025]]; [[commoncrawl-2025]]).

## Právní spor a ekonomická asymetrie nejsou totéž

Ve veřejné debatě se právní a ekonomická rovina často mísí. Právní spor se týká otázky, zda byl sběr
a využití obsahu přípustné, zda šlo o transformační užití a zda byla data získána legálně. Sem patří
například spor [[nyt-v-openai|The New York Times proti OpenAI a Microsoftu]] ([[copyright-alliance-2026]];
[[norton-rose-2026]]). Že nejde jen o otevřená řízení, ukazuje miliardové narovnání ve věci Bartz
v. Anthropic: signál, že část sporů o trénovací data už nachází ekonomické vypořádání, byť zatím mimo
doménu zpravodajství.

Ekonomická rovina se neptá jen na to, zda je využití legální, ale kdo z nového trhu s daty skutečně
získává příjem. Právě zde se ukazuje strukturální asymetrie: licenční dohody s AI firmami uzavírají
především globální a kapitálově silné mediální domy, zatímco menší, lokální a specializovaní vydavatelé
zůstávají převážně mimo hlavní proud těchto smluv.

## Licenční dohody zatím zvýhodňují především velké hráče

Pod tlakem kritiky i regulatorních debat začaly některé technologické firmy uzavírat s vydavateli
licenční dohody. [[reuters-institute|Reuters Institute]] uvádí, že přibližně 70 procent dotázaných
mediálních manažerů očekává v příštích letech nějaké příjmy z licencování, většinou však jen jako
vedlejší zdroj. Pětina respondentů naopak nepředpokládá, že z tohoto trhu získá jakýkoli příjem
([[newman-2026]]).

Jde však o očekávání trhu, nikoli o exaktně vykázané příjmy. Chybějí veřejně srovnatelná data
o řádové velikosti většiny dohod i o tom, jaký podíl příjmů médií by musely představovat, aby skutečně
změnily jejich ekonomickou situaci. Veřejně známé dohody se soustřeďují k několika největším značkám.
Brookings mezi partnery [[openai|OpenAI]] zmiňuje například Associated Press, Axel Springer, Le Monde,
Prisa Media, Financial Times, Time nebo Condé Nast ([[radsch-2024]]). Další dohody uzavřely News Corp,
CNN, USA Today, Fox News nebo People. Z hlediska mediální plurality to znamená, že nově vznikající
příjmy se koncentrují u několika velkých hráčů, zatímco menší a lokální média nemají srovnatelnou
vyjednávací sílu.

## Pohled platforem a alternativní výklad

Z perspektivy technologických firem vypadá situace jinak. Platformy argumentují, že generativní souhrny
mohou uživatelům poskytovat lepší službu, že část provozu, o který média přicházejí, měla i dříve
nízkou hodnotu, a že odpovídací rozhraní uspokojují dotazy, které by stejně nevedly k dlouhé nebo
kvalitní návštěvě. Tento protiargument nelze jednoduše odmítnout, zejména u komoditního a servisního
obsahu.

Část současné zranitelnosti médií navíc nevznikla až s AI. Řada vydavatelů v předchozí dekádě sama
investovala do velkých objemů SEO-orientovaného evergreen a servisního obsahu, jehož ekonomika stála
na maximalizaci kliků. Generativní AI tak nenarušuje jen model kvalitní žurnalistiky, ale i segment,
který už předtím stál na levné produkci komoditních odpovědí. Problém trhu tím nezmizí, ale jeho
interpretace je střízlivější.

## Kolektivní řešení se teprve rodí

Oborové a konceptuální analýzy upozorňují, že individuální licenční dohody s AI platformami mohou dále
prohlubovat tržní asymetrii a zvýhodňovat největší hráče ([[newman-2026]]; [[radsch-2024]]). Vedle
individuálních smluv proto vznikají návrhy na [[crawler-separation-opt-out|kolektivnější postup]].
Příkladem je iniciativa [[rsl-collective|RSL Collective]], která chce zavést otevřený, strojově čitelný
licenční standard, aby vydavatelé mohli nabízet svá data za předem určených podmínek ([[guaglione-2025]];
[[rsl-collective-2025]]). V zahraniční debatě se objevují i širší návrhy na oborové aliance nebo na
rozšíření stávajících news media bargaining codes na oblast vytěžování dat pro generativní AI
([[radsch-2024]]; [[newman-2026]]).

Pro menší vydavatele jsou tyto modely důležité hlavně jako obrana proti asymetrickému trhu. Oborová
data však zatím neukazují, že by už dnes představovaly ekonomicky stabilní řešení: podle Reuters
Institute očekává 49 procent mediálních manažerů z AI licencování jen minoritní příjem a dalších 20
procent nepředpokládá žádný příjem vůbec ([[newman-2026]]). Kolektivní licencování a standardizace
práv tak v této fázi představují spíše obranný mechanismus než osvědčený ekonomický model.

## Levný syntetický obsah zvyšuje tlak na celý informační prostor

Debata o datech a licencování se neodehrává ve vakuu. Generativní AI snižuje náklady nejen na legitimní
tvorbu, ale i na [[synteticky-obsah|produkci nízkohodnotného nebo klamavého obsahu]]. Systematizovaný
přehled 185 studií z let 2012–2024 mapuje rychle rostoucí pole automatizované žurnalistiky; mezi
obavami, které z literatury sbírá, je i nárůst objemu pseudozpravodajského a dezinformačního obsahu —
jde tu ovšem o citovanou obavu, ne o vlastní měření ([[bartleman-2026]]). Ekonomický model Sandriniho
a Somogyiho je přitom záměrně nejednoznačný: raná, nezralá generativní AI zvyšuje atraktivitu klamavého
obsahu a snižuje investice do tvorby zpráv, po překročení technologického prahu se ale spotřebitelé ke
kvalitnímu obsahu vracejí ([[sandrini-somogyi-2023]]). Z dat tedy neplyne jednosměrná zkáza, ale napětí,
v němž rozhoduje vyspělost technologie.

Tím roste hodnota původního, lidsky editovaného a reputačně neseného obsahu. Ne jako romantického
protikladu technologie, ale jako vzácnějšího typu dat i produktu v prostředí, které se zaplňuje levnou
obsahovou imitací.

## Česká republika: malý trh, slabá vyjednávací pozice

Na [[cesky-trh|českém trhu]] je tento problém pravděpodobně výraznější. K jaru 2026 podle veřejně
dostupných informací neexistovala dohoda mezi domácím médiem a vývojářem generativní AI o placeném
využití českého zpravodajského obsahu. Malý jazykový trh a roztříštěná vyjednávací pozice vydavatelů
ztěžují individuální dohody s globálními technologickými firmami. Proto se v českém prostředí vrací
otázka kolektivního vyjednávání a standardizace postupu.

Českou pozici komplikuje i právní rámec kolem text and data miningu. Opt-out představuje nástroj
obrany, sám o sobě však nevytváří ekonomický kompenzační režim a bez vymahatelnosti může mít jen
omezený účinek ([[prchal-2024]]). Mediální zpravodajství z amerického antitrustového řízení navíc
naznačuje, že hranice mezi zákazem využití obsahu pro AI trénink a jeho faktickým použitím v AI
souhrnech může být u velkých platforem slabší, než vydavatelé předpokládají. Podle citovaného svědectví
se opt-out z tréninku modelu Gemini nevztahuje automaticky na následné nasazení téhož modelu ve
vyhledávání Google Search a v AI Overviews ([[deck-2025]]).

Regulatorní debata ve Velké Británii proto stále častěji míří k požadavku oddělit crawlery podle účelu
použití. [[cloudflare|Cloudflare]] ve stanovisku ke konzultaci britské CMA tvrdí, že vydavatelé
potřebují možnost povolit klasickou indexaci pro vyhledávání a samostatně blokovat využití obsahu pro
generativní funkce typu AI Overviews či AI Mode ([[palmieri-hufnagel-2026]]). Jde o stanovisko
zainteresovaného aktéra, přesto přesně pojmenovává strukturální problém: pokud jedna dominantní
platforma spojuje vyhledávací a AI crawling, zůstává kontrola vydavatelů nad využitím obsahu jen
částečná.

---

Pokračovat: [[reputacni-skody|Reputační a faktické škody →]] · zpět na [[index|úvod reportu]]
