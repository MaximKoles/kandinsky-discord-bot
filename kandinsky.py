import os
import aiogram
from aiogram import types
from aiogram.dispatcher import dispatcher
import replicate
from yandex.Translater import Translater  # импортируем класс Translater

# устанавливаем токен для взаимодействия с Telegram API
BOT_TOKEN = 'YOUR_BOT_TOKEN'
# устанавливаем токен для взаимодействия с Replicate API
REPLICATE_API_TOKEN = 'YOUR_REPLICATE_API_TOKEN'
# создаем класс переводчика Yandex
translater = Translater()

bot = aiogram.Bot(token=BOT_TOKEN)
dp = aiogram.dispatcher.Dispatcher(bot)

# функция генерации изображения на Replicate
async def generate_image(input_text: str):
    output = replicate.run(
       "ai-forever/kandinsky-2:601eea49d49003e6ea75a11527209c4f510a93e2112c969d548fbb45b9c4f19f",
        input={"prompt": input_text}
    )
    return output[0]  # возвращаем ссылку на сгенерированное изображение


# функция, которая будет вызываться при отправке сообщений боту
async def get_image(message: types.Message):
    try:
        # инициализируем объект Translater с параметрами
        translater.set_key('YOUR_YANDEX_TRANSLATE_API_KEY')
        translater.set_from_lang('ru')
        translater.set_to_lang('en')
        # переводим входной текст на английский язык
        input_text = translater.translate(message.text)
        # запрашиваем изображение на Replicate
        image_url = await generate_image(input_text)
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
