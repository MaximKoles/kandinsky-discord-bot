import os
import aiogram
from aiogram import types
from aiogram.dispatcher import dispatcher
import replicate
from googletrans import Translator

# устанавливаем токен для взаимодействия с Telegram API
BOT_TOKEN = 'YOUR_BOT_TOKEN'
# устанавливаем токен для взаимодействия с Replicate API
REPLICATE_API_TOKEN = 'YOUR_REPLICATE_API_TOKEN'

bot = aiogram.Bot(token=BOT_TOKEN)
dp = aiogram.dispatcher.Dispatcher(bot)

# функция генерации изображения на Replicate
async def generate_image(input_text: str):
    output = replicate.run(
       "ai-forever/kandinsky-2:601eea49d49003e6ea75a11527209c4f510a93e2112c969d548fbb45b9c4f19f",
        input={"prompt": input_text}
    )
    return output[0]  # возвращаем ссылку на сгенерированное изображение

# функция для перевода текста на английский язык
async def translate_message(message: str):
    translator = Translator()
    translation = translator.translate(message, dest='en')
    return translation.text

# функция, которая будет вызываться при отправке сообщений боту
async def get_image(message: types.Message):
    try:
        print(f"Получено сообщение: {message.text}")
        # переводим текст на английский язык
        input_text = await translate_message(message.text)
        print(f"Переведенный текст: {input_text}")
        # запрашиваем изображение на Replicate
        image_url = await generate_image(input_text)
        print(f"Сгенерированное изображение: {image_url}")
        # отправляем пользователю ссылку на сгенерированное изображение
        await bot.send_message(message.chat.id, f"Вот ваше изображение: {image_url}")
    except Exception as e:
        print(f"Ошибка: {e}")
        await bot.send_message(message.chat.id, "Извините, произошла ошибка, повторите попытку позднее.")


# запускаем бота
if __name__ == '__main__':
    # устанавливаем токен для взаимодействия с Replicate API как переменную среды
    os.environ['REPLICATE_API_TOKEN'] = REPLICATE_API_TOKEN
    # создаем обработчик сообщений
    dp.register_message_handler(get_image, content_types=types.ContentType.TEXT)
    # запускаем бота
    aiogram.executor.start_polling(dp, skip_updates=True)
