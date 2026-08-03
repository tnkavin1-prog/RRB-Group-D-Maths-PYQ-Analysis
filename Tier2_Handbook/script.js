// RRB Group D Mathematics - Premium Master Handbook JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initNavigation();
    initThemeToggle();
    initSearch();
    initBackToTop();
    initProgressTracker();
    initBookmarks();
    populateDynamicSections();
});

// Navigation System
function initNavigation() {
    const navItems = document.querySelectorAll('.nav-item[data-chapter]');
    const sections = document.querySelectorAll('.chapter-section');
    const menuToggle = document.getElementById('menuToggle');
    const sidebar = document.getElementById('sidebar');
    
    navItems.forEach(item => {
        item.addEventListener('click', function() {
            const chapterId = this.dataset.chapter;
            
            // Update active nav item
            navItems.forEach(nav => nav.classList.remove('active'));
            this.classList.add('active');
            
            // Show corresponding section
            sections.forEach(section => {
                section.classList.remove('active');
                if (section.id === chapterId) {
                    section.classList.add('active');
                    updatePageTitle(chapterId);
                }
            });
            
            // Close mobile menu
            if (window.innerWidth <= 1024) {
                sidebar.classList.remove('active');
            }
            
            // Scroll to top
            window.scrollTo({ top: 0, behavior: 'smooth' });
            
            // Save progress
            saveProgress(chapterId);
        });
    });
    
    // Mobile menu toggle
    if (menuToggle) {
        menuToggle.addEventListener('click', function() {
            sidebar.classList.toggle('active');
        });
    }
}

function updatePageTitle(chapterId) {
    const titles = {
        'home': 'RRB Group D Mathematics Master Handbook',
        'trigonometry': '📐 Trigonometry - Complete Guide',
        'number-system': '🔢 Number System - Foundation Concepts',
        'percentage': '📊 Percentage - Master Guide',
        'profit-loss': '💰 Profit & Loss - Business Maths',
        'si-ci': '🏦 Simple & Compound Interest',
        'mensuration-3d': '📦 Mensuration 3D - Volume & Surface Area',
        'mensuration-2d': '📏 Mensuration 2D - Area & Perimeter',
        'time-speed-distance': '🚂 Time, Speed & Distance',
        'average': '📈 Average - Mean Calculations',
        'ratio-proportion': '⚖️ Ratio & Proportion',
        'time-work': '⏱️ Time & Work - Efficiency Problems',
        'height-distance': '🏔️ Height & Distance Applications',
        'algebra': '🔤 Algebra - Expressions & Equations',
        'geometry': '🔷 Geometry - Shapes & Properties',
        'probability': '🎲 Probability - Chance & Likelihood',
        'age-problems': '👤 Age Problems - Time-based Questions',
        'formulas': '📝 Master Formula Database',
        'shortcuts': '⚡ Ultimate Shortcut Handbook',
        'practice': '✏️ Complete Practice Sets',
        'revision': '🔄 Last Minute Revision',
        'predictions': '🔮 Exam Predictions & Analysis'
    };
    
    const pageTitle = document.getElementById('pageTitle');
    if (pageTitle && titles[chapterId]) {
        pageTitle.textContent = titles[chapterId];
    }
}

// Theme Toggle
function initThemeToggle() {
    const themeToggle = document.getElementById('themeToggle');
    const html = document.documentElement;
    
    // Check saved theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-theme', savedTheme);
    updateThemeButton(themeToggle, savedTheme);
    
    themeToggle.addEventListener('click', function() {
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeButton(themeToggle, newTheme);
    });
}

function updateThemeButton(button, theme) {
    button.textContent = theme === 'dark' ? '☀️ Light Mode' : '🌙 Dark Mode';
}

// Search Functionality
function initSearch() {
    const searchInput = document.getElementById('searchInput');
    const navItems = document.querySelectorAll('.nav-item[data-chapter]');
    
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase().trim();
            
            navItems.forEach(item => {
                const text = item.querySelector('.nav-text').textContent.toLowerCase();
                
                if (searchTerm === '' || text.includes(searchTerm)) {
                    item.style.display = 'flex';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    }
}

// Back to Top Button
function initBackToTop() {
    const backToTop = document.getElementById('backToTop');
    
    if (backToTop) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTop.style.opacity = '1';
                backToTop.style.visibility = 'visible';
            } else {
                backToTop.style.opacity = '0';
                backToTop.style.visibility = 'hidden';
            }
        });
        
        backToTop.addEventListener('click', function() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
}

