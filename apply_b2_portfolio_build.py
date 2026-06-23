#!/usr/bin/env python3
"""
Aplica VATS + Portfolio Build a B2 Class 3-22 (no toca Class 1, 2 que ya estan hechas).

Estrategia minimo-invasiva:
1. Inserta VATS de 5 min al inicio del primer bloque (## PLAN DE CLASE).
2. NO ajusta los timestamps de los bloques existentes.
3. Inserta Portfolio Build como NUEVO bloque al final (antes de Self-Check),
   con el dia del ciclo correspondiente segun el numero de clase.
4. Actualiza el bloque HOMEWORK con la nota de Goldlist Profesional como inversion diaria.

NOTA: como NO ajustamos timestamps, la clase pasa de ~232 min a ~252 min.
El profesor lo absorbe cortando un bloque sobrante. Este es el costo de no hacer
una refactorizacion completa de cada clase.

Si Pedro prefiere tiempos exactos, lo arreglamos por archivo despues.
"""
import os, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
B2_DIR = ROOT / 'B2'

# Rotacion de virtudes por semana (B2 = 5 clases/semana asumido)
def virtue_for_class(n):
    # Class 1-5: Prudence, 6-10: Temperance, 11-15: Justice, 16-20: Fortitude, 21-22: Prudence
    week = (n - 1) // 5
    virtues = ['PRUDENCE', 'TEMPERANCE', 'JUSTICE', 'FORTITUDE']
    return virtues[week % 4]

VIRTUE_QUESTIONS = {
    'PRUDENCE': [
        'What\'s a recent decision you regret? What would prudence have done?',
        'Is it smarter to act fast or wait and analyze? Give an example.',
        'When did you choose discipline over impulse this month?',
        'What\'s a long-term goal worth waiting for?',
        'A decision your past self made that your present self thanks them for?',
    ],
    'TEMPERANCE': [
        'What habit do you over-do? What would moderation look like?',
        'Where in your life do you say "yes" too often?',
        'What\'s something you enjoyed more BECAUSE you had less of it?',
        'Tell me about a time you said "enough" — and were right.',
        'What\'s your relationship with comparison? Healthy or hurtful?',
    ],
    'JUSTICE': [
        'Have you ever helped someone who couldn\'t pay you back?',
        'A time you spoke up against unfairness even when uncomfortable?',
        'What does fairness mean to you in a team setting?',
        'When did you receive justice — and what did it feel like?',
        'Who in your life lives justice every day? Why?',
    ],
    'FORTITUDE': [
        'Tell me about a time you almost gave up — but didn\'t.',
        'What\'s the hardest "no" you\'ve had to say?',
        'When did you keep going past the point of comfort? Why?',
        'What\'s a fear you walked toward instead of running from?',
        'A challenge you took on that no one expected you to finish?',
    ],
}

# Ciclo de Portfolio Build por clase (Class 2 = Day 1, Class 3 = Day 2, etc.)
def cycle_day_for_class(n):
    # Class 2 = Day 1, Class 3 = Day 2, ... Class 6 = Day 5, Class 7 = Day 1 again
    return ((n - 2) % 5) + 1

CYCLE_DAYS = {
    1: 'Mock Interview Round',
    2: '60-Second Video Pitch',
    3: 'Project Presentation Sprint',
    4: 'Mock Phone Call (BPO Simulation)',
    5: 'Correct the Recruiter',
}

CYCLE_BANK_QUESTIONS = {
    # cycle_number -> (pairs_q, recording_q) from STAR bank
    1: ('#3 "Tell me about a time you faced a difficult challenge at work and how you handled it."',
        '#5 "Describe a situation where you had to meet a tight deadline. How did you handle it?"'),
    2: ('#4 "Tell me about a time you had to work with a difficult team member."',
        '#6 "Give me an example of a time you took initiative without being asked."'),
    3: ('#7 "Tell me about a mistake you made and what you learned from it."',
        '#9 "Tell me about a time you led a project or a team."'),
    4: ('#14 "Give me an example of a successful team you were part of."',
        '#18 "Tell me about a time you had to give difficult feedback to a colleague."'),
}


def vats_block(virtue, question):
    return f"""### ☐ 00:00–00:05 | VATS: VIRTUE OF THE WEEK — {virtue} (5 min)

**Virtue of the week: {virtue}**

Write on the board:
```
{virtue} — "{question}"
```

Say: "Daily ritual. {virtue} this week. Pairs. English only — give it a try."

**V (1 min):** Read aloud. Point to board.
**A (30 sec):** "Think in silence."
**T (2 min):** "Pairs. Discuss."
**S (1.5 min):** 2 students share with the class. No correction — celebrate the attempt.

> Daily opening ritual. Virtues rotate weekly: Prudence → Temperance → Justice → Fortitude.

"""


def portfolio_block_day1(cycle_num):
    pairs_q, rec_q = CYCLE_BANK_QUESTIONS.get(cycle_num, CYCLE_BANK_QUESTIONS[1])
    return f"""### ☐ PORTFOLIO BUILD — DAY 1: MOCK INTERVIEW ROUND (15 min)

**⚠️ Use `ANEXO_PORTFOLIO_BUILD_B2_PROFESOR.pdf` (Day 1 section) and `ANEXO_BANCO_PREGUNTAS_STAR.pdf`.**

Today is **Day 1 of Portfolio Build Cycle {cycle_num}**. Students practice STAR-format interview answers.

**Setup (1 min):** Today's questions (Cycle {cycle_num}):
- **Pairs question:** {pairs_q}
- **Volunteer recording question:** {rec_q}

Write the STAR reminder on the board:
```
S — Situation: When? Where? What was happening?
T — Task:      What was your specific responsibility?
A — Action:    What did YOU specifically do?
R — Result:    Outcome (numbers / change if possible)
```

**Pairs round (8 min):** "Pairs. Person A answers using STAR. 90 sec. Person B times. Switch." 2 rounds of 90 sec each per person → 6 min speaking + 2 min switching.

**Volunteer recording (4 min):** "Who wants to record their answer for coordination feedback?" Pick 1. 60 seconds. Press record on YOUR phone. Send to coordination via WhatsApp same day.

**Group reflection (2 min):** "What was hardest about using STAR?" 2 students share.

**Your feedback during activity:** Pronunciation only. Filler words ("like", "you know") signaled by hand gesture. **Don't critique content.**

> See `ANEXO_PORTFOLIO_BUILD_B2_PROFESOR.pdf` Day 1 for the full script.

"""


def portfolio_block_day2():
    return """### ☐ PORTFOLIO BUILD — DAY 2: 60-SECOND VIDEO PITCH (15 min)

**⚠️ Use `ANEXO_PORTFOLIO_BUILD_B2_PROFESOR.pdf` (Day 2 section).**

Today is **Day 2 of the Portfolio Build Cycle**. Students record a 60-second video pitch on their phone, listen back, and improve.

**Setup (1 min):** Write the pitch structure on the board:
```
60-SECOND PITCH:
[10s] HOOK: Who am I in one phrase?
[15s] WHAT I DO + 1 RESULT
[15s] PASSION + 1 EXAMPLE
[15s] WHAT I'M LOOKING FOR
[5s]  CLOSE: name + email/LinkedIn
```

**Plan round (3 min):** "3 minutes. Write your 5 sections in your notebook. Single bullet each. No paragraphs."

**Record round 1 (4 min):** "Stand up. Phone in selfie mode. 60 seconds — GO." Set timer. Walk silently. At 60 sec: "Stop. Replay it. Listen to yourself."

**Improve round (5 min):** "What's ONE thing to fix? Record AGAIN, 60 sec."

**Submit (2 min):** "Send the IMPROVED version to WhatsApp with tag: PITCH-CYCLE[N]-[YourName]." Coordination collects pitches and gives written feedback before next Day 2.

**Your feedback during activity:** Walk silently. If someone freezes: "Just say one true sentence. Then keep going." After replay: "What did YOU notice?"

> See `ANEXO_PORTFOLIO_BUILD_B2_PROFESOR.pdf` Day 2 for the full script.

"""


def portfolio_block_day3():
    return """### ☐ PORTFOLIO BUILD — DAY 3: PROJECT PRESENTATION SPRINT (15 min)

**⚠️ Use `ANEXO_PORTFOLIO_BUILD_B2_PROFESOR.pdf` (Day 3 section).**

Today is **Day 3 of the Portfolio Build Cycle**. Each student gets ~1 minute to rehearse 1 slide / 1 section of their B2 final project (Shark Tank pitch / business plan / research presentation — coordination defines per cohort).

**Setup (1 min):** Write on the board:
```
TODAY'S SPRINT:
- 1 minute per student
- Speak only ABOUT the section you're working on this week
- No reading from screen
- Listen for: clarity + 1 strong sentence per section
```

**Rehearsal round (12 min):** ~12 students × ~1 min each. Each student stands. Says "My project section this week is about X." Speaks ~1 min about it. No notes.

**Peer feedback (2 min):** After each student: "What was clear? What was the strongest sentence?" One peer answers.

**Your feedback during activity:** Pronunciation, clarity, pacing. "Stronger ending — repeat that last sentence with more confidence." Don't critique content.

> If a student doesn't have a project section ready: "Then practice your 60-sec pitch instead. 1 minute, GO." Don't penalize.

"""


def portfolio_block_day4():
    return """### ☐ PORTFOLIO BUILD — DAY 4: MOCK PHONE CALL (15 min)

**⚠️ Use `ANEXO_PORTFOLIO_BUILD_B2_PROFESOR.pdf` (Day 4 section). 5 BPO scenarios available.**

Today is **Day 4 of the Portfolio Build Cycle**. Pairs simulate a customer service phone call in English.

**Setup (1 min):** Pick 1 scenario from the annex (rotate weekly):
- Scenario 1: Internet customer (irritated)
- Scenario 2: Hotel booking issue
- Scenario 3: Product return
- Scenario 4: Healthcare appointment
- Scenario 5: Tech support B2B

**Run the simulation (10 min):** Read the scenario aloud. Pairs choose roles. 4 minutes per call. At minute 4: "Switch roles. New call."

**Group debrief (4 min):** "What phrases worked best? What was hard?" Write the BEST phrases on board: "I understand your frustration." / "Let me see what I can do." / "I'll personally follow up by [time]."

**Your feedback during activity:** Pronunciation immediate correction. Filler words signaled.

> See `ANEXO_PORTFOLIO_BUILD_B2_PROFESOR.pdf` Day 4 for full scenario scripts.

"""


def portfolio_block_day5():
    return """### ☐ PORTFOLIO BUILD — DAY 5: CORRECT THE RECRUITER (15 min)

**⚠️ Use `ANEXO_PORTFOLIO_BUILD_B2_PROFESOR.pdf` (Day 5 section). 5 scripts with intentional errors available.**

Today is **Day 5 of the Portfolio Build Cycle**. YOU pretend to be a recruiter calling the student, with intentional errors. Students listen and correct you AT THE END.

**Setup (1 min):** "I will pretend to be a recruiter with intentional errors. After I finish, you correct me." Pick 1 of 5 scripts (rotate weekly):
- Script A: Phone screening
- Script B: Job offer
- Script C: Rejection
- Script D: Salary negotiation
- Script E: Reference check

**The script — read aloud as the "recruiter" (5 min):** Read the script slowly, naturally, with the planted errors. Don't emphasize the errors — speak as if you really were a recruiter.

**Correction round (8 min):** "What errors did I make? Don't say all at once. Raise hands. One at a time." Each student catches 1 error → 1 English Point. For each: student says wrong version → student says correct version → class repeats correct version 2x.

**Reflection (1 min):** "Which error would have been EMBARRASSING in a real interview?"

> See `ANEXO_PORTFOLIO_BUILD_B2_PROFESOR.pdf` Day 5 for the 5 scripts with errors.

"""


def portfolio_block_for_day(day, cycle_num):
    if day == 1:
        return portfolio_block_day1(cycle_num)
    if day == 2:
        return portfolio_block_day2()
    if day == 3:
        return portfolio_block_day3()
    if day == 4:
        return portfolio_block_day4()
    if day == 5:
        return portfolio_block_day5()


