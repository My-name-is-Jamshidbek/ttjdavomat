"""
log in
"""
from aiogram.types import Message as m
from aiogram.dispatcher import FSMContext as s
from buttons.keyboardbuttons import login_buttons_menu, btn
from config import menus
from database.database import *
from states import *


async def cmd_start(m: m):
    """
    :param m:
    :return:
    """
    await m.answer("Assalomu aleykum\nFoydalanuvchi idsini kiriting:", reply_markup=login_buttons_menu)
    await Main_state.username.set()


async def login_username(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    if m.text == "Dasturchi malumoti":
        await m.answer(text=str(programmer_get_data()))
    else:
        await m.answer("Parolingizni kiriting:")
        await state.update_data(username=m.text)
        await Main_state.password.set()


async def login_password(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    if m.text == "Dasturchi malumoti":
        await m.answer(text=str(programmer_get_data()))
    else:
        data = await state.get_data()
        username = data.get("username")
        password = m.text
        if admin_check(username, password):
            user = "admin"
            await m.answer("Admin botga hush kelibsiz!\nKerakli menyuni tanlang:", reply_markup=btn(menus[user]))
            await state.update_data(user_name=user)
            await Main_state.main_menu.set()
        elif subadmin_check(username, password):
            user = "subadmin"
            data = subadmin_view_data(username)
            await m.answer(f"{data[1]} {data[2]}\nKerakli menyuni tanlang:", reply_markup=btn(menus[user]))
            await state.update_data(user_name=user)
            await Main_state.main_menu.set()
        elif educator_check(username, password):
            user = "educator"
            data = educator_view_data(username, tek=False)
            await state.update_data(educator_id=data[0])
            await m.answer(f"{data[1]} {data[2]}\nKerakli menyuni tanlang:", reply_markup=btn(menus[user]))
            await state.update_data(user_name=user)
            await Main_state.main_menu.set()
        else:
            await m.answer("ID yoki parol xato iltimos tekshirib qaytadan kiriting!")
            await Main_state.username.set()
