---
title: Oddělení crawlerů a opt-out
type: koncept
tags: [data, regulace, technika, opt-out]
updated: 2026-06-21
zdroje: [prchal-2024, deck-2025, palmieri-hufnagel-2026, zhao-berman-2025, copyright-alliance-2026, norton-rose-2026, abbas-2026-unite]
publish: true
---

Technická a regulatorní obrana přístupu k obsahu: `robots.txt`, **TDM opt-out** a požadavek
**oddělit crawlery podle účelu** — jiný režim pro klasickou indexaci do vyhledávání, jiný
pro trénink modelů a jiný pro generativní funkce (AI Overviews, AI Mode).

## Co o tom víme
- **Opt-out bez vymahatelnosti má omezený účinek** a sám o sobě nevytváří kompenzační
  režim ([[prchal-2024]]).
- Opt-out z tréninku se nemusí vztahovat na nasazení modelu jinde: podle soudního svědectví
  se opt-out z tréninku Gemini nevztahuje automaticky na použití téhož modelu v
  [[google|Google]] Search a AI Overviews ([[deck-2025]]).
- Britská debata (CMA) a [[cloudflare|Cloudflare]] proto tlačí na oddělení crawlerů, aby
  vydavatelé mohli povolit indexaci a samostatně blokovat generativní využití
  ([[palmieri-hufnagel-2026]] — ⚠️ advokační aktér, komerční zájem).
- **Plošná blokace všech botů škodí i lidské návštěvnosti** — u velkých webů vedlo zablokování
  botů k poklesu celkové i lidské návštěvnosti (ztráta citovanosti v nových rozhraních); obrana
  má cenu, ale i náklady ([[zhao-berman-2025]] — ⚠️ working paper, indikativní, ne pravidlo).
- **Crawleři obcházejí `robots.txt`:** Perplexity používal stealth crawling (předstíral Chrome,
  rotoval ASN — odhalen [[cloudflare|Cloudflare]] honeypotem), backdoor crawleři (Exa, Firecrawl,
  Tavily) berou i obsah za paywallem (jen **4 % z 220 vydavatelů** blokuje Exabot). **Provoz botů
  už překonal lidský**; odtud strategie „block by default, allow by agreement" i úvahy zablokovat
  i Googlebot ([[abbas-2026-unite]] — ⚠️ advokační aktér, strana vydavatelů).
- Právní rámec sporu (fair use, legalita sběru) je oddělený od této technické roviny
  ([[copyright-alliance-2026]], [[norton-rose-2026]]).

## Výhrady a otevřené otázky
- Klíčový advokační zdroj ([[palmieri-hufnagel-2026]]) přesně pojmenovává problém, ale je
  zainteresovaný — hodnota je v rámcování, ne v důkazu.
- Pokud jedna dominantní platforma spojuje vyhledávací a AI crawling, zůstává kontrola
  vydavatelů jen částečná. Agenda je proto i soutěžní, nejen autorskoprávní — viz
  [[regulace-eu-ai-act-dsa]] (UK CMA, AI Act, DSA).

## České specifikum
[[aov|AOV]] doporučuje **diferencovaný přístup** k robotům místo plošné blokace; praxe je
zatím roztříštěná a chybí jednotný standard.

## Zdroje
- [[prchal-2024]], [[deck-2025]], [[palmieri-hufnagel-2026]], [[zhao-berman-2025]]

Souvisí s: [[licencovani-trzni-asymetrie]], [[halucinace-falesne-atribuce]],
[[generativni-optimalizace]], [[google]], [[cloudflare]], [[aov]].
