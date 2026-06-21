---
title: "4. Reputační a faktické škody"
type: report
tags: [report, halucinace, reputace]
updated: 2026-06-21
publish: true
---
**Halucinace, falešné atribuce a meze obrany.**

Vedle ekonomických dopadů generativní AI čelí média také riziku reputačních a faktických škod. Část
vydavatelů reagovala technickou blokací robotů nebo omezením přístupu k obsahu. Tato obrana však má
vedlejší náklady a sama o sobě neřeší hlavní problém: AI systémy mohou nepřesně shrnovat, vytrhávat
z kontextu a [[halucinace-falesne-atribuce|přisuzovat médiím tvrzení]], která nikdy nepublikovala.

## Technická obrana má vedlejší náklady

Mnoho vydavatelů začalo chránit své články úpravou souboru `robots.txt`, tedy omezením přístupu
některých automatizovaných systémů k obsahu. Logika tohoto kroku je srozumitelná: zabránit využívání
redakční práce bez souhlasu vydavatele. Dostupná data však naznačují, že plošná blokace může mít
i negativní důsledky pro viditelnost média.

Working paper Zhaoa a Bermana ukazuje, že u velkých webů vedlo zablokování botů k poklesu celkové
návštěvnosti i návštěvnosti od lidských uživatelů. Autoři to vysvětlují tím, že médium po omezení
přístupu ztrácí část citovanosti v nových odpovídacích rozhraních a tím i část sekundární viditelnosti
([[zhao-berman-2025]]). Jde o pracovní studii, nikoli o definitivní důkaz. Přesto dobře ukazuje
[[crawler-separation-opt-out|strategické dilema]]: technická obrana proti těžbě dat nemusí automaticky
chránit distribuci ani reputaci.

## Problém nejsou jen halucinace, ale i způsob zdrojování

Nejsilnější empirickou oporu má v této kapitole studie [[bbc-ebu|BBC a EBU]], jejíž autory jsou Fletcher
a Verckist a do níž se zapojil i [[cesky-rozhlas|Český rozhlas]]. Testování více než 2 700 odpovědí
čtyř hlavních AI asistentů našlo závažné zkreslení zhruba ve 45 procentech odpovědí a ukázalo, že pro
média nejsou nejrizikovější jen prosté věcné chyby. Závažná jsou i strukturální selhání ve zdrojování:
falešné citace, zaměněné autorství, vkládání vlastních hodnotících soudů do odpovědi nebo odkazy, které
pouze předstírají přesnost ([[fletcher-verckist-2025]]).

Tyto chyby lze rozlišit do čtyř typů:

- *věcná chyba*, kdy model uvede nesprávný údaj nebo zastaralý fakt,
- *ztráta kontextu*, kdy AI zjednoduší nebo posune význam původního sdělení,
- *falešná atribuce*, kdy model médiu nebo autorovi připíše tvrzení, které nikdy nevyslovili,
- *ceremoniální citace*, kdy odpověď vypadá zdrojovaně, ale odkazovaný článek generované tvrzení ve
  skutečnosti nepodporuje.

Poslední dva mechanismy jsou pro média zvlášť citlivé. Nejde už jen o technologickou nepřesnost, ale
o zásah do důvěryhodnosti konkrétní značky.

## Falešné atribuce představují přímé reputační riziko

Studie BBC/EBU ukazuje, že modely mohou směšovat fakta, citace a názory způsobem, který poškozuje
vnímání nestrannosti médií. V některých případech AI připisovala veřejnoprávním médiím aktivistické
nebo hodnotící postoje, které v původním textu nebyly. Jinde si naopak vymýšlela přímé citace nebo
odkazovala na reálně existující článek, jenž však příslušné tvrzení vůbec neobsahoval
([[fletcher-verckist-2025]]).

To je rozdíl oproti běžné chybě v odpovědi chatbota. Pokud AI uvede chybnou informaci bez zdroje,
uživatel může chybu připsat stroji. Pokud tentýž výrok falešně opře o důvěryhodné médium, přenáší se
část reputačního nákladu právě na tuto značku. Dotazníková data citovaná ve studii naznačují, že část
publika má tendenci přenášet vinu za chybu AI i na citovaný zdroj. Nejde o dlouhodobě změřený propad
důvěry, ale o doložené reputační riziko, které vzniká už samotným mechanismem falešné atribuce.

