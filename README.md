### Telegram Service Bot
Простой Telegram-бот для записи клиентов на услуги.
Подходит для малого бизнеса: барбершопы, мастера, репетиторы и т.д.
#### 🚀 Функционал
- Приветствие пользователя (`/start`)
- Выбор услуги
- Выбор времени
- Подтверждение записи
- Уведомление администратора
- Защита от повторной записи
#### 🛠 Стек
- Python
- aiogram
#### 📂 Структура проекта
service_bot/
|- bot.py
|- config.py/
|- handlers.py/
|- requirements.txt
|- .env
#### ⚙️ Установка и запуск
1. Клонировать репозиторий:
``` bash
git clone https://github.com/thefirsthouse/service-bot.git
cd service-bot
```
2. Установить зависимости:
``` bash
pip install -r requirements.txt
```
3. Создать файл `.env`:
``` env
TOKEN=your-telegram-bot-token
ADMIN_ID=your-telegram-id
```
4. Запустить бота:
``` bash
python bot.py
```
#### 🔐 Безопасность
Токены хранятся в `.env` и не попадают в репозиторий.
#### 📌 Планы по развитию
- Добавление базы данных
- Админ-панель
- Календарь записей
- Онлайн-оплата
- Деплой
