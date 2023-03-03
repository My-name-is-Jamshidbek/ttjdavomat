"""
subadmin
"""
from aiogram.types import Message as m
from aiogram.dispatcher import FSMContext as s

from buttons.keyboardbuttons import admin_main_menu, btn
from database.database import subadmin_view_data_by_name, subadmin_delete_data, subadmin_view_data, subadmin_insert_data
from states import state_admin


async def subadmins_main_menu(m:m, state:s):
    if m.text == "Chiqish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    elif m.text == "Qo'shish":
        await m.answer("Ismni kiriting:", reply_markup=btn(["Bekor qilish"]))
        await state_admin.subadmin_qoshish_ism.set()
    else:
        data = subadmin_view_data_by_name(m.text)
        if len(data) != 0:
            await m.answer(f"ID {data[0]}\nIsm: {data[1]}\nFamiliya: {data[2]}\nTelefon: {data[3]}\nAloqa:"
                           f" {data[4]}\nUsername: "
                           f"{data[5]}\nPassword: {data[6]}",
                           reply_markup=btn(["O'chirish", "Chiqish"]))
            await state.update_data(subadmin_id = data[0])
            await state_admin.subadmin_main_menu.set()


async def subadmin_main_menu(m:m, state:s):
    if m.text == "Chiqish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    elif m.text == "O'chirish":
        data = await state.get_data()
        _id = data.get("subadmin_id")
        subadmin_delete_data(_id)
        await m.answer("Admin o'chirildi!")
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()


async def subadmin_qoshish_ism(m:m, state:s):
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    else:
        await state.update_data(subadmin_qoshish_ism=m.text)
        await m.answer("Familiyani kiriting:")
        await state_admin.subadmin_qoshish_familiya.set()


async def subadmin_qoshish_familiya(m:m, state:s):
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    else:
        await state.update_data(subadmin_qoshish_familiya=m.text)
        await m.answer("Telefon raqamini kiriting:")
        await state_admin.subadmin_qoshish_telefon.set()


async def subadmin_qoshish_telefon(m:m, state:s):
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    else:
        await state.update_data(subadmin_qoshish_telefon=m.text)
        await m.answer("Aloqa uchun link kiriting:")
        await state_admin.subadmin_qoshish_aloqa.set()


async def subadmin_qoshish_aloqa(m:m, state:s):
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    else:
        await state.update_data(subadmin_qoshish_username=m.text)
        await m.answer("Username kiriting:")
        await state_admin.subadmin_qoshish_username.set()




async def subadmin_qoshish_username(m:m, state:s):
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    else:
        if subadmin_view_data(m.text) is None:
            await state.update_data(subadmin_qoshish_username=m.text)
            await m.answer("Parolni kiriting:")
            await state_admin.subadmin_qoshish_parol.set()
        else:
            await m.answer("Bu username allaqachon bant!\nIltimos yangi username kiriting:")
async def subadmin_qoshish_parol(m:m, state:s):
    if m.text == "Bekor qilish":
        await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
        await state_admin.main_menu.set()
    else:
        try:
            data = await state.get_data()
            subadmin_insert_data(
                ism=data.get("subadmin_qoshish_ism"),
                familiya=data.get("subadmin_qoshish_familiya"),
                telefon=data.get("subadmin_qoshish_telefon"),
                aloqa=data.get("subadmin_qoshish_aloqa"),
                username=data.get("subadmin_qoshish_username"),
                parol=m.text
            )
            await m.answer("Admin muvaffaqiyatli qo'shildi!")
            await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
            await state_admin.main_menu.set()
        except:
            await m.answer("Malumotlarni saqlashda xatolik yuzaga keldi!\nIltimos qaytadan urinib koring:")
            await m.answer("Kerakli menyuni tanlang:", reply_markup=admin_main_menu)
            await state_admin.main_menu.set()