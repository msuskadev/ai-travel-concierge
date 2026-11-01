# AI Travel Concierge

Instrukcja przygotowania lokalnego środowiska i uruchomienia projektu. Przejdź kolejno przez wszystkie kroki.

## Spis treści

- [Wymagane narzędzia](#wymagane-narzędzia)
- [1. Terminal](#1-terminal)
- [2. Git](#2-git)
- [3. Visual Studio Code](#3-visual-studio-code)
- [4. Python 3.13 lub nowszy](#4-python-313-lub-nowszy)
- [5. uv](#5-uv)
- [6. Docker Desktop](#6-docker-desktop)
- [7. Ollama](#7-ollama)
- [8. Klucz API](#8-klucz-api)
- [9. Sklonuj repozytorium](#9-sklonuj-repozytorium)
- [10. Skonfiguruj plik .env](#10-skonfiguruj-plik-env)
- [11. Zainstaluj zależności i uruchom projekt](#11-zainstaluj-zależności-i-uruchom-projekt)
- [Rozwiązywanie problemów](#rozwiązywanie-problemów)

## Wymagane narzędzia

| Narzędzie | Do czego służy |
|---|---|
| Terminal (Windows: PowerShell) | uruchamianie poleceń |
| Git | pobieranie kodu projektu |
| Visual Studio Code | edytor kodu |
| Python 3.13+ | język, w którym napisano projekt |
| `uv` | zarządzanie wersją Pythona, zależnościami i uruchamianiem projektu |
| Docker Desktop | uruchamianie kontenerów |
| Ollama | uruchamianie modeli AI lokalnie |
| Klucz API (Google Gemini, Anthropic lub OpenAI) | dostęp do modelu AI w chmurze |

---

## 1. Terminal

- **Windows** – użyj **PowerShell**. Wciśnij `Win`, wpisz `PowerShell` i uruchom aplikację *Windows PowerShell* (lub *Terminal*).
- **macOS** – otwórz aplikację **Terminal** (Spotlight: `Cmd + Spacja` → `Terminal`).
- **Linux** – otwórz dowolny emulator terminala (np. `Ctrl + Alt + T`).

Wszystkie polecenia z tej instrukcji wpisuj właśnie tam.

## 2. Git

Pobierz instalator dla swojego systemu ze strony [git-scm.com/downloads](https://git-scm.com/downloads) i zainstaluj z domyślnymi ustawieniami.

Alternatywnie na Windowsie (PowerShell):

```powershell
winget install --id Git.Git -e
```

Na macOS (Homebrew):

```bash
brew install git
```

Sprawdź instalację (po instalacji zamknij i otwórz terminal ponownie):

```bash
git --version
```

## 3. Visual Studio Code

Pobierz i zainstaluj VS Code ze strony [code.visualstudio.com](https://code.visualstudio.com/).

Alternatywnie na Windowsie:

```powershell
winget install --id Microsoft.VisualStudioCode -e
```

Sprawdź instalację:

```bash
code --version
```

Polecenie `code .` otwiera bieżący katalog w VS Code. Jeśli nie jest dostępne, uruchom VS Code z menu aplikacji i wybierz **File → Open Folder...** (na macOS: **File → Open...**).

**Polecane rozszerzenia** (zakładka Extensions, `Ctrl+Shift+X`):

- *Python* (Microsoft)
- *Docker* (Microsoft)

## 4. Python 3.13 lub nowszy

Projekt wymaga Pythona w wersji **3.13 lub nowszej**.

> 💡 Nie musisz instalować Pythona ręcznie – `uv` (krok 5) potrafi sam pobrać odpowiednią wersję. Jeśli jednak wolisz zainstalować go samodzielnie, skorzystaj z poniższych opcji.

- Instalator: [python.org/downloads](https://www.python.org/downloads/)
  **Windows:** podczas instalacji zaznacz opcję **„Add python.exe to PATH”**.
- Windows (PowerShell):

  ```powershell
  winget install --id Python.Python.3.13 -e
  ```

- macOS (Homebrew):

  ```bash
  brew install python@3.13
  ```

Sprawdź instalację:

```bash
python --version
```

Na macOS/Linux może być konieczne użycie `python3 --version`.

## 5. uv

`uv` zarządza wersją Pythona, środowiskiem wirtualnym i zależnościami projektu.

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Po instalacji **zamknij i ponownie otwórz terminal**, a następnie sprawdź:

```bash
uv --version
```

Opcjonalnie – zainstaluj Pythona 3.13 przez `uv`:

```bash
uv python install 3.13
```

## 6. Docker Desktop

1. Pobierz Docker Desktop ze strony [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/) i zainstaluj.
2. **Windows:** instalator zaproponuje użycie **WSL 2** – zostaw tę opcję zaznaczoną. Po instalacji może być wymagany restart komputera.
3. Uruchom Docker Desktop i poczekaj, aż w lewym dolnym rogu pojawi się status **„Engine running”**.

Sprawdź instalację:

```bash
docker --version
docker run hello-world
```

## 7. Ollama

Ollama pozwala uruchamiać modele AI lokalnie na własnym komputerze.

- **Windows / macOS:** pobierz instalator ze strony [ollama.com/download](https://ollama.com/download) i zainstaluj.
- **Windows (PowerShell), alternatywnie:**

  ```powershell
  winget install --id Ollama.Ollama -e
  ```

- **Linux:**

  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

Sprawdź instalację:

```bash
ollama --version
```

Pobierz i przetestuj przykładowy model (np. mały model do szybkich testów):

```bash
ollama pull llama3.2
ollama run llama3.2
```

Aby wyjść z trybu rozmowy, wpisz `/bye`. Lista pobranych modeli:

```bash
ollama list
```

> ⚠️ Modele zajmują kilka GB miejsca na dysku i wymagają odpowiedniej ilości pamięci RAM. Jeśli masz słabszy komputer, wybierz mniejszy model.

## 8. Klucz API

Aby korzystać z modeli w chmurze, potrzebujesz klucza API **jednego** z dostawców:

| Dostawca | Gdzie wygenerować klucz |
|---|---|
| Google Gemini | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) |
| Anthropic | [console.anthropic.com](https://console.anthropic.com/) → *API Keys* |
| OpenAI | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) |

**Ważne:**

- Klucz widoczny jest zwykle tylko raz – skopiuj go od razu w bezpieczne miejsce.
- Nie udostępniaj klucza nikomu i nie wysyłaj go w wiadomościach.
- Nie wrzucaj klucza do repozytorium Git (plik `.env` jest ignorowany przez `.gitignore`).
- Anthropic i OpenAI mogą wymagać doładowania konta (płatności) przed pierwszym użyciem API.

## 9. Sklonuj repozytorium

W terminalu przejdź do katalogu, w którym chcesz trzymać projekty (np. `cd ~/projekty`), a następnie wykonaj:

```bash
git clone https://github.com/msuskadev/ai-travel-concierge.git
cd ai-travel-concierge
```

Otwórz projekt w VS Code:

```bash
code .
```

W katalogu projektu powinny znajdować się m.in. pliki `main.py`, `pyproject.toml`, `uv.lock` oraz `.env.template`.

## 10. Skonfiguruj plik .env

1. Skopiuj szablon pliku konfiguracyjnego:

   **Windows (PowerShell):**

   ```powershell
   Copy-Item .env.template .env
   ```

   **macOS / Linux:**

   ```bash
   cp .env.template .env
   ```

2. Otwórz plik `.env` w VS Code i wpisz swój klucz API. Projekt domyślnie korzysta z Google Gemini:

   ```env
   GOOGLE_API_KEY=wklej_tutaj_swoj_klucz
   ```

   Jeśli używasz innego dostawcy, ustaw odpowiednią zmienną (dokładne nazwy sprawdź w `.env.template`), np.:

   ```env
   ANTHROPIC_API_KEY=wklej_tutaj_swoj_klucz
   OPENAI_API_KEY=wklej_tutaj_swoj_klucz
   ```

Nie dodawaj cudzysłowów wokół klucza.

## 11. Zainstaluj zależności i uruchom projekt

W katalogu projektu uruchom:

```bash
uv sync
```

Polecenie utworzy lokalne środowisko wirtualne `.venv` i zainstaluje wszystkie pakiety z `uv.lock`. Nie musisz ręcznie tworzyć ani aktywować środowiska.

Uruchom aplikację:

```bash
uv run main.py
```

## Rozwiązywanie problemów

- **`git`, `uv`, `code`, `docker` lub `ollama`: command not found** – zamknij i ponownie otwórz terminal (a w ostateczności zrestartuj komputer), aby odświeżyć zmienne środowiskowe `PATH`.
- **PowerShell blokuje uruchamianie skryptów** – uruchom jednorazowo:

  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
  ```

- **Błąd wersji Pythona** – zainstaluj wymaganą wersję przez `uv python install 3.13` i ponów `uv sync`.
- **Błąd klucza API** – sprawdź, czy plik `.env` znajduje się w tym samym katalogu co `main.py`, czy nazwa zmiennej jest poprawna i czy klucz nie zawiera spacji ani cudzysłowów.
- **Docker: „Cannot connect to the Docker daemon”** – upewnij się, że Docker Desktop jest uruchomiony (status *Engine running*).
- **Docker na Windowsie nie startuje** – włącz wirtualizację w BIOS/UEFI oraz zainstaluj/aktualizuj WSL 2 poleceniem `wsl --install` (PowerShell jako administrator).
- **Ollama: „connection refused”** – uruchom aplikację Ollama lub wykonaj `ollama serve` w osobnym oknie terminala.
- **Błąd modelu lub dostępu do API** – sprawdź połączenie z internetem, saldo/limity konta oraz to, czy wybrany model jest dostępny dla Twojego klucza.