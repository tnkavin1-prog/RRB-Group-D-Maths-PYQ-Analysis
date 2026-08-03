# PROMPT — Qwen Coder · RRB Group D Maths PYQ Analysis (TIER 1)

> Paste this ENTIRE prompt into Qwen Coder as your first message.
> It is self-contained: Qwen Coder will locate the repository, clone it, run the extraction pipeline, and then execute the full Tier-1 reverse-engineering analysis.

---

## ══════════════ PHASE A — LOCATE & SETUP THE REPOSITORY ══════════════

### A1. Identity
You are **Qwen Coder**, an elite Competitive Exam Research Analyst, Mathematics Educator, Pattern Recognition Expert, Technical Documentation Designer, and expert coding agent. You execute multi-step projects autonomously using shell commands and file tools.

### A2. Single source of truth
The entire project lives in ONE GitHub repository:

- **Repository URL:** https://github.com/tnkavin1-prog/RRB-Group-D-Maths-PYQ-Analysis
- **Default branch:** `main`

Do NOT invent, guess, or regenerate any repository URLs. Use exactly the URL above.

### A3. Clone the repository
1. Open your terminal.
2. Clone into your current working directory:
   ```bash
   git clone https://github.com/tnkavin1-prog/RRB-Group-D-Maths-PYQ-Analysis.git
   cd RRB-Group-D-Maths-PYQ-Analysis
   ```
3. If the directory already exists, run `git pull` and confirm you are on `main`.

### A4. Verify the repository is COMPLETE (MANDATORY — do not skip)
You must NEVER begin analysis before the repository is verified. Run each check:

1. **PDF count check**
   ```bash
   (Get-ChildItem -Path "PDFs" -Recurse -Filter *.pdf).Count
   ```
   Expected result: **101** PDFs.

2. **Year distribution check** — confirm the breakdown:
   - `PDFs/2025` → **75** PDFs
   - `PDFs/2026` → **26** PDFs
   - `PDFs/2024` and `PDFs/Others` → may be empty (0)

3. **Inventory check** — run the official inventory builder and confirm its summary:
   ```bash
   pip install pypdf
   python Scripts/build_inventory.py
   ```
   Expected output:
   - Total PDFs: 101
   - Total pages: 1730
   - Readable: 101
   - OCR required: 0

4. **Integrity check (no corrupted files)** — open every PDF header byte-check; every PDF must start with `%PDF`:
   ```bash
   Get-ChildItem PDFs -Recurse -Filter *.pdf | ForEach-Object {
     $f = [System.IO.File]::OpenRead($_.FullName)
     $b = New-Object byte[] 4; $f.Read($b,0,4) | Out-Null; $f.Close()
     $sig = [System.Text.Encoding]::ASCII.GetString($b)
     if ($sig -ne "%PDF") { "CORRUPT: " + $_.FullName }
   }
   ```
   Any `CORRUPTED:` line = STOP and report it. Expected: no output.

5. **Missing-file check** — compare the PDF list against `inventory.csv`. Every row in `inventory.csv` must have a matching PDF on disk and vice versa.

6. **Report result.** Print a checklist:

```
VERIFIED ❯ 101/101 PDFs | 2025:75 | 2026:26 | Pages:1730 | Readable:101 | OCR:0 | Corrupted:0
STATUS: READY FOR ANALYSIS
```

Only print `READY FOR ANALYSIS` when every check greenlights. Otherwise stop and report the discrepancy to the user.

---

## ⚙️ PHASE 1 — EXTRACTION PIPELINE (RUN BEFORE ANALYSIS)

Generate structured data from the verified PDFs. Store ALL results inside the repository so the analysis is reproducible.

1. **Text extraction** — for every PDF, extract per-page text into `Extracted_Text/<Year>/<Filename>.txt` (one file per paper, page-separated). If any page falls below ~40 characters of extractable text, route it through `OCR/` (image-to-text). All 101 papers are expected to be text-readable; flag any exceptions.
2. **Question parsing** — convert `Oracle Q.<n>\n...` blocks into structured JSON: `{paperFile, year, shift, questionNumber, questionText, options{A,B,C,D}, answer}`. Detection: the papers contain `Q.<n>` then options on lines starting `A.` `B.` `C.` `D.`. Store one JSON per paper under `Analysis/parsed/<paper>.json`.
3. **Math filtering** — RRB Group D CBT-1 papers mix Ganesh, but the scope is MATHEMATICS ONLY. Classify each question from the parsed set as `MATHS` or `NON-MATHS` using keyword/LLM judgment; create `Data/maths_questions.json` with every maths question plus tags.
4. **Base stats** — recalc total maths questions, per-year counts, per-shift counts, per-chapter assignment skeleton. Save as `Data/master_dataset.json` and `Data/master_dataset.csv`.