## Právní odpovědnost se poprvé přesouvá na platformu

Reputační riziko falešné atribuce přestává být jen teoretické. V červnu 2026 [[regulace-eu-ai-act-dsa|mnichovský
soud rozhodl]], že [[google|Google]] je právně odpovědný za nepravdivá tvrzení ve svých AI Overviews,
a označil je za „vlastní obsah Googlu", nikoli za pouhé zobrazení cizího webu. Žalobu podali dva němečtí
vydavatelé, které AI souhrny falešně spojily s podvodnými praktikami, tedy přesně ten typ falešné
atribuce, který tato kapitola popisuje. Google se odvolává s argumentem, že jde o úzké a ojedinělé chyby
a většina výstupů je přesná ([[foo-2026]]).

Jde zatím o jediný prvostupňový rozsudek pod odvoláním, jurisdikčně omezený na Německo, takže z něj
nelze dělat ustálený precedent. Význam má ale v jednom ohledu: poprvé je část odpovědnosti za chybu
přiřčena platformě, která odpověď vygenerovala, nikoli pouze značce, jež byla falešně ocitována. Pokud
by tento výklad obstál i u vyšších soudů, posunul by debatu o falešných atribucích z roviny reputační
škody do roviny přímé právní odpovědnosti vývojářů AI.

## Nepřesnost je širší problém než jen u zpravodajství

Podobné mechanismy se objevují i mimo oblast zpráv. Peters a Chin-Yee ukázali, že některé modely mají
při shrnování vědeckých textů sklon k nadsazování tvrzení a k nepřesným zobecněním častěji než lidští
autoři ([[peters-chin-yee-2025]]). Další analýzy upozorňují na problém neexistujících nebo chybných
zdrojů v odpovědích, které pouze vytvářejí dojem důvěryhodného doložení ([[noreika-2026]];
[[zuccon-2023]]).

Pro zpravodajství je však problém citlivější než v jiných oblastech. Média svou legitimitu stavějí na
tom, že výrok lze přiřadit konkrétnímu zdroji, kontextu a odpovědnosti. Když AI tento řetězec naruší,
poškozuje samotný mechanismus důvěry.

## Česká scéna: chytrá obrana a konkrétní selhání

V domácím prostředí se ukazuje, že úplné uzamykání webů nemusí být nejúčinnější strategií.
[[aov|Asociace online vydavatelů]] doporučila svým členům spíše diferencovaný přístup: blokovat roboty
určené pro stahování tréninkových dat, ale pečlivě zvažovat, zda nechat otevřený přístup systémům,
které ovlivňují citovanost a vyhledávací viditelnost ([[aov-2025]]).

Český trh se zároveň už setkal i s konkrétními reputačními selháními. Český rozhlas v rámci testování
EBU doložil případy, kdy AI systémy používaly problematické zdroje z českého informačního prostoru nebo
šířily věcně nepravdivá tvrzení, například o právním statusu náhradního mateřství ([[cesky-rozhlas-2025]]).
Tyto příklady ukazují, že nejde jen o zahraniční problém nebo o anglofonní prostředí.

### Česká perspektiva: Jan Cibulka a minimální hranice spolehlivosti

[[nfnz-debata|Debata NFNZ]] v pražském Operu doplnila tato zjištění o konkrétní redakční zkušenost. Jan
Cibulka z Českého rozhlasu zde upozornil, že zpravodajství nemůže hodnotit AI podle jejího maximálního
potenciálu, ale podle minimální garantované spolehlivosti v běžném provozu. U tvrdého zpravodajství může
i zdánlivě malá chyba, například vypuštěný zápor nebo ztracený kontext výroku, zásadně změnit význam
sdělení.

Tato zkušenost vysvětluje, proč jsou pro seriózní redakce tak nebezpečné právě falešné atribuce
a významové posuny. Nejde jen o technickou nepřesnost, ale o zásah do základního vztahu mezi médiem
a publikem, který stojí na předpokladu, že zveřejněné tvrzení lze dohledat, ověřit a přiřadit
konkrétnímu zdroji a odpovědnosti.

---

Pokračovat: [[promena-redakce|Exo-žurnalistika →]] · zpět na [[index|úvod reportu]]
