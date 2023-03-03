"""
log in
"""
from aiogram.types import Message as m
from aiogram.dispatcher import FSMContext as s
from buttons.keyboardbuttons import login_buttons_menu, admin_main_menu, subadmin_main_menu, educator_main_menu
from database.database import *
from states import *


async def cmd_start(m: m):
    """
    :param m:
    :return:
    """
    await m.answer("Assalomu aleykum\nFoydalanuvchi idsini kiriting:", reply_markup=login_buttons_menu)
    await state_login.username.set()


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
        await state_login.password.set()


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
            await m.answer("Admin botga hush kelibsiz!\nKerakli menyuni tanlang:", reply_markup=admin_main_menu)
            await state.finish()
            await state_admin.main_menu.set()
        elif subadmin_check(username, password):
            data = subadmin_view_data(username)
            await m.answer(f"{data[1]} {data[2]}\nKerakli menyuni tanlang:", reply_markup=subadmin_main_menu)
            await state.finish()
            await state_subadmin.main_menu.set()
        elif educator_check(username, password):
            data = educator_view_data(username)
            await m.answer(f"{data[1]} {data[2]}\nKerakli menyuni tanlang:", reply_markup=educator_main_menu)
            await state.finish()
            await state_educator.main_menu.set()
        else:
            await m.answer("ID yoki parol xato iltimos tekshirib qaytadan kiriting!")
            await state_login.username.set()