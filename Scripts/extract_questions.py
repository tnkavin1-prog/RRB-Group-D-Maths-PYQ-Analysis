import os, csv, json, re
from pypdf import PdfReader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_ROOT = os.path.join(ROOT, "PDFs")
OUTPUT_DIR = os.path.join(ROOT, "Extracted_Text")
PARSED_DIR = os.path.join(ROOT, "Analysis", "parsed")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PARSED_DIR, exist_ok=True)

def extract_questions_from_text(text, filename, year):
    """Extract structured questions from PDF text"""
    questions = []
    
    # Find Mathematics section
    math_idx = text.find('Section : Mathematics')
    if math_idx == -1:
        return questions  # No math section found
    
    # Get only mathematics portion
    math_text = text[math_idx:]
    
    # Pattern to match questions: Q.<number> followed by content
    # Questions typically start with Q.<n> or Q.<n>\n
    q_pattern = r'Q\.(\d+)\s*\n?(.*?)(?=Q\.\d+\s*\n|$)'
    
    matches = re.findall(q_pattern, math_text, re.DOTALL)
    
    for q_num, q_content in matches:
        q_content = q_content.strip()
        if not q_content:
            continue
        
        # Extract question text and options
        lines = q_content.split('\n')
        question_text = ""
        options = {"A": "", "B": "", "C": "", "D": ""}
        answer = ""
        
        # Parse content
        current_option = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check for Ans marker
            if line.startswith('Ans'):
                current_option = None
                continue
            
            # Check for options
            if re.match(r'^[A-D]\.\s*', line):
                opt_match = re.match(r'^([A-D])\.\s*(.*)', line)
                if opt_match:
                    current_option = opt_match.group(1)
                    options[current_option] = opt_match.group(2)
            elif current_option:
                options[current_option] += " " + line
            else:
                question_text += line + " "
        
        question_text = question_text.strip()
        
        # Clean up options - remove "✓" or other markers for correct answer
        for opt in options:
            options[opt] = re.sub(r'[✓✔]', '', options[opt]).strip()
        
        if question_text:
            questions.append({
                "paperFile": filename,
                "year": year,
                "questionNumber": int(q_num),
                "questionText": question_text,
                "options": options,
                "answer": ""  # Will be filled later
            })
    
    return questions

total_questions = 0
all_papers = []

for year_dir in sorted(os.listdir(PDF_ROOT)):
    d = os.path.join(PDF_ROOT, year_dir)
    if not os.path.isdir(d):
        continue
    
    print(f"Processing {year_dir}...")
    for name in sorted(os.listdir(d)):
        if not name.lower().endswith(".pdf"):
            continue
        
        full_path = os.path.join(d, name)
        
        try:
            reader = PdfReader(full_path)
            full_text = ""
            for page in reader.pages:
                full_text += page.extract_text() or ""
            
            # Save extracted text
            txt_output_dir = os.path.join(OUTPUT_DIR, year_dir)
            os.makedirs(txt_output_dir, exist_ok=True)
            txt_path = os.path.join(txt_output_dir, name.replace('.pdf', '.txt'))
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(full_text)
            
            # Extract questions
            questions = extract_questions_from_text(full_text, name, year_dir)
            
            if questions:
                # Save parsed questions
                parsed_output = os.path.join(PARSED_DIR, name.replace('.pdf', '.json'))
                with open(parsed_output, 'w', encoding='utf-8') as f:
                    json.dump(questions, f, indent=2, ensure_ascii=False)
                
                all_papers.extend(questions)
                total_questions += len(questions)
                print(f"  {name}: {len(questions)} math questions")
            
        except Exception as e:
            print(f"  ERROR processing {name}: {e}")

print(f"\n=== SUMMARY ===")
print(f"Total math questions extracted: {total_questions}")
print(f"Total papers with math: {len(set(q['paperFile'] for q in all_papers))}")
