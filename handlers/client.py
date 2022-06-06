from aiogram import types, Dispatcher
from settings import bot
from keyboards.clent_kb import kb_client
from aiogram.types import ReplyKeyboardRemove


# @dp.message_handler(commands=['start', 'help'])
async def command_start(mes: types.Message):
    try:
        await bot.send_message(mes.from_user.id, f'Приятного аппетита', reply_markup=kb_client)
        await mes.delete()
    except:
        await mes.reply(f'Уважаемый {mes.from_user.full_name}, напиши боту: \nhttps://t.me/FOT0ROBOT')


# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(mes: types.Message):
    await bot.send_message(mes.from_user.id, f'Вс-Чт с 9:00 до 20:0, Пт-Сб с 10:00 до 23:00',
                           reply_markup=ReplyKeyboardRemove())


# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(mes: types.Message):
    await bot.send_message(mes.from_user.id, f'ул. Колбасная 15')


def register_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])