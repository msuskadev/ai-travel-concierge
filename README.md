# AI Restaurant Agent

Prosty agent AI oparty na Gemini i bibliotece Deep Agents. Poniższa instrukcja przeprowadzi Cię przez przygotowanie lokalnego środowiska i uruchomienie aplikacji.

## Wymagania

- Python w wersji 3.13 lub nowszej
- `uv` do instalowania Pythona, zarządzania zależnościami i uruchamiania projektu
- Klucz API Google Gemini
- Terminal (na Windowsie: PowerShell)

## 1. Zainstaluj `uv`

Jeśli nie masz jeszcze `uv`, zainstaluj go:

**macOS / Linux**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell)**

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

Po instalacji zamknij i ponownie otwórz terminal, a następnie sprawdź, czy `uv` działa:

```bash
uv --version
```

## 2. Otwórz katalog projektu

W terminalu przejdź do katalogu, w którym znajduje się ten projekt. Przykładowo:

```bash
cd ścieżka/do/ai-travel-concierge
```

W tym katalogu powinny znajdować się pliki `pyproject.toml` i `uv.lock`.

## 3. Skonfiguruj klucz API Google

Utwórz w głównym katalogu projektu plik o nazwie `.env`. Skopiuj do niego poniższą linię i wstaw swój klucz API uzyskany w Google AI Studio:

```dotenv
GOOGLE_API_KEY=wklej_tutaj_swoj_klucz
```

Nie dodawaj cudzysłowów wokół klucza. Nie udostępniaj pliku `.env` ani nie wysyłaj klucza w wiadomościach. Plik `.env` jest ignorowany przez Git.

## 4. Zainstaluj zależności projektu

W katalogu projektu uruchom:

```bash
uv sync
```

Polecenie utworzy lokalne środowisko wirtualne `.venv` i zainstaluje pakiety zapisane w `uv.lock`. Nie musisz ręcznie tworzyć ani aktywować środowiska.

## 5. Uruchom aplikację

```bash
uv run main.py
```

Przy pierwszym uruchomieniu `uv` użyje środowiska projektu. W terminalu powinien pojawić się tekst wygenerowany przez agenta.

## Rozwiązywanie problemów

- **`uv: command not found`** — zamknij i otwórz ponownie terminal. Jeśli problem pozostaje, sprawdź, czy instalacja `uv` zakończyła się poprawnie.
- **Błąd dotyczący klucza API** — sprawdź, czy plik `.env` znajduje się obok `main.py`, a zmienna ma nazwę `GOOGLE_API_KEY`.
- **Błąd wersji Pythona** — projekt wymaga Pythona 3.13 lub nowszego. `uv` może zainstalować odpowiednią wersję poleceniem `uv python install 3.13`, a następnie ponów `uv sync`.
- **Błąd modelu lub dostępu do Gemini** — sprawdź połączenie z internetem oraz dostępność modelu dla Twojego klucza API.
