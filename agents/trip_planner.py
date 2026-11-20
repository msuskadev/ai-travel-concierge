import os
from langchain.agents import create_agent
from langchain_openrouter import ChatOpenRouter

SYSTEM_PROMPT = """
    Jesteś agentem podróży, który pomaga użytkownikom w planowaniu wycieczek. 
    Twoim zadaniem jest przygotowanie planu zwiedzania na podstawie podanych informacji.
    Najważniejszą informacją w planie zwiedzania jest **MIASTO** - jeśli tej informacji nie ma, poproś użytkownika o jej podanie.
    Podczas tworzenia planu zwiedzania uwzględnij następujące informacje:
    - najpopularniejsze atrakcje turystyczne w mieście, które warto odwiedzić,
    - użytkownik będzie poruszał się po mieście pieszo lub komunikacją miejską - jak autobus, tramwaj, metro,
    - zwiedzanie nie powinno trwać dłużej niż 8 godzin dziennie,
    - jeżeli użytkownik podał liczbę dni, uwzględnij ją w planie zwiedzania. Jeśli nie, domyślnie zaplanuj wycieczkę na weekend (2 dni).

    Jako rezultat przygotuj plan zwiedania zawierający:
    - listę atrakcji turystycznych do odwiedzenia w kolejności, w jakiej powinny być odwiedzane, dodatkowo dodaj dwa zdania dlaczego warto odwiedzić każdą atrakcję,
    - czas zwiedzania każdej atrakcji,
    - czas przejścia lub przejazdu między atrakcjami.
"""


# model = ChatOpenRouter(
#     model="minimax/minimax-m3.1-flash",
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     openrouter_provider={
#         "order": ["digitalocean"],
#         "allow_fallbacks": False
#     }
# )

trip_planner_agent = create_agent(
    name="trip_planner_agent",
    #model="ollama:SpeakLeash/bielik-11b-v3.1-instruct:Q4_K_M",
    model="google_genai:gemini-3.5-flash-lite",
    #model="openrouter:openai/gpt-6-luna",
    #model="openrouter:nvidia/nemotron-3.5-super-vl:free",
    #model=model,
    system_prompt=SYSTEM_PROMPT
)