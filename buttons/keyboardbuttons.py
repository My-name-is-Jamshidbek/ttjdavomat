"""
buttons reply
"""
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from database.database import student_view_rooms, student_view_room_types, student_view_by_room_and_type, \
    educator_view_data_name, subadmins_view_data_name

login_buttons_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
login_buttons_menu.add("Dasturchi malumoti")

admin_main_menu = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
admin_main_menu.add("Yoqlama jadvallari")
admin_main_menu.add("Adminlar")
admin_main_menu.add("Tarbiyachilar")
admin_main_menu.add("Studentlar")
admin_main_menu.add("Student qoshish")
admin_main_menu.add("Chiqish")


subadmin_main_menu = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
subadmin_main_menu.add("Yoqlama jadvallari")
subadmin_main_menu.add("educatorlar")
subadmin_main_menu.add("Studentlar")
subadmin_main_menu.add("Student qoshish")
subadmin_main_menu.add("Chiqish")


educator_main_menu = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
educator_main_menu.add("Yoqlama jadvallari")
educator_main_menu.add("studentlar")
educator_main_menu.add("yo'qlama olish")
educator_main_menu.add("Chiqish")


def btn_student_xonalari():
    """
    :return:
    """
    rooms = student_view_rooms()
    btn = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    for i in range(2,len(rooms), 3): btn.add(str(rooms[i-2]), str(rooms[i-1]), str(rooms[i]))
    if len(rooms)-i == 3: btn.add(str(rooms[i+1]), str(rooms[i+2]))
    if len(rooms) - i == 2: btn.add(str(rooms[i + 1]))
    btn.add("Chiqish")
    return  btn

def btn_student_xona_turlari(room):
    """
    :return:
    """
    rooms = student_view_room_types(room)
    btn = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    for i in range(2, len(rooms), 3): btn.add(str(rooms[i - 2]), str(rooms[i - 1]), str(rooms[i]))
    if len(rooms) - i == 3: btn.add(str(rooms[i + 1]), str(rooms[i + 2]))
    if len(rooms) - i == 2: btn.add(str(rooms[i + 1]))
    btn.add("Chiqish")
    return  btn


def btn_students_xona(room: str, type: str) -> None:
    """
    :return:
    """
    rooms = student_view_by_room_and_type(room, type)
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    for i in rooms: btn.add(str(i))
    btn.add("Chiqish")
    return btn


def btn(btns):
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    for i in btns: btn.add(str(i))
    return btn


def btn_educators():
    names = educator_view_data_name()
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    for i in names: btn.add(str(i))
    btn.add("Qo'shish")
    btn.add("Chiqish")
    return btn


def btn_admins():
    names = subadmins_view_data_name()
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    for i in names: btn.add(str(i))
    btn.add("Qo'shish")
    btn.add("Chiqish")
    return btn
