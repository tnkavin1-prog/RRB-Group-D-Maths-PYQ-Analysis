# RRB Group D Maths PYQ Analysis

Deep analysis of RRB Group D Mathematics Previous Year Papers for concept extraction, pattern recognition, formula derivation, and premium cheat sheet generation.

## Project Overview

This repository is the source of truth for a systematic mathematical analysis of RRB Group D (CBT-1) previous year question papers. Every paper PDF is versioned here, and all downstream artifacts — extracted text, OCR data, concept databases, formula banks, frequency analyses, pattern reports, predictions, and cheat sheets — are generated from these files and stored in the corresponding folders.

## Dataset Stats

| Metric | Value |
|---|---|
| Number of PDFs | **101** |
| Years available | **2025, 2026** |
| Total pages | **1,730** |
| Total size | **65.91 MB** |
| Text-readable | **101 (100%)** |
| OCR required | **0** |

### Papers per year

| Year | Papers (PDFs) | Shifts (S1/S2/S3) |
|---|---|---|
| 2025 | 75 | 25 exam days × 3 shifts |
| 2026 | 26 | 9 exam days (incl. 8-1-2026) × 3 shifts + partial |

## Folder Structure

```
RRB-Group-D-Maths-PYQ-Analysis/
├── PDFs/                 # Source exam papers (classified by year)
│   ├── 2024/
│   ├── 2025/
│   ├── 2026/
│   └── Others/
├── Extracted_Text/       # Raw text pulled from each PDF
├── OCR/                  # OCR pipeline output for image-only pages (0 needed so far)
├── Images/               # Rendered page images for visual checks
├── Analysis/             # Per-paper & per-year analysis artifacts
├── Formula_Database/     # All formulas encountered, indexed by topic
├── Concept_Database/     # Mathematical concepts mapped to questions
├── Pattern_Recognition/  # Repeated question types, trends, traps
├── Frequency_Analysis/   # Topic/chapter frequency counts and percentages
├── Predictions/          # Upcoming exam high-probability topic estimates
├── Cheat_Sheet/          # Premium condensed formula & trick sheets
├── Final_Report/         # Consolidated markdown/PDF reports
├── Scripts/              # Analysis automation (inventory, extraction, stats)
├── Data/                 # Intermediate structured data (CSV/JSON)
└── README.md
```

## Purpose of Project

1. **Concept extraction** — identify every mathematical concept tested in RRB Group D CBT-1 across shifts.
2. **Pattern recognition** — detect which question types repeat, with which numbers/options.
3. **Formula derivation** — collect, derive, and verify all shortcuts and formulas relevant to the exam.
4. **Frequency analysis** — quantify topic weightage per year/shift to rank preparation priorities.
5. **Premium cheat sheet** — generate a condensed, exam-ready cheat sheet from real data.

## Analysis Workflow

```
PDFs/ ──► build_inventory.py ──► inventory.csv
   │
   ├──► text extraction (pypdf) ──► Extracted_Text/ (per paper)
   ├──► OCR fallback (if unreadable) ──► OCR/
   ├──► question parsing ──► Analysis/ (structured Q&A JSON/CSV)
   ├──► topic tagging ──► Concept_Database/ + Frequency_Analysis/
   ├──► formula mining ──► Formula_Database/
   ├──► pattern detection ──► Pattern_Recognition/ ──► Predictions/
   └──► aggregation ──► Cheat_Sheet/ ──► Final_Report/
```

Every stage is scripted under `Scripts/` and reproducible.

## Inventory

`inventory.csv` at the repository root lists every PDF with: Filename, Year, Pages, File Size (bytes), Folder, OCR Required (Yes/No), Readable (Yes/No).

## License

MIT — see [LICENSE](LICENSE).