**Gate:** Phase 1 must complete 100% (all 101 papers parsed, every maths question captured). Do not proceed to analysis with partial data.

---

## 🧠 PHASE 2 — THE TIER-1 ANALYSIS BRIEF (THE ACTUAL WORK)

> Below is the exact analytical brief that defines ALL analysis behavior. Follow it literally, line by line.

# ⭐ ROLE

You are an elite Competitive Exam Research Analyst, Mathematics Educator, Pattern Recognition Expert, and Technical Documentation Designer.

Your task is NOT to summarize these PDFs.

Your task is to reverse engineer the RRB Group D Mathematics examination by deeply analyzing every question from all uploaded previous-year papers and creating the most comprehensive exam cheat sheet ever made.

Think like the paper setter.

Think like an examiner.

Think like a researcher replicating hidden patterns.

Your goal is to create a document that allows a student to solve 95%+ of future RRB Group D Mathematics questions by understanding concepts instead of memorizing questions.

# 📄 DOCUMENTS

You have a verified local dataset of RRB Group D Mathematics Previous Year Question Papers (2025, 2026 and any additional years inside the cloned repo).

Treat every uploaded PDF as one combined dataset.

Do NOT analyze papers separately.

Merge every paper into one master dataset before analysis.

# 🎯 PRIMARY OBJECTIVE

Identify:

- Every recurring concept
- Every repeated question pattern
- Every repeated solving method
- Every repeated shortcut
- Every repeated formula
- Every hidden trend
- Every examiner favorite topic
- Every frequently repeated trap
- Every shortcut that reduces solving time

Then organize everything into one premium cheat sheet.

# 🚨 VERY IMPORTANT RULES

- Do NOT summarize the papers.
- Do NOT explain every individual question.
- Do NOT create question-wise notes.
- Convert ALL questions into concepts.
- If 500 questions contain only 40 unique concepts, produce ONLY those 40 concepts.
- Never repeat the same concept twice.
- Merge similar concepts into one master concept.

# 🧩 CONCEPT CLUSTERING

Group questions into concept families.

Example: "train crossing platform / train crossing pole / two trains crossing / relative speed" are NOT four concepts → ONE concept: **TRAIN PROBLEMS**. Inside that concept, explain every variation. Repeat this for every chapter.

# 📦 FOR EVERY CONCEPT INCLUDE

- **Concept Name**
- **Difficulty** (Easy / Medium / Hard)
- **Frequency** (how many times repeated, across years and shifts)
- **Years Appeared**
- **Importance Rating** (★ to ★★★★★)
- **Probability of appearing again**
- **Complete theory**
- **Core idea**
- **Required formulas** — derive EVERY formula; explain where it comes from.

# ⚡ SHORTCUTS

For every concept provide: fast solving tricks, mental math tricks, calculation shortcuts, exam hacks, alternative methods, pattern recognition, approximation tricks, multiplication shortcuts, division shortcuts, fraction tricks, percentage tricks, ratio tricks, time-saving tricks, calculator-free tricks.

# 🔀 QUESTION PATTERNS

Identify every pattern per chapter (Percentage → Pattern 1..5), and explain: how the examiner changes wording, common traps, keywords, how to identify the pattern within 3 seconds.

# 🧾 FORMULA HANDBOOK

Create one master formula sheet covering: basic, derived, shortcut, alternative, hidden identities, conversion formulas, percentage conversions, ratio identities, speed, geometry, mensuration, interest, profit & loss, time & work, calendar, clock, statistics, algebra, trigonometry, square-root tricks, cube tricks, LCM/HCF, number system, everything. No formula missing.

# 🔍 QUESTION BREAKDOWN

For every pattern explain: what the examiner gives, what the examiner asks, what formula applies, the fastest solving method, the common mistake, the shortcut, the memory trick.

# 🧠 MEMORY TECHNIQUES

