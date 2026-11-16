---
# 🧩 Versioning – systém dopĺňa automaticky
fm_version: "1.0.1"

# Dátum buildu – generuje skript
fm_build: "2026-11-16T13:50:35.743148+00:00"

# Poznámka k verzii – voliteľné
fm_version_comment: ""


# 🆔 IDENTITY --------------------------------------------------------

# ID generuje CLI / skript

# Unikátne UUID – generuje skript
guid: "d7da8eea-9711-497d-9511-eeddc0c7b1fa"


# 🧭 CONTEXT ---------------------------------------------------------

# DAO / doména (knife, sdlc, q12, 7ds...) dopĺňa skript
dao: "sthdf"

# Názov zápisu – dopĺňa používateľ
title: "05.WorkActivitiesEvidence"

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

# Work Activities Evidence

## Zdroje a spôsob čítania dokumentácie

Stav zachytený podľa podkladov dostupných **16. 11. 2026**. Projekt: PRJ_070_ST044_ST009_ST040.

- **Doložené artefaktom:** súbor alebo obrázok je dostupný v tomto repozitári.
- **Hlásené v komunikácii:** tvrdenie člena tímu; chýba nezávislé overenie alebo spustiteľný artefakt.
- **Plán / návrh:** zamýšľaná funkcia alebo odporúčaný ďalší postup.
- **TODO:** údaj alebo dôkaz treba doplniť.

### Register podkladov

| Zdroj | Obsah | Obmedzenie |
|---|---|---|
| S1 | Discord export `DirectMessages-SMVIT.json`, 223 správ, 29. 9. – 16. 11. 2026; export 16. 11. 2026 o 15:34 +01:00 | Súkromný originál je v rodičovskom priečinku; celý chat sa do dokumentácie nekopíruje. |
| S2 | [Snímka modelu](../../../../assets/model.png) | Doklad vizuálneho návrhu; neobsahuje overiteľné rozmery ani parametrický zdroj. |
| S3 | [Poster MemoBox Junior](../../../../assets/poster.png) | Propagačný koncept, nie fotografia funkčného produktu ani výsledok testu. |
| S4 | Mená a ST ID zadané používateľom | ST044 Oleksandr, ST009 Yehor, ST040 Ján. |
| S5 | Doplnenie používateľa pri príprave dokumentácie | Potvrdil názov MemoBox Junior; _signum_ = Oleksandr, upsil00n = Yehor, janinix = Ján; komponenty objednané/dodané/testované a prvá verzia hry testovaná na Pi. Kryt nie je vytlačený. V tomto okamihu používateľ ešte nemal kód/EA/CAD; následne doplnil S6/S7. Podrobné testy a kiosk neboli potvrdené. |

### Vybrané záznamy zo S1

Dátumy sú uvedené podľa časových značiek exportu. Texty sú vecné parafrázy.

| Dátum | ID správy | Autor účtu | Projektová informácia |
|---|---|---|---|
| 29. 9. 2026 | 1554525698318798859 | upsil00n | Návrh Raspberry Pi, dotykového displeja, hier Memory a Chimp, kiosk režimu, 3D krytu a systémového modelu. Druhá výrobná technológia je iba návrh. |
| 29. 9. 2026 | 1554526396519546932 | upsil00n | Orientačný AI odhad približne 100 EUR; nejde o rozpočet ani skutočné výdavky. |
| 29. 9. 2026 | 1554592479632957440 | upsil00n | Odkaz na Raspberry Pi 3 Model A+; výber/obstaranie konkrétneho kusu treba doložiť. |
| 5. 10. 2026 | 1556598067040354395 | janinix | Displej podľa autora fungoval po pripojení k PC; bez testovacieho protokolu. |
| 11. 10. 2026 | 1558799954653216809 | upsil00n | Diagramy kreslené do EA s textovou pomocou Claude. |
| 19. 10. 2026 | 1561679053419716611 | upsil00n | Softvér označený za hotový; kód ani ukážka neboli dodané na kontrolu. |
| 19. 10. 2026 | 1561679099120984065 | upsil00n | Diagramy odhadnuté približne na 25 %; historický odhad, nie dnešný stav. |
| 19. 10. 2026 | 1561745209065218264 | janinix | Zdieľané prílohy lid.stl, bezel.stl, body.stl. |
| 19. 10. 2026 | 1561748757048070305 | _signum_ | Otázka priestoru pre HDMI kábel v kryte. |
| 26. 10. 2026 | 1564302043794120804 | janinix | Zdieľaná snímka z modelára pre dokumentáciu. |
| 2. 11. 2026 | 1566749881148903446, 1566749945195667536 | upsil00n | Úloha pre _signum_: overiť rozmery modelu a následne vytlačiť kryt. |
| 2. 11. 2026 | 1566751021110399026 | janinix | Novšie prílohy diffuser.stl, lid.stl, bezel.stl, body.stl; historické názvy príloh; neskôr bola dodaná výrobná sada S7. |
| 2. 11. 2026 | 1566752737327054963 | janinix | Parametre displeja: 5 palcov, 800 × 480, vonkajšie rozmery 121,11 × 95,24 mm, HDMI a USB dotyk. Ide o údaje z chatu, nie overený datasheet. |
| 2. 11. 2026 | 1566824782903902261, 1566825783987539989 | upsil00n, _signum_ | Varianty názvu PyMemTest a MemTest. |
| 2. 11. 2026 | 1566827548435026081 | _signum_ | Zdieľaný poster MemoBox Junior. |
| 16. 11. 2026 | 1571823879578583104 | _signum_ | E-mail SmartLabu približne pred dvoma týždňami bez odpovede. Výroba nie je potvrdená. |

### Referencie minulého ročníka

- [Index projektov 2025–2026](https://sthdf-2025.systemthinking.sk/sk/class_sthdf_dashboard/class_sthdf_dashboard_2025-2026/projects/PRJ_INDEX/): rozcestník, veľa úvodov zostáva šablónových.
- [PRJ006 Woodies – prezentácia](https://sthdf-2025.systemthinking.sk/sk/class_sthdf_dashboard/class_sthdf_dashboard_2025-2026/projects/PRJ006/presentation/slides/): referencia pre členenie od hodnoty po návrh, realizáciu a testovanie; výslovne uvádza dosiahnutý rozsah digitálneho návrhu.
- [PRJ003 – prehľad](https://sthdf-2025.systemthinking.sk/sk/class_sthdf_dashboard/class_sthdf_dashboard_2025-2026/projects/PRJ003/): referencia na rozdelenie prezentácie a detailného SDLC.

Z referencií preberáme iba spôsob členenia. Ich výsledky a požiadavky sa neprenášajú na náš projekt.

## Navigácia

- [↩️ Späť](../index.md)

## Identifikácia súborových podkladov

SHA-256 originálov pri analýze:

- `DirectMessages-SMVIT.json`: `3b0d4512328204dbd5bebba09931f5332b282d8b8aa2838d50b2cc1c06ef52a4`
- `model.png`: `ac1397deb2deb2c3bdcf8ae5a7ade7e2fcf3d01b8d4e88155c72723c5680fb92`
- `MemoBox_Junior_Classroom_Learning_Poster.png`: `a525e8e9ead270b8f43119499d5dc9e1c090e4c24963214d549e2dca87a754e0`

## Následne dodané zdroje

- **S6:** [memory.py](../../../../assets/software/memory.py), skontrolovaný bez zmeny originálu. Päť hier, Python/Pygame, 800 × 480, cieľ 30 FPS, žiadna perzistencia výsledkov ani boot konfigurácia.
- **S7:** [PRINT-AND-ASSEMBLY.txt](../../../../assets/model/PRINT-AND-ASSEMBLY.txt) a päť STL z priečinka model. Handoff uvádza Elecrow Display-B Rev 1.1 a Pi 3 Model A+, orientácie tlače a montáž. Editovateľný parametrický CAD ani EA dodané neboli.

### Kontroly pri dokumentovaní

Python zdroj prešiel syntaktickou kontrolou cez ast.parse a compile bez spustenia aplikácie. Pygame v dokumentačnom prostredí nie je nainštalovaný; lokálny runtime/GUI test sa nevykonal. Predchádzajúce testovanie na Pi je používateľské potvrdenie a nie výsledok tejto kontroly.

Všetkých päť STL má dĺžku zodpovedajúcu deklarovanému počtu binárnych trojuholníkov. Z vrcholov boli vypočítané obálky uvedené v D4. Tieto kontroly nenahrádzajú fyzickú skúšku konektorov a displeja.

SHA-256 nových originálov:

- `memory.py`: `cbf957055e7a6d12642d2b3d5c8277321eb3c14f02f023828f277f099247e7cd`
- `01-body.stl`: `deecf0d897b373a9a3ae2ba44f449a01edf521a101fb9535b31c63386cd30b13`
- `02-bezel.stl`: `b716f91d371b21765555a817e6965b8ea664ca5165687c99a5ab436e49f22835`
- `03-lid-with-pi-mount.stl`: `07dcece5424499e338a2b4bb9028b10d0f175f4e8b75c70741a815a046270281`
- `04-diffuser.stl`: `eb45f368981c37ccc6ef429b0a0962e3e2a2c26b442a7b847bb189be5248c1b2`
- `05-display-connector-fit-test.stl`: `4e3dc84308b378c77b1f0478a904c835effee0287b06d9f68dd22270c7ee5c02`
- `PRINT-AND-ASSEMBLY.txt`: `d6e62c90e00c2e04b8c4e36b2893efa7fcb6d0f4a309f2afdb4c94a2ce562308`
