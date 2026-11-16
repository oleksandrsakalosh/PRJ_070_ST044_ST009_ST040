---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-16T13:50:35.722519+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "f376603d-0bcb-4844-8c7b-430c63b70543"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "setup instructions"

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

# ⚙️ Setup Instructions

## Dodané podklady

- [Herný zdroj memory.py](../../../assets/software/memory.py)
- [Pôvodný print/assembly handoff](../../../assets/model/PRINT-AND-ASSEMBLY.txt)
- [STL diely a rozmery](../../7ds/04.D4-Design/index.md)

### Spustenie – odvodené z kódu, lokálne runtime neoverený

Potrebný je Python 3, Pygame a grafická relácia s funkčným displejom/vstupom. Z koreňa repozitára možno pripraviť samostatné prostredie:

```bash
python3 -m venv /tmp/memobox-venv
/tmp/memobox-venv/bin/python -m pip install pygame
/tmp/memobox-venv/bin/python content/docs/sk/sthdf/PRJ_070_ST044_ST009_ST040/assets/software/memory.py
```

Nejde o reprodukciu pôvodného prostredia na Pi: presná verzia Python/Pygame a OS nie sú dodané. Inštalácia na konkrétnom Pi môže vyžadovať balíky grafického systému. Automatický štart treba doplniť samostatnou konfiguráciou; tento súbor ho nenastavuje.

### Príprava tlače – podľa dodaného handoffu

1. STL importovať v mm pri 100 % mierke. Hlavné teleso vyžaduje približne 169 × 111 × 101 mm priestoru pred pridaním brimu.
2. Najskôr vytlačiť [test konektorov](../../../assets/model/05-display-connector-fit-test.stl). Skontrolovať reálny displej, nízkoprofilový HDMI Type-A a microUSB dátový konektor; zapnúť displej a skontrolovať viditeľnú plochu oproti rámu.
3. Použiť školský profil tlačiarne/filamentu. Handoff uvádza PLA a vrstvu 0,20 mm ako východisko, nie ako odskúšané nastavenie. Náhľad podpor preveriť najmä pri otvoroch a montážnych bodoch.
4. Teleso: strechou na podložke; rám naplocho; spodný kryt stĺpikmi nahor. Difúzor naplocho, priehľadný filament iba ak bude prekrývať svetlo.

### Montáž – návrh podľa handoffu, fyzicky ešte neoverený

1. Displej vložiť spredu s HDMI/USB vpravo pri pohľade spredu. Montážne plôšky sú podľa handoffu 8,7 mm za čelnou plochou; tenké nylonové podložky majú vyrovnať sklo bez jeho zovretia. M2.5 skrutky pre plast zvoliť podľa skutočnej hrúbky uší/podložiek; slepé pilotné otvory asi 5 mm.
2. Pi upevniť na stĺpiky spodného krytu s HDMI a napájaním k pravej stene. M2.5 skrutky; pilotné otvory asi 6 mm. microSD vložiť pri otvorenom kryte.
3. Pre obraz použiť HDMI Type-A na oboch koncoch, pri displeji nízky pravouhlý konektor smerujúci od skla dovnútra. USB-A → microUSB dátový kábel prepojí Touch port displeja a Pi. Napájací kábel Pi viesť bočným otvorom.
4. Rám/spodný kryt používajú M3 spojovací materiál; dĺžku overiť proti slepým otvorom. Difúzor vložiť do hornej priehlbiny, ak sa použije.

TODO: potvrdiť skrutky, podložky, káble, napájanie displeja, tlačiareň, materiál, podporu, výšku reálnej zostavy, následné fotografie a výsledky skúšok.

## Navigácia

- [↩️ Späť](./index.md)

Podklady a rozlíšenie stavov: [evidencia zdrojov](../../7ds/01.D1-Management/05.WorkActivitiesEvidence/index.md).
