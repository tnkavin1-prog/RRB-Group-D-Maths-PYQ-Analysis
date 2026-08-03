import json, os
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "Data")
FREQ_DIR = os.path.join(ROOT, "Frequency_Analysis")
FORMULA_DIR = os.path.join(ROOT, "Formula_Database")
CONCEPT_DIR = os.path.join(ROOT, "Concept_Database")
PATTERN_DIR = os.path.join(ROOT, "Pattern_Recognition")
PREDICTION_DIR = os.path.join(ROOT, "Predictions")
CHEAT_DIR = os.path.join(ROOT, "Cheat_Sheet")

for d in [FREQ_DIR, FORMULA_DIR, CONCEPT_DIR, PATTERN_DIR, PREDICTION_DIR, CHEAT_DIR]:
    os.makedirs(d, exist_ok=True)

# Load maths questions
with open(os.path.join(DATA_DIR, 'maths_questions.json'), 'r') as f:
    maths_questions = json.load(f)

print(f"Loaded {len(maths_questions)} maths questions for analysis")

# Topic mapping to human-readable names
TOPIC_NAMES = {
    'trigonometry': 'Trigonometry',
    'number_system': 'Number System',
    'percentage': 'Percentage',
    'profit_loss': 'Profit & Loss',
    'si_ci': 'Simple & Compound Interest',
    'mensuration_3d': 'Mensuration (3D)',
    'time_speed_distance': 'Time, Speed & Distance',
    'mensuration_2d': 'Mensuration (2D)',
    'average': 'Average',
    'ratio_proportion': 'Ratio & Proportion',
    'time_work': 'Time & Work',
    'height_distance': 'Height & Distance',
    'age_problems': 'Age Problems',
    'algebra': 'Algebra',
    'probability': 'Probability',
    'geometry': 'Geometry'
}

# Frequency Analysis
topic_freq = defaultdict(int)
year_freq = defaultdict(int)
paper_freq = defaultdict(int)

for q in maths_questions:
    if q.get('primaryTopic'):
        topic_freq[q['primaryTopic']] += 1
    year_freq[q['year']] += 1
    paper_freq[q['paperFile']] += 1

# Save frequency tables
freq_data = {
    'topicFrequency': dict(topic_freq),
    'yearFrequency': dict(year_freq),
    'totalQuestions': len(maths_questions)
}

with open(os.path.join(FREQ_DIR, 'topic_frequency.json'), 'w') as f:
    json.dump(freq_data, f, indent=2)

# Generate topic frequency table markdown
table_md = "# Topic Frequency Analysis\n\n"
table_md += "| Topic | Frequency | Percentage |\n"
table_md += "|-------|-----------|------------|\n"
total = sum(topic_freq.values())
for topic, count in sorted(topic_freq.items(), key=lambda x: -x[1]):
    pct = (count / total * 100) if total > 0 else 0
    table_md += f"| {TOPIC_NAMES.get(topic, topic)} | {count} | {pct:.1f}% |\n"

with open(os.path.join(FREQ_DIR, 'topic_frequency.md'), 'w') as f:
    f.write(table_md)

print("✓ Topic frequency analysis saved")

# Concept Database - Group questions by concept patterns
concepts = defaultdict(list)
for q in maths_questions:
    topic = q.get('primaryTopic', 'other')
    concepts[topic].append(q)

concept_summary = {}
for topic, qs in concepts.items():
    concept_summary[topic] = {
        'count': len(qs),
        'questionNumbers': [q['questionNumber'] for q in qs],
        'papers': list(set(q['paperFile'] for q in qs))
    }

with open(os.path.join(CONCEPT_DIR, 'concept_summary.json'), 'w') as f:
    json.dump(concept_summary, f, indent=2)

print("✓ Concept database created")

