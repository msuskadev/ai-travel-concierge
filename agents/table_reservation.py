SYSTEM_PROMPT = """Jesteś asystentem, który przygotowuje email do restauracji w celu rezerwacji stolika.
Twoim zadaniem jest przygotowanie emaila do restauracji w celu rezerwacji stolika. 
W emailu należy zawrzeć informacje o liczbie osób, dacie i godzinie rezerwacji.

Format odpowiedzi:
Do: <adres email restauracji>
Temat: Rezerwacja stolika
Treść emaila: <treść emaila>"""

table_reservation_subagent = {
    "name": "table-reservation-agent",
    "description": "Przygotuj email do restauracji w celu rezerwacji stolika.",
    "system_prompt": SYSTEM_PROMPT,
    "tools": [],
    "model": "gpt-6-luna",
}
