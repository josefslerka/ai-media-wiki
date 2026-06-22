---
title: Licencování a tržní asymetrie
type: koncept
tags: [data, licence, ekonomika]
updated: 2026-06-21
zdroje: [egan-2026-dnr, schaul-2023, radsch-2024, reisner-2025, commoncrawl-2025, guaglione-2025, deck-2025, prchal-2024, copyright-alliance-2026, norton-rose-2026, rsl-collective-2025, slpv-2026, nyt-v-openai, abbas-2026-unite]
publish: true
---

Dvě roviny, které se v debatě pletou: **právní spor** o legitimitu dat (smí se na
mediálním obsahu trénovat?) a **ekonomická asymetrie** (kdo z nového trhu reálně získává).

## Co o tom víme
- Žurnalistika nebyla pro raný vývoj LLM okrajová (C4, velké korpusy obsahovaly NYT,
  Guardian, Forbes — [[schaul-2023|Schaul et al. 2023]], [[radsch-2024]]). Silnější teze
  „bez novinářských dat by modely nefungovaly" je plauzibilní strategický závěr, ne změřený fakt.
- Licenční dohody uzavírá hlavně [[openai|OpenAI]]: Brookings mezi partnery jmenuje
  **Associated Press, Axel Springer, Le Monde, Prisa Media, Financial Times, Time, Condé Nast**
  ([[radsch-2024]]); další dohody uzavřely **News Corp, CNN, USA Today, Fox News, People**.
  Menší a lokální vydavatelé zůstávají mimo → koncentrace příjmů u pár velkých hráčů
  ([[radsch-2024]], [[guaglione-2025]]).
- ~70 % mediálních manažerů čeká nějaký příjem z licencování, většinou jen vedlejší;
  konkrétněji **49 % čeká jen minoritní příjem a 20 % žádný** (Newman 2026). Jde o
  **očekávání**, ne vykázané příjmy.
- **Právní rovina** (legitimita dat, fair use, [[nyt-v-openai|spor NYT vs. OpenAI]]) je
  oddělená od ekonomické ([[copyright-alliance-2026]] — ⚠️ hájí držitele práv; [[norton-rose-2026]]).
  Regulatorní rámec viz [[regulace-eu-ai-act-dsa]].
- Kolektivní řešení ([[rsl-collective|RSL Collective]], [[slpv|SLPV]], oborové aliance jako News
  Media Alliance) a monetizační/licenční protokoly (TollBit, Prorata, x402, IAB) se teprve rodí —
  zatím spíš obranný mechanismus než ověřený ekonomický model ([[rsl-collective-2025]],
  [[slpv-2026]], [[abbas-2026-unite]] — ⚠️ strana vydavatelů). Marginální přínos AI dokládá i podíl
  **0,27 % návštěvnosti** zpravodajství z generativní AI (SimilarWeb, [[abbas-2026-unite]]).
- Technická obrana přístupu k obsahu → [[crawler-separation-opt-out]]; tlak na levný
  [[synteticky-obsah]] zvyšuje hodnotu původního obsahu.

## Výhrady a otevřené otázky
- Chybí veřejně srovnatelná data o velikosti dohod.
- Transparentnost původu dat ([[common-crawl|Common Crawl]]) zůstává omezená
  ([[reisner-2025]] vs. ⚠️ [[commoncrawl-2025]]).
- Opt-out z tréninku se nemusí vztahovat na nasazení modelu ve vyhledávání
  ([[deck-2025]]; debata o oddělení crawlerů u [[google|Googlu]] a [[cloudflare|Cloudflare]]).

## České specifikum
Malý jazykový trh, roztříštěná vyjednávací pozice; k jaru 2026 žádná dohoda domácí médium ↔
vývojář AI. Institucionální rámec: [[spir|SPIR]] a [[slpv|SLPV]] (kolektivní správa práv
vydavatelů). Právní rámec TDM opt-outu je obranný, ale bez vymahatelnosti omezený
([[prchal-2024]]). Viz [[cesky-trh]].
