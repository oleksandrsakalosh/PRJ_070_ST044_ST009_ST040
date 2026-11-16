---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-16T13:50:35.762518+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "e87e6ee3-3ece-49d8-9fc5-480f573b1aeb"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "project summary"

# Krátky popis – dopĺňa používateľ (voliteľné)
description: "{{DESCRIPTION}}"


# 👥 AUTHORSHIP ------------------------------------------------------

# Hlavný autor – z globálneho configu
author: "Roman Kazicka"

# Zoznam autorov – generuje skript
authors:
  - "Roman Kazicka"


# 🗂 CLASSIFICATION ---------------------------------------------------

# Nadradená kategória – môže doplniť používateľ
category: ""

# Typ dokumentu (guide, case, tutorial...) – používateľ (voliteľné)
type: ""

# Priorita (low/medium/high) – voliteľné
priority: ""

# Tagy – odporúča sa 2–6 tagov.
# Typy tagov:
#   - rámce: knife, 7ds, sdlc, q12
#   - účel: tutorial, guide, pattern, case-study
#   - téma: git, backup, ai, communication
#   - úroveň: beginner, intermediate, advanced
tags: []


# 🌍 LOCALIZATION -----------------------------------------------------

# Jazyk dokumentu – doplní skript podľa štruktúry
locale: "sk"


# 🕒 LIFECYCLE --------------------------------------------------------

# Dátum vytvorenia – generuje skript
created: "2026-11-16 14:50"

# Dátum poslednej úpravy – dopĺňa človek
modified: "2026-11-16 14:50"

# Stav dokumentu – default "backlog"
status: "backlog"

# Viditeľnosť – default "public"
privacy: "public"


# ⚖ INTELLECTUAL PROPERTY -------------------------------------------

# Držiteľ práv k obsahu – dopĺňa skript
rights_holder_content: "Roman Kazicka"

# Systémový vlastník práv
rights_holder_system: "CAA / KNIFE / LetItGrow"

# Licencia
license: "CC-BY-NC-SA-4.0"

# Disclaimer
disclaimer: "Use at your own risk. Methods provided as-is; participation is voluntary and context-aware."

# Copyright
copyright: "© 2025 Roman Kazicka"


# 🔗 ORIGIN / PROVENANCE ---------------------------------------------

# Repozitár pôvodu
origin_repo: ""

# URL pôvodného repozitára
origin_repo_url: ""

# Commit pôvodu
origin_commit: ""

# Branch pôvodu
origin_branch: ""

# Systém pôvodu (CAA/KNIFE/STHDF…)
origin_system: "CAA"

# Pôvodný autor
origin_author: "Roman Kazicka"

# Importovaný zdroj
origin_imported_from: ""

# Dátum importu
origin_import_date: ""


# 🧱 RESERVED ---------------------------------------------------------

fm_reserved1: ""
fm_reserved2: ""
---

<!-- SDLC_INSTANCE_ID: PRJ_070_ST044_ST009_ST040 -->

# 📝 Project Summary – MemoBox Junior

## Identifikácia a zámer

- **Kód:** PRJ_070_ST044_ST009_ST040.
- **Názov:** MemoBox Junior, potvrdený používateľom.
- **Opis:** samostatné stolové zariadenie s Raspberry Pi a dotykovou obrazovkou pre pamäťové a reakčné hry. Súčasťou zámeru je vlastný kryt vyrobený 3D tlačou a systémový model v EA.

### Členovia a evidencia príspevkov

| ST ID | Meno | Potvrdená rola / príspevok |
|---|---|---|
| ST044 | Sakalosh Oleksandr, Bc. | Príspevky uvedené nižšie; TODO presný rozsah |
| ST009 | Lykhachov Yehor, Bc. | Príspevky uvedené nižšie; TODO presný rozsah |
| ST040 | Mareček Ján, Bc. | Príspevky uvedené nižšie; TODO presný rozsah |

Používateľ potvrdil účty a mená. Chat dokladá tieto aktivity:

- **ST009 Yehor / upsil00n:** pôvodný návrh, komunikácia o softvéri a EA, výber komponentov.
- **ST040 Ján / janinix:** poskytnutie a skúška displeja, zdieľanie modelov a STL, parametre displeja.
- **ST044 Oleksandr / _signum_:** poster, kontrola montážnych otázok, kontaktovanie SmartLabu a tímový repozitár.

Ide o evidenciu konkrétnych aktivít, nie o automatické pridelenie formálnych rolí. TODO potvrdiť úplný rozsah a autorstvo zdrojových súborov.

### Motivácia, cieľ a hodnota

Spojiť vývoj interaktívnych hier, systémový návrh a digitálnu fabrikáciu do jedného prototypu. Memory test má pracovať s opakovaním sekvencie; Chimp test s poradím čísel po ich skrytí. V dodanom kóde sa čísla skryjú po 1,2 s a vstup pred skrytím sa ignoruje.

Poster navrhuje hravé používanie v materských školách a pri práci pedagógov s deťmi. Ide o hodnotovú hypotézu. Prínos pre pamäť, vhodnosť pre konkrétny vek a bezpečnosť produktu nie sú overené.

### Rozsah a úspech

Pôvodný rozsah: Memory a Chimp. Dodaný kód navyše implementuje Whack-a-Mole, Rock-Paper-Scissors a Reaction Time, spolu päť hier. Automatické spustenie po zapnutí, fyzický kryt a dokumentácia zostávajú súčasťou zámeru; boot konfigurácia nie je dodaná. Kritériá prevzatia sú zatiaľ návrh: pôvodné dve hry ovládateľné na cieľovom displeji, funkčný štart, komponenty bez kolízií v kryte, zdokumentované výsledky testov. TODO schváliť s tímom.

Mimo doloženého rozsahu zostávajú cloudové účty, klinická diagnostika, overené zlepšenie pamäti a komerčné nasadenie.

### Plán a očakávané výstupy

1. Doplniť EA a parametrický CAD; označiť verziu dodaného kódu a STL.
2. Skontrolovať rozmery displeja, dosky, otvorov a priestor HDMI.
3. Dohodnúť SmartLab, materiál a parametre tlače.
4. Vytlačiť, zmontovať a vykonať integračné skúšky.
5. Pripraviť demo, výsledky a prezentáciu.

TODO: termíny, zodpovednosti, rozpočet a týždenná kapacita. Približne 100 EUR zo septembrového chatu bol iba orientačný AI odhad.

### Riziká a ďalšie kroky

Hlavné riziká: neoverené rozmery, káble, odozva dotyku, dostupnosť tlače, chýbajúce EA/CAD a dôkazy testov. Druhá výrobná technológia bola navrhnutá, jej použitie ani aktuálna požiadavka kurzu nie sú potvrdené.

[Podrobný projektový dashboard](../../projects/index.md)

## Navigácia

- [↩️ Späť](../index.md)

Podklady a rozlíšenie stavov: [evidencia zdrojov](../../projects/7ds/01.D1-Management/05.WorkActivitiesEvidence/index.md).
