from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')

# b4 = KeyboardButton('Поделится номером', request_contact=True)
# b4 = KeyboardButton('Поделится номером', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_client.add(b1).add(b2).add(b3)
# kb_client.add(b1).add(b2).insert(b3)
# kb_client.row(b1, b2, b3)
kb_client.insert(b1).row(b3, b2)
