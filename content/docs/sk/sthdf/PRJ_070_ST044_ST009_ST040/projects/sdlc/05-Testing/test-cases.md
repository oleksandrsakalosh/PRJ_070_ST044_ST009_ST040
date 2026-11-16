---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-16T13:50:35.727051+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "5950dc90-eeb3-42bf-8496-bbad976a6d24"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "test cases"

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

# ✅ Test Cases

## Návrh testovacích scenárov

Všetky scenáre čakajú na vykonanie alebo doloženie výsledku.

| ID | Väzba | Kroky | Očakávaný výsledok |
|---|---|---|---|
| T01 | FR-01 | Spustiť aplikáciu, vybrať postupne pôvodné dve hry. | Obe hry dostupné z menu. |
| T02 | FR-02 | Zopakovať sekvenciu správne a potom s chybou. | Rozlíši správny a chybný vstup. |
| T03 | FR-03 | Zapamätať čísla, po skrytí zvoliť správne/chybné poradie. | Vyhodnotí poradie podľa potvrdených pravidiel. |
| T04 | FR-04 | Dokončiť hru, začať nový pokus. | Výsledok sa zobrazí a nový pokus resetuje stav. |
| T05 | FR-05 | Ovládať menu a herné polia po celej ploche displeja. | Dotyk zodpovedá obrazu, bez vynechania/dvojitého vstupu. |
| T06 | FR-06 | Zapnúť napájanie a sledovať štart. | Rozhranie sa spustí bez práce s desktopom. |
| T07 | HW-01 | Overiť rozmery, osadiť dosku/displej/káble, uzavrieť kryt. | Bez kolízií a namáhania konektorov; prístup k portom. |
| T08 | DOC-01 | Porovnať artefakty s dokumentáciou. | Verzie, modely, montáž a výsledky dohľadateľné. |

TODO: tester, termín, verzia softvéru/CAD, limity odozvy, opakovania a prílohy ku každému testu. Prehrievanie a stabilitu zariadenia treba doplniť po návrhu prevádzkových podmienok.

## Navigácia

- [↩️ Späť](./index.md)

Podklady a rozlíšenie stavov: [evidencia zdrojov](../../7ds/01.D1-Management/05.WorkActivitiesEvidence/index.md).

## Doplnené scenáre podľa S6/S7 – nevykonané pri dokumentovaní

| ID | Rozsah | Overenie |
|---|---|---|
| T09 | Whack-a-Mole | Správny zásah zvýši hits; chyba a timeout ukončia pokus. |
| T10 | Rock-Paper-Scissors | Overiť všetky kombinácie výhra/prehra/remíza, počítadlá a návrat do menu. |
| T11 | Reaction Time | Predčasný dotyk, päť platných kôl a priemerný výsledok v ms. |
| T12 | Stav aplikácie | Nový pokus resetuje stav; Back to Menu a Esc fungujú podľa návrhu. |
| T13 | Mechanický fit-test | Vytlačiť skúšobný diel, vložiť skutočné HDMI/USB, zapnúť displej a preveriť obraz proti rámu. |

TODO: potvrdiť prevzatie rozšíreného päťherného rozsahu a výsledky každej hry. Kódový cieľ 30 FPS ani meranie pygame.time.get_ticks nie sú presnou validáciou hardvérovej latencie.
