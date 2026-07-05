#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""Generate editable oral placement test PDF with checkboxes and text fields."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
import re

DARK = HexColor('#1a1a2e')
GRAY = HexColor('#555555')
GREEN = HexColor('#28a745')
BLUE = HexColor('#007bff')
YELLOW = HexColor('#ffc107')
RED = HexColor('#dc3545')
WARN = HexColor('#fff3cd')
w, h = letter

fn = 'EVALUACION_ORAL_EDITABLE.pdf'
c = canvas.Canvas(fn, pagesize=letter)

def new_page():
    c.showPage()
    return h - 40

def header(y, text, color):
    c.setFillColor(color)
    c.rect(40, y-3, w-80, 20, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('Helvetica-Bold', 12)
    c.drawString(50, y+1, text)
    return y - 28

def question(y, num, q, struct, pas, fail, pg):
    if y < 110:
        y = new_page()
    c.setFont('Helvetica-Bold', 9)
    c.setFillColor(DARK)
    c.drawString(40, y, f'{num}.')
    # Question
    c.setFont('Helvetica-Bold', 8.5)
    c.setFillColor(black)
    # Simple wrap
    if len(q) > 85:
        c.drawString(55, y, q[:85])
        y -= 11
        c.setFont('Helvetica-Bold', 8.5)
        c.drawString(55, y, q[85:])
    else:
        c.drawString(55, y, q)
    y -= 11
    # Structure
    c.setFont('Helvetica-Oblique', 7)
    c.setFillColor(GRAY)
    c.drawString(55, y, f'Tests: {struct}')
    y -= 10
    # Pass/Fail
    c.setFont('Helvetica', 7)
    c.setFillColor(GREEN)
    c.drawString(55, y, f'PASS: {pas[:90]}')
    y -= 9
    c.setFillColor(RED)
    c.drawString(55, y, f'FAIL: {fail[:90]}')
    # Checkboxes on right
    c.acroForm.checkbox(name=f'p{pg}q{num}ok', x=470, y=y+16, size=10, borderWidth=0.5)
    c.setFillColor(black)
    c.setFont('Helvetica', 6)
    c.drawString(483, y+18, 'OK')
    c.acroForm.checkbox(name=f'p{pg}q{num}x', x=505, y=y+16, size=10, borderWidth=0.5)
    c.drawString(518, y+18, 'X')
    y -= 10
    return y

def result_line(y, level):
    c.setFont('Helvetica-Bold', 10)
    c.setFillColor(DARK)
    c.drawString(40, y, f'{level} RESULT:')
    c.acroForm.checkbox(name=f'{level}_pass', x=130, y=y-2, size=12, borderWidth=0.5)
    c.setFont('Helvetica', 9)
    c.setFillColor(black)
    c.drawString(146, y, 'PASS')
    c.acroForm.checkbox(name=f'{level}_fail', x=200, y=y-2, size=12, borderWidth=0.5)
    c.drawString(216, y, f'FAIL > Place in {level}')
    y -= 16
    c.setFont('Helvetica', 8)
    c.drawString(40, y, 'Notes:')
    c.acroForm.textfield(name=f'{level}_notes', x=75, y=y-4, width=w-125, height=13, fontSize=8, borderWidth=0.5)
    return y - 20

# ===== PAGE 1: HEADER + A1 =====
y = h - 35
c.setFont('Helvetica-Bold', 16)
c.setFillColor(DARK)
c.drawString(40, y, 'HEIIU - Oral Placement Test')
y -= 16
c.setFont('Helvetica', 8)
c.setFillColor(GRAY)
c.drawString(40, y, 'Evaluator: Breagh / Greg | 20-30 min | Ladder: A1 > A2 > B1 > B2 | Fill digitally or print')
y -= 22

c.setFont('Helvetica-Bold', 9)
c.setFillColor(black)
c.drawString(40, y, 'Student:')
c.acroForm.textfield(name='student', x=90, y=y-3, width=160, height=14, fontSize=9, borderWidth=0.5)
c.drawString(270, y, 'Date:')
c.acroForm.textfield(name='date', x=300, y=y-3, width=80, height=14, fontSize=9, borderWidth=0.5)
c.drawString(400, y, 'Evaluator:')
c.acroForm.textfield(name='evaluator', x=455, y=y-3, width=110, height=14, fontSize=9, borderWidth=0.5)
y -= 22

# Instructions
c.setFillColor(WARN)
c.rect(40, y-28, w-80, 32, fill=1, stroke=0)
c.setFillColor(black)
c.setFont('Helvetica', 7)
c.drawString(48, y-3, 'CONVERSATION, not exam. Never correct. Rephrase ONCE if needed. Skip ahead if obvious. Trust your gut.')
c.drawString(48, y-14, 'Start: "Hey [name], nice to meet you! This is just a chat. No right or wrong, just talk naturally. Cool, let\'s start."')
y -= 38

# A1
y = header(y, 'LEVEL A1 (Minutes 0-5) - Basic structures', GREEN)
a1 = [
    ("So, what do you do? Do you work or study?", "Present simple do/does", "I work at a bank.", "I working... / I am work..."),
    ("Does your mom work too?", "Does + 3rd person", "She works at a school.", "She work... / She don't work..."),
    ("What time do you usually wake up?", "What time + present simple", "I wake up at seven.", "I waking seven."),
    ("Where do you eat lunch?", "Where + present simple", "I eat lunch at work.", "Doesn't understand 'where'."),
    ("Do you play any sports?", "Do you + verb", "Yes, I play soccer.", "Yes, I playing..."),
    ("Can you cook?", "Can/can't + short answer", "Yes, I can. / No, I can't.", "Yes, I cooking."),
    ("If you feel sick, should you go to work?", "Should", "I should stay home.", "Doesn't understand 'should'."),
    ("What will you do this weekend?", "Will/won't", "I will visit my mom.", "I go park... / No 'will'."),
    ("How much does a coffee cost here?", "Numbers/prices", "About two dollars.", "Can't produce number."),
    ("Tell me about your family.", "Pronouns + verb-s", "My sister lives in... He works...", "Mixes he/she. No verb-s."),
    ("Where should I go if I visit your city?", "Should (advice)", "You should go to the park.", "Can't use 'should'."),
]
for i, (q, s, p, f) in enumerate(a1):
    y = question(y, i+1, q, s, p, f, 1)
y = result_line(y, 'A1')

# ===== A2 =====
y = new_page()
y = header(y, 'LEVEL A2 (Minutes 5-12) - Future forms, conditionals, tenses', BLUE)
a2 = [
    ("Any plans for the weekend? What are you going to do?", "Going to (planned future)", "I'm going to visit my parents.", "I will visit... / I go visit..."),
    ("Anything you might do but you're not sure?", "Might (possibility)", "I might go to the movies.", "Maybe I go... / No 'might'."),
    ("Concert at 8pm Saturday. How would you tell a friend?", "Present simple for schedules", "The concert starts at 8.", "The concert will start..."),
    ("If you have free time tomorrow, what will you do?", "First conditional", "If I have time, I will go to the gym.", "If I will have... / If I have, I go..."),
    ("If you had a million dollars, what would you do?", "Second conditional", "If I had a million, I would travel.", "If I have million, I will buy..."),
    ("Have you ever traveled to another country?", "Present perfect", "Yes, I have. I've been to Mexico.", "Yes, I travel Mexico last year."),
    ("What were you doing yesterday at 3pm?", "Past continuous", "I was working. / I was watching TV.", "I work. / I watched. (no continuous)"),
    ("Were you doing something when someone interrupted?", "Past continuous + interruption", "I was cooking when my phone rang.", "I cook and phone ring."),
    ("I think English is important. What do you think?", "Relative 'that'", "I think that English is very important.", "Can't form complex opinions."),
    ("When's your birthday? And today's date?", "Ordinals + dates", "March twenty-third.", "March twenty-three. No ordinals."),
    ("If it rains during your vacation, what will you do?", "During/while + conditional", "During the rain, I'll stay in the hotel.", "Can't use 'during' properly."),
]
for i, (q, s, p, f) in enumerate(a2):
    y = question(y, i+1, q, s, p, f, 2)
y = result_line(y, 'A2')

# ===== B1 =====
y = new_page()
y = header(y, 'LEVEL B1 (Minutes 12-20) - Sustained speech, blending, detail', YELLOW)
b1 = [
    ("Tell me about a trip. Where, what happened, would you go back?", "Storytelling + multiple tenses", "Uses 2-3 tenses. Sustains 1+ min.", "Only 1 tense. Very short."),
    ("What do you think about social media? Good or bad?", "Opinions with reasons", "I think... because... but also...", "Is good. / One sentence."),
    ("Describe your best friend. Looks and personality.", "Description + detail", "She's tall, dark hair, funny, kind.", "She is good. She is nice. No detail."),
    ("What had you planned before studying English here?", "Past perfect", "I had tried online but it didn't work.", "I try online before. No past perfect."),
    ("If you could change one thing about your city?", "2nd conditional + reasoning", "If I could, I would improve transport because...", "Short. No reasoning."),
    ("Tell me your typical day. Morning to night. Full detail.", "Sustained 2+ min + routine", "Speaks 1-2 min. Varied vocab. Flow.", "I wake up. I go work. I come home."),
    ("Plans for the next 5 years?", "Multiple future forms blended", "I'm going to... I might... I'll probably...", "I will work. One form only."),
    ("How do you make your favorite food? Step by step.", "Sequencing + imperatives", "First chop onion. Then fry until golden. After that...", "You put... thing... cook."),
    ("What have you been doing lately that you enjoy?", "Present perfect continuous", "I've been going to the gym a lot.", "I go gym. No structure."),
]
for i, (q, s, p, f) in enumerate(b1):
    y = question(y, i+1, q, s, p, f, 3)
y = result_line(y, 'B1')

# ===== B2 =====
y = new_page()
y = header(y, 'LEVEL B2 (Minutes 20-28) - Advanced grammar, argumentation', RED)
b2 = [
    ("You like traveling, don't you?", "Question tags", "Responds + produces own tag.", "Confused. Can't produce one."),
    ("City or countryside? Or both?", "Either/neither/both", "I like both. / Neither is perfect.", "Can't use either/neither/both."),
    ("If you hadn't studied English young, how would life differ now?", "Third/mixed conditional", "If I hadn't studied, I wouldn't have gotten my job.", "If I didn't study, I don't have job."),
    ("Famous building in your country. When built? Used for?", "Passive voice", "It was built in 1920. Used as a museum.", "They build it 1920. People use for museum."),
    ("Recent conversation. What did the other person say?", "Reported speech", "My boss told me that I needed to finish by Friday.", "Boss say finish project. Direct only."),
    ("Gotten anything done recently? Haircut, car repair?", "Causative", "I got my car serviced last week.", "I cut my hair (someone else did it)."),
    ("Tell me about someone who influenced you.", "Relative clauses", "My grandfather, who was a teacher, told me...", "My grandfather. He was teacher."),
    ("Should everyone learn a second language? Does anyone only need one?", "Indefinite pronouns", "Uses everyone, anyone, nobody naturally.", "Avoids or uses incorrectly."),
    ("DEBATE: AI will replace teachers. Agree/disagree? Convince me.", "Arguing 3+ min", "3+ min with examples, concessions, counter-arguments.", "Can't sustain. Short. Major errors."),
    ("Something went wrong but was a blessing in disguise.", "Complex narrative + vocab", "Detailed, proper tenses, advanced vocabulary.", "Disorganized. Limited. Tense errors."),
]
for i, (q, s, p, f) in enumerate(b2):
    y = question(y, i+1, q, s, p, f, 4)
y = result_line(y, 'B2')

# ===== FINAL PLACEMENT =====
y -= 10
c.setFillColor(DARK)
c.rect(40, y-3, w-80, 24, fill=1, stroke=0)
c.setFillColor(white)
c.setFont('Helvetica-Bold', 14)
c.drawString(50, y+2, 'FINAL PLACEMENT:')

y -= 28
c.setFillColor(black)
for lvl, px in [('A1', 80), ('A2', 170), ('B1', 260), ('B2', 350), ('B2+', 440)]:
    c.acroForm.checkbox(name=f'final_{lvl}', x=px, y=y-2, size=16, borderWidth=0.5)
    c.setFont('Helvetica-Bold', 13)
    c.setFillColor(black)
    c.drawString(px + 20, y, lvl)

y -= 22
c.setFont('Helvetica-Bold', 9)
c.drawString(40, y, 'Final notes:')
c.acroForm.textfield(name='final_notes', x=110, y=y-4, width=w-160, height=13, fontSize=8, borderWidth=0.5)
y -= 18
c.acroForm.textfield(name='final_notes2', x=40, y=y-4, width=w-80, height=13, fontSize=8, borderWidth=0.5)
y -= 22
c.setFont('Helvetica', 8)
c.drawString(40, y, 'Evaluator signature: _________________________')
c.drawString(320, y, 'Coordination: _________________________')

c.save()

with open(fn, 'rb') as f:
    pages = len(re.findall(rb'/Type\s*/Page[^s]', f.read()))
print(f'OK: {fn} - {pages} pages, fully editable')
