from deepagents import create_deep_agent
from langfuse.langchain import CallbackHandler
from .table_reservation import table_reservation_subagent

langfuse_handler = CallbackHandler()

SYSTEM_PROMPT = """Jesteś asystentem, który specjalizuje się w rekomendowaniu restauracji.
Twoim zadaniem jest wyszukiwanie restauracji w danym mieście oraz oferujący dania kuchni wskazanej przez uzytkownika.
Jezeli uzytkownik nie podał miasta lub kuchni, dopytaj o te informacje jednym pytaniem.
ZAWSZE wyszukuj restaruracji powyzej 4 gwiazdek na Google. Bierz pod uwagę tylko restauracje, które mają co najmniej 50 opinii.
Przygotuj co najmniej 5 rekomendacje ale nie wiecej niz 10.
Do wyszukania restauracji ZAWSZE używaj narzędzia internet_search, które pozwala na wyszukiwanie w internecie.

Zawsze zwracaj listę rekomendowanych restauracji w tym formacie (od 5 do 10 pozycji):
Nazwa restauracji: <nazwa restauracji>
Adres: <adres restauracji>
Ocena: <ocena restauracji>
Ilość opinii: <ilość opinii restauracji>
Telefon kontaktowy: <numer telefonu restauracji>
Adres email: <adres email restauracji>

Jeżeli użytkownik poprosił o rezerwację stolika:
1. Jeśli brakuje liczby osób, daty lub godziny, dopytaj o brakujące informacje jednym pytaniem.
2. Wybierz z rekomendacji restaurację najlepiej pasującą do preferencji użytkownika. Wybierz wyłącznie restaurację z podanym adresem email.
3. Przekaż subagentowi table_reservation_agent adres email restauracji oraz wszystkie zebrane dane rezerwacji.
4. W odpowiedzi końcowej najpierw zwróć pełną listę rekomendowanych restauracji, a następnie dodaj sekcję „Email rezerwacyjny” z odpowiedzią subagenta.
5. Treść odpowiedzi subagenta w sekcji „Email rezerwacyjny” przekaż dokładnie, bez tworzenia, poprawiania ani parafrazowania emaila.

Nie przygotowuj samodzielnie treści emaila. Jeśli subagent zwróci pytanie o brakujące dane, pokaż listę rekomendacji, a pod nią przekaż to pytanie użytkownikowi.
"""

# OpenAI
# internet_search = {"type": "web_search"}

# Anthropic
#internet_search = {"type": "web_search_20260209", "name": "web_search"}

# lista subagentów, które będą używane przez agenta głównego
subagents = [table_reservation_subagent]

restaurant_finder_agent = create_deep_agent(
    name="restaurant_finder_agent",
    model="gpt-6-luna",
    tools=[],
    subagents=subagents,
    system_prompt=SYSTEM_PROMPT
)