// Progress Tracker
function initProgressTracker() {
    loadProgress();
}

function saveProgress(chapterId) {
    let progress = JSON.parse(localStorage.getItem('handbookProgress') || '{}');
    progress[chapterId] = {
        visited: true,
        timestamp: Date.now()
    };
    localStorage.setItem('handbookProgress', JSON.stringify(progress));
    updateProgressDisplay();
}

function loadProgress() {
    updateProgressDisplay();
}

function updateProgressDisplay() {
    const progress = JSON.parse(localStorage.getItem('handbookProgress') || '{}');
    const totalChapters = 20; // Total navigable chapters
    const visitedChapters = Object.keys(progress).length;
    const percentage = Math.round((visitedChapters / totalChapters) * 100);
    
    const progressFill = document.getElementById('progressFill');
    if (progressFill) {
        progressFill.style.width = percentage + '%';
        progressFill.textContent = percentage + '%';
    }
}

// Bookmarks System
function initBookmarks() {
    const bookmarkBtn = document.getElementById('bookmarkBtn');
    
    if (bookmarkBtn) {
        bookmarkBtn.addEventListener('click', function() {
            const currentSection = document.querySelector('.chapter-section.active');
            if (currentSection) {
                const chapterId = currentSection.id;
                toggleBookmark(chapterId);
            }
        });
    }
}

function toggleBookmark(chapterId) {
    let bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
    
    const index = bookmarks.indexOf(chapterId);
    if (index > -1) {
        bookmarks.splice(index, 1);
        alert('Bookmark removed!');
    } else {
        bookmarks.push(chapterId);
        alert('Chapter bookmarked!');
    }
    
    localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
}

// Populate Dynamic Sections
function populateDynamicSections() {
    populateFormulaDatabase();
    populateShortcutHandbook();
    populatePracticeSets();
    populateRevisionGuide();
    populatePredictions();
}

function populateFormulaDatabase() {
    const container = document.querySelector('.formula-database-container');
    if (!container) return;
    
    const formulas = {
        'Percentage': [
            { formula: 'Percentage = (Part/Whole) × 100', description: 'Basic percentage formula' },
            { formula: 'New Value = Original × (1 + rate/100)', description: 'Percentage increase' },
            { formula: 'New Value = Original × (1 - rate/100)', description: 'Percentage decrease' },
            { formula: 'Net % = a + b + (ab/100)', description: 'Successive percentage change' }
        ],
        'Profit & Loss': [
            { formula: 'Profit = SP - CP', description: 'Basic profit calculation' },
            { formula: 'Profit% = (Profit/CP) × 100', description: 'Profit percentage' },
            { formula: 'SP = CP × (100 + Profit%)/100', description: 'Selling price from cost price' },
            { formula: 'Discount% = (MP - SP)/MP × 100', description: 'Discount percentage' }
        ],
        'Simple Interest': [
            { formula: 'SI = (P × R × T)/100', description: 'Simple interest formula' },
            { formula: 'A = P(1 + RT/100)', description: 'Amount with simple interest' }
        ],
        'Compound Interest': [
            { formula: 'A = P(1 + R/100)^T', description: 'Amount with compound interest' },
            { formula: 'CI = A - P', description: 'Compound interest' }
        ],
        'Trigonometry': [
            { formula: 'sin²θ + cos²θ = 1', description: 'Fundamental identity' },
            { formula: '1 + tan²θ = sec²θ', description: 'Tangent-Secant identity' },
            { formula: '1 + cot²θ = cosec²θ', description: 'Cotangent-Cosecant identity' }
        ],
        'Time & Work': [
            { formula: 'If A does work in n days, 1 day work = 1/n', description: 'Work rate' },
            { formula: 'Together = xy/(x+y) days', description: 'Combined work' }
        ],
        'Mensuration 2D': [
            { formula: 'Rectangle Area = l × b', description: 'Rectangle area' },
            { formula: 'Circle Area = πr²', description: 'Circle area' },
            { formula: 'Triangle Area = ½ × base × height', description: 'Triangle area' }
        ],
        'Mensuration 3D': [
            { formula: 'Cube Volume = side³', description: 'Cube volume' },
            { formula: 'Cylinder Volume = πr²h', description: 'Cylinder volume' },
            { formula: 'Sphere Volume = 4/3 πr³', description: 'Sphere volume' }
        ]
    };
    
    let html = '<div class="formula-grid">';
    for (const [category, items] of Object.entries(formulas)) {
        html += `<div class="formula-category-block">
            <h4>${category}</h4>`;
        items.forEach(item => {
            html += `<div class="formula-item">
                <div class="formula-display">${item.formula}</div>
                <div class="formula-desc">${item.description}</div>
            </div>`;
        });
        html += '</div>';
    }
    html += '</div>';
    
    container.innerHTML = html;
}

