import os
import replicate
from aiogram import Bot, Dispatcher

# Получить токены доступа для бота и модели из переменных окружения
BOT_TOKEN = os.environ.get('BOT_TOKEN')
API_TOKEN = os.environ.get('API_TOKEN')

# Создать экземпляр бота и диспетчер
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

# Функция для вызова модели и генерации изображений
async def generate_images(prompt):
    try:
        # Запустить модель
        output = replicate.run(
            "ai-forever/kandinsky-2:601eea49d49003e6ea75a11527209c4f510a93e2112c969d548fbb45b9c4f19f",
            input={"prompt": prompt}
        )
        # Вернуть URI-адреса сгенерированных изображений в виде строки
        return '\n'.join(output)
    except Exception as e:
        # Обработать ошибки (например, если API модели недоступно)
        return f'Error: {e}'

# Обработчик команды /start
@dp.command_handler(commands=['start'])
async def start_handler(message):
    await bot.send_message(message.chat.id, 'Привет! Я могу сгенерировать изображения на основе твоего текстового запроса.')

# Обработчик команды /generate
@dp.command_handler(commands=['generate'])
async def generate_handler(message):
    # Получить текстовое сообщение от пользователя
    prompt = message.text.split(' ')[1]
    # Запустить модель и получить URI-адреса сгенерированных изображений
    output = await generate_images(prompt)
    # Отправить изображения пользователю в виде URI-адресов
    await bot.send_message(message.chat.id, output)

# Запустить бота
bot.run_forever()
