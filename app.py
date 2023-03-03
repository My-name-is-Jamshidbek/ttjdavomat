"""
app file
"""
from aiogram.types import ContentType as ct

from apps.educator import educators_main_menu, educator_main_menu, educator_qoshish_ism, educator_qoshish_familiya, \
    educator_qoshish_telefon, educator_qoshish_aloqa, educator_qoshish_username, educator_qoshish_parol
from apps.subadmin import subadmins_main_menu, subadmin_main_menu, subadmin_qoshish_ism, subadmin_qoshish_familiya, \
    subadmin_qoshish_telefon, subadmin_qoshish_aloqa, subadmin_qoshish_username, subadmin_qoshish_parol
from loader import dp
from states import *
from apps.login import \
    cmd_start,\
    login_username,\
    login_password
from apps.admin import \
    admin_menu
from apps.student import \
    student_xona, student_xona_turi, student_students, student_students_menu, student_qoshish_name, \
    student_qoshish_surname, student_qoshish_qavat, student_qoshish_room_number, student_qoshish_room_type, \
    student_qoshish_gender, student_qoshish_photo, student_qoshish_phone_number, student_qoshish_aloqa, \
    student_qoshish_addres

# cmd start
dp.register_message_handler(cmd_start, content_types=[ct.TEXT])

# login username
dp.register_message_handler(login_username, state=state_login.username, content_types=[ct.TEXT])

# login password
dp.register_message_handler(login_password, state=state_login.password, content_types=[ct.TEXT])


# ADMIN
## main menu
dp.register_message_handler(admin_menu, state=state_admin.main_menu, content_types=[ct.TEXT])

## students
dp.register_message_handler(student_xona, state=state_admin.student_xona, content_types=[ct.TEXT])
dp.register_message_handler(student_xona_turi, state=state_admin.student_xona_turi, content_types=[ct.TEXT])
dp.register_message_handler(student_students, state=state_admin.student_students, content_types=[ct.TEXT])
dp.register_message_handler(student_students_menu, state=state_admin.student_students_menu, content_types=[ct.TEXT])

## student add
dp.register_message_handler(student_qoshish_name, state=state_admin.student_qoshish_name, content_types=[ct.TEXT])
dp.register_message_handler(student_qoshish_surname, state=state_admin.student_qoshish_surname, content_types=[ct.TEXT])
dp.register_message_handler(student_qoshish_qavat, state=state_admin.student_qoshish_qavat, content_types=[ct.TEXT])
dp.register_message_handler(student_qoshish_room_number, state=state_admin.student_qoshish_room_number, content_types=[ct.TEXT])
dp.register_message_handler(student_qoshish_room_type, state=state_admin.student_qoshish_room_type, content_types=[ct.TEXT])
dp.register_message_handler(student_qoshish_gender, state=state_admin.student_qoshish_gender, content_types=[ct.TEXT])
dp.register_message_handler(student_qoshish_photo, state=state_admin.student_qoshish_photo, content_types=[ct.TEXT,
                                                                                                           ct.PHOTO])
dp.register_message_handler(student_qoshish_phone_number, state=state_admin.student_qoshish_phone_number, content_types=[ct.TEXT])
dp.register_message_handler(student_qoshish_aloqa, state=state_admin.student_qoshish_aloqa, content_types=[ct.TEXT])
dp.register_message_handler(student_qoshish_addres, state=state_admin.student_qoshish_addres, content_types=[ct.TEXT])

## educators
dp.register_message_handler(educators_main_menu, state=state_admin.educators_main_menu, content_types=[ct.TEXT])
dp.register_message_handler(educator_main_menu, state=state_admin.educator_main_menu, content_types=[ct.TEXT])
## educator add
dp.register_message_handler(educator_qoshish_ism, state=state_admin.educator_qoshish_ism, content_types=[ct.TEXT])
dp.register_message_handler(educator_qoshish_familiya, state=state_admin.educator_qoshish_familiya, content_types=[
    ct.TEXT])
dp.register_message_handler(educator_qoshish_telefon, state=state_admin.educator_qoshish_telefon, content_types=[
    ct.TEXT])
dp.register_message_handler(educator_qoshish_aloqa, state=state_admin.educator_qoshish_aloqa, content_types=[ct.TEXT])
dp.register_message_handler(educator_qoshish_username, state=state_admin.educator_qoshish_username, content_types=[
    ct.TEXT])
dp.register_message_handler(educator_qoshish_parol, state=state_admin.educator_qoshish_parol, content_types=[ct.TEXT])
## admins
dp.register_message_handler(subadmins_main_menu,state=state_admin.subadmins_main_menu, content_types=[ct.TEXT])
dp.register_message_handler(subadmin_main_menu, state=state_admin.subadmin_main_menu, content_types=[ct.TEXT])

## admin add
dp.register_message_handler(subadmin_qoshish_ism, state=state_admin.subadmin_qoshish_ism, content_types=[ct.TEXT])
dp.register_message_handler(subadmin_qoshish_familiya, state=state_admin.subadmin_qoshish_familiya, content_types=[ct.TEXT])
dp.register_message_handler(subadmin_qoshish_telefon, state=state_admin.subadmin_qoshish_telefon, content_types=[ct.TEXT])
dp.register_message_handler(subadmin_qoshish_aloqa, state=state_admin.subadmin_qoshish_aloqa, content_types=[ct.TEXT])
dp.register_message_handler(subadmin_qoshish_username, state=state_admin.subadmin_qoshish_username, content_types=[ct.TEXT])
dp.register_message_handler(subadmin_qoshish_parol, state=state_admin.subadmin_qoshish_parol, content_types=[ct.TEXT])




