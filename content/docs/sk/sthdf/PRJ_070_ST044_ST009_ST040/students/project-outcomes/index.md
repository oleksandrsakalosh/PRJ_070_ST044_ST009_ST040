---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-16T13:50:35.761987+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "520d58c1-acbe-470a-9a9e-fab1a3194a46"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "project outcomes"

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

# 📦 Project Outcomes

## Dostupné výstupy k 16. 11. 2026

| Výstup | Stav | Dôkaz / obmedzenie |
|---|---|---|
| Vizuálny model krytu | Dostupný | [Snímka modelu](../../assets/model.png); bez rozmerového overenia |
| Poster | Dostupný | [MemoBox Junior](../../assets/poster.png); propagačný koncept |
| Herný softvér | Prvá verzia vyvinutá a testovaná na Pi podľa používateľa | Používateľské potvrdenie; [memory.py](../../assets/software/memory.py); TODO demo a verzia testu |
| STL a montážny handoff | Dostupné | [Päť dielov a rozmery](../../projects/7ds/04.D4-Design/index.md); parametrický CAD TODO |
| Systémové diagramy | Rozpracovanosť hlásená | TODO EA a exporty |
| Vytlačený a zmontovaný prototyp | Nepotvrdený | TODO fotografie a postup |
| Test komponentov a hry na Pi | Potvrdený používateľom | TODO konfigurácia, rozsah a výsledky |

### Plán verzus dosiahnutý stav

Zámerom je kompletné zariadenie; pôvodný koncept má dve hry, dodaný kód päť. Dostupné artefakty dokladajú vizuálny návrh a poster; komunikácia a používateľské potvrdenie dopĺňajú softvér testovaný na Pi a dodané/otestované komponenty. Nemožno z nej potvrdiť hotový integrovaný produkt.

### Čo doplniť na odovzdanie

- [ ] Potvrdenie, že dodaný memory.py zodpovedá verzii testovanej na Pi.
- [ ] Parametrický CAD a fotografie vyrobených častí (STL už dodané).
- [ ] EA diagramy a väzba na požiadavky.
- [ ] Video alebo fotografie behu oboch hier na zariadení.
- [ ] Protokol testov a individuálne príspevky potvrdené členmi.

[Projektový dashboard](../../projects/index.md)

## Navigácia

- [↩️ Späť](../index.md)

Podklady a rozlíšenie stavov: [evidencia zdrojov](../../projects/7ds/01.D1-Management/05.WorkActivitiesEvidence/index.md).
