---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-16T13:50:35.722723+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "1cd8e136-bdf5-41ec-83b7-cb443ca046aa"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "used technologies"

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

# 🧰 Used Technologies

## Doložené technológie

| Prvok | Zdroj / stav |
|---|---|
| Python + Pygame | Importy a implementácia v memory.py; verzie TODO |
| 800 × 480, fullscreen/scaled, 30 FPS cieľ | Konštanty a inicializácia aplikácie; nejde o nameraný výkon |
| Päť hier | Triedy a GAME_CLASSES v dodanom zdroji |
| Raspberry Pi 3 Model A+ | Cieľová doska uvedená v print/assembly handoffe |
| Elecrow 5-inch LCD Display-B Rev 1.1 | Cieľový displej uvedený v handoffe |
| HDMI Type-A / USB-A → microUSB data | Navrhnuté zapojenie v handoffe |
| 5 STL súborov | Teleso, rám, spodný kryt s Pi držiakom, difúzor, test konektorov |
| PLA, 0,20 mm vrstva | Odporúčané východisko v handoffe; neodskúšané |
| EA | Práca hlásená v chate; zdroj a exporty TODO |
| Raspberry Pi OS, kiosk | Pôvodný návrh; verzia OS a boot konfigurácia TODO |

Používateľ potvrdil dodanie a testovanie komponentov. Parametre displeja 121,11 × 95,24 mm a 5-bodový kapacitný dotyk pochádzajú z chatu; fyzické rozmery a aktuálny datasheet ešte nie sú doložené. Objednávky, zdroj napájania, microSD a skutočné náklady: TODO.

## Navigácia

- [↩️ Späť](./index.md)

Podklady a rozlíšenie stavov: [evidencia zdrojov](../../7ds/01.D1-Management/05.WorkActivitiesEvidence/index.md).