# Pattern Recognition - Identify common question patterns
patterns = {
    'trigonometry': ['Value finding', 'Identity simplification', 'Height-distance application'],
    'number_system': ['Divisibility rules', 'LCM/HCF finding', 'Remainder problems', 'Digit problems'],
    'percentage': ['Successive percentage', 'Percentage increase/decrease', 'Percentage of number'],
    'profit_loss': ['Basic profit/loss %', 'Successive discount', 'CP/SP calculation'],
    'si_ci': ['Simple interest calculation', 'Difference between SI and CI'],
    'mensuration_3d': ['Cylinder volume/surface', 'Cube/cuboid problems', 'Sphere/hemisphere'],
    'time_speed_distance': ['Average speed', 'Train crossing', 'Relative speed'],
    'mensuration_2d': ['Area calculation', 'Perimeter problems'],
    'average': ['Mean of observations', 'Weighted average'],
    'ratio_proportion': ['Ratio division', 'Equivalent ratio', 'Compound ratio'],
    'time_work': ['Pipe and cistern', 'Work efficiency'],
    'height_distance': ['Angle of elevation/depression'],
    'age_problems': ['Present age calculation'],
    'algebra': ['Expression simplification', 'Linear equations'],
    'probability': ['Basic probability'],
    'geometry': ['Rectangle properties', 'Triangle properties']
}

with open(os.path.join(PATTERN_DIR, 'question_patterns.json'), 'w') as f:
    json.dump(patterns, f, indent=2)

print("✓ Pattern recognition data saved")

# Predictions based on frequency
predictions = []
sorted_topics = sorted(topic_freq.items(), key=lambda x: -x[1])
for i, (topic, count) in enumerate(sorted_topics[:10]):
    confidence = min(95, 60 + (count * 2))  # Simple confidence calculation
    predictions.append({
        'rank': i+1,
        'topic': TOPIC_NAMES.get(topic, topic),
        'frequency': count,
        'confidence': f"{confidence}%",
        'prediction': f"High probability of {max(1, count-1)}-{count+1} questions"
    })

with open(os.path.join(PREDICTION_DIR, 'topic_predictions.json'), 'w') as f:
    json.dump(predictions, f, indent=2)

print("✓ Predictions generated")

