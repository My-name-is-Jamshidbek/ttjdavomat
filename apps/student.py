"""
student
"""
import os
import string
import random

from aiogram.types import Message as m, InputFile
from aiogram.dispatcher import FSMContext as s

from buttons.keyboardbuttons import btn_student_xona_turlari, \
    btn_students_xona, btn
from config import menus
from database.database import student_view_data_, student_delete_data, \
    student_insert_data
from states import Main_state


async def student_xona(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Chiqish":
        await m.answer("Asosiy menyu:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        await m.answer("Xona turini tanlang:", reply_markup=btn_student_xona_turlari(m.text))
        await state.update_data(student_xona=m.text)
        await Main_state.student_xona_turi.set()


async def student_xona_turi(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Chiqish":
        await m.answer("Asosiy menyu:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        data = await state.get_data()
        room = data.get("student_xona")
        type = m.text
        await state.update_data(student_xona_turi=type)
        await m.answer("Talabani tanlang:", reply_markup=btn_students_xona(room, type))
        await Main_state.student_students.set()


async def student_students(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Chiqish":
        await m.answer("Asosiy menyu:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        data = await state.get_data()
        room, _type, name = data.get('student_xona'), data.get('student_xona_turi'), m.text
        data = student_view_data_(room=room, type=_type, name=name)
        await state.update_data(student_name=m.text)
        await state.update_data(student_surname=data[1])
        photo = data[6]
        try:
            photo = InputFile(photo)
            await m.answer_photo(
                photo=photo,
                caption=f"Ism: {data[0]}.\n"
                     f"Familiya: {data[1]}.\n"
                     f"Qavat: {data[2]}.\n"
                     f"Xona: {data[3]} {data[4]}.\n"
                     f"Jinsi: {data[5]}.\n"
                     f"Telefon: {data[9]}.\n"
                     f"Aloqa: {data[10]}.\n"
                     f"Manzil: {data[11]}.",
                reply_markup=btn(["O'chirish", "Orqaga"]))
        except Exception as _:
            await m.answer(text=f"Ism: {data[0]}.\n"
                            f"Familiya: {data[1]}.\n"
                            f"Qavat: {data[2]}.\n"
                            f"Xona: {data[3]} {data[4]}.\n"
                            f"Jinsi: {data[5]}.\n"
                            f"Telefon: {data[9]}.\n"
                            f"Aloqa: {data[10]}.\n"
                            f"Manzil: {data[11]}.",
                       reply_markup=btn(["O'chirish", "Orqaga"]))
        await Main_state.student_students_menu.set()


async def student_students_menu(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Orqaga":
        await m.answer("Asosiy menyu:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    elif m.text == "O'chirish":
        data = await state.get_data()
        student_delete_data(
            room_number=data.get("student_xona"),
            room_type=data.get("student_xona_turi"),
            name=data.get("student_name"),
            surname=data.get("student_surname")
        )
        await m.answer("Talaba o'chirildi:", reply_markup=btn_students_xona(
            room=data.get("student_xona"),
            type=data.get("student_xona_turi"))),
        await Main_state.student_students.set()
    # elif m.text == "Tahrirlash":
    #     await m.answer("Tahrirlash uchun malumotni tanlang:", reply_markup=btn(["ism","familiya","qavat", "xona",
    #                                                                             "jinsi", "telefon", "aloqa"]))
    #     await state_admin.


async def student_qoshish_name(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        await state.update_data(student_qoshish_name=m.text)
        await m.answer("Familiyasini kiriting:", reply_markup=btn(["Bekor qilish"]))
        await Main_state.student_qoshish_surname.set()


async def student_qoshish_surname(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        await state.update_data(student_qoshish_surname=m.text)
        await m.answer("Qavatni kiriting:", reply_markup=btn(["1", "2", "3", "Bekor qilish"]))
        await Main_state.student_qoshish_qavat.set()


async def student_qoshish_qavat(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        await state.update_data(student_qoshish_qavat=m.text)
        await m.answer("Xona raqamini kiriting:", reply_markup=btn(["Bekor qilish"]))
        await Main_state.student_qoshish_room_number.set()


async def student_qoshish_room_number(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        await state.update_data(student_qoshish_room_number=m.text)
        await m.answer("Xona turini kiriting:", reply_markup=btn(["A", "B", "Bekor qilish"]))
        await Main_state.student_qoshish_room_type.set()


async def student_qoshish_room_type(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        await state.update_data(student_qoshish_room_type=m.text)
        await m.answer("Jinsini kiriting:", reply_markup=btn(["Bekor qilish", "Erkak", "Ayol"]))
        await Main_state.student_qoshish_gender.set()


async def student_qoshish_gender(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        await state.update_data(student_qoshish_gender=m.text)
        await m.answer("Suratini jo'nating:", reply_markup=btn(["Bekor qilish"]))
        await Main_state.student_qoshish_photo.set()


async def student_qoshish_photo(m: m, state: s):
    """
    :param m: 
    :param state: 
    :return: 
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    elif m.photo:
        pn = ''.join(random.choices(string.ascii_letters, k=16))
        await m.photo[-1].download(destination_file=f"database/photos/{pn}.jpg")
        await state.update_data(student_qoshish_photo=f"database/photos/{pn}.jpg")
        await m.answer("Telefon raqamini kiriting:")
        await Main_state.student_qoshish_phone_number.set()


async def student_qoshish_phone_number(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        await state.update_data(student_qoshish_phone_number=m.text)
        await m.answer("Aloqa uchun manzil kiriting:")
        await Main_state.student_qoshish_aloqa.set()


async def student_qoshish_aloqa(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        await state.update_data(student_qoshish_aloqa=m.text)
        await m.answer("Uy manzilini kiriting:")
        await Main_state.student_qoshish_addres.set()


async def student_qoshish_addres(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        try:
            await state.update_data(student_qoshish_addres=m.text)
            data = await state.get_data()
            student_insert_data(
                name=data.get("student_qoshish_name"),
                surname=data.get("student_qoshish_surname"),
                qavat=data.get("student_qoshish_qavat"),
                room_number=data.get("student_qoshish_room_number"),
                room_type=data.get("student_qoshish_room_type"),
                gender=data.get("student_qoshish_gender"),
                photo=data.get("student_qoshish_photo"),
                username=data.get("student_qoshish_photo"),
                password=data.get("student_qoshish_photo"),
                phone_number=data.get("student_qoshish_phone_number"),
                aloqa=data.get("student_qoshish_aloqa"),
                address=data.get("student_qoshish_addres")
            )
            await m.answer("Talaba muvaffaqiyatli qo'shildi.")
            await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
            await Main_state.main_menu.set()
        except Exception as _:
            await m.answer(
                "Talabani malumotlar bazasiga qo'shishda xatolik vujudga keldi iltimos qaytadan urinib ko'ring!")
