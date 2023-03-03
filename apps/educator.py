"""
educators
"""
from aiogram.types import Message as m
from aiogram.dispatcher import FSMContext as s

from buttons.keyboardbuttons import admin_main_menu, btn
from database.database import educator_view_data_by_name, educator_delete_data, educator_insert_data, educator_view_data
from states import state_admin


async def educators_main_menu(m:m, state:s):
    if m.text == "Chiqish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    elif m.text == "Qo'shish":
        await m.answer("Ismni kiriting:", reply_markup=btn(["Bekor qilish"]))
        await state_admin.educator_qoshish_ism.set()
    else:
        data = educator_view_data_by_name(m.text)
        if len(data) != 0:
            await m.answer(f"ID {data[0]}\nIsm: {data[1]}\nFamiliya: {data[2]}\nTelefon: {data[3]}\nAloqa:"
                           f" {data[4]}\nUsername: "
                           f"{data[5]}\nPassword: {data[6]}",
                           reply_markup=btn([
                "O'chirish",
                                                                                                "Chiqish"]))
            await state.update_data(educator_id = data[0])
            await state_admin.educator_main_menu.set()


async def educator_main_menu(m:m, state:s):
    if m.text == "Chiqish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    elif m.text == "O'chirish":
        data = await state.get_data()
        _id = data.get("educator_id")
        educator_delete_data(_id)
        await m.answer("Tarbiyachi o'chirildi!")
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()


async def educator_qoshish_ism(m:m, state:s):
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    else:
        await state.update_data(educator_qoshish_ism=m.text)
        await m.answer("Familiyani kiriting:")
        await state_admin.educator_qoshish_familiya.set()


async def educator_qoshish_familiya(m:m, state:s):
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    else:
        await state.update_data(educator_qoshish_familiya=m.text)
        await m.answer("Telefon raqamini kiriting:")
        await state_admin.educator_qoshish_telefon.set()


async def educator_qoshish_telefon(m:m, state:s):
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    else:
        await state.update_data(educator_qoshish_telefon=m.text)
        await m.answer("Aloqa uchun link kiriting:")
        await state_admin.educator_qoshish_aloqa.set()


async def educator_qoshish_aloqa(m:m, state:s):
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    else:
        await state.update_data(educator_qoshish_username=m.text)
        await m.answer("Username kiriting:")
        await state_admin.educator_qoshish_username.set()




async def educator_qoshish_username(m:m, state:s):
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    else:
        if len(educator_view_data(m.text))==0:
            await state.update_data(educator_qoshish_username=m.text)
            await m.answer("Parolni kiriting:")
            await state_admin.educator_qoshish_parol.set()
        else:
            await m.answer("Bu username allaqachon bant!\nIltimos yangi username kiriting:")
async def educator_qoshish_parol(m:m, state:s):
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    else:
        try:
            data = await state.get_data()
            educator_insert_data(
                ism=data.get("educator_qoshish_ism"),
                familiya=data.get("educator_qoshish_familiya"),
                telefon=data.get("educator_qoshish_telefon"),
                aloqa=data.get("educator_qoshish_aloqa"),
                username=data.get("educator_qoshish_username"),
                parol=m.text
            )
            await m.answer("Tarbiyachi muvaffaqiyatli qo'shildi!")
            await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
            await state_admin.main_menu.set()
        except:
            await m.answer("Malumotlarni saqlashda xatolik yuzaga keldi!\nIltimos qaytadan urinib koring:")
            await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
            await state_admin.main_menu.set()
