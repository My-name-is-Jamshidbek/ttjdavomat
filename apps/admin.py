"""
admin
"""
from aiogram.types import Message as m
from aiogram.dispatcher import FSMContext as s
from buttons.keyboardbuttons import login_buttons_menu, btn_student_xonalari, btn, btn_educators, btn_admins
from database.database import student_view_qavat, attendance_datas
from states import Main_state
from config import menus


async def admin_menu(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    await state.update_data(state_name="admin")
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Chiqish":
        await m.answer("Foydalanuvchi idsini kiriting:", reply_markup=login_buttons_menu)
        await Main_state.username.set()
    elif m.text == "Studentlar" and (m.text in menus[user]):
        await m.answer("Student xonasini tanlang:", reply_markup=btn_student_xonalari())
        await Main_state.student_xona.set()
    elif m.text == "Student qoshish" and (m.text in menus[user]):
        await m.answer("Ismini kiriting:", reply_markup=btn(["Bekor qilish"]))
        await Main_state.student_qoshish_name.set()
    elif m.text == "Tarbiyachilar" and (m.text in menus[user]):
        await m.answer("Tarbiyachilar:", reply_markup=btn_educators())
        await Main_state.educators_main_menu.set()
    elif m.text == "Adminlar" and (m.text in menus[user]):
        await m.answer("Adminlar:", reply_markup=btn_admins())
        await Main_state.subadmins_main_menu.set()
    elif m.text == "Yoqlama jadvallari" and (m.text in menus[user]):
        data = attendance_datas()
        if len(data) == 0:
            await m.answer("Dars jadvallari mavjud emas!")
        else:
            datas = []
            for i in data:
                datas.append(f"{i[0]}.{i[1]}.{i[2]}")
                datas.append("Chiqish")
            await m.answer("Sanani tanlang:", reply_markup=btn(datas))
            await Main_state.attendances.set()

    elif m.text == "Yoqlama qilish" and (m.text in menus[user]):
        qavatlar = student_view_qavat()
        qavatlar.append("Chiqish")
        await m.answer("Qavatni tanlang:", reply_markup=btn(qavatlar))
        await Main_state.attendance_qavat.set()
