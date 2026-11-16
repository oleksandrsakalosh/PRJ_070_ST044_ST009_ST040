---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-16T13:50:35.726103+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "e94b5b06-12c7-488a-a755-63ec028630a5"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "user guide"

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

# 📚 User Guide

## Ovládanie dodanej verzie podľa kódu

Po spustení memory.py sa otvorí menu Memory Testing Device s piatimi voľbami. Automatické spustenie po zapnutí Pi zatiaľ nie je doložené.

1. Vyberte hru kliknutím alebo dotykom mapovaným na kliknutie.
2. **Memory:** počkajte na sekvenciu rozsvietených polí a zopakujte poradie. Po úspechu pribudne úroveň; chyba zobrazí úroveň ako skóre.
3. **Chimp:** čísla si zapamätajte počas 1,2 s; až po skrytí vyberajte pozície v poradí 1, 2, 3… Chyba ukončí pokus.
4. **Whack-a-Mole:** stláčajte rozsvietený cieľ pred uplynutím času. Chyba alebo omeškanie ukončí pokus.
5. **Rock-Paper-Scissors:** zvoľte Rock/Paper/Scissors, sledujte počítadlá výhier, prehier a remíz. Ukončite cez Back to Menu.
6. **Reaction Time:** čakajte na zelenú a potom stlačte plochu; predčasný dotyk vyžaduje opakovanie čakania. Po každom kole pokračujte ďalším dotykom; po piatich kolách sa zobrazí priemer v ms.

Back to Menu je dostupné počas hier. Výsledková obrazovka podporuje Play Again a Back to Menu. Esc ukončí aplikáciu, nie operačný systém.

TODO: screenshoty z Pi, overený spôsob zapnutia/vypnutia zariadenia a obsluha bez klávesnice. Vhodnosť pre konkrétny detský vek zostáva neoverená.

## Navigácia

- [↩️ Späť](./index.md)

Podklady a rozlíšenie stavov: [evidencia zdrojov](../../7ds/01.D1-Management/05.WorkActivitiesEvidence/index.md).
