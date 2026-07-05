#!/usr/bin/env python3
import os as _hos, sys as _hsys
_hsys.path.insert(0, _hos.path.dirname(_hos.path.dirname(_hos.path.abspath(__file__))))
"""
Actualiza la virtud en cada PRINT.md de A1 y A2 segun el modelo nuevo:
- Virtud por NUMERO DE CLASE (no por calendario)
- A1 nocturno (3 clases/sem): bloques de 3 clases por virtud
- A2 nocturno (3 clases/sem asumido): bloques de 3 clases por virtud
- A2 4h intensivo (5 clases/sem): bloques de 5 clases por virtud

Reemplaza solo la cabecera VATS y el bloque pregunta. Conserva la estructura V/A/T/S
y las notas finales (puede haber inconsistencia con el contenido viejo, pero la
virtud del header es la canonica).
"""
import os, re

VIRTUES = ['PRUDENCIA', 'TEMPLANZA', 'JUSTICIA', 'FORTALEZA']

VIRTUE_DEFINITIONS = {
    'PRUDENCIA': 'planificar bien, pensar antes de actuar, decisiones inteligentes',
    'TEMPLANZA': 'autocontrol, equilibrio, moderacion',
    'JUSTICIA': 'equidad, trabajo en equipo, empatia, gratitud',
    'FORTALEZA': 'coraje, resistencia, no rendirse',
}

VIRTUE_QUESTIONS = {
    'PRUDENCIA': [
        '"Es mas prudente practicar 30 min cada dia, o 3 horas un solo dia?"',
        '"Que es una decision PRUDENTE que tomaste el ano pasado?"',
        '"Si tuvieras que ahorrar para una meta, como lo harias?"',
        '"Cuando es prudente decir NO?"',
        '"Que decision estas evitando que deberias enfrentar?"',
    ],
    'TEMPLANZA': [
        '"En que area de tu vida tienes mas autocontrol? Y menos?"',
        '"Cuando fue la ultima vez que te excediste?"',
        '"Es mejor decir mucho o decir poco?"',
        '"Que actividad te controla a ti? Que actividad controlas tu?"',
        '"Como mantienes la calma cuando algo te molesta?"',
    ],
    'JUSTICIA': [
        '"Quien en tu vida merece un gracias que no le has dado?"',
        '"Cuando trabajaste bien en equipo? Cuando mal?"',
        '"Como tratas a alguien que tiene menos que tu?"',
        '"Que es lo mas justo que has hecho?"',
        '"Que injusticia has visto y no has dicho nada?"',
    ],
    'FORTALEZA': [
        '"Cual es la cosa mas dificil que has hecho?"',
        '"Cuando fue la ultima vez que querias rendirte y no lo hiciste?"',
        '"Que te da miedo y como lo enfrentas?"',
        '"Si alguien te critica, como respondes?"',
        '"Que cambio dificil estas evitando?"',
    ],
}

def get_virtue(class_num, classes_per_block):
    """Calcula la virtud y vuelta segun el numero de clase."""
    block = (class_num - 1) // classes_per_block + 1
    virtue_idx = (block - 1) % 4
    cycle_num = (block - 1) // 4 + 1
    virtue = VIRTUES[virtue_idx]
    if cycle_num == 1:
        return virtue, virtue, 1
    else:
        return virtue, f'{virtue} v{cycle_num}', cycle_num

def get_question_for_class(class_num, virtue, classes_per_block):
    """Rota entre las 5 preguntas segun la posicion en el bloque."""
    pos_in_block = (class_num - 1) % classes_per_block
    questions = VIRTUE_QUESTIONS[virtue]
    return questions[pos_in_block % len(questions)]


def build_vats_a1_style(class_num, virtue, virtue_label, question):
    """Bloque VATS para guias A1 (estilo nocturno con horario 00:00-00:05)."""
    return f"""### ☐ 00:00–00:05 | VATS: VIRTUD DE LA CLASE — {virtue_label} (5 min)

**Virtud de esta clase: {virtue_label} ({VIRTUE_DEFINITIONS[virtue]})**

Escribe en el tablero:
```
{virtue_label} — {question}
```

Di: "Esta clase trabajamos {virtue_label}. Pregunten en parejas. Pueden mezclar espanol e ingles, pero traten de decir AL MENOS UNA frase en ingles."

**V (1 min):** Lee la pregunta. Senala el tablero.
**A (30 seg):** Di: "Piensen en silencio."
**T (2 min):** Di: "Parejas. Discutan. Al menos UNA frase en ingles."
**S (1.5 min):** 2 estudiantes comparten. Celebra cualquier intento en ingles.

> Virtud asignada por modelo de rotacion por numero de clase. Si necesitas cambiar la pregunta, usa una de las 5 estandar de CALENDARIO_VIRTUDES_2026.md."""


def build_vats_a2_4h_style(class_num, virtue, virtue_label, question):
    """Bloque VATS para guias A2 4h (estilo intensivo con horario 8:00-8:05)."""
    return f"""### 1. 8:00-8:05 | VATS: VIRTUD DE LA CLASE -- {virtue_label} (5 min)

**Virtud de esta clase: {virtue_label} ({VIRTUE_DEFINITIONS[virtue]})**

Escribe en el tablero:
```
{virtue_label} -- {question}
```

**V -- Virtud (1 min).** Senala el tablero. Lee la pregunta. Di: "Esta clase trabajamos {virtue_label}."

**A -- Activar (30 seg).** Di: "30 segundos. Piensen en silencio."

**T -- Talk en parejas (2 min).** Di: "Parejas. Cuentense en ingles -- usen lo que saben. Pueden mezclar palabras en espanol."

**S -- Share (1.5 min).** Di: "Quien quiere compartir?" 2 estudiantes comparten.

> Virtud asignada por modelo de rotacion por numero de clase."""


def replace_vats_block(content, new_vats_block, file_marker='nocturno'):
    """Reemplaza el bloque VATS existente con el nuevo. Detecta el patron del bloque viejo."""
    if file_marker == 'nocturno':
        # A1/A2 nocturno: empieza con "### ☐" o "### " + horario + VATS
        # Termina antes de "### " del siguiente bloque o "## " seccion
        pattern = re.compile(
            r'### ☐ 00:00.{1,3}00:05 \| VATS:.*?(?=### ☐ 00:05|### ☐ 00:00|---\n)',
            re.DOTALL
        )
    else:  # intensivo 4h
        # A2 4h: empieza con "### 1. 8:00-8:05" + VATS
        # Termina antes de "### 2." o similar
        pattern = re.compile(
            r'### 1\. 8:00-8:05 \| VATS:.*?(?=### 2\.)',
            re.DOTALL
        )

    match = pattern.search(content)
    if match:
        return content.replace(match.group(0), new_vats_block + '\n\n')
    return None  # No se encontro el patron


def process_file(filepath):
    """Procesa un archivo PRINT.md, actualiza la virtud."""
    filename = os.path.basename(filepath)

    # Determinar tipo y clase
    is_a1 = filename.startswith('A1_Class')
    is_a2_nocturno = filename.startswith('A2_Class')
    is_a2_4h = filename.startswith('A2_4h_Class')

    # Extraer numero de clase
    m = re.search(r'Class(\d+)_PRINT\.md$', filename)
    if not m:
        return f'SKIP {filename} (no class number)'
    class_num = int(m.group(1))

    # Determinar bloque y estilo
    # Todos los cohortes son Lu-Vi (5 dias/semana) -> bloques de 5 clases por virtud
    if is_a2_4h:
        classes_per_block = 5
        style = 'intensivo'
        builder = build_vats_a2_4h_style
    elif is_a1 or is_a2_nocturno:
        classes_per_block = 5  # actualizado: A1 y A2 nocturno son Lu-Vi tambien
        style = 'nocturno'
        builder = build_vats_a1_style
    else:
        return f'SKIP {filename} (unknown type)'

    # Calcular virtud
    virtue_base, virtue_label, cycle = get_virtue(class_num, classes_per_block)
    question = get_question_for_class(class_num, virtue_base, classes_per_block)

    # Construir nuevo bloque VATS
    new_vats = builder(class_num, virtue_base, virtue_label, question)

    # Leer archivo
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Reemplazar bloque VATS
    new_content = replace_vats_block(content, new_vats, file_marker=style)
    if new_content is None:
        return f'WARN {filename} (VATS pattern not found, manual check)'

    # Guardar
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return f'OK {filename} -> {virtue_label} (clase {class_num}, bloque de {classes_per_block})'


if __name__ == '__main__':
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    targets = []
    a1_dir = os.path.join(base, 'A1')
    a2_dir = os.path.join(base, 'A2')

    if os.path.isdir(a1_dir):
        for f in os.listdir(a1_dir):
            if f.startswith('A1_Class') and f.endswith('_PRINT.md'):
                targets.append(os.path.join(a1_dir, f))

    if os.path.isdir(a2_dir):
        for f in os.listdir(a2_dir):
            if (f.startswith('A2_Class') or f.startswith('A2_4h_Class')) and f.endswith('_PRINT.md'):
                targets.append(os.path.join(a2_dir, f))

    print(f'Processing {len(targets)} files...')
    for f in sorted(targets):
        result = process_file(f)
        print(result)
