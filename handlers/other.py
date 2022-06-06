from aiogram import types, Dispatcher
import json
import string


# @dp.message_handler()
async def echo_send(mes: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in mes.text.split(' ')} \
            & set(json.load(open('cenzura.json'))):
        # if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in mes.text.split(' ')} \
        #         & set(json.load(open('cenzura.json'))) != set():
        await mes.reply(f'У нас не матерятся {mes.from_user.full_name}')
        await mes.delete()


def register_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
