---
title: Zuccon, Koopman & Shaik (2023) — ChatGPT halucinuje při atribucích
type: zdroj
zdroj-typ: recenzovaná studie
sila-dukazu: střední
rok: 2023
updated: 2026-06-21
publish: true
---

**Plná citace:** Zuccon, G., Koopman, B. & Shaik, R. (2023). „ChatGPT Hallucinates when
Attributing Answers." In *SIGIR-AP '23*, 46–51. DOI: 10.1145/3624918.3625329 (University of
Queensland + CSIRO).
**Odkaz:** https://dl.acm.org/doi/10.1145/3624918.3625329

## Klíčová zjištění
- **První systematická analýza referencí generovaných ChatGPT (GPT-3.5):** 160 odborných otázek
  ze sbírky Ag-valuate (**zemědělství**), s žádostí o odpověď + zdroje, posouzeno experty.
- Odpovědi byly správné/částečně správné jen **~51 %** (49,4 % chybných; 13,1 % plně správných).
- **86 % referencí (385 z 450) neexistovalo** — masivní halucinace zdrojů; z těch existujících
  bylo 85 % na Wikipedii. Reference **vypadají věrohodně** (názvy, „top" časopisy), ale často
  neexistují nebo tvrzení nepodporují → přesně mechanismus **„ceremoniální citace"**.

## Kam ve wiki vstupuje
- [[halucinace-falesne-atribuce]] — empirická opora typu chyby „ceremoniální citace" / falešná atribuce.

## Výhrady / síla důkazu
- **střední:** systematická, ale **doména zemědělství** a **GPT-3.5** — přenos na zpravodajství
  je analogie; novější modely se mohou v atribuci posunout (mechanismus ale zůstává relevantní).
