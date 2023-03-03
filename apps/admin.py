"""
admin
"""
from aiogram.types import Message as m
from aiogram.dispatcher import FSMContext as s
from buttons.keyboardbuttons import login_buttons_menu, btn_student_xonalari, btn, btn_educators, btn_admins
from database.database import *
from states import state_admin, state_login


async def admin_menu(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    await state.update_data(state_name="admin")
    if m.text == "Chiqish":
        await m.answer("Foydalanuvchi idsini kiriting:", reply_markup=login_buttons_menu)
        await state_login.username.set()
    elif m.text == "Studentlar":
        await m.answer("Student xonasini tanlang:", reply_markup=btn_student_xonalari())
        await state_admin.student_xona.set()
    elif m.text == "Student qoshish":
        await m.answer("Ismini kiriting:", reply_markup=btn(["Bekor qilish"]))
        await state_admin.student_qoshish_name.set()
    elif m.text == "Tarbiyachilar":
        await m.answer("Tarbiyachilar:", reply_markup=btn_educators())
        await state_admin.educators_main_menu.set()
    elif m.text == "Adminlar":
        await m.answer("Adminlar:", reply_markup=btn_admins())
        await state_admin.subadmins_main_menu.set()