function populateShortcutHandbook() {
    const container = document.querySelector('.shortcut-handbook-container');
    if (!container) return;
    
    const shortcuts = [
        {
            category: 'Calculation Shortcuts',
            tips: [
                'Multiply by 5: Multiply by 10 and divide by 2',
                'Multiply by 25: Multiply by 100 and divide by 4',
                'Square of numbers ending in 5: (n5)² = n(n+1) | 25',
                '√3 ≈ 1.732, √2 ≈ 1.414, π ≈ 22/7 or 3.14'
            ]
        },
        {
            category: 'Percentage Tricks',
            tips: [
                '10% = Divide by 10',
                '20% = Divide by 5',
                '25% = Divide by 4',
                '33⅓% = Divide by 3',
                '50% = Divide by 2'
            ]
        },
        {
            category: 'Trigonometry Quick Tips',
            tips: [
                'sin²θ + cos²θ = 1 → Instant answer for such expressions',
                'At 45°: sin = cos = 1/√2, tan = 1',
                'At 30° & 60°: Values swap between sin/cos',
                'Remember 3-4-5 triangle for quick ratio calculations'
            ]
        },
        {
            category: 'Time-Saving Methods',
            tips: [
                'Use options to verify answers quickly',
                'Approximate when options are far apart',
                'Learn multiplication tables up to 20',
                'Practice mental math for basic operations'
            ]
        }
    ];
    
    let html = '<div class="shortcut-grid">';
    shortcuts.forEach(shortcut => {
        html += `<div class="shortcut-card-large">
            <h4>⚡ ${shortcut.category}</h4>
            <ul class="shortcut-list">`;
        shortcut.tips.forEach(tip => {
            html += `<li>${tip}</li>`;
        });
        html += '</ul></div>';
    });
    html += '</div>';
    
    container.innerHTML = html;
}

function populatePracticeSets() {
    const container = document.querySelector('.practice-handbook-container');
    if (!container) return;
    
    const practiceSets = [
        {
            title: 'Mixed Topic Practice Set 1',
            questions: [
                'If sin θ = 3/5, find cos θ',
                'A number is increased by 20% and then decreased by 20%. Find net change%',
                'Find CI on ₹10,000 at 10% p.a. for 2 years',
                'If CP = ₹500 and SP = ₹600, find profit%',
                'Find area of circle with radius 7 cm'
            ]
        },
        {
            title: 'Mixed Topic Practice Set 2',
            questions: [
                'Evaluate: sin 30° + cos 60° + tan 45°',
                'Find HCF of 36, 54, and 90',
                'A train covers 180 km in 3 hours. Find speed in m/s',
                'If A:B = 2:3 and B:C = 4:5, find A:B:C',
                'Find volume of cube with side 6 cm'
            ]
        },
        {
            title: 'Speed Practice Set',
            questions: [
                'What is 15% of 200?',
                '√144 = ?',
                'sin 90° = ?',
                '1/2 as percentage = ?',
                'Average of first 5 natural numbers = ?'
            ]
        }
    ];
    
    let html = '<div class="practice-sets-collection">';
    practiceSets.forEach(set => {
        html += `<div class="practice-set-block">
            <h4>${set.title}</h4>
            <ol class="practice-question-list">`;
        set.questions.forEach(q => {
            html += `<li>${q}</li>`;
        });
        html += '</ol></div>';
    });
    html += '</div>';
    
    container.innerHTML = html;
}

function populateRevisionGuide() {
    const container = document.querySelector('.revision-handbook-container');
    if (!container) return;
    
    const revisionContent = `
        <div class="revision-section">
            <h3>📋 One-Page Formula Revision</h3>
            <div class="quick-revision-grid">
                <div class="quick-rev-card">
                    <h5>Percentage</h5>
                    <p>% = (Part/Whole)×100</p>
                    <p>Net% = a+b+(ab/100)</p>
                </div>
                <div class="quick-rev-card">
                    <h5>Profit/Loss</h5>
                    <p>P = SP - CP</p>
                    <p>P% = (P/CP)×100</p>
                </div>
                <div class="quick-rev-card">
                    <h5>SI</h5>
                    <p>SI = PRT/100</p>
                    <p>A = P(1+RT/100)</p>
                </div>
                <div class="quick-rev-card">
                    <h5>CI</h5>
                    <p>A = P(1+R/100)^T</p>
                    <p>CI = A - P</p>
                </div>
                <div class="quick-rev-card">
                    <h5>Trigonometry</h5>
                    <p>sin²θ+cos²θ=1</p>
                    <p>1+tan²θ=sec²θ</p>
                </div>
                <div class="quick-rev-card">
                    <h5>Mensuration</h5>
                    <p>Circle: πr²</p>
                    <p>Cube: side³</p>
                </div>
            </div>
        </div>
        
        <div class="revision-section">
            <h3>⚡ One-Page Shortcut Revision</h3>
            <ul class="rapid-fire-list">
                <li><strong>× 5:</strong> ×10 ÷2</li>
                <li><strong>× 25:</strong> ×100 ÷4</li>
                <li><strong>× 125:</strong> ×1000 ÷8</li>
                <li><strong>sq of 5-ending:</strong> n(n+1)|25</li>
                <li><strong>10%:</strong> ÷10</li>
                <li><strong>20%:</strong> ÷5</li>
                <li><strong>25%:</strong> ÷4</li>
                <li><strong>33⅓%:</strong> ÷3</li>
                <li><strong>50%:</strong> ÷2</li>
                <li><strong>sin²+cos²:</strong> =1</li>
            </ul>
        </div>
        
        <div class="revision-section">
            <h3>🧠 One-Page Concept Revision</h3>
            <div class="concept-cards">
                <div class="concept-mini">
                    <strong>Divisibility by 3:</strong> Sum of digits divisible by 3
                </div>
                <div class="concept-mini">
                    <strong>Pythagorean Triplets:</strong> 3-4-5, 5-12-13, 8-15-17
                </div>
                <div class="concept-mini">
                    <strong>At 45°:</strong> Height = Distance
                </div>
                <div class="concept-mini">
                    <strong>Successive Change:</strong> a+b+(ab/100)
                </div>
            </div>
        </div>
    `;
    
    container.innerHTML = revisionContent;
}

function populatePredictions() {
    const container = document.querySelector('.predictions-container');
    if (!container) return;
    
    const predictions = [
        { rank: 1, topic: 'Trigonometry', frequency: 12, confidence: '84%', prediction: 'High probability of 11-13 questions' },
        { rank: 2, topic: 'Number System', frequency: 9, confidence: '78%', prediction: 'High probability of 8-10 questions' },
        { rank: 3, topic: 'Percentage', frequency: 9, confidence: '78%', prediction: 'High probability of 8-10 questions' },
        { rank: 4, topic: 'Profit & Loss', frequency: 8, confidence: '76%', prediction: 'High probability of 7-9 questions' },
        { rank: 5, topic: 'SI & CI', frequency: 7, confidence: '74%', prediction: 'High probability of 6-8 questions' },
        { rank: 6, topic: 'Mensuration 3D', frequency: 6, confidence: '72%', prediction: 'High probability of 5-7 questions' },
        { rank: 7, topic: 'Time Speed Distance', frequency: 6, confidence: '72%', prediction: 'High probability of 5-7 questions' },
        { rank: 8, topic: 'Mensuration 2D', frequency: 5, confidence: '70%', prediction: 'High probability of 4-6 questions' }
    ];
    
    let html = '<div class="predictions-table-container">';
    html += '<table class="predictions-table">';
    html += '<thead><tr><th>Rank</th><th>Topic</th><th>Frequency</th><th>Confidence</th><th>Prediction</th></tr></thead>';
    html += '<tbody>';
    
    predictions.forEach(p => {
        const badgeClass = p.confidence.includes('8') ? 'badge-high' : p.confidence.includes('7') ? 'badge-medium' : 'badge-low';
        html += `<tr>
            <td>${p.rank}</td>
            <td><strong>${p.topic}</strong></td>
            <td>${p.frequency}</td>
            <td><span class="${badgeClass}">${p.confidence}</span></td>
            <td>${p.prediction}</td>
        </tr>`;
    });
    
    html += '</tbody></table>';
    
    html += '<div class="prediction-summary"><h4>🔮 Key Insights</h4>';
    html += '<ul>';
    html += '<li><strong>Top 5 topics</strong> account for ~65% of all mathematics questions</li>';
    html += '<li><strong>Trigonometry</strong> has been consistently appearing across all shifts</li>';
    html += '<li><strong>Focus areas:</strong> Master Trigonometry, Number System, and Percentage first</li>';
    html += '<li><strong>Expected difficulty:</strong> Easy to Moderate based on PYQ trends</li>';
    html += '</ul></div>';
    
    html += '</div>';
    
    container.innerHTML = html;
}