def updated_homework_block():
    return """### ☐ HOMEWORK + CLOSE (5 min)

Write on the board:
```
DAILY INVESTMENT (15-30 min today):
1. PROFESSIONAL GOLDLIST: 10 new business / academic
   phrases (idioms, connectors, STAR vocabulary).
   Send a photo of your notebook to WhatsApp.
2. WATCH any recording from today (pitch / interview).
   Write 3 things you'd improve.
3. CV / LinkedIn / Project: continue your work.
   Coordination reviews on schedule.
```

Say: "Daily investment is non-negotiable for B2. The Goldlist now lives in your daily WhatsApp routine — not in our class. In class we use that time for your portfolio."

"""


def process_class(class_num):
    """Procesa B2_ClassN_PRINT.md."""
    if class_num in (1, 2):
        return f'  Class {class_num}: skipped (already done)'

    path = B2_DIR / f'B2_Class{class_num}_PRINT.md'
    if not path.exists():
        return f'  Class {class_num}: file not found'

    text = path.read_text(encoding='utf-8')

    # 1. Insertar VATS
    virtue = virtue_for_class(class_num)
    questions = VIRTUE_QUESTIONS[virtue]
    q = questions[(class_num - 1) % len(questions)]
    vats = vats_block(virtue, q)

    # Buscar el primer "### ☐" o "### " y meter VATS antes
    pattern_first_block = re.compile(r'^(### [☐]?\s*\d+:\d+)', re.MULTILINE)
    match = pattern_first_block.search(text)
    if not match:
        # fallback: buscar primer ###
        pattern_first_block = re.compile(r'^### ', re.MULTILINE)
        match = pattern_first_block.search(text)
    if not match:
        return f'  Class {class_num}: no first block found'

    pos = match.start()
    text = text[:pos] + vats + text[pos:]

    # 2. Insertar Portfolio Build justo antes del Self-Check
    day = cycle_day_for_class(class_num)
    cycle_num = ((class_num - 2) // 5) + 1
    pb_block = portfolio_block_for_day(day, cycle_num)

    # Buscar "### ☐ ... | SELF-CHECK" o "### ... SELF-CHECK"
    pattern_selfcheck = re.compile(r'^(### [☐]?\s*\d+:\d+[–-]\d+:\d+\s*\|\s*SELF.?CHECK.*)$', re.MULTILINE | re.IGNORECASE)
    match_sc = pattern_selfcheck.search(text)
    if match_sc:
        pos_sc = match_sc.start()
        text = text[:pos_sc] + pb_block + text[pos_sc:]
    else:
        # fallback: buscar HOMEWORK
        pattern_hw = re.compile(r'^### .*HOMEWORK.*', re.MULTILINE | re.IGNORECASE)
        match_hw = pattern_hw.search(text)
        if match_hw:
            pos_hw = match_hw.start()
            text = text[:pos_hw] + pb_block + text[pos_hw:]
        else:
            return f'  Class {class_num}: no Self-Check or Homework found'

    # 3. Reemplazar el bloque HOMEWORK con el nuevo (Goldlist como inversion diaria)
    pattern_hw_block = re.compile(
        r'### [☐]?\s*\d+:\d+[–-]\d+:\d+\s*\|\s*HOMEWORK.*?(?=\n### |\n## |\nNotes:|\Z)',
        re.MULTILINE | re.DOTALL | re.IGNORECASE
    )
    text, n_replaced = pattern_hw_block.subn(updated_homework_block(), text, count=1)

    path.write_text(text, encoding='utf-8')
    return f'  Class {class_num}: VATS ({virtue}) + Portfolio Day {day} (Cycle {cycle_num}) + HW updated ({n_replaced} HW replaced)'


def main():
    print('Aplicando VATS + Portfolio Build a B2 Class 3-22...\n')
    for n in range(3, 23):
        print(process_class(n))
    print('\nListo. Ahora corre regen_all_pdfs.py para generar los PDFs.')


if __name__ == '__main__':
    main()
