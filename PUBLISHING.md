# Publikační workflow — AI, média a žurnalistika

Operační návod, jak se web **[www.aiamedia.cz](https://www.aiamedia.cz/)** staví a aktualizuje.
Filozofii a obsahová pravidla drží `CLAUDE.md` ve vaultu; tady je **jak to technicky publikovat**.

---

## Architektura (kdo je kdo)

| Vrstva | Kde | Role |
|---|---|---|
| **Vault** (kuchyně) | `~/vault/ai-media-wiki` | zdroj pravdy — píše se v Obsidianu; obsahuje i `raw/` (copyright) a interní `%%` poznámky. **NENÍ git repo.** |
| **Web projekt** (generátor) | `~/ai-media-web` | Quartz v4, `publish.py`, deploy workflow. Git repo → GitHub. |
| **Repo** | `github.com/josefslerka/ai-media-wiki` (veřejný) | obsahuje jen `content/` (vydestilovaný web), ne vault ani `raw/`. |
| **Live web** | `www.aiamedia.cz` | GitHub Pages, vlastní doména, HTTPS (Let's Encrypt). |

**Dvouvrstvý model:** vault = kuchyně, web = jídlo. Mezi nimi stojí `publish.py`, který vault
**vydestiluje** do `content/`.

---

## Jak publikovat (3 kroky)

```bash
# 1) Edituj vault (v Obsidianu nebo jakkoli) — ~/vault/ai-media-wiki
#    Stránky na web musí mít ve frontmatteru:  publish: true

# 2) Vygeneruj publikovatelný obsah
cd ~/ai-media-web
python3 publish.py

# 3) Commitni a pushni → GitHub Action sám buildne a nasadí (~2 min)
git add -A
git commit -m "popis změny"
git push
```

Po pushi běží workflow **Deploy Quartz site to GitHub Pages**. Stav:
```bash
gh run watch "$(gh run list --workflow deploy.yml -L1 --json databaseId -q '.[0].databaseId')" --exit-status
```
Po doběhu může **CDN propagace** trvat pár minut (nová stránka chvíli vrací 404 — počkej / hard refresh).

---

## Co `publish.py` dělá (dvouvrstvý model v praxi)

Čte vault → píše `content/`. Konkrétně:

- **Bere jen stránky s `publish: true`** (z adresářů `wiki/ koncept/ entita/ zdroj/ report/` + kořenové
  `index.md`, `katalog.md`, `o-projektu.md`).
- **Stripuje interní bloky `%% … %%`** (reconciliační/provenienční poznámky → zůstávají ve vaultu,
  na web nejdou).
- **Stripuje nadbytečný úvodní `# H1`** (Quartz bere titulek z frontmatteru `title:`, jinak by se
  dubloval).
- **Nikdy nevpustí** `raw/` (cizí/copyrightové materiály) ani `CLAUDE.md`, `STYLE.md`, `log.md`,
  `PROMPTY.md`, `README.md`.

Skript na konci ověří, že v `content/` nezůstal `%%` ani nic z `raw/`.

---

## Obsahová pravidla pro web (shrnutí)

- **`publish: true`** přepíná **člověk po revizi** (generování ≠ publikování). Drafty nech bez pole.
- **Interní vrstvu** (rozpor s parafrází reportu, provenience, „⚠️ Rozpor") obal do `%% … %%`.
  Advokační flagy, sílu důkazu a otevřené otázky nech jako běžný text (jdou ven jako čtenářský hedge).
- **Žádné odkazy na interní schéma** na webu — „viz `CLAUDE.md`", „epistemická pravidla" apod. pryč.
- **Wikilink se zobrazeným textem nesmí mít `/`** — Quartz ho ořízne na poslední segment.
  Místo `[[bbc-ebu|BBC/EBU]]` piš `[[bbc-ebu|BBC a EBU]]`.
- **Závěr vs detail:** mění-li nový zdroj *závěr* → uprav report-hub (`index.md` / `report/*`) +
  řádek do `wiki/co-je-noveho.md`. Jen *detail/obohacení* → stačí dotčená garden stránka.

---

## Struktura webu

- **Domovská `/`** = `index.md` (executive summary, vstupní brána).
- **`/report/*`** = 7 očíslovaných kapitol reportu (`report/` ve vaultu).
- **Garden** = `koncept/ entita/ zdroj/` (prokliknutelná hloubka).
- **`/katalog`**, **`/o-projektu`**, **`/co-je-noveho`**, **`/otevrene-otazky`**.
- Pořadí v levém menu řídí `explorerSort` v `quartz.layout.ts` (report nahoře, O projektu hned za ním).

---

## Doména, HTTPS, náhledové karty

- **Doména:** `www.aiamedia.cz` je GitHub Pages custom domain (Settings → Pages). Apex `aiamedia.cz`
  přesměrovává na www. `baseUrl` v `quartz.config.ts` musí sedět = `www.aiamedia.cz`.
- **HTTPS:** Let's Encrypt, „Enforce HTTPS" zapnuto. Po změně domény trvá vystavení certifikátu i pár hodin.
- **Náhledové karty (OG):** `CustomOgImages` je zapnuté → každá stránka má vlastní kartu s titulem
  v barvách webu. Sociální sítě si první sken cachují (Facebook/LinkedIn mají debugger na re-scrape).

---

## Kontrola před pushem (volitelné)

```bash
cd ~/ai-media-web && python3 publish.py
# rozbité odkazy + uniklé %% + odkazy na CLAUDE.md
python3 - <<'PY'
import re, glob, os
slugs = {os.path.splitext(os.path.basename(f))[0] for f in glob.glob("content/**/*.md", recursive=True)}
bad, leak, schema = set(), [], []
for f in glob.glob("content/**/*.md", recursive=True):
    t = open(f, encoding="utf-8").read()
    if "%%" in t: leak.append(f)
    if "CLAUDE.md" in t: schema.append(f)
    for l in re.findall(r"\[\[([^\]|#]+)", t):
        if l.strip() and l.strip() not in slugs: bad.add(l.strip())
print("rozbité odkazy:", sorted(bad) or "žádné")
print("uniklé %%:", leak or "žádné")
print("odkazy na CLAUDE.md:", schema or "žádné")
PY
```

---

## Troubleshooting (na co jsme narazili)

- **Quartz musí být v4, ne v5** — config je v4-tvaru (`git checkout v4`, pin `@jackyzha0/quartz` v4.x).
- **Menu „Procházet" se nerozbaluje** → `explorerSort` v `quartz.layout.ts` **nesmí mít vnořenou
  funkci** (`const f = () => …`). esbuild ji obalí helperem `__name()`, který v klientském
  `new Function()` neexistuje → celý Explorer spadne. Piš řazení **ploše** (consty + ternární operátor).
- **Dvojitý titulek** → stránka má `# H1` shodný s `title:`. Řeší `publish.py` (strip úvodního H1);
  u kapitol reportu je popisek místo H1 jako tučný perex.
- **Rozbitý náhledový text odkazu** (`SparkToro / Datos` → ` Datos`) → `/` v `[[…|text]]`. Nahraď.
- **Dolarové částky** (`$1,5 mld.`) se lámaly jako LaTeX → `Plugin.Latex` je v configu **vypnutý**.
- **Po pushi vidím starou verzi** → CDN cache + service worker. Hard refresh (Cmd+Shift+R) nebo inkognito.
- **`gh run watch` hlásí „already completed"** → buď doběhlo rychle, nebo se ptáš na předchozí běh;
  ověř `headSha` proti `git rev-parse HEAD`.

---

## Co se NIKDY nepushuje

`raw/` (97 MB cizích/copyrightových PDF), drafty bez `publish: true`, interní `%%` bloky, `CLAUDE.md`,
`STYLE.md`, `log.md`, `PROMPTY.md`. Veřejný repo obsahuje jen čistou publikovanou vrstvu.
