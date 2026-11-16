---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-16T13:50:35.727761+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "c6bb8790-2691-43d2-9124-5a6e8b521d45"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "ui mockups"

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

# 🎨 UI Mockups

## Rozhranie podľa dodaného kódu

Menu Memory Testing Device obsahuje päť volieb: Memory Test, Chimp Test, Whack-a-Mole, Rock-Paper-Scissors a Reaction Time. Logický priestor má 800 × 480 px; aplikácia používa fullscreen a škálovanie Pygame.

- **Memory:** 4 × 4 polí po 80 px, medzera 14 px. Sekvencia má level + 2 prvky, prvá úroveň tri. Zobrazenie prvku 0,6 s, medzi prvkami 0,25 s; chyba ukončí hru a zobrazí aktuálnu úroveň.
- **Chimp:** 5 × 4 polí po 78 px, medzera 10 px. Čísla sú viditeľné 1,2 s; dovtedy sa herné kliknutia ignorujú. Po skrytí sa vyberajú vzostupne. Počet čísel min(level + 2, 20); chyba zobrazí aktuálnu úroveň.
- **Whack:** 3 × 3 cieľov, limit od 1,6 s k minimu 0,5 s so zrýchlením 0,1 s na zásah. Chybný zásah alebo vypršanie času ukončí hru; skóre je počet zásahov.
- **RPS:** voľby Rock/Paper/Scissors, priebežné výhry/prehry/remízy. Hra pokračuje do návratu do menu, nepoužíva spoločnú výsledkovú obrazovku.
- **Reaction:** náhodné čakanie 1–3 s, potom zelená plocha. Predčasný dotyk vyvolá Too soon; po piatich platných kolách výsledok zobrazí priemerný reakčný čas v ms.

Pri hrách je Back to Menu. Spoločný výsledok má Play Again a Back to Menu. Esc ukončuje aplikáciu.

[Poster](../../../assets/poster.png) ilustruje pôvodný dvojherný koncept; nie je screenshotom tejto päťhernej verzie. UI je anglické; veková vhodnosť, dotyková ergonómia a reálne screenshoty: TODO.

## Navigácia

- [↩️ Späť](./index.md)

Podklady a rozlíšenie stavov: [evidencia zdrojov](../../7ds/01.D1-Management/05.WorkActivitiesEvidence/index.md).
