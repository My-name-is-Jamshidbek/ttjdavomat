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

    # print("Database created")

    import pandas as pd

    # Excel faylini yuklash
    df = pd.read_excel('data.xlsx')

    d = df.iterrows()
    # Faylni qatorma-qator o'qish
    for index, row in df.iterrows():
        gr = row["Гурух рақами"]
        name_surname = row["Ф.И.О"]
        xona_raqami = row["Хона рақами"]
        if len(str(xona_raqami)) != 3:
            xr = xona_raqami

        if len(str(gr)) == 3 or len(str(name_surname)) == 3:
            pass
        else:
            surname = name_surname.split()[0]
            name = name_surname.split()[1]
            qavat = str(xr[0])
            room_number = str(xr.split('-')[0])
            room_type = xr.split('-')[1]
            if room_type == 'А':
                room_type="A"
            else:
                room_type="B"
            if surname[-1] == 'а':
                gender = 'Ayol'
            elif surname[-1] == 'в':
                gender = 'Erkak'
            else:
                gender = 'Kiritilmagan'
            photo = 'Kiritilmagan'
            username = surname+'_'+name
            password = surname+'_'+name
            phone_number = 'Kiritilmagan'
            aloqa = 'Kiritilamagn'
            address = 'Kiritilmagan'
            print(name,surname,qavat,room_number,room_type,gender,photo,username,password,phone_number,aloqa,address)
            student_insert_data(
                name=name,
                surname=surname,
                qavat=qavat,
                room_number=room_number,
                room_type=room_type,
                gender=gender,
                photo=photo,
                username=username,
                password=password,
                phone_number=phone_number,
                aloqa=aloqa,
                address=address
            )
        # print(gr)
    # for i in range(300):
    #     student_insert_data(
    #         name=f"student_name {i}",
    #         surname=f"surname_{i}",
    #         qavat=str(random.randint(1, 5)),
    #         room_number=str(random.randint(1, 50)),
    #         room_type=f"{chr(random.randint(65, 67))}",
    #         gender=f"{chr(random.randint(71, 73))}",
    #         photo="NO",
    #         username=f"username_{i}",
    #         password=f"password_{i}",
    #         phone_number=str(random.randint(990000000, 999999999)),
    #         aloqa=f"aloqa_{i}",
    #         address="Xorazm Bagatdatabase_test_create()
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

# print(attendance_datas())
#
# for i in student_view_id_by_qavat('2'):
#     print(student_view_data_by_id(i))
