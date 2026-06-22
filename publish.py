#!/usr/bin/env python3
"""
Publikační krok pro dvouvrstvý model (viz CLAUDE.md ve vaultu).

Vault = kuchyně (zdroj pravdy, vč. raw/ a interních %% bloků).
content/ = jídlo = jen to, co jde ven:
  - jen stránky s `publish: true`
  - interní bloky `%% … %%` stripnuté
  - raw/, CLAUDE.md, STYLE.md, log.md, PROMPTY.md, README.md, .obsidian NIKDY

Spouštěj lokálně před commitem. content/ se commituje; CI ho jen builduje.
"""
import os, re, shutil, sys

VAULT = "/Users/josefslerka/vault/ai-media-wiki"
OUT   = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")
# adresáře vaultu, které se publikují (zbytek se ignoruje úplně)
INCLUDE_DIRS = ["wiki", "koncept", "entita", "zdroj", "report"]
INCLUDE_ROOT_FILES = ["index.md", "katalog.md", "o-projektu.md"]
# pojistka: tyhle se nepublikují, ani kdyby měly publish:true
NEVER = {"CLAUDE.md", "STYLE.md", "log.md", "PROMPTY.md", "README.md"}

FM_RE = re.compile(r'^---\n(.*?)\n---', re.S)
PUB_RE = re.compile(r'^publish:\s*true\s*$', re.M)

def is_published(text):
    m = FM_RE.match(text)
    return bool(m and PUB_RE.search(m.group(1)))

def strip_internal(text):
    # odstraň Obsidian komentáře %% … %% (interní vrstva) + slij vzniklé prázdné řádky
    text = re.sub(r'%%.*?%%', '', text, flags=re.S)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text

def strip_title_h1(text):
    # Quartz vykresluje title z frontmatteru jako nadpis stránky; nadbytečný úvodní # H1
    # v těle by se dubloval. Strip jen vede-li hned za frontmatterem. (Kapitoly reportu
    # mají popisek jako tučný perex, ne H1 — ty se nesmažou.)
    m = FM_RE.match(text)
    if not m:
        return text
    end = m.end()
    head, body = text[:end], text[end:]
    body = re.sub(r'^\s*# [^\n]*\n', '\n', body, count=1)
    return head + body

def collect():
    files = []
    for d in INCLUDE_DIRS:
        p = os.path.join(VAULT, d)
        if os.path.isdir(p):
            for fn in sorted(os.listdir(p)):
                if fn.endswith(".md"):
                    files.append((d, fn))
    for fn in INCLUDE_ROOT_FILES:
        if os.path.exists(os.path.join(VAULT, fn)):
            files.append(("", fn))
    return files

def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT, exist_ok=True)
    published = skipped = 0
    leaked = []
    for d, fn in collect():
        if fn in NEVER:
            continue
        src = os.path.join(VAULT, d, fn)
        text = open(src, encoding="utf-8").read()
        if not is_published(text):
            skipped += 1
            continue
        out_text = strip_title_h1(strip_internal(text))
        if "%%" in out_text:
            leaked.append(os.path.join(d, fn))
        outdir = os.path.join(OUT, d)
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, fn), "w", encoding="utf-8") as f:
            f.write(out_text)
        published += 1
    print(f"publikováno: {published} | přeskočeno (ne publish:true): {skipped}")
    if leaked:
        print("‼️ VAROVÁNÍ: nepárový %% zůstal v:", leaked)
        sys.exit(1)
    # pojistka proti copyrightu: ať se do content/ nikdy nedostane nic z raw/
    if os.path.exists(os.path.join(OUT, "raw")):
        print("‼️ raw/ se objevilo v content/ — to nesmí!")
        sys.exit(1)
    print("OK ✅  (raw/ ani interní bloky v content/ nejsou)")

if __name__ == "__main__":
    main()
