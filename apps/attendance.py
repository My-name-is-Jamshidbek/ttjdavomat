"""
attendance
"""
import os
import random

from aiogram.types import Message as m, InputFile
from aiogram.dispatcher import FSMContext as s

from buttons.keyboardbuttons import btn
from config import menus
from database.database import student_view_qavat, student_view_id_by_qavat, student_view_attendance_data_by_id, \
    attendance_save, attendance_export_data_to_excel
from states import Main_state


async def attendance_menu(m:m,state:s):
    if m.text == "Chiqish":
        data = await state.get_data()
        user = data.get("user_name")
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        qavatlar = student_view_qavat()
        if m.text in qavatlar:
            ids1 = student_view_id_by_qavat(m.text)
            _id = ids1.pop(0)
            if ids1[0] == '':t = False
            else:t = True
            ids = ""
            for i in ids1:ids+=str(i)+"_"
            await state.update_data(attendance_data=" ")
            await state.update_data(attendance_qavat=ids)
            await state.update_data(attendance_id=_id)
            data = student_view_attendance_data_by_id(_id)
            try:
                photo = data[7]
            except:
                print(data)
            try:
                await m.answer_photo(
                    photo=InputFile(photo),
                    caption=f"Ism: {data[1]}.\n"
                            f"Familiya: {data[2]}.\n"
                            f"Qavat: {data[3]}.\n"
                            f"Xona: {data[4]} {data[5]}.\n"
                            f"Jinsi: {data[6]}.\n"
                            f"Telefon: {data[10]}.\n"
                            f"Aloqa: {data[11]}.\n"
                            f"Manzil: {data[12]}.",
                    reply_markup=btn(["Bor", "Yo'q", "Chiqish"]))
            except Exception as e:
                print(e)
                await m.answer(text=f"Ism: {data[1]}.\n"
                                    f"Familiya: {data[2]}.\n"
                                    f"Qavat: {data[3]}.\n"
                                    f"Xona: {data[4]} {data[5]}.\n"
                                    f"Jinsi: {data[6]}.\n"
                                    f"Telefon: {data[10]}.\n"
                                    f"Aloqa: {data[11]}.\n"
                                    f"Manzil: {data[12]}.",
                               reply_markup=btn(["Bor", "Yo'q", "Chiqish"]))
            if t:await Main_state.attendance_main.set()
            else:await Main_state.attendance_stop.set()


async def attendance_main(m:m, state:s):
    if m.text == "Chiqish":
        data = await state.get_data()
        user = data.get("user_name")
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        data = await state.get_data()
        ids1 = data.get("attendance_qavat").split("_")
        a_id = data.get("attendance_id")
        a_data = data.get("attendance_data")
        _id = ids1.pop(0)
        if ids1[0] == '':t = False
        else:t = True
        ids = ""
        for i in ids1:ids+=i+"_"
        a_data += str(a_id)+'_'+str(m.text)+"|"
        await state.update_data(attendance_data=a_data)
        await state.update_data(attendance_id=_id)
        await state.update_data(attendance_qavat=ids)
        data = student_view_attendance_data_by_id(_id)
        try:photo = data[7]
        except:print(data)
        try:
            await m.answer_photo(
                photo=InputFile(photo),
                caption=f"Ism: {data[1]}.\n"
                                f"Familiya: {data[2]}.\n"
                                f"Qavat: {data[3]}.\n"
                                f"Xona: {data[4]} {data[5]}.\n"
                                f"Jinsi: {data[6]}.\n"
                                f"Telefon: {data[10]}.\n"
                                f"Aloqa: {data[11]}.\n"
                                f"Manzil: {data[12]}.",
                           reply_markup=btn(["Bor", "Yo'q", "Chiqish"]))
        except Exception as e:
            print(e)
            await m.answer(text=f"Ism: {data[1]}.\n"
                                f"Familiya: {data[2]}.\n"
                                f"Qavat: {data[3]}.\n"
                                f"Xona: {data[4]} {data[5]}.\n"
                                f"Jinsi: {data[6]}.\n"
                                f"Telefon: {data[10]}.\n"
                                f"Aloqa: {data[11]}.\n"
                                f"Manzil: {data[12]}.",
                           reply_markup=btn(["Bor", "Yo'q", "Chiqish"]))
        if t:await Main_state.attendance_main.set()
        else:await Main_state.attendance_stop.set()
async def attendance_stop(m:m, state:s):
    if m.text == "Chiqish":
        data = await state.get_data()
        user = data.get("user_name")
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        data = await state.get_data()
        qavat = data.get("attendance_qavat")
        a_id = data.get("attendance_id")
        a_data = data.get("attendance_data")
        a_data+=a_id+"_"+m.text
        if attendance_save(a_data, data.get("educator_id")):
            await m.answer("Yoqlama muvaffaqiyatli saqlandi!")
            qavatlar = student_view_qavat()
            qavatlar.append("Chiqish")
            await m.answer("Qavatni tanlang:", reply_markup=btn(qavatlar))
            await Main_state.attendance_qavat.set()
        else:
            await m.answer("Yoqlamani saqlashda muammo yuzaga keldi!")
            qavatlar = student_view_qavat()
            qavatlar.append("Chiqish")
            await m.answer("Qavatni tanlang:", reply_markup=btn(qavatlar))
            await Main_state.attendance_qavat.set()


async def attendances(m:m, state:s):
    if m.text == "Chiqish":
        data = await state.get_data()
        user = data.get("user_name")
        await m.answer("Kerakli menyuni tanlang:", reply_markup=btn(menus[user]))
        await Main_state.main_menu.set()
    else:
        try:
            year = m.text.split(".")[0]
            month = m.text.split(".")[1]
            day = m.text.split(".")[2]
            name = attendance_export_data_to_excel(str(random.randint(10000,99999)), year=year,
                                                   month=month,
                                                       day=day)
            document = InputFile(name)
            await m.answer_document(document=document)
            os.remove(name)
        except Exception as _:
            await m.answer("Malumotlarni yuklashda xatolik yuzaga keldi!")