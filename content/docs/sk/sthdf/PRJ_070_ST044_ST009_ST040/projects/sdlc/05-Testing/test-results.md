---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-16T13:50:35.727312+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "b1379c96-c01d-41e4-8f4e-ca7527a9598a"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "test results"

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

# 📊 Test Results

## Dostupné záznamy overenia

| Udalosť | Záznam | Čo dokladá |
|---|---|---|
| Displej s PC, hlásenie 5. 10. 2026 | Správa janinix, S1 | Autorské hlásenie funkčnosti na PC; bez protokolu |
| Komponenty a prvá herná verzia na Pi | Potvrdené používateľom | Komponenty dodané a testované, hra testovaná na Pi; konfigurácia a presný rozsah TODO |
| Overenie rozmerov CAD | TODO | Úloha bola zadaná, dokončenie nepotvrdené |
| Tlač a montáž | TODO | Výroba nebola doložená |
| T01–T08 | TODO | Návrh testov nie je úspešný výsledok |

Konkrétne T01–T08 zatiaľ nie sú označené ako úspešné. Používateľské potvrdenie všeobecného testovania nie je podrobný protokol oboch hier alebo kiosk režimu. Doplniť dátum, testera, konfiguráciu, skutočný výsledok a prílohu.

## Navigácia

- [↩️ Späť](./index.md)

Podklady a rozlíšenie stavov: [evidencia zdrojov](../../7ds/01.D1-Management/05.WorkActivitiesEvidence/index.md).

## Kontrola nových súborov pri dokumentovaní

- S6: syntaktická kontrola Pythonu úspešná; runtime test nevykonaný, Pygame tu nie je nainštalovaný.
- S7: binárna dĺžka, počty trojuholníkov a obálky piatich STL skontrolované. Tlač ani fyzický fit nevykonané.
- T09–T13: navrhnuté, bez výsledkov.

TODO: potvrdiť zhodu dodanej päťhernej verzie s predchádzajúcim testom na Raspberry Pi.
