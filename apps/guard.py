"""
subadmin
"""
from aiogram.types import Message as m
from aiogram.dispatcher import FSMContext as s

from buttons.keyboardbuttons import btn
from database.database import qorovul_view_data_by_name, qorovul_delete_data, qorovul_view_data, qorovul_insert_data
from states import Main_state
from config import menus


async def qorovuls_main_menu(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Chiqish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    elif m.text == "Qo'shish":
        await m.answer("Ismni kiriting:", reply_markup=btn(["Bekor qilish"]))
        await Main_state.qorovul_qoshish_ism.set()
    else:
        data = qorovul_view_data_by_name(m.text)
        if len(data) != 0:
            await m.answer(f"ID {data[0]}\nIsm: {data[1]}\nFamiliya: {data[2]}\nTelefon: {data[3]}\nAloqa:"
                           f" {data[4]}\nUsername: "
                           f"{data[5]}\nPassword: {data[6]}",
                           reply_markup=btn(["O'chirish", "Chiqish"]))
            await state.update_data(qorovul_id=data[0])
            await Main_state.qorovul_main_menu.set()


async def qorovul_main_menu(m: m, state: s):
    """
    :param m:
    :param state:
    :return:
    """
    data = await state.get_data()
    user = data.get("user_name")
    if m.text == "Chiqish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    elif m.text == "O'chirish":
        data = await state.get_data()
        _id = data.get("qorovul_id")
        qorovul_delete_data(_id)
        await m.answer("Qorovul o'chirildi!")
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()


async def qorovul_qoshish_ism(m: m, state: s):
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
        await state.update_data(qorovul_qoshish_ism=m.text)
        await m.answer("Familiyani kiriting:")
        await Main_state.qorovul_qoshish_familiya.set()


async def qorovul_qoshish_familiya(m: m, state: s):
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
        await state.update_data(qorovul_qoshish_familiya=m.text)
        await m.answer("Telefon raqamini kiriting:")
        await Main_state.qorovul_qoshish_telefon.set()


async def qorovul_qoshish_telefon(m: m, state: s):
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
        await state.update_data(qorovul_qoshish_telefon=m.text)
        await m.answer("Aloqa uchun link kiriting:")
        await Main_state.qorovul_qoshish_aloqa.set()


async def qorovul_qoshish_aloqa(m: m, state: s):
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
        await state.update_data(qorovul_qoshish_username=m.text)
        await m.answer("Username kiriting:")
        await Main_state.qorovul_qoshish_username.set()


async def qorovul_qoshish_username(m: m, state: s):
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
        if qorovul_view_data(m.text) is None:
            await state.update_data(qorovul_qoshish_username=m.text)
            await m.answer("Parolni kiriting:")
            await Main_state.qorovul_qoshish_parol.set()
        else:
            await m.answer("Bu username allaqachon bant!\nIltimos yangi username kiriting:")


async def qorovul_qoshish_parol(m: m, state: s):
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
            data = await state.get_data()
            qorovul_insert_data(
                ism=data.get("qorovul_qoshish_ism"),
                familiya=data.get("qorovul_qoshish_familiya"),
                telefon=data.get("qorovul_qoshish_telefon"),
                aloqa=data.get("qorovul_qoshish_aloqa"),
                username=data.get("qorovul_qoshish_username"),
                parol=m.text
            )
            await m.answer("Qorovul muvaffaqiyatli qo'shildi!")
            await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
            await Main_state.main_menu.set()
        except Exception as _:
            await m.answer("Malumotlarni saqlashda xatolik yuzaga keldi!\nIltimos qaytadan urinib koring:")
            await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
            await Main_state.main_menu.set()