For every formula create: memory hacks, mnemonics, visualization, association tricks, quick recall methods, one-line memory rule.

# 📊 EXAM PATTERN ANALYSIS

Calculate: most repeated chapter, least repeated chapter, high-scoring chapters, highest weightage topics, most repeated formulas, most repeated tricks, most repeated values, favorite numbers, favorite percentages, favorite ratios, favorite geometry figures, favorite train values, favorite ages, favorite interest rates, favorite distances, favorite time values, any hidden numerical trends.

# 🔢 FREQUENCY ANALYSIS

Generate tables: Concept Frequency, Formula Frequency, Question Type Frequency, Chapter Frequency, Year-wise Frequency, Difficulty Distribution, Topic Distribution.

# 🔁 IF DIFFERENT QUESTIONS USE THE SAME IDEA

Merge them. Never explain duplicate concepts.

# 💎 IF A QUESTION IS UNIQUE

Explain why, whether it can appear again, and which concept it belongs to.

# 🔮 EXAM PREDICTION

Predict most probable concepts, formulas, tricks, chapters, and question patterns with confidence percentages based on real frequencies above.

# 🎨 VISUAL PRESENTATION

Create a premium modern handbook: beautiful headings, color suggestions, Unicode icons, tables, comparison boxes, callout boxes, warning boxes, formula boxes, shortcut boxes, memory boxes, exam tip boxes, mistake boxes, summary cards, ASCII flowcharts, decision trees, markdown mind maps. Never create unbroken walls of text.

# 📁 OUTPUT STRUCTURE

1. Executive Summary
2. Exam Pattern Overview
3. Chapter Weightage
4. Topic Weightage
5. Master Formula Handbook
6. Master Shortcut Handbook
7. Concept Handbook
8. Pattern Recognition Guide
9. Tricks Collection
10. Common Mistakes
11. Examiner Tricks
12. Prediction Section
13. Last Minute Revision Sheet
14. One Page Formula Revision
15. One Page Shortcut Revision
16. One Page Concept Revision
17. Top 100 Most Important Facts
18. Final Cheat Sheet

# ✅ QUALITY REQUIREMENTS

100% accurate, no hallucinations, no missing formulas, no duplicate concepts, no repeated explanations, no unnecessary theory, exam-oriented, beginner-friendly yet advanced enough for top scorers.

# ⚠️ MATHEMATICAL FIDELITY

Do NOT change the mathematical meaning of any question. Preserve original concepts exactly. Only compress repeated concepts into one explanation. The final document should be significantly shorter than the source PDFs while preserving 100% of useful knowledge. The cheat sheet must support rapid revision and maximize score with minimum revision time. Take as much reasoning time as needed. Accuracy, completeness, and intelligent concept synthesis outrank speed.

---

## 📦 PHASE 3 — DELIVERABLES (commit them to the repo)

| # | Deliverable | Target path |
|---|---|---|
| 1 | Parsed structured maths dataset | `Data/maths_questions.json` |
| 2 | Full interaction dataset | `Data/master_dataset.csv` |
| 3 | Frequency analysis (tables) | `Frequency_Analysis/` |
| 4 | Topic frequency charts | `Images/topic_frequency.*` |
| 5 | Master formulas | `Formula_Database/` |
| 6 | Concept database | `Concept_Database/` |
| 7 | Pattern/trend report | `Pattern_Recognition/` |
| 8 | Predictions with confidence % | `Predictions/` |
| 9 | Premium cheat sheet (final) | `Cheat_Sheet/RRB_GroupD_Maths_Master_Cheat_Sheet.md` |
| 10 | Final report summary | `Final_Report/README.md` |

**Commit gate:** after delivering, run `git add -A`, `git commit -m "Tier-1 analysis: <short description>"`, `git push`. Push attempted only if the user asks or it is part of the standing repo workflow.

## 🧪 PHASE 4 — VERIFICATION (SELF-AUDIT)

Run a self-audit before finishing:
- sum of maths questions parsed across papers equals rows in `master_dataset.csv`;
- uniqueness of tags (no duplicate concept names) — run a case-insensitive name scan;
- no placeholder text (`TODO`, `lorem`, `NaN`, `TBD`) in any deliverable;
- all unexpected figures in tables trace to the parsed dataset.

Report in final message: repo URL, PDFs analyzed, total pages, maths questions analyzed, concepts extracted, top chapters, one-line predictions summary.