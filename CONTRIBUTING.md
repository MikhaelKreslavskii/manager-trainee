# Руководство по работе с репозиторием (GitHub Flow)

Мы используем GitHub Flow для организации работы с репозиторием. Следуйте этому руководству, чтобы обеспечить эффективную совместную работу и избежать ошибок. ✅

---

## Основные принципы GitHub Flow 🌐

1. **Главная ветка (`main`) всегда рабочая.** Ветка `main` содержит только стабильный и протестированный код. 🛠️
2. **Разработка ведётся в отдельных ветках.** Для каждой задачи или исправления создавайте новую ветку. Сначала указывается тип изменения, а потом через слеш `/` - название задачи или его id 🌿 Например: `feature/task-name` или `hotfix/issue-id`.
3. **Можно делать ответвления от ответвлений.** Если надо делать доработку поверх другой доработки, то делается ответвление из ответвлённой ветки.
4. **Код-ревью обязательно.** Перед слиянием изменений в `main` (или уже из вспомогательной ветки) запросите ревью у коллег. 🔍
4. **Автономная разработка.** Изменения в ветке не должны ломать функциональность других частей проекта. 🔒
5. **Частые коммиты.** Пишите осмысленные сообщения к каждому коммиту. ✏️

---

## Алгоритм работы 🚀

### 1. Клонирование репозитория 🔄
Сначала склонируйте репозиторий на свой компьютер:
```bash
git clone https://github.com/username/project-name.git
```

### 2. Создание новой ветки 🌿
Создавайте отдельную ветку для каждой задачи:
```bash
git checkout -b feature/task-name
```
> **Пример имени ветки:** `feature/add-login` или `bugfix/fix-button-click`.

### 3. Разработка и коммиты ✏️
- Вносите изменения в код. 💻
- Фиксируйте изменения с осмысленными сообщениями:
```bash
git add .
git commit -m "Краткое описание изменений"
```

### 4. Синхронизация с `main` 🔄
Перед отправкой ветки убедитесь, что вы синхронизированы с последней версией `main` (или из второстепенной ветки):
```bash
git checkout main
git pull origin main
git checkout feature/task-name
git merge main
```

### 5. Отправка ветки на сервер 🌐
Отправьте изменения в репозиторий:
```bash
git push origin feature/task-name
```

### 6. Создание Pull Request 🔄
На GitHub создайте Pull Request:
1. Перейдите в репозиторий. 📂
2. Нажмите **"Compare & pull request"**. 🔗
3. Убедитесь, что ветка `main` (или второстепенная) указана как целевая. 🎯
4. Напишите описание ваших изменений. 📝
5. Запросите ревью у коллег. 👥

### 7. Исправление замечаний 🛠️
Если на этапе ревью будут даны рекомендации:
- Внесите изменения в своей ветке. 💡
- Сделайте коммит и отправьте изменения:
```bash
git add .
git commit -m "Исправления по ревью"
git push origin feature/task-name
```

### 8. Слияние в `main` ✔️
После успешного ревью владелец репозитория или коллеги с правами могут выполнить слияние. 🔗
