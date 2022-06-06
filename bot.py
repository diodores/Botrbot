from aiogram import executor
from settings import dp
from handlers import client, admin, other


async def on_startup(_):
    print('Бот в он-лайне...')


if __name__ == "__main__":
    client.register_client(dp)
    other.register_other(dp)

    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
