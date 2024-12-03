from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from PIL import Image
from model_for_bot import get_latex_code


BOT_TOKEN = "*"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def process_start_command(message: Message):
    await message.answer("Привет! Пришли картинку с формулой.")


async def process_help_command(message: Message):
    await message.answer("Пришли картинку с формулой. Я отпарвлю тебе LaTex верстку")


async def send_photo_echo(message: Message):
    await message.bot.download(
        file=message.photo[-1].file_id,
        destination="/Users/beespal/Documents/ML_and_DL/projects/image2latex/test_image.png",
    )
    latex_code = get_latex_code(
        "/Users/beespal/Documents/ML_and_DL/projects/image2latex/test_image.png"
    )
    await message.answer(latex_code)


async def send_echo(message: Message):
    await message.answer("Ну я даже не знаю")


dp.message.register(process_start_command, Command(commands="start"))
dp.message.register(process_help_command, Command(commands="help"))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_echo)


if __name__ == "__main__":
    dp.run_polling(bot)
