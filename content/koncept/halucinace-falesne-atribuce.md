---
title: Halucinace a falešné atribuce
type: koncept
tags: [reputace, fakta, zdrojování]
updated: 2026-06-21
zdroje: [fletcher-verckist-2025, zhao-berman-2025, peters-chin-yee-2025, zuccon-2023, noreika-2026, cesky-rozhlas-2025, aov-2025, foo-2026]
publish: true
---
# Halucinace a falešné atribuce

Problém nejsou jen věcné chyby, ale **strukturální selhání ve zdrojování** — a riziko
dopadá i na média, která AI sama nepoužívají.

## Typy chyb (BBC/EBU: 22 PSM, 18 zemí, 14 jazyků; 4 asistenti; **45 %** odpovědí se závažným problémem)
Studie reálně dělí chyby na: **accuracy, sourcing (zdrojování), opinion-vs-fact, editorialization,
context**. **Sourcing je největší příčina (31 %)**, a **Gemini** v něm vyčníval — **72 %** jeho
odpovědí mělo závažný sourcing problém (ostatní asistenti < 25 %). Naše zjednodušené „čtyři typy"
pro práci s nimi:
- **věcná chyba** — nesprávný či zastaralý údaj,
- **ztráta kontextu** — zjednodušení nebo posun významu,
- **falešná atribuce** — médiu/autorovi připsáno tvrzení, které nevyslovil,
- **ceremoniální citace** — odpověď vypadá zdrojovaně, ale článek tvrzení nepodporuje.

Poslední dvě jsou pro značky nejcitlivější: **42 % lidí** by méně důvěřovalo původnímu zdroji,
kdyby AI souhrn obsahoval chyby ([[fletcher-verckist-2025|BBC/EBU]]).

## Co o tom víme
- AI připisovala veřejnoprávním médiím hodnotící/aktivistické postoje, které v textu nebyly,
  nebo si vymýšlela citace ([[fletcher-verckist-2025]], [[bbc-ebu]]).
- **Neexistující/chybné zdroje:** v systematickém testu (160 zemědělských otázek, GPT-3.5)
  **86 % referencí ChatGPT neexistovalo**, přitom vypadaly věrohodně ([[zuccon-2023]]) —
  empirická opora pro „ceremoniální citaci" (⚠️ doména zemědělství, přenos na zprávy nepřímý).
- Sklon k nadsazování platí i mimo zprávy: při shrnování vědeckých textů modely nadsazují
  tvrzení a nepřesně zobecňují **častěji než lidští autoři** ([[peters-chin-yee-2025]] —
  doména jsou vědecké texty, přenos na zpravodajství je nepřímý).
- ⚠️ Senzační mediální zmínka o rozsahu chyb ([[noreika-2026]] — slabý zdroj, jen ilustrace).
- **Technická obrana má vedlejší náklady:** plošná blokace botů může snížit i lidskou
  návštěvnost ([[zhao-berman-2025]] — working paper). Doporučovaný je proto spíš
  [[crawler-separation-opt-out|diferencovaný opt-out]] než plošná blokace ([[aov-2025]], [[aov]]).

## Právní odpovědnost platformy (nový vývoj)
Reputační náklad se nemusí přenášet jen na falešně citovanou značku — může dopadnout i na
**platformu**. Mnichovský soud rozhodl, že Google je **právně odpovědný** za nepravdivá
tvrzení v AI Overviews, která falešně spojila dva německé vydavatele s podvody; soud označil
AI Overviews za **„vlastní obsah Googlu"**. Google se odvolává ([[foo-2026]], [[google]]).
> ⚠️ Jeden prvostupňový rozsudek (Německo) pod odvoláním — indikativní vývoj, ne ustálený
> precedent. Širší rámec viz [[regulace-eu-ai-act-dsa]].

## České specifikum
Český rozhlas v rámci EBU doložil konkrétní selhání (např. nepravdivé tvrzení o právním
statusu náhradního mateřství) — viz [[cesky-rozhlas]], [[cesky-rozhlas-2025]] (zkreslení
zpravodajství ~45 % případů). Doporučená je diferencovaná, ne plošná obrana ([[cesky-trh]],
[[aov-2025]]).

## Datová mezera
⚠️ [[fletcher-verckist-2025|BBC/EBU]] je **statický snímek**. Otevřená otázka: zlepšují se
atribuce a citace napříč generacemi modelů, nebo zůstávají stejně chybové? Viz [[otevrene-otazky]].

## Zdroje
- [[fletcher-verckist-2025]], [[zhao-berman-2025]], [[peters-chin-yee-2025]], [[zuccon-2023]],
  [[cesky-rozhlas-2025]], [[aov-2025]], ⚠️ [[noreika-2026]]
