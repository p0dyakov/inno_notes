# agents.md — воркфлоу автоматизации inno_files → inno_notes

Этот файл — карта автоматизации для агентов и людей. Полный цикл работает
**без участия человека**: от файлов в Moodle до опубликованного сайта.

Два репозитория:

- `inno_files` — сырьё: PDF/презентации с Moodle + сгенерированные `.md`-транскрипты.
- `inno_notes` — этот репозиторий: Quarto-сайт (статьи `.qmd`), публикуется на `innonotes.ru` (gh-pages).

---

## 1. Полная последовательность (шаги 1–7)

### Шаг 1. Windows забирает файлы с Moodle

Машина `clovet-windows`, папка `C:\Users\usful\inno_files`.
Планировщик Windows: задача **`InnoFilesMoodleSync`** — каждый час + при старте/логине
(`inno_files/scripts/moodle_sync/deploy/install_task.ps1`).

Каждый запуск (`deploy/run_sync.ps1`, идемпотентный, с mutex от параллельных запусков):

1. `setup_routes.ps1` — обходные маршруты к Moodle (best-effort, не роняет прогон);
2. `git pull --rebase --autostash` (GitHub ходит через SOTA VPN, тоже best-effort);
3. проверка venv и зависимостей (`requirements.txt`: httpx, bs4, pymupdf…);
4. `sync.py --config config.json`:
   - проверка логина в Moodle, при протухших куках — **автообновление через SSO (ADFS)**
     (`moodle_auth.py`, `cookies.json`; `credentials.json` — только если SSO не справился);
   - скачивание новых ресурсов (`state.json` — идемпотентность, повтор не качает);
   - переименование по правилам (`renamer.py`: имя файла + первая страница PDF,
     маппинг курсов — `config.json → course_name_map`);
   - `.ppt/.pptx → .pdf` (`office_convert.py`: PowerShell/LibreOffice);
   - транскрипты: для новых PDF + backfill пропущенных — Gemini
     (повторная генерация не делается);
   - транскрибируется ВСЁ входящее (`gemini_transcript.py`, Pro-модель `gemini-3.1-pro-preview`,
     ключ `gemini_api_key` из env/config, состояние — `transcript_state.json`); скип-лист
     `transcript_skip_semesters` держит только уже обработанные семестры (сейчас
     semester-1/2/3 — по ним есть статьи; semester-4 и будущие идут полностью),
     плюс только учебные файлы
     (лекции/лабы/туториалы/главы; скип по `skip_filename_patterns`: solution, рпд…);
5. коммит + `git push` с 3 попытками (`auto_commit`/`auto_push` в `config.json`,
   включается через `deploy/enable_autopush.ps1`);
6. маркер `logs/last_run.json` для health-check.

Разовая настройка Windows: `setup_windows.ps1` (клонирует репо, чинит venv/таск/маршруты/гит),
`setup_git.ps1` + `auth_github.ps1` (gh CLI), `update_config.ps1`.

### Шаг 2. Пуш в гит

`inno_files`, ветка `main`. Исходники PDF + готовые `Lecture.md / Tutorial.md` рядом
(пример: `semester-4/OS/1/Lecture.pdf` + `Lecture.md`).

### Шаг 3. Триггер в inno_notes

`.github/workflows/trigger-notes.yml` в `inno_files`: срабатывает на пуш в `main`
по путям `semester-4/**/*.md` и шлёт `repository_dispatch` (`inno-files-update`, sha + файлы)
в `inno_notes` через секрет `NOTES_PAT`. Никакого поллинга — event-driven.

### Шаг 4. Генерация статей (CI-агент inno_notes)

`.github/workflows/agent.yml` (`agent-generate-semester4`, concurrency без отмены):

1. чекаут `inno_notes`, клонирование `inno_files` на присланный sha (`INNO_FILES_PAT`);
2. `python3 scripts/agent/generate.py --inno-files /tmp/inno_files --sha …`:
   - только управляемые семестры (есть `<semester>/course_map.json`; semester-1/2/3 заморожены);
   - только изменившиеся транскрипты; ранний выход, если менять нечего;
   - статьи пишутся посекционно **параллельно**, каждая контентная секция — Pro-моделью (`gemini-3.1-pro-preview`), flash только для мелочей и автофиксов,
     контекст стиля — из соседних статей папки;
   - цикл до 3 попыток: `fix_formatting.py` + `renumber_examples.py` + рендер одного файла,
     ошибки скармливаются обратно модели; упавший черновик удаляется/откатывается —
     **битые статьи никогда не пушатся**;
   - в конце `update_sidebar()` дописывает новые файлы в `_quarto.yml`;
3. коммит `semester-4/ + index.qmd + _quarto.yml` в `main` от `inno-notes-agent`.

Формат статей — жёсткий: `prompt.md` (структура Theory/Definitions/Formulas/Practice,
`Example`/`Task` с решениями в `<details>`), `rules.md` (нумерация `W<N>`, заголовки,
метки источников), `translation-rules.md` (EN↔RU только для TCS).
`fix_formatting.py` чинит списки/отступы и ловит AI-артефакты (`formatting_report.md`).

LLM-бэкенды (`scripts/agent/LLM_BACKENDS.md`, env `LLM_BACKEND`):

- `apikey` (default, используется в CI) — ключ `GEMINI_API_KEY`;
- `antigravity` — локальный хаб Antigravity (подписка, без ключа); на Windows
  разворачивается через `scripts/agent/windows/setup.ps1` (статус без флагов,
  применение — `-Apply` под админом: Yandex DoH-политика, proxy-исключения, Tailscale SSH);
- `xproxy.py` — локальный CONNECT-форвардер, если egress к Google API за-DNS-гейчен.

### Шаг 5. Быстрый инкрементальный рендер (Windows CI)

Пуш в `main` включает `.github/workflows/deploy.yml`, job `build` на **`windows-latest`**:

- `python scripts/render_changed.py --base <before> --jobs 4` — **только изменённые файлы,
  параллельно** (см. раздел 2);
- гейт: `formatting_report.md` без нарушений и AI-артефактов, иначе билд красный;
- smoke: `_site/index.html` существует;
- коммит `_site/ + index.qmd + _freeze/` обратно в `main`.

Полный `quarto render` здесь — только если изменился сам `_quarto.yml` (навигация глобальна).

### Шаг 6. Публикация в прод

Job `deploy` (ubuntu, после `build`): берёт свежий `main`, кладёт `_site/` в `gh-pages`
(`peaceiris/actions-gh-pages`, CNAME `innonotes.ru`). Весь путь «пуш→прод» — около минуты.

**Важно про триггеры:** пуши, сделанные `GITHUB_TOKEN` (все боты выше), **не запускают
новые workflow-раны**. Поэтому: `build` коммитит `_site` без зацикливания (так задумано),
а `repair.yml` после своего пуша явно дёргает `gh workflow run deploy-site` через PAT
(`INNO_FILES_PAT`, коммит `a30cdfc1`). У `agent.yml` такого явного триггера сейчас нет —
после генерации статей деплой сам не стартует, это известное узкое место цепочки.

При падении деплоя срабатывает `.github/workflows/repair.yml`: скачивает лог,
`scripts/agent/repair_deploy.py` чинит известные случаи, проверяет `fix_formatting.py` + YAML,
коммитит фикс в `main` (после чего деплой перезапускается сам).

**Правило стадий: rerun с места падения, без повторного regen.**
Конвейер идёт строго по стадиям, каждая выполняется один раз:
`generate` (agent.yml) → `build` (deploy.yml, Windows) → `deploy` (gh-pages).
Упавшая стадия НИКОГДА не перезапускает предыдущие зелёные:
- упал `deploy`/`build` → чинится и повторяется только он
  (`gh workflow run deploy-site`), генерация НЕ трогается;
- упал `push` в agent.yml → коммит не теряется: сначала `fetch + rebase`
  (уже в workflow), итог генерации всегда лежит в артефакте `regen-qmd`
  рана (`if: always()`); повторный dispatch с `regen_theory` — только если
  упала сама генерация, иначе результат забирается из артефакта/коммита;
- повторный прогон стадии — только после фикса причины падения.

**Правило стадий: rerun с места падения, без повторного regen.**
Конвейер идёт строго по стадиям, каждая выполняется один раз:
`generate` (agent.yml) → `build` (deploy.yml, Windows) → `deploy` (gh-pages).
Упавшая стадия НИКОГДА не перезапускает предыдущие зелёные:
- упал `deploy`/`build` → чинится и повторяется только он
  (`gh workflow run deploy-site`), генерация НЕ трогается;
- упал `push` в agent.yml → коммит не теряется: сначала `fetch + rebase`
  (уже в workflow), итог генерации всегда лежит в артефакте `regen-qmd`
  рана (`if: always()`); повторный dispatch с `regen_theory` — только если
  упала сама генерация, иначе результат забирается из артефакта/коммита;
- повторный прогон стадии — только после фикса причины падения.

---

## 2. Что когда использовать (локально)

| Задача | Команда | Почему |
|---|---|---|
| Смотреть сайт локально | `scripts/preview.sh --port 4300` (= `quarto preview --render all`) | Пререндерит **всё** на старте — дальше мгновенная навигация без Render-оверлея. Голый `quarto preview` так не умеет: каждая неоткрытая страница будет рендериться по клику 10–15+ с |
| Быстро опубликовать правки (тот же результат, что CI, но локально) | `bash scripts/publish.sh` | Ре-рендер **только изменённого** (секунды), патч `_includes`, затем `git add _site/ index.qmd _freeze/` — дальше review → commit → push, прод соберёт Actions ~за минуту |
| Посмотреть, что изменится, ничего не трогая | `python3 scripts/render_changed.py --dry-run` | Печатает список changed-файлов vs `origin/main` |
| Принудительно всё перерендерить | `python3 scripts/render_changed.py --full` | Только если `_quarto.yml` менялся или инкремент разошёлся с полным |
| Другой base / больше параллелизма | `--base <ref>`, `--jobs N` (default 4) | Параллельные рендеры с ретраями коллизий `site_libs` |
| Сгенерировать/перегенерировать статью из транскриптов | `python3 scripts/agent/generate.py --inno-files <путь>` | Сам находит изменения; `--semester semester-4`, `--limit N` (тест), `--dry-run`, `--regen-theory <qmd> --tries 3` (Theory Pro-моделью), `--scaffold-semester semester-N` (новый семестр) |
| Проверить здоровье Antigravity-хаба (без траты квоты) | `python3 scripts/agent/llm_antigravity.py` | Discovery хаба + квоты |
| Починить форматирование всех qmd | `python3 fix_formatting.py` | + пишет `formatting_report.md`; CI гейтится на «No format-rule violations» |
| Пересобрать таблицу курсов на главной | `python3 scripts/update_index.py` | Источник: `semester-*/course_map.json`; обычно вызывается сам (pre-render / render_changed) |
| Обновить «Last updated» | `python3 scripts/update_last_updated.py` | Тоже авто (pre-render); руками не нужно |
| Прогнать SPA+math smoke-тест | см. `scripts/test-spa-math.mjs` (playwright, `BASE` внутри) | Навигация + бейкнутая CHTML-математика на локальном `_site` |
| Вручную вшить `_includes` в собранный HTML | `python3 sync_includes.py` | render_changed делает это сам для `_includes/*` (in-place патч собранных страниц без рендера) |

### Как `render_changed.py` классифицирует изменения (vs base, default `origin/main`)

- `_quarto.yml` → полный `quarto render`;
- `*.qmd` → рендер каждого файла отдельно (`--jobs` параллельно) + персональный bake;
- правило pre-bake: новый/изменённый `.qmd` обязан быть полностью испечён ДО пуша
  (`python3 scripts/agent/prebake.py`), иначе он роняет весь deploy;
- самолечение: страница из навигации, чьего HTML нет в `_site` (приехала сломанным
  билдом), печётся при следующем прогоне автоматически;
- `_includes/*` → быстрая замена старого блока новым прямо в `_site/**/*.html`, без рендера;
- `styles/*`, ассеты (`*.png/mp4/pdf` под `semester-*/`) → зеркальное копирование в `_site`;
- удалённые исходники → удаление их HTML/ассетов из `_site` + чистка `search.json`;
- `search.json` снапшотится до рендеров (одиночный рендер перезаписывает его одной записью)
  и пересобирается после — из собранного HTML, как это делает сам quarto;
- на время параллельных рендеров project pre/post-render (`update_*`, `bake-static-html.sh`)
  подавляются в копии `_quarto.yml` (скрипты уже отработали один раз серийно), потом файл
  восстанавливается; bake запускается точечно (`bake-static-html.mjs <файлы>`).

---

## 3. Правила для агентов (не забывай)

