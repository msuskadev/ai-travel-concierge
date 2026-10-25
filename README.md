# AI Restaurant Agent

Prosty agent AI oparty na Gemini i bibliotece Deep Agents. Poniższa instrukcja przeprowadzi Cię przez przygotowanie lokalnego środowiska i uruchomienie aplikacji.

## Wymagane narzędzia

- Git — do pobrania kodu projektu
- Visual Studio Code (VS Code) — edytor kodu
- Python 3.13 lub nowszy
- `uv` — do zarządzania wersją Pythona, zależnościami i uruchamianiem projektu
- Klucz API Google Gemini
- Terminal (na Windowsie: PowerShell)

Docker Desktop jest opcjonalny. Projekt nie zawiera obecnie konfiguracji Dockera, więc nie jest potrzebny do uruchomienia aplikacji.

## 1. Zainstaluj Git

Pobierz instalator dla swojego systemu z [git-scm.com](https://git-scm.com/downloads) i zainstaluj go z domyślnymi ustawieniami. Sprawdź instalację w terminalu:

```bash
git --version
```

## 2. Zainstaluj Visual Studio Code

Pobierz i zainstaluj VS Code z [code.visualstudio.com](https://code.visualstudio.com/). Po instalacji możesz otworzyć katalog projektu w VS Code poleceniem:

```bash
code .
```

Jeśli polecenie `code` nie jest dostępne, uruchom VS Code z menu aplikacji i wybierz **File → Open Folder...** (na macOS: **File → Open...**), a następnie wskaż katalog projektu.

## 3. Zainstaluj Docker Desktop

Jeśli chcesz mieć Dockera gotowego do przyszłej pracy z kontenerami, pobierz [Docker Desktop](https://www.docker.com/products/docker-desktop/) dla swojego systemu i zainstaluj zgodnie z instrukcjami instalatora. Uruchom Docker Desktop po instalacji. Aplikacja z tego repozytorium nie wymaga Dockera.

## 4. Zainstaluj `uv`

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

## 5. Pobierz i otwórz projekt

Jeśli projekt nie znajduje się jeszcze na komputerze, sklonuj repozytorium Git, podając jego adres:

```bash
git clone ADRES_REPOZYTORIUM
cd ai-travel-concierge
```

Zamień `ADRES_REPOZYTORIUM` na adres Git projektu. Jeśli masz już projekt, przejdź w terminalu do jego katalogu:

```bash
cd ścieżka/do/ai-travel-concierge
```

W katalogu powinny znajdować się pliki `pyproject.toml` i `uv.lock`. Możesz otworzyć go w VS Code poleceniem:

```bash
code .
```

## 6. Skonfiguruj klucz API Google

Utwórz w głównym katalogu projektu plik o nazwie `.env`. Skopiuj do niego poniższą linię i wstaw swój klucz API uzyskany w Google AI Studio:

```dotenv
GOOGLE_API_KEY=wklej_tutaj_swoj_klucz
```

Nie dodawaj cudzysłowów wokół klucza. Nie udostępniaj pliku `.env` ani nie wysyłaj klucza w wiadomościach. Plik `.env` jest ignorowany przez Git.

## 7. Zainstaluj zależności projektu

W katalogu projektu uruchom:

```bash
uv sync
```

Polecenie utworzy lokalne środowisko wirtualne `.venv` i zainstaluje pakiety zapisane w `uv.lock`. Nie musisz ręcznie tworzyć ani aktywować środowiska.

## 8. Uruchom aplikację

```bash
uv run main.py
```

Przy pierwszym uruchomieniu `uv` użyje środowiska projektu. W terminalu powinien pojawić się tekst wygenerowany przez agenta.

## Rozwiązywanie problemów

- **`uv: command not found`** — zamknij i otwórz ponownie terminal. Jeśli problem pozostaje, sprawdź, czy instalacja `uv` zakończyła się poprawnie.
- **Błąd dotyczący klucza API** — sprawdź, czy plik `.env` znajduje się obok `main.py`, a zmienna ma nazwę `GOOGLE_API_KEY`.
- **Błąd wersji Pythona** — projekt wymaga Pythona 3.13 lub nowszego. `uv` może zainstalować odpowiednią wersję poleceniem `uv python install 3.13`, a następnie ponów `uv sync`.
- **Błąd modelu lub dostępu do Gemini** — sprawdź połączenie z internetem oraz dostępność modelu dla Twojego klucza API.
