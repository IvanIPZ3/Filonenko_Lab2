# ЛР2 — Контейнеризація Python-додатків (Filonenko Ivan)

## 1) Локальне віртуальне оточення (Python ≥ 3.13.1)

**Windows (PowerShell):**
```powershell
py -3.13 -m venv filonenko
.\filonenko\Scripts\Activate.ps1
python --version
pip install -r requirements.txt
```

**Linux/macOS:**
```bash
python3.13 -m venv filonenko
source filonenko/bin/activate
python --version
pip install -r requirements.txt
```

Запуск програми (у віртуальному середовищі):
```bash
python -m src.translator_cli
```

Приклад для звіту:
```text
Введіть текст для перекладу: Доброго дня. Як справи?
На яку мову перекласти (код або назва): en

--- Результати ---
Detected(lang=uk, confidence=1)
Good day. How are you?
English
en
```

Вивід пакетів:
```bash
pip list
```

## 2) Docker (Linux + Python 3.12 + googletrans==3.1.0a0)

Файли у папці `docker/`:

- `Dockerfile`
- `requirements.txt` (під контейнер)

### Збірка образу
```bash
cd docker
docker build -t filonenko_ia:1.0 .
docker images
```

### Запуск контейнера
```bash
docker run --name filonenko_ia -it filonenko_ia:1.0
```

Всередині контейнера:
```bash
python --version
cat /etc/os-release
pip list
ls -la /Filonenko
python /Filonenko/app.py
```

Перевірка образів та контейнерів для скріншотів:
```bash
docker images
docker ps -a
```

## 3) Структура проєкту
```text
Filonenko_Lab2_Python_Docker/
├─ .gitignore
├─ README.md
├─ requirements.txt            # для локального оточення (googletrans==4.0.0rc1)
├─ src/
│  ├─ translator_lib.py
│  └─ translator_cli.py
├─ docker/
│  ├─ Dockerfile
│  └─ requirements.txt         # для контейнера (googletrans==3.1.0a0)
└─ report/
   └─ report_template.docx     # шаблон звіту
```

## 4) GitHub
1. Створіть репозиторій, наприклад `Filonenko_Lab2`.
2. Додайте все, окрім віртуального середовища — `.gitignore` вже готовий.
3. Зробіть скріншоти за чеклістом і додайте у звіт.

## 5) Чекліст скріншотів для звіту
- VSCode з відкритим `translator_cli.py` або `translator_lib.py` (п.2).
- `python --version` у **активованому** віртуальному середовищі (п.1).
- `pip list` у віртуальному середовищі (п.1).
- Результати роботи програми (п.2).
- Docker Desktop: список **Images** і **Containers** з вашими назвами.
- `docker images` і `docker ps -a` у терміналі.
- Всередині контейнера: `cat /etc/os-release` і `python --version`.
- Всередині контейнера: `pip list`.
- Всередині контейнера: вивід файлової структури, де є `/Filonenko`.
- Всередині контейнера: запуск програми та вивід результатів (п.5–6).
```

## 6) Примітки
- У локальному середовищі використовується `googletrans==4.0.0rc1` (краще працює на нових Python).
- У контейнері згідно завдання — `googletrans==3.1.0a0`.
- Якщо сервіс перекладу тимчасово недоступний, функції повертають повідомлення про помилку — цього достатньо для демонстрації обробки винятків у звіті.