1. **Локально — никогда голый `quarto render` / голый `quarto preview`.**
   Смотреть → `preview.sh`, публиковать правки → `publish.sh` / `render_changed.py`.
   Полный рендер 300+ страниц — только осознанно (`--full`) или в CI.
   - Правки `_includes/*` → render_changed делает in-place inject в собранный HTML
     (секунды, без рендера); правки `styles/*` и ассетов → зеркальное копирование
     в `_site`. Ради этого превью НЕ перезапускается и полный рендер НЕ гоняется.
   - ⚠️ `quarto preview --render all` при старте **сносит `_site/`** (наблюдалось:
     закоммиченные файлы `_site` висят как `D`, пока рендер не добежит до конца).
     Не рестартить его «просто посмотреть»; пока идёт рендер — не запускать
     `publish.sh` и не коммитить `_site` (иначе уедут массовые удаления).
   - После точечных правок состояние `_site` проверяется так:
     `git status --short -- _site/` — допустимы только `M` своих файлов
     (и удаление старых хэшированных ассетов `site_libs`, если хэши сменились).
2. **Не коммить `_site/` вручную** — его коммитит CI-билд (`build(site): refresh _site …`).
   Локально `publish.sh` только стейджит; коммит/пуш — после review.
3. **Не трогай чужие незакоммиченные файлы.** В репо параллельно работает `inno-notes-agent`
   (коммиты `agent: …`, `build(site): …`, `fix(deploy): …`) — перед `git add` всегда
   `git status`, стейдж только свои пути.
4. **Секреты и локальные файлы — не в гит:** `cookies.json`, `credentials.json`,
   `config.json` (есть `*.example.json`), `*_state.json`, `.venv/`, `logs/` —
   проверены `.gitignore`; токены — только через Secrets (`NOTES_PAT` в inno_files,
   `GEMINI_API_KEY` + `INNO_FILES_PAT` в inno_notes).
5. **Статьи — по `prompt.md`/`rules.md`.** Заголовки `#### **N. …**`, примеры/таски
   `##### **4.N. Title** (Source X, Task/Example N)` с решением в `<details>` —
   иначе не встанут Solved-пилюли (`_includes/index.html`) и упадёт гейт форматирования.
6. **Фоновая инфраструктура на Mac:** превью inno_notes — LaunchAgent
   `com.user.inno-notes-4300` (`:4300`, `--render all`); exam bank — `com.user.os-site-4200`
   (`:4200`, статика). Перезапуск: `launchctl bootout|bootstrap … + kickstart`.
   Фоновые процессы из обычных exec-вызовов не выживают — долгоживущее только через launchd.
7. Pre-render `_quarto.yml` (`update_last_updated.py`, `update_index.py`) при каждом рендере
   трогает `index.qmd` (timestamp) — это штатно; post-render `bake-static-html.sh` печёт
   математику в статику для SPA-навигации.
8. **Ожидание CI — только через хук, никакого опроса.** Запущенный ран (`deploy-site`
   идёт ~10 мин) НЕЛЬЗЯ караулить циклом `gh run view` — это жжёт токены впустую.
   Один раз взводится detached-хук, который сам следит за статусом; агент читает
   файл итога один раз в конце (успех либо падение с ошибкой) и в промежутке
   занимается другими задачами.
   - Обычные `cmd &` / `nohup … &` из exec-вызовов умирают вместе с сессией —
     хук обязан делать double-fork + `setsid` (проверено: только так переживает
     завершение вызова; долгоживущее иначе — только через launchd).
   - Рецепт (RUN_ID — id рана из `gh run list`):
     ```bash
     python3 - <<'EOF'
     import os, subprocess, sys
     run_id = 'RUN_ID'; log = '/tmp/inno_deploy_hook.log'
     if os.fork() > 0: sys.exit(0)
     os.setsid()
     if os.fork() > 0: os._exit(0)
     with open(log, 'w') as f:
         r = subprocess.run(['gh', 'run', 'watch', run_id, '--exit-status'],
                            stdout=f, stderr=subprocess.STDOUT, text=True, cwd='.')
         f.write(f'HOOK_EXIT={r.returncode}\n')
     EOF
     ```
   - `gh run watch` сам рефрешит статус каждые 3 с и возвращает ненулевой код,
     если ран упал. Итог: `cat /tmp/inno_deploy_hook.log` → в конце `HOOK_EXIT=0|1`.
   - Пока хук висит — не опрашивать файл в цикле; проверять редко (по готовности
     других задач) или один раз в конце.
