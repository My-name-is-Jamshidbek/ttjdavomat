"""
states
"""
from aiogram.dispatcher.filters.state import State, StatesGroup


class Main_state(StatesGroup):
    """
    main state
    """
    login_main_menu = State()
    username = State()
    password = State()

    user_name = State()
    state_name = State()

    main_menu = State()

    student_xona = State()
    student_xona_turi = State()
    student_students = State()

    student_name = State()
    student_surname = State()

    student_students_menu = State()

    student_tahrirlash = State()

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

    qorovuls_main_menu = State()
    qorovul_main_menu = State()

    qorovul_id = State()

    qorovul_qoshish_ism = State()
    qorovul_qoshish_familiya = State()
    qorovul_qoshish_telefon = State()
    qorovul_qoshish_aloqa = State()
    qorovul_qoshish_username = State()
    qorovul_qoshish_parol = State()

    educator_qoshish_ism = State()
    educator_qoshish_familiya = State()
    educator_qoshish_telefon = State()
    educator_qoshish_aloqa = State()
    educator_qoshish_username = State()
    educator_qoshish_parol = State()

    attendance = State()

    attendance_qavat = State()
    attendance_id = State()
    attendance_data = State()
    attendance_main = State()

    attendance_stop = State()

    attendances = State()
