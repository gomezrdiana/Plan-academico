#!/usr/bin/env python3
"""Genera los 9 PDFs para la VIP HOTEL ACTIVITY de B1 Cl 11 Grammar:
- 8 role cards individuales (uno por estudiante segun rol asignado)
- 1 Common Resource Pack (vocab + expressions + grammar reminder) que TODOS reciben.

Diana envia estos digital a los estudiantes ANTES de la clase."""
import os
from gen_a1_a2_clases_pdfs import md_to_pdf

D = os.path.dirname(os.path.abspath(__file__))
CARDS_DIR = os.path.join(D, 'B1', 'vip_hotel_cards')

cards = [
    'B1_VIP_HOTEL_Card_01_FrontDeskAgent',
    'B1_VIP_HOTEL_Card_02_ReservationsManager',
    'B1_VIP_HOTEL_Card_03_Chef',
    'B1_VIP_HOTEL_Card_04_FacilitiesManager',
    'B1_VIP_HOTEL_Card_05_Concierge',
    'B1_VIP_HOTEL_Card_06_DutyManager',
    'B1_VIP_HOTEL_Card_07_HousekeepingSupervisor',
    'B1_VIP_HOTEL_Card_08_RoomServiceServer',
    'B1_VIP_HOTEL_Common_VocabExpressions',
]

for name in cards:
    md_to_pdf(
        os.path.join(CARDS_DIR, f'{name}.md'),
        os.path.join(CARDS_DIR, f'{name}.pdf'),
    )

print(f'\n{len(cards)} PDFs generados en B1/vip_hotel_cards/:')
for name in cards:
    print(f'  - {name}.pdf')
