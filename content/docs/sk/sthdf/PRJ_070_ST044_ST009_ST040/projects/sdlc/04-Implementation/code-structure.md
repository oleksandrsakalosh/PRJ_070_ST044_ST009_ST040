---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-16T13:50:35.722941+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "0fea3d04-0da1-4dcd-9a84-f86d1c5540fc"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "code structure"

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

# 🧩 Code Structure

## Dodaný zdrojový kód

[Originálny memory.py](../../../assets/software/memory.py) je uložený bez úprav. Obsahuje Python aplikáciu s Pygame; ďalšie importy random a sys patria do štandardnej knižnice.

| Trieda / funkcia | Zodpovednosť |
|---|---|
| App | Inicializácia, hlavná slučka, menu, výber hry, výsledok a návrat |
| Button, draw_text, header | Kreslenie a interakcia |
| TileGame, decay | Mriežka polí a časované zvýraznenia |
| MemoryGame | Opakovanie sekvencie na mriežke 4 × 4 |
| ChimpGame | Poradie čísel na mriežke 5 × 4 po skrytí |
| WhackGame | Zásahy cieľa na mriežke 3 × 3 |
| RPSGame | Kameň–papier–nožnice s náhodnou voľbou počítača |
| ReactionGame | Päť kôl merania reakcie a priemer v ms |
| GAME_CLASSES | Mapovanie piatich volieb menu na triedy |

### Implementované správanie podľa kódu

Logické rozlíšenie 800 × 480; plná obrazovka so škálovaním; slučka cieli na 30 FPS. Kliknutia sa prijímajú cez MOUSEBUTTONDOWN. Nie je tu samostatná obsluha FINGERDOWN; dotyk musí byť na cieľovom systéme mapovaný na kliknutia.

App drží stav menu/hra/result a posledné skóre. Výsledok sa neukladá do súboru, databázy ani na server. Play Again vytvorí novú inštanciu hry; Esc alebo zatvorenie okna ukončí aplikáciu.

Názov v menu/okne je ešte Memory Testing Device, nie MemoBox Junior. Nie je dodaná konfigurácia automatického spustenia po boote. Plná obrazovka aplikácie sama osebe nie je nastavenie kiosk režimu OS.

TODO: verzia Python/Pygame použitá na Pi, pôvodný commit, autorstvo a licencia zdroja; potvrdiť, či ide presne o verziu predtým testovanú na Pi.

## Navigácia

- [↩️ Späť](./index.md)

Podklady a rozlíšenie stavov: [evidencia zdrojov](../../7ds/01.D1-Management/05.WorkActivitiesEvidence/index.md).
