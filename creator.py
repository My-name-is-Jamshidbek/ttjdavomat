"""
environment create
"""
import random

from database.database import *


def database_test_create():
    """
    :return:
    """
    create_database()

    print("Database created")

    for i in range(300):
        student_insert_data(
            name=f"student_name {i}",
            surname=f"surname_{i}",
            qavat=str(random.randint(1, 5)),
            room_number=str(random.randint(1, 50)),
            room_type=f"{chr(random.randint(65, 67))}",
            gender=f"{chr(random.randint(71, 73))}",
            photo="NO",
            username=f"username_{i}",
            password=f"password_{i}",
            phone_number=str(random.randint(990000000, 999999999)),
            aloqa=f"aloqa_{i}",
            address="Xorazm Bagat"
        )

    # for i in range(3):
    #     educator_insert_data(
    #         ism=f"educator_name_{i}",
    #         familiya=f"educator_familiya_{i}",
    #         telefon=str(random.randint(990000000, 999999999)),
    #         username=f"username_{i}",
    #         parol=f"password_{i}",
    #         aloqa=f"aloqa_{i}",
    #     )
    #
    # for i in range(20):
    #     for ids in student_view_data_all_id():
    #         attendance_insert_data(
    #             student_id=ids[0],
    #             attendance=chr(random.randint(0, 1)),
    #             reason="NO",
    #             educator_id=str(random.randint(1, 3)),
    #             year=str(i),
    #             month=str(i),
    #             day=str(i),
    #             time=str("00:00")
    #         )
    # attendance_export_data_to_excel("test1", str(1), str(1), str(1))
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

# names = subadmins_view_data_name()
# # print(names)
# print(student_view_attendance_data_by_id(3002))

#
# attendance_save(
#     data="188_Bor|228_Bor|190_Bor|218_Bor|220_Bor|219_Bor|135_Bor|148_Bor|85_Bor|147_Bor|169_Bor|256_Bor|66_Bor"
#          "|163_Bor|274_Bor|24_Bor|296_Bor|166_Bor|174_Bor|222_Bor|19_Bor|268_Bor|16_Bor|288_Bor|240_Bor|251_Bor|295_Bor|200_Bor|211_Bor|81_Bor|191_Bor|34_Bor|128_Bor|138_Bor|8_Bor|159_Bor|21_Bor|3_Bor|102_Bor|234_Bor|48_Bor|7_Bor|49_Bor|140_Bor|277_Bor|76_Bor|15_Bor|93_Bor|233_Bor|59_Bor|43_Bor|91_Bor|73_Bor|203_Bor|151_Bor|80_Bor|87_Bor|139_Bor|36_Bor|54_Bor|98_Bor|23_Bor|278_Bor|82_Bor|116_Bor|257_Bor",
#     educator="1"
# )

print(attendance_datas())