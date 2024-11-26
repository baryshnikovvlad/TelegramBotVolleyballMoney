import datetime

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, PollAnswer
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database import models
import app.keyboards as kb
from database.requests import create_poll_, select_users, select_user, insert_user_from_register, insert_vote_in_table
import main

router = Router()

class Register(StatesGroup):
    name = State()
    user_tg_id = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Выбер пункт', reply_markup=kb.main)

@router.message(F.text == 'Список тренирующихся')
async def list_(message: Message):
    await message.answer('Тык', reply_markup=kb.list_of_wishes)

@router.message(F.text == 'Голосование')
async def poll(message: Message):
    await create_poll_(main.bot)

@router.poll_answer()
async def hadler_poll_answer(poll_answer: PollAnswer):
    user_id = poll_answer.user.id
    poll_id = poll_answer.poll_id
    options = poll_answer.option_ids
    date = datetime.datetime.now()

    insert_vote_in_table(user_id, poll_id, options, date)

@router.message(F.data == 'list')
async def cmd_help(callback: CallbackQuery):
    await callback.message.answer(select_users(models.path))

@router.message(F.text == 'Регистрация')
async def registracia(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введите ФИО')

@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.user_tg_id)
    await message.answer('Нажмите на кнопку чтобы передать контакт боту', reply_markup=kb.get_number)

@router.message(Register.user_tg_id, F.contact)
async def register_number(message: Message, state: FSMContext):
    await state.update_data(user_tg_id=message.contact.user_id)
    data = await state.get_data()
    insert_user_from_register(data["name"], 0, data["user_tg_id"], message.contact.phone_number)
    user = select_user(models.path, data["user_tg_id"])
    await message.answer(f"Вы теперь юзер: {user}")
    await state.clear()
