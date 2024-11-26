from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Список тренирующихся')],
                                     [KeyboardButton(text='Голосование')],
                                     [KeyboardButton(text='Каго'),
                                      KeyboardButton(text='Регистрация')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выбери пункт меню')

list_of_wishes = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Список', callback_data='list')]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Номер тык', request_contact=True)]],
                                  resize_keyboard=True)
