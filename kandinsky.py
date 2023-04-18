# Импортируем нужные модули для Telegram-бота
import os
import replicate
from dotenv import load_dotenv
import telegram
from telegram.ext import CommandHandler, Updater
from telegram.constants import ParseMode

# Загружаем переменные token из .env файла
load_dotenv()
api_token = os.environ['TELEGRAM_API_TOKEN']

# экземпляр бота Telegram
bot = telegram.Bot(token=api_token)

# функция для обработки команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Привет! Я бот, который может создавать картины в стиле Кандинского. \
                             С помощью команды /kandinsky ты можешь создать свою картину.")
    
# функция для обработки команды /kandinsky
def kandinsky(update, context):
    prompt = str(context.args[0]) # получаем текст запроса от пользователя
    steps = int(context.args[1]) # получаем количество шагов
    scale = float(context.args[2]) # получаем масштаб
    model = replicate.models.get("cjwbw/kandinsky-2") # загружаем модель
    version = model.versions.get("65a15f6e3c538ee4adf5142411455308926714f7d3f5c940d9f7bc519e0e5c1a") # загружаем версию модели
    image = version.predict(prompt=prompt, num_inference_steps=steps, guidance_scale=scale) # генерируем изображение
    context.bot.send_photo(chat_id=update.effective_chat.id, caption="Kandinsky Art",
                           photo=image) # отправляем изображение

# создаем обработчик команд для /start
start_handler = CommandHandler('start', start)
# создаем обработчик команд для /kandinsky
kandinsky_handler = CommandHandler('kandinsky', kandinsky)

# создаем экземпляр Updater
updater = Updater(token=api_token, use_context=True)

# добавляем обработчики команд в Updater
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(kandinsky_handler)

# запускаем бота
updater.start_polling()
