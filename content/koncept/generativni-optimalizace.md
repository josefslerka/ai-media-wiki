---
title: Generativní optimalizace (AEO / GEO)
type: koncept
tags: [distribuce, vyhledávání, seo, infrastruktura]
updated: 2026-06-21
zdroje: [newman-2026]
publish: true
---
# Generativní optimalizace (AEO / GEO)

Snaha přizpůsobit obsah tomu, jak ho čtou **odpovídací systémy**, ne jen klasické
vyhledávače. Vedle tradičního SEO sem patří **AEO** (Answer Engine Optimization), **GEO**
(Generative Engine Optimization) a standardy typu `llms.txt`. Cíl: aby byl článek čitelný
a citovatelný pro AI souhrny, ne aby jen rankoval v seznamu odkazů.

## Co o tom víme
- **Termíny a techniky.** Tři pojmy, které report uvádí společně:
  - **AEO** (Answer Engine Optimization) — optimalizace na to, aby obsah posloužil jako
    podklad přímé odpovědi odpovídacího rozhraní.
  - **GEO** (Generative Engine Optimization) — optimalizace pro citovatelnost v generativních
    souhrnech (AI Overviews, chatboti).
  - **`llms.txt`** — navrhovaný standard (soubor v kořeni webu), který má LLM nástrojům
    strukturovaně sdělit, co a jak na webu číst.
- **Konkrétní praktiky** (report, doporučení #8 „Přizpůsobit technickou infrastrukturu AI
  vyhledávání"): kvalitní **strukturovaná metadata**, jasné označení **autora, zdroje, data
  publikace a aktualizace** a **logická stavba textu** čitelná pro odpovídací systémy vedle
  klasického SEO.
- Reaguje na posun, kdy vyhledávač přestává hlavně odkazovat a začíná odpovídat
  ([[ai-overviews-zero-click]]).
- Souvisí s defenzivní stranou distribuce: kdo a jak smí obsah číst → [[crawler-separation-opt-out]].

## Výhrady a otevřené otázky
- ⚠️ **Zatím EXPERIMENTÁLNÍ strategie, ne ověřené řešení.** Pojmy AEO/GEO i
  standard `llms.txt` zatím nemají doložený stabilní efekt na viditelnost ani návštěvnost —
  pro tento koncept neexistují tvrdá čísla, síla je v pojmenování technik, ne v měřené účinnosti.
- Riziko: optimalizace pro AI odpovědi může vést k obsahu snadno **zredukovatelnému** na
  souhrn — tedy přesně tomu typu, který odpovídací rozhraní nahrazují nejdřív.
- Není garance, že provoz získaný citací v AI odpovědi nahradí ztracené prokliky (referral
  z AI platforem zatím <1 %).

## České specifikum
ČR má dvě brány (Google + [[seznam|Seznam]]) s vlastními odpovídacími prvky → optimalizace
necílí na jediný systém. Viz [[cesky-trh]]; konec klasického SEO tematizoval i Pavel Ungr
([[nfnz-debata]]).

## Zdroje
- [[newman-2026]] (redakční strategie a infrastruktura), report kap. „Doporučení" (bod 8).
