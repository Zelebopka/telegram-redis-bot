# Telegram Redis Bot

## Описание

Телеграм-бот на Python, который принимает сообщения пользователей и сохраняет их в Redis.

## Функционал

* Приём сообщений от пользователей Telegram.
* Сохранение сообщений в Redis.
* Подтверждение успешного сохранения сообщения.

## Используемые технологии

* Python 3
* aiogram
* Redis
* Docker
* python-dotenv

## Установка и запуск

### Запуск Redis

```bash
docker run -d --name redis -p 6379:6379 redis
```

### Настройка переменных окружения

Создать файл `.env`:

```env
BOT_TOKEN=YOUR_TOKEN
REDIS_HOST=localhost
REDIS_PORT=6379
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

### Запуск бота

```bash
python bot.py
```

## Пример работы

Пользователь отправляет сообщение:

```text
123
```

Бот отвечает:

```text
Сообщение сохранено в Redis ✅
```

Проверка сохранения в Redis:

```bash
docker exec -it redis redis-cli
LRANGE messages 0 -1
```

Результат:

```text
1) "Son_0f_talent: 123"
```
