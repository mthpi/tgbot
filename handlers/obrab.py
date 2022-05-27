from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import *


#@dp.message_handlers(commands='start')
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приветствуем!')
    await bot.send_message(message.from_user.id, 'Услуга: Доступ к каналу \nСтоимость: 2 300.00 KZT \nСрок действия: бессрочно \n\nВыберите способ оплаты:', reply_markup=keyboard_sub)

#@dp.callback_query_handlers(text="sub")
async def sub(call: types.CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id, title="Доступ к телеграм каналу", description="Сразу после успешной оплаты вы получите ссылку на телеграм канал", payload="1", provider_token="381764678:TEST:37180", currency="RUB", start_parameter="test_bot", prices=[{"label": "Тг", "amount": 34000}])

#@dp.pre_checkout_query_handlers()
async def check(check: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(check.id, ok=True)

#@dp.message_handlers(content_type=types.ContentType.SUCCESSFUL_PAYMENT)
async def pay(message: types.Message):
    if message.successful_payment.invoice_payload == "1":
        await bot.send_message(message.from_user.id, "t.me/+W0IVz_o8SUZhZmQy")


def register_handlers_oplata(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_callback_query_handler(sub, text="sub")
    dp.register_pre_checkout_query_handler(check)
    dp.register_message_handler(pay, content_types=types.ContentType.SUCCESSFUL_PAYMENT)