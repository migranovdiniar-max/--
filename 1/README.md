# Email Domain Checker

Простой скрипт на Python для проверки валидности доменов email-адресов по наличию MX-записей в DNS.

## Что делает скрипт

Для каждого email возвращает один из статусов:
- `домен валиден` — домен существует и имеет хотя бы одну MX-запись  
- `домен отсутствует` — домен не найден в DNS или email некорректный (без @, без домена и т.п.)  
- `MX-записи отсутствуют или некорректны` — ошибка DNS-запроса или сервер не отвечает корректно

## Требования и зависимости

- Python 3.8+
- Библиотека: `dnspython` (единственная внешняя зависимость)

## Установка (один раз)

1. **Скачайте скрипт**  
   Сохраните код в файл `email_checker.py` (или клонируйте репозиторий).

2. **(Рекомендуется) Создайте виртуальное окружение**  
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux / macOS
   # или
   venv\Scripts\activate         # Windows

# Запуск скрипта
python email_checker.py email1@example.com email2@example.com ...

# Пример
python email_checker.py test@gmail.com test@yahoo.com test@mail.ru

python email_checker.py test@proton.me

python email_checker.py wrong test@ fake@fake-domain-987654.xyz

# Пример вывода
test@gmail.com: домен валиден
test@yahoo.com: домен валиден
test@mail.ru: домен валиден

test@proton.me: домен валиден

wrong: домен отсутствует
test@: домен отсутствует
fake@fake-domain-987654.xyz: домен отсутствует