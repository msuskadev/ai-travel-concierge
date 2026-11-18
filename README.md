# AI Travel Concierge

Aplikacja Streamlit pomaga przygotować plan zwiedzania miasta.

## Wymagania

- Git
- Python 3.13 lub nowszy
- [uv](https://docs.astral.sh/uv/getting-started/installation/) do instalowania zależności i obsługi środowiska
- Klucz API do dostawcy modelu skonfigurowanego w aplikacji

## Pobranie projektu

W terminalu wykonaj:

```bash
git clone https://github.com/msuskadev/ai-travel-concierge.git
cd ai-travel-concierge
git switch wyklad-02
```

Sprawdź, czy jesteś na właściwym branchu:

```bash
git branch --show-current
```

Wynik powinien być `wyklad-02`.

## Instalacja zależności i środowisko wirtualne

W katalogu projektu uruchom:

```bash
uv sync
```

Polecenie utworzy środowisko `.venv` i zainstaluje zależności zapisane w `uv.lock`. Aktywuj środowisko:

```bash
source .venv/bin/activate
```

W terminalu powinien pojawić się prefiks `(.venv)`. Aktywacja jest opcjonalna, jeśli uruchamiasz aplikację przez `uv run`.

## Konfiguracja klucza API

Utwórz plik `.env` z szablonu:

```bash
cp .env_template .env
```

Otwórz `.env` i wklej swój klucz po znaku `=`. Nie dodawaj cudzysłowów ani spacji, na przykład:

```dotenv
GOOGLE_API_KEY=twój_klucz
```

Klucze uzyskasz po założeniu konta u wybranego dostawcy: [OpenAI](https://platform.openai.com/api-keys), [Anthropic](https://console.anthropic.com/settings/keys) lub [Google AI Studio](https://aistudio.google.com/apikey). Google AI Studio udostępnia bezpłatny limit dla wybranych modeli; sprawdź aktualne limity i warunki na swoim koncie.

## Uruchomienie

W katalogu projektu, przy aktywnym środowisku wirtualnym, uruchom:

```bash
streamlit run main.py
```

Możesz też uruchomić aplikację bez aktywowania środowiska:

```bash
uv run streamlit run main.py
```

Streamlit wypisze lokalny adres aplikacji, zwykle `http://localhost:8501`, i otworzy go w przeglądarce. Wpisz miasto w polu wiadomości, aby sprawdzić działanie planera. Do odpowiedzi modelu potrzebne jest poprawne API key oraz dostępny limit u dostawcy.

Zatrzymaj serwer skrótem `Ctrl+C` w terminalu.
