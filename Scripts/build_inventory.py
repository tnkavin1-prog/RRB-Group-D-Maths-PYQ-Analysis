import os, csv, re, io

from pypdf import PdfReader

ROOT = r"E:\RRB PYQ\RRB-Group-D-Maths-PYQ-Analysis"
PDF_ROOT = os.path.join(ROOT, "PDFs")
OUT = os.path.join(ROOT, "inventory.csv")

# Frequency-analysis-level thresholds
MIN_TEXT_CHARS_PER_PAGE = 40  # below this a page is treated as image-only

rows = []
total_pages = 0
for year_dir in sorted(os.listdir(PDF_ROOT)):
    d = os.path.join(PDF_ROOT, year_dir)
    if not os.path.isdir(d):
        continue
    for name in sorted(os.listdir(d)):
        if not name.lower().endswith(".pdf"):
            continue
        full = os.path.join(d, name)
        size = os.path.getsize(full)
        pages = 0
        extracted_chars = 0
        try:
            reader = PdfReader(full)
            pages = len(reader.pages)
            for p in reader.pages:
                try:
                    t = p.extract_text() or ""
                except Exception:
                    t = ""
                extracted_chars += len(t)
        except Exception as e:
            pages = 0

        per_page = (extracted_chars / pages) if pages else 0
        readable = "Yes" if per_page >= MIN_TEXT_CHARS_PER_PAGE else "No"
        ocr_required = "Yes" if readable == "No" else "No"
        total_pages += pages
        rows.append({
            "Filename": name,
            "Year": year_dir,
            "Pages": pages,
            "File Size": size,
            "Folder": f"PDFs/{year_dir}",
            "OCR Required": ocr_required,
            "Readable": readable,
        })

with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=["Filename", "Year", "Pages", "File Size", "Folder", "OCR Required", "Readable"])
    w.writeheader()
    w.writerows(rows)

print(f"Total PDFs: {len(rows)}")
print(f"Total pages: {total_pages}")
print(f"Readable: {sum(1 for r in rows if r['Readable'] == 'Yes')}")
print(f"OCR required: {sum(1 for r in rows if r['OCR Required'] == 'Yes')}")
print(f"Wrote {OUT}")