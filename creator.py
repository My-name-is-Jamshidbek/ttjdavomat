"""
environment create
"""
from database.database import *


def database_test_create():
    """
    :return:
    """
    create_database()

    print("Database created")

    for i in range(3000):
        student_insert_data(
            name=f"student_name {i}",
            surname=f"surname_{i}",
            qavat=str(random.randint(1, 5)),
            room_number=str(random.randint(1, 50)),
            room_type=f"{chr(random.randint(65, 90))}",
            gender=f"{chr(random.randint(71, 75))}",
            photo="NO",
            username=f"username_{i}",
            password=f"password_{i}",
            phone_number=str(random.randint(990000000, 999999999)),
            aloqa=f"aloqa_{i}",
            address="Xorazm Bagat"
        )

    for i in range(3):
        educator_insert_data(
            ism=f"educator_name_{i}",
            familiya=f"educator_familiya_{i}",
            telefon=str(random.randint(990000000, 999999999)),
            username=f"username_{i}",
            parol=f"password_{i}",
            aloqa=f"aloqa_{i}",
        )

    for i in range(20):
        for ids in student_view_data_all_id():
            attendance_insert_data(
                student_id=ids[0],
                attendance=chr(random.randint(0, 1)),
                reason="NO",
                educator_id=str(random.randint(1, 3)),
                year=str(i),
                month=str(i),
                day=str(i),
                time=str("00:00")
            )
    attendance_export_data_to_excel("test1", str(1), str(1), str(1))
    admin_insert_data(
        ism="Jamshidbek",
        familiya="Ollanazarov",
        telefon="+998 91 277 96 93",
        aloqa="https://t.me/mal_un",
        username="jamshidbekollanazarov",
        parol="Jamshid_bek2003."
    )
    print("Database full created")

# database_test_create()
#
# print(student_view_room_types(1))
#
# subadmin_insert_data(
#     ism="Jamshidbek",
#     familiya="Ollanazarov",
#     telefon="912779693",
#     aloqa="t.me/mal_un",
#     username="jamshidbekollanazarov",
#     parol="Jamshid_bek2003."
# )

names = subadmins_view_data_name()
print(names)