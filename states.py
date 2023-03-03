"""
states
"""
from aiogram.dispatcher.filters.state import State, StatesGroup

class state_login(StatesGroup):
    main_menu = State()
    username = State()
    password = State()


class state_admin(StatesGroup):
    state_name = State()

    main_menu = State()

    student_xona = State()
    student_xona_turi = State()
    student_students = State()

    student_name = State()
    student_surname = State()

    student_students_menu = State()

    student_tahrirlash= State()

    student_qoshish = State()

    student_qoshish_name = State()
    student_qoshish_surname = State()
    student_qoshish_qavat = State()
    student_qoshish_room_number = State()
    student_qoshish_room_type = State()
    student_qoshish_gender = State()
    student_qoshish_photo = State()
    student_qoshish_phone_number = State()
    student_qoshish_aloqa = State()
    student_qoshish_addres = State()

    educators_main_menu = State()
    educator_main_menu = State()
    educator_id = State()

    subadmins_main_menu = State()
    subadmin_main_menu = State()

    subadmin_id = State()

    subadmin_qoshish_ism = State()
    subadmin_qoshish_familiya = State()
    subadmin_qoshish_telefon = State()
    subadmin_qoshish_aloqa = State()
    subadmin_qoshish_username = State()
    subadmin_qoshish_parol = State()

    educator_qoshish_ism = State()
    educator_qoshish_familiya = State()
    educator_qoshish_telefon = State()
    educator_qoshish_aloqa = State()
    educator_qoshish_username = State()
    educator_qoshish_parol = State()
class state_subadmin(StatesGroup):
    main_menu = State()


class state_educator(StatesGroup):
    main_menu = State()

class state_student(StatesGroup):
    state_name = State()