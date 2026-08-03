import json, os, csv
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARSED_DIR = os.path.join(ROOT, "Analysis", "parsed")
DATA_DIR = os.path.join(ROOT, "Data")

os.makedirs(DATA_DIR, exist_ok=True)

# Math classification keywords - RRB Group D Mathematics topics
MATH_KEYWORDS = {
    # Arithmetic
    'percentage': ['percentage', 'percent', '%'],
    'profit_loss': ['profit', 'loss', 'discount', 'selling price', 'cost price', 'marked price'],
    'si_ci': ['simple interest', 'compound interest', 'interest', 'principal', 'rate per annum'],
    'ratio_proportion': ['ratio', 'proportion', 'divided in the ratio'],
    'average': ['average', 'mean'],
    'number_system': ['number', 'divisible', 'remainder', 'prime', 'composite', 'factor', 'multiple', 'LCM', 'HCF'],
    
    # Algebra
    'algebra': ['algebra', 'equation', 'quadratic', 'polynomial', 'expression', 'simplify'],
    'linear_equations': ['linear', 'simultaneous equations'],
    
    # Geometry
    'geometry': ['triangle', 'circle', 'rectangle', 'square', 'polygon', 'angle', 'parallel', 'perpendicular', 'rhombus'],
    'mensuration_2d': ['area', 'perimeter', 'circumference', 'diameter', 'radius'],
    'mensuration_3d': ['volume', 'surface area', 'cylinder', 'cone', 'sphere', 'hemisphere', 'cube', 'cuboid'],
    
    # Trigonometry
    'trigonometry': ['sin', 'cos', 'tan', 'cot', 'sec', 'cosec', 'trigonometric', 'θ', 'theta'],
    'height_distance': ['height', 'distance', 'angle of elevation', 'angle of depression'],
    
    # Time & Work
    'time_work': ['work', 'efficiency', 'together', 'days to complete'],
    'time_speed_distance': ['speed', 'distance', 'time', 'train', 'boat', 'stream', 'relative speed'],
    'pipes_cisterns': ['pipe', 'tank', 'cistern', 'fill', 'empty'],
    
    # Statistics
    'statistics': ['mean', 'median', 'mode', 'frequency', 'data', 'bar graph', 'pie chart', 'histogram'],
    
    # Others
    'age_problems': ['age', 'years old', 'elder', 'younger'],
    'mixture_allegation': ['mixture', 'allegation', 'concentration'],
    'probability': ['probability', 'chance', 'dice', 'coin', 'card'],
    'permutation_combination': ['permutation', 'combination', 'arrangement', 'selection'],
    'sequence_series': ['AP', 'GP', 'arithmetic progression', 'geometric progression', 'sequence', 'series'],
    'logarithms': ['log', 'logarithm'],
    'indices_surds': ['indices', 'surds', 'exponent', 'power', 'root', 'square root', 'cube root']
}

def classify_question(question_text):
    """Classify a question as MATHS or NON-MATHS and assign topic tags"""
    text_lower = question_text.lower()
    
    # Check if it's a math question based on keywords
    matched_topics = []
    for topic, keywords in MATH_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in text_lower:
                matched_topics.append(topic)
                break
    
    # Remove duplicates while preserving order
    seen = set()
    unique_topics = []
    for t in matched_topics:
        if t not in seen:
            seen.add(t)
            unique_topics.append(t)
    
    # Primary topic assignment (prioritize more specific topics)
    primary_topic = None
    if unique_topics:
        # Priority order for primary topic
        priority = ['mensuration_3d', 'mensuration_2d', 'trigonometry', 'height_distance', 
                   'time_speed_distance', 'time_work', 'pipes_cisterns', 'si_ci', 
                   'profit_loss', 'percentage', 'geometry', 'algebra', 'number_system',
                   'ratio_proportion', 'average', 'statistics', 'age_problems',
                   'mixture_allegation', 'probability', 'sequence_series', 'indices_surds']
        
        for p in priority:
            if p in unique_topics:
                primary_topic = p
                break
        
        if not primary_topic:
            primary_topic = unique_topics[0]
    
    return 'MATHS' if unique_topics else 'NON-MATHS', primary_topic, unique_topics

# Load all parsed questions
all_questions = []
for fname in sorted(os.listdir(PARSED_DIR)):
    if fname.endswith('.json'):
        with open(os.path.join(PARSED_DIR, fname), 'r') as f:
            data = json.load(f)
            all_questions.extend(data)

print(f"Total questions loaded: {len(all_questions)}")

# Classify each question
maths_questions = []
non_maths_questions = []

for q in all_questions:
    classification, primary_topic, all_topics = classify_question(q['questionText'])
    q['classification'] = classification
    q['primaryTopic'] = primary_topic
    q['allTopics'] = all_topics
    
    if classification == 'MATHS':
        maths_questions.append(q)
    else:
        non_maths_questions.append(q)

print(f"Maths questions: {len(maths_questions)}")
print(f"Non-maths questions: {len(non_maths_questions)}")

# Save maths questions
maths_output = os.path.join(DATA_DIR, 'maths_questions.json')
with open(maths_output, 'w', encoding='utf-8') as f:
    json.dump(maths_questions, f, indent=2, ensure_ascii=False)
print(f"Saved {len(maths_questions)} maths questions to {maths_output}")

# Build master dataset CSV
master_csv_path = os.path.join(DATA_DIR, 'master_dataset.csv')
with open(master_csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'PaperFile', 'Year', 'QuestionNumber', 'QuestionText', 
                    'OptionA', 'OptionB', 'OptionC', 'OptionD', 'Classification', 
                    'PrimaryTopic', 'AllTopics'])
    
    for i, q in enumerate(all_questions, 1):
        writer.writerow([
            i,
            q['paperFile'],
            q['year'],
            q['questionNumber'],
            q['questionText'],
            q['options'].get('A', ''),
            q['options'].get('B', ''),
            q['options'].get('C', ''),
            q['options'].get('D', ''),
            q['classification'],
            q['primaryTopic'],
            '|'.join(q['allTopics'])
        ])

print(f"Saved master dataset with {len(all_questions)} rows to {master_csv_path}")

# Generate summary statistics
topic_counts = defaultdict(int)
year_counts = defaultdict(int)
for q in maths_questions:
    if q['primaryTopic']:
        topic_counts[q['primaryTopic']] += 1
    year_counts[q['year']] += 1

print("\n=== TOPIC DISTRIBUTION ===")
for topic, count in sorted(topic_counts.items(), key=lambda x: -x[1]):
    print(f"{topic}: {count}")

print("\n=== YEAR DISTRIBUTION ===")
for year, count in sorted(year_counts.items()):
    print(f"{year}: {count}")

# Save master dataset JSON
master_json_path = os.path.join(DATA_DIR, 'master_dataset.json')
master_data = {
    'totalQuestions': len(all_questions),
    'mathsQuestions': len(maths_questions),
    'nonMathsQuestions': len(non_maths_questions),
    'topicDistribution': dict(topic_counts),
    'yearDistribution': dict(year_counts),
    'questions': all_questions
}
with open(master_json_path, 'w', encoding='utf-8') as f:
    json.dump(master_data, f, indent=2, ensure_ascii=False)
print(f"\nSaved master dataset JSON to {master_json_path}")