# Formula Database - Core formulas per topic
formulas = {
    'percentage': {
        'basic': 'Percentage = (Part/Whole) × 100',
        'increase': 'New Value = Original × (1 + rate/100)',
        'decrease': 'New Value = Original × (1 - rate/100)',
        'successive': 'Net % = a + b + (ab/100)'
    },
    'profit_loss': {
        'profit': 'Profit = SP - CP',
        'profit_percent': 'Profit% = (Profit/CP) × 100',
        'loss': 'Loss = CP - SP',
        'loss_percent': 'Loss% = (Loss/CP) × 100',
        'sp_from_cp': 'SP = CP × (100 + Profit%)/100',
        'cp_from_sp': 'CP = SP × 100/(100 + Profit%)',
        'discount': 'Discount% = (MP - SP)/MP × 100'
    },
    'si_ci': {
        'simple_interest': 'SI = (P × R × T)/100',
        'amount': 'A = P + SI = P(1 + RT/100)',
        'compound_interest': 'CI = P(1 + R/100)^T - P',
        'amount_ci': 'A = P(1 + R/100)^T'
    },
    'ratio_proportion': {
        'basic': 'a : b = a/b',
        'proportion': 'a : b :: c : d ⇒ a/b = c/d ⇒ ad = bc',
        'compound_ratio': '(a:b) and (c:d) = ac : bd'
    },
    'average': {
        'mean': 'Average = Sum of observations / Number of observations',
        'weighted': 'Weighted Avg = (w1x1 + w2x2 + ...)/(w1 + w2 + ...)'
    },
    'time_speed_distance': {
        'speed': 'Speed = Distance/Time',
        'avg_speed_equal_dist': 'Average Speed = 2xy/(x+y) (for equal distances)',
        'relative_speed_same': 'Relative Speed (same direction) = |x - y|',
        'relative_speed_opposite': 'Relative Speed (opposite) = x + y',
        'train_platform': 'Time = (L1 + L2)/Relative Speed',
        'km_to_ms': 'km/hr to m/s: multiply by 5/18',
        'ms_to_km': 'm/s to km/hr: multiply by 18/5'
    },
    'time_work': {
        'work_rate': 'If A does work in n days, A\'s 1 day work = 1/n',
        'together': 'If A in x days, B in y days: Together = xy/(x+y) days',
        'pipe_fill': 'If pipe fills in x min: Rate = 1/x per min',
        'pipe_empty': 'If pipe empties in y min: Rate = -1/y per min',
        'net_rate': 'Net rate = Fill rate - Empty rate'
    },
    'number_system': {
        'divisibility_2': 'Last digit even',
        'divisibility_3': 'Sum of digits divisible by 3',
        'divisibility_5': 'Last digit 0 or 5',
        'divisibility_9': 'Sum of digits divisible by 9',
        'divisibility_10': 'Last digit 0',
        'lcm_hcf': 'LCM × HCF = Product of two numbers'
    },
    'mensuration_2d': {
        'rectangle_area': 'Area = l × b',
        'rectangle_perimeter': 'Perimeter = 2(l + b)',
        'square_area': 'Area = side²',
        'square_perimeter': 'Perimeter = 4 × side',
        'triangle_area': 'Area = ½ × base × height',
        'circle_area': 'Area = πr²',
        'circle_circumference': 'Circumference = 2πr'
    },
    'mensuration_3d': {
        'cube_volume': 'Volume = side³',
        'cube_surface': 'Surface Area = 6 × side²',
        'cuboid_volume': 'Volume = l × b × h',
        'cuboid_surface': 'Surface Area = 2(lb + bh + hl)',
        'cylinder_volume': 'Volume = πr²h',
        'cylinder_curved': 'Curved SA = 2πrh',
        'cylinder_total': 'Total SA = 2πr(r + h)',
        'cone_volume': 'Volume = ⅓πr²h',
        'cone_curved': 'Curved SA = πrl (l = slant height)',
        'sphere_volume': 'Volume = 4/3 πr³',
        'sphere_surface': 'Surface Area = 4πr²',
        'hemisphere_volume': 'Volume = 2/3 πr³',
        'hemisphere_surface': 'Surface Area = 3πr²'
    },
    'trigonometry': {
        'sin': 'sin θ = Perpendicular/Hypotenuse',
        'cos': 'cos θ = Base/Hypotenuse',
        'tan': 'tan θ = Perpendicular/Base',
        'identity': 'sin²θ + cos²θ = 1',
        'tan_identity': '1 + tan²θ = sec²θ',
        'cot_identity': '1 + cot²θ = cosec²θ'
    },
    'algebra': {
        '(a+b)²': '(a+b)² = a² + 2ab + b²',
        '(a-b)²': '(a-b)² = a² - 2ab + b²',
        'a²-b²': 'a² - b² = (a+b)(a-b)',
        '(a+b)³': '(a+b)³ = a³ + b³ + 3ab(a+b)',
        '(a-b)³': '(a-b)³ = a³ - b³ - 3ab(a-b)'
    },
    'age_problems': {
        'present_age': 'Present age + n years = Future age',
        'past_age': 'Present age - n years = Past age',
        'ratio_method': 'Use ratio units and solve equation'
    },
    'geometry': {
        'triangle_sum': 'Sum of angles = 180°',
        'exterior_angle': 'Exterior angle = Sum of opposite interior angles',
        'pythagoras': 'In right triangle: Hypotenuse² = Base² + Perpendicular²',
        'rectangle_property': 'For any point inside rectangle: PA² + PC² = PB² + PD²'
    },
    'height_distance': {
        'angle_elevation': 'Angle formed when looking up from horizontal',
        'angle_depression': 'Angle formed when looking down from horizontal',
        'application': 'Use tan θ = height/distance for most problems'
    },
    'probability': {
        'basic': 'P(E) = Favorable outcomes / Total outcomes',
        'complement': 'P(not E) = 1 - P(E)',
        'range': '0 ≤ P(E) ≤ 1'
    }
}

with open(os.path.join(FORMULA_DIR, 'master_formulas.json'), 'w') as f:
    json.dump(formulas, f, indent=2)

print("✓ Formula database created")

# Summary stats
print("\n=== ANALYSIS SUMMARY ===")
print(f"Total Maths Questions: {len(maths_questions)}")
print(f"Topics Identified: {len(topic_freq)}")
print(f"Papers Analyzed: {len(paper_freq)}")
print(f"\nTop 5 Topics:")
for topic, count in sorted(topic_freq.items(), key=lambda x: -x[1])[:5]:
    print(f"  {TOPIC_NAMES.get(topic, topic)}: {count} questions ({count/len(maths_questions)*100:.1f}%)")

print("\n✓ All analysis files generated successfully!")
