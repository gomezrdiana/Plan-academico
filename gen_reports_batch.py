#!/usr/bin/env python3
"""Generate batch reports for classes 10-14 A1/A2, A2 4h 2-5, B2 19-22."""
import os
from generate_pdfs import get_styles, build_report

S = get_styles()
D = os.path.dirname(os.path.abspath(__file__))

std_deliv = [
    'Hojas de autochequeo completadas',
    'Papel de errores (entregado fisico con la guia)',
    'Tarea enviada al grupo de WhatsApp (copia exacta)',
    'Contenido para redes sociales (si se grabo)',
]
b2_deliv = [
    'Error paper (photographed + sent to coordination)',
    'Self-check sheets completed',
    'Homework sent to WhatsApp group (exact copy)',
    'Social media content (if recorded)',
]
def std_eval(v):
    return ['Los estudiantes hablaron 80%+ del tiempo','Hable menos de 20 min en total','Fui guia, no conferencista','Camine con papel de errores (min 5 errores)','Mi celular estaba boca abajo',f'Hice el ritual VATS ({v})','Libro y ejercicios NO se pasaron de tiempo','Grabe contenido para redes sociales','Envie entregables a coordinacion','Envie la tarea al grupo de WhatsApp']
b2_eval = ['Students spoke 80%+ of the time','I spoke less than 20 min total','I was a guide, not a lecturer','I walked with error paper (min 5 errors written)','My phone was face-down','I recorded social media content','I sent deliverables to coordination','I sent homework to WhatsApp group']

def sa(items):
    return [(a, m+' min') for a, m in items]

std_2h = [('VATS','5'),('Analizo','8'),('Libro','15'),('Ejercicios','10'),('Simulacion','20'),('Shadowing','10'),('Historia','10'),('Competencia','10'),('Juego','7'),('GoldList','10'),('Autochequeo','3'),('Tarea+Cierre','2')]

# A1 2h Classes 10-14
for c, m, v in [(10,'M10: Past Simple Did','Fortaleza'),(11,'M11: Irregular Verbs Past','Fortaleza'),(12,'M12: How Often - Adverbs','Templanza'),(13,'M13: Twice a Week','Templanza'),(14,'M14: Who Do You Study With','Templanza')]:
    build_report(os.path.join(D,'A1',f'A1_Clase{c}_REPORTE.pdf'), f'A1 | Clase {c} de 45', m, sa(std_2h), std_deliv, std_eval(v), S)
    print(f'OK: A1_Clase{c}_REPORTE.pdf')

# A2 2h Classes 10-14
for c, m, v in [(10,'M12: Past Continuous','Fortaleza'),(11,'M13: Already/Still/Until','Fortaleza'),(12,'M14: While/During/Again','Templanza'),(13,'M15: Present Perfect Regular','Templanza'),(14,'M16: Present Perfect Irregular','Templanza')]:
    build_report(os.path.join(D,'A2',f'A2_Clase{c}_REPORTE.pdf'), f'A2 | Clase {c} de 55', m, sa(std_2h), std_deliv, std_eval(v), S)
    print(f'OK: A2_Clase{c}_REPORTE.pdf')

# A2 4h Classes 2-5
a2_4h_acts = [('VATS','5'),('Rompehielo','10'),('Libro Mod A','15'),('Ejercicios Mod A','10'),('Simulacion Mod A','20'),('Shadowing','10'),('Competencia Mod A','10'),('GoldList #1','10'),('Transicion','10'),('BREAK','20'),('Rompehielo Mod B','10'),('Libro Mod B','15'),('Ejercicios Mod B','10'),('Simulacion Mod B','15'),('Competencia Mod B','10'),('GoldList #2','10'),('Autochequeo','5'),('Tarea+Cierre','5')]
for c, m, v in [(2,'M3+M5: Ordinales + 3 Futuros','Templanza'),(3,'M6+M7: Scheduled + Might','Justicia'),(4,'M8+M10: That + First Conditional','Justicia'),(5,'M11+M12: Second Cond + Past Continuous','Fortaleza')]:
    build_report(os.path.join(D,'A2',f'A2_4h_Clase{c}_REPORTE.pdf'), f'A2 INTENSIVO | Clase {c}', m, sa(a2_4h_acts), std_deliv, std_eval(v), S)
    print(f'OK: A2_4h_Clase{c}_REPORTE.pdf')

# B2 4h Classes 19-22
b2_data = [
    (19, 'Blending Review M1-12 + Project', [('Icebreaker','20'),('Homework Review','15'),('Station Rotation','40'),('BREAK','20'),('Structured Conversation','30'),('Correct the Teacher','25'),('Project Workshop','25'),('Self-check+HW+Close','10')]),
    (20, 'Exam Prep + Project', [('Icebreaker','15'),('Homework Review','15'),('Exam Review Rapid-fire','30'),('Practice Exam Mock','30'),('BREAK','20'),('Hot Seat','30'),('Debate','20'),('Project Workshop','25'),('Self-check+HW+Close','10')]),
    (21, 'Presentation Rehearsal', [('Icebreaker','15'),('Homework Review','10'),('Mock Presentations','90'),('BREAK','20'),('Correct the Teacher','25'),('Group Feedback','20'),('Project Workshop','25'),('Self-check+HW+Close','10')]),
    (22, 'Final Review + Last Polish', [('Icebreaker','15'),('Homework Review','10'),('Exam Prep Practice','30'),('The Interview','30'),('BREAK','20'),('Mock Presentations R2','60'),('Final Project Polish','25'),('Self-check+HW+Close','10')]),
]
for c, m, acts in b2_data:
    build_report(os.path.join(D,'B2',f'B2_Clase{c}_REPORTE.pdf'), f'B2 | Class {c} of 50', m, sa(acts), b2_deliv, b2_eval, S)
    print(f'OK: B2_Clase{c}_REPORTE.pdf')

print('\nAll 18 reports generated.')