// Keyboard Navigation
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K for search
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            searchInput.focus();
        }
    }
    
    // Escape to close mobile menu
    if (e.key === 'Escape') {
        const sidebar = document.getElementById('sidebar');
        if (sidebar && sidebar.classList.contains('active')) {
            sidebar.classList.remove('active');
        }
    }
});

// Add CSS for dynamic content
const style = document.createElement('style');
style.textContent = `
    .formula-grid, .shortcut-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        padding: 1rem;
    }
    
    .formula-category-block, .shortcut-card-large {
        background: var(--bg-secondary);
        padding: 1.5rem;
        border-radius: var(--radius-md);
        border-left: 4px solid var(--primary-color);
    }
    
    .formula-category-block h4, .shortcut-card-large h4 {
        margin-bottom: 1rem;
        color: var(--primary-color);
    }
    
    .formula-item {
        background: var(--bg-tertiary);
        padding: 1rem;
        border-radius: var(--radius-sm);
        margin-bottom: 0.75rem;
    }
    
    .formula-display {
        font-family: 'Courier New', monospace;
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
    }
    
    .formula-desc {
        font-size: 0.75rem;
        color: var(--text-secondary);
    }
    
    .shortcut-list {
        list-style: none;
        padding: 0;
    }
    
    .shortcut-list li {
        padding: 0.5rem 0;
        padding-left: 1.5rem;
        position: relative;
        font-size: 0.875rem;
    }
    
    .shortcut-list li::before {
        content: "⚡";
        position: absolute;
        left: 0;
    }
    
    .practice-sets-collection, .predictions-table-container {
        padding: 1rem;
    }
    
    .practice-set-block {
        background: var(--bg-secondary);
        padding: 1.5rem;
        border-radius: var(--radius-md);
        margin-bottom: 1.5rem;
    }
    
    .practice-question-list {
        list-style: decimal;
        padding-left: 1.5rem;
        margin-top: 1rem;
    }
    
    .practice-question-list li {
        padding: 0.5rem 0;
        font-size: 0.875rem;
    }
    
    .quick-revision-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 1rem;
        margin: 1.5rem 0;
    }
    
    .quick-rev-card {
        background: var(--bg-secondary);
        padding: 1rem;
        border-radius: var(--radius-md);
        text-align: center;
    }
    
    .quick-rev-card h5 {
        color: var(--primary-color);
        margin-bottom: 0.5rem;
        font-size: 0.875rem;
    }
    
    .quick-rev-card p {
        font-size: 0.75rem;
        font-family: 'Courier New', monospace;
    }
    
    .rapid-fire-list {
        list-style: none;
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 0.75rem;
    }
    
    .rapid-fire-list li {
        background: var(--bg-secondary);
        padding: 0.75rem;
        border-radius: var(--radius-sm);
        font-size: 0.875rem;
    }
    
    .concept-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
    }
    
    .concept-mini {
        background: linear-gradient(135deg, #e0e7ff, #c7d2fe);
        padding: 1rem;
        border-radius: var(--radius-md);
        font-size: 0.875rem;
    }
    
    .predictions-table {
        width: 100%;
        border-collapse: collapse;
        margin: 1.5rem 0;
    }
    
    .predictions-table th,
    .predictions-table td {
        padding: 1rem;
        text-align: left;
        border-bottom: 1px solid var(--border-color);
    }
    
    .predictions-table th {
        background: var(--bg-tertiary);
        font-weight: 600;
    }
    
    .prediction-summary {
        background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
        padding: 1.5rem;
        border-radius: var(--radius-md);
        margin-top: 1.5rem;
        border: 1px solid #bae6fd;
    }
    
    .prediction-summary h4 {
        margin-bottom: 1rem;
        color: #0369a1;
    }
    
    .prediction-summary ul {
        list-style: none;
    }
    
    .prediction-summary li {
        padding: 0.5rem 0;
        font-size: 0.875rem;
    }
    
    .revision-section {
        background: var(--bg-primary);
        padding: 2rem;
        border-radius: var(--radius-lg);
        margin-bottom: 2rem;
        box-shadow: var(--shadow-md);
    }
    
    .revision-section h3 {
        margin-bottom: 1.5rem;
        color: var(--text-primary);
    }
`;
document.head.appendChild(style);
