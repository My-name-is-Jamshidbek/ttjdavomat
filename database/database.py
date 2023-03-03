"""
data base
"""
import random

import xlsxwriter

from config import DATABASE_NAME
# import pandas as pd
import sqlite3


# create database
def create_database():
    """
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    conn.execute('''CREATE TABLE IF NOT EXISTS Dasturchi
           (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
           Tugilgan_yil            INT     NOT NULL,
           Ism            TEXT    NOT NULL,
           Familiya        TEXT    NOT NULL,
           Oqish_joyi     TEXT    NOT NULL,
           Loyihalar       TEXT,
           Telefon         TEXT,
           Aloqa           TEXT);''')
    conn.execute('''CREATE TABLE IF NOT EXISTS Adminlar
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     Ism TEXT NOT NULL,
                     Familiya TEXT NOT NULL,
                     Telefon TEXT NOT NULL,
                     Aloqa TEXT NOT NULL,
                     Username TEXT NOT NULL,
                     Parol TEXT NOT NULL);''')
    conn.execute('''CREATE TABLE IF NOT EXISTS SubAdminlar
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Ism TEXT NOT NULL,
                    Familiya TEXT NOT NULL,
                    Telefon TEXT NOT NULL,
                    Aloqa TEXT NOT NULL,
                    Username TEXT NOT NULL UNIQUE,
                    Parol TEXT NOT NULL);''')
    conn.execute('''CREATE TABLE IF NOT EXISTS Educatorlar
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Ism TEXT NOT NULL,
                    Familiya TEXT NOT NULL,
                    Telefon TEXT NOT NULL,
                    Aloqa TEXT NOT NULL,
                    Username TEXT NOT NULL UNIQUE,
                    Parol TEXT NOT NULL);''')
    conn.execute('''CREATE TABLE IF NOT EXISTS students 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  surname TEXT NOT NULL,
                  qavat TEXT,
                  room_number TEXT,
                  room_type TEXT,
                  gender TEXT,
                  photo BLOB,
                  username TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL,
                  phone_number TEXT,
                  aloqa TEXT NOT NULL,
                  address TEXT)''')
    conn.execute('''CREATE TABLE IF NOT EXISTS Adminlar
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         Ism TEXT NOT NULL,
                         Familiya TEXT NOT NULL,
                         Telefon TEXT NOT NULL,
                         Aloqa TEXT NOT NULL,
                         Username TEXT NOT NULL,
                         Parol TEXT NOT NULL);''')
    conn.execute('''CREATE TABLE IF NOT EXISTS attendance (
                          student_id INTEGER,
                          attendance TEXT,
                          reason TEXT,
                          educator_id INTEGER,
                          year INTEGER,
                          month INTEGER,
                          day INTEGER,
                          time TEXT);''')

    conn.commit()

    conn.close()


# programmer
## create
def programmer_insert_data(tugilgan_yil, ism, familiya, oqish_joyi, loyihalar='', telefon='', aloqa=''):
    """
    :param tugilgan_yil:
    :param ism:
    :param familiya:
    :param oqish_joyi:
    :param loyihalar:
    :param telefon:
    :param aloqa:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    conn.execute(
        f'INSERT INTO Dasturchi (Tugilgan_yil, Ism, Familiya, Oqish_joyi, Loyihalar, Telefon, Aloqa) VALUES '
        f'({tugilgan_yil}, \'{ism}\', \'{familiya}\', \'{oqish_joyi}\', \'{loyihalar}\', \'{telefon}\', \'{aloqa}\')')

    conn.commit()

    conn.close()


## read
def programmer_get_data():
    """
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.execute("SELECT ID, Tugilgan_yil, Ism, Familiya, Oqish_joyi, Loyihalar, Telefon, "
                          "Aloqa from Dasturchi")
    rows = cursor.fetchall()

    conn.close()

    return rows


## update
def programmer_update_data(_id, tugilgan_yil=None, ism=None, familiya=None, oqish_joyi=None, loyihalar=None,
                           telefon=None, aloqa=None):
    """
    :param _id:
    :param tugilgan_yil:
    :param ism:
    :param familiya:
    :param oqish_joyi:
    :param loyihalar:
    :param telefon:
    :param aloqa:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    fields = []
    if tugilgan_yil is not None:
        fields.append(f"Tugilgan_yil = {tugilgan_yil}")
    if ism is not None:
        fields.append(f"Ism = '{ism}'")
    if familiya is not None:
        fields.append(f"Familiya = '{familiya}'")
    if oqish_joyi is not None:
        fields.append(f"Oqish_joyi = '{oqish_joyi}'")
    if loyihalar is not None:
        fields.append(f"Loyihalar = '{loyihalar}'")
    if telefon is not None:
        fields.append(f"Telefon = '{telefon}'")
    if aloqa is not None:
        fields.append(f"Aloqa = '{aloqa}'")

    query = f"UPDATE Dasturchilar SET {', '.join(fields)} WHERE ID = {_id}"

    conn.execute(query)

    conn.commit()

    conn.close()


# admin
## create
def admin_insert_data(ism, familiya, telefon, aloqa, username, parol):
    """
    :param ism:
    :param familiya:
    :param telefon:
    :param aloqa:
    :param username:
    :param parol:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    conn.execute(
        f"INSERT INTO Adminlar (Ism, Familiya, Telefon, Aloqa, Username, Parol) VALUES ('{ism}', '{familiya}', "
        f"'{telefon}', '{aloqa}', '{username}', '{parol}')")

    conn.commit()

    conn.close()


## read
def admin_check(username, password):
    """
    :param username:
    :param password:
    :return:
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)

        cursor = conn.execute(f"SELECT * FROM Adminlar WHERE Username = ? and Parol = ?", (username, password))

        data = cursor.fetchall()

        if len(data) == 0:
            return False
        else:
            return True
    except:
        return False


def admin_view_data():
    """
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.execute("SELECT * FROM Adminlar")

    data = cursor.fetchall()

    conn.close()

    return data


## update
def admin_update_data(_id, ism=None, familiya=None, telefon=None, aloqa=None, username=None, parol=None):
    """
    :param _id:
    :param ism:
    :param familiya:
    :param telefon:
    :param aloqa:
    :param username:
    :param parol:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    set_query = ""
    if ism:
        set_query += f"Ism = '{ism}',"
    if familiya:
        set_query += f"Familiya = '{familiya}',"
    if telefon:
        set_query += f"Telefon = '{telefon}',"
    if aloqa:
        set_query += f"Aloqa = '{aloqa}',"
    if username:
        set_query += f"Username = '{username}',"
    if parol:
        set_query += f"Parol = '{parol}',"
    set_query = set_query.rstrip(',')

    conn.execute(f"UPDATE Adminlar SET {set_query} WHERE ID = {_id}")

    conn.commit()

    conn.close()


## delete
def admin_delete_data(_id):
    """
    :param _id:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    conn.execute(f"DELETE FROM Adminlar WHERE ID = {_id}")

    conn.commit()

    conn.close()


# subadmin
## create
def subadmin_insert_data(ism, familiya, telefon, aloqa, username, parol):
    """
    :param ism:
    :param familiya:
    :param telefon:
    :param aloqa:
    :param username:
    :param parol:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    conn.execute(
        f"INSERT INTO SubAdminlar (Ism, Familiya, Telefon, Aloqa, Username, Parol) VALUES ('{ism}', '{familiya}', "
        f"'{telefon}', '{aloqa}', '{username}', '{parol}')")

    conn.commit()

    conn.close()


## read
def subadmin_check(username, password):
    """
    :param username:
    :param password:
    :return:
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)

        cursor = conn.execute(f"SELECT * FROM SubAdminlar WHERE Username = ? and Parol = ?", (username, password))

        data = cursor.fetchall()

        if len(data) == 0:
            return False
        else:
            return True
    except:
        return False


def subadmin_view_data(username):
    """
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.execute("SELECT * FROM SubAdminlar WHERE Username = ?", (username,))

    data = cursor.fetchone()

    conn.close()

    return data


def subadmins_view_data_name():
    """
    :return:
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)

        cursor = conn.execute("SELECT Ism FROM SubAdminlar")

        data = list(tuple([i[0] for i in cursor.fetchall()]))
    except:
        data = []
    conn.close()

    return data


def subadmin_view_data_by_name(name):
    """
    :return:
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)

        cursor = conn.execute("SELECT * FROM SubAdminlar WHERE Ism = ?", (name,))

        data = cursor.fetchone()

        conn.close()
    except:
        data=[]
    return data




## update
def subadmin_update_data(_id, ism=None, familiya=None, telefon=None, aloqa=None, username=None, parol=None):
    """
    :param _id:
    :param ism:
    :param familiya:
    :param telefon:
    :param aloqa:
    :param username:
    :param parol:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    set_query = ""
    if ism:
        set_query += f"Ism = '{ism}',"
    if familiya:
        set_query += f"Familiya = '{familiya}',"
    if telefon:
        set_query += f"Telefon = '{telefon}',"
    if aloqa:
        set_query += f"Aloqa = '{aloqa}',"
    if username:
        set_query += f"Username = '{username}',"
    if parol:
        set_query += f"Parol = '{parol}',"
    set_query = set_query.rstrip(',')

    conn.execute(f"UPDATE SubAdminlar SET {set_query} WHERE ID = {_id}")

    conn.commit()

    conn.close()


## delete
def subadmin_delete_data(_id):
    """
    :param _id:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    conn.execute(f"DELETE FROM SubAdminlar WHERE ID = {_id}")

    conn.commit()

    conn.close()


# educator
## crete
def educator_insert_data(ism, familiya, telefon, aloqa, username, parol):
    """
    :param ism:
    :param familiya:
    :param telefon:
    :param aloqa:
    :param username:
    :param parol:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    conn.execute(
        f"INSERT INTO educatorlar (Ism, Familiya, Telefon, Aloqa, Username, Parol) VALUES ('{ism}', '{familiya}', "
        f"'{telefon}', '{aloqa}', '{username}', '{parol}')")

    conn.commit()

    conn.close()


## read
def educator_view_data_name():
    """
    :return:
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)

        cursor = conn.execute("SELECT Ism FROM Educatorlar")

        data = cursor.fetchall()

        data = list(tuple([i[0] for i in data]))
    except:
        data = []
    conn.close()

    return data


def educator_view_data_by_name(name):
    """
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.execute("SELECT * FROM Educatorlar WHERE Ism = ?", (name,))

    data = cursor.fetchall()

    conn.close()

    return data[0]


def educator_view_data(username):
    """
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.execute("SELECT * FROM Educatorlar WHERE Username = ?", (username,))

    data = cursor.fetchall()

    conn.close()

    return data


def educator_check(username, password):
    """
    :param username:
    :param password:
    :return:
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)

        cursor = conn.execute(f"SELECT * FROM Educatorlar WHERE Username = ? and Parol = ?", (username,password))

        data = cursor.fetchall()

        if len(data) == 0:
            return False
        else:
            return True
    except:
        return False


def educator_view_data_by_id(_id):
    """
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.execute(f"SELECT * FROM Educatorlar WHERE ID = ?", (_id,))

    data = cursor.fetchall()

    conn.close()

    return data


## update
def educator_update_data(_id, ism=None, familiya=None, telefon=None, aloqa=None, username=None, parol=None):
    """
    :param _id:
    :param ism:
    :param familiya:
    :param telefon:
    :param aloqa:
    :param username:
    :param parol:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    set_query = ""
    if ism:
        set_query += f"Ism = '{ism}',"
    if familiya:
        set_query += f"Familiya = '{familiya}',"
    if telefon:
        set_query += f"Telefon = '{telefon}',"
    if aloqa:
        set_query += f"Aloqa = '{aloqa}',"
    if username:
        set_query += f"Username = '{username}',"
    if parol:
        set_query += f"Parol = '{parol}',"
    set_query = set_query.rstrip(',')

    conn.execute(f"UPDATE educatorlar SET {set_query} WHERE ID = {_id}")

    conn.commit()

    conn.close()


## delete
def educator_delete_data(_id):
    """
    :param _id:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)

    conn.execute(f"DELETE FROM educatorlar WHERE ID = {_id}")

    conn.commit()

    conn.close()


# student
## create
def student_insert_data(name, surname, qavat, room_number, room_type, gender, photo, username, password, phone_number,
                        aloqa, address):
    """
    :param name:
    :param surname:
    :param qavat:
    :param room_number:
    :param room_type:
    :param gender:
    :param photo:
    :param username:
    :param password:
    :param phone_number:
    :param aloqa:
    :param address:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    try:
        c.execute('''INSERT INTO students (name, surname, qavat, room_number, room_type, gender, photo, 
        username, password, phone_number, aloqa, address)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (
                      name, surname, qavat, room_number, room_type, gender, photo, username, password, phone_number,
                      aloqa, address))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    conn.close()


## read
def student_view_rooms():
    """
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''SELECT DISTINCT room_number
                 FROM students''')
    result = c.fetchall()
    conn.close()
    result = sorted([int(i[0]) for i in result])
    return result


def student_view_room_types(room):
    """
    :param room:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''SELECT DISTINCT room_type
                 FROM students WHERE room_number = ? ORDER BY room_type''', (room,))
    result = c.fetchall()
    conn.close()
    result = [i[0] for i in result]
    return result


def student_view_by_room_and_type(room, type):
    """
    :param room:
    :param type:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''SELECT name
                 FROM students WHERE room_number = ? and room_type = ?''', (room, type))
    result = c.fetchall()
    conn.close()
    result = [i[0] for i in result]
    return result


def student_view_data_(room, type, name):
    """
    :param room:
    :param type:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''SELECT name, surname, qavat, room_number, room_type, gender, photo, username, password, phone_number, 
    aloqa, address 
                 FROM students WHERE room_number = ? and room_type = ? and name = ?''', (room, type, name))
    result = c.fetchone()
    conn.close()
    return result


def student_view_data(username, password):
    """
    :param username:
    :param password:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))
    result = c.fetchone()
    conn.close()
    return result


def student_view_data_by_id(_id):
    """
    :param _id:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE id=?", (_id,))
    result = c.fetchone()
    conn.close()
    return result


def student_view_data_all_id():
    """
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''SELECT id FROM students''')
    result = c.fetchall()
    conn.close()
    return result


## update
def student_room_update(room_number, room_type, first_name, last_name, new_room_number, new_room_type):
    """
    :param room_number:
    :param room_type:
    :param first_name:
    :param last_name:
    :param new_room_number:
    :param new_room_type:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute(
        '''UPDATE students SET room_number = ?, room_type = ? WHERE room_number = ? AND room_type = ? AND first_name 
        = ? AND last_name = ?''',
        (new_room_number, new_room_type, room_number, room_type, first_name, last_name))
    conn.commit()
    conn.close()


## delete
def student_delete_data(room_number, room_type, name, surname):
    """
    :param surname:
    :param name:
    :param room_number:
    :param room_type:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''DELETE FROM students WHERE room_number = ? AND room_type = ? AND name = ? AND surname = ?''',
              (room_number, room_type, name, surname))
    conn.commit()
    conn.close()


# attendance
def attendance_insert_data(student_id, attendance, reason, educator_id, year, month, day, time):
    """
    :param student_id:
    :param attendance:
    :param reason:
    :param educator_id:
    :param year:
    :param month:
    :param day:
    :param time:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    query = "INSERT INTO attendance (student_id, attendance, reason, educator_id, year, month, day, time) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    data = (student_id, attendance, reason, educator_id, year, month, day, time)
    cursor.execute(query, data)
    conn.commit()
    conn.close()


def attendance_update_data(year, month, day, time, student_id, educator_id, attendance, reason):
    """
    :param year:
    :param month:
    :param day:
    :param time:
    :param student_id:
    :param educator_id:
    :param attendance:
    :param reason:
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    query = "UPDATE attendance SET attendance=?, reason=? WHERE year=? AND month=? AND day=? AND time=? AND student_id=? AND educator_id=?"
    data = (attendance, reason, year, month, day, time, student_id, educator_id)
    cursor.execute(query, data)
    conn.commit()
    conn.close()


def attendance_export_data_to_excel(attendance_data, year, month, day):
    """
    :return:
    """
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    query = f"SELECT student_id FROM attendance WHERE year = {year} AND month = {month} AND day = {day}"
    cursor.execute(query)
    student_ids = list([i[0] for i in cursor.fetchall()])

    query = f"SELECT educator_id FROM attendance WHERE year = {year} AND month = {month} AND day = {day}"
    cursor.execute(query)
    educator_ids = list([i[0] for i in cursor.fetchall()])

    query = f"SELECT attendance, reason, time FROM attendance WHERE year = {year} AND month =" \
            f" {month} AND day = {day}"
    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()

    workbook = xlsxwriter.Workbook(str(attendance_data)+'.xlsx')
    worksheet = workbook.add_worksheet()

    headers = ['Talaba', 'Hona', 'Yo\'qlama', 'Vaqt', 'Tarbiyachi']
    talabalar, yoqlar = 0, 0
    for i, header in enumerate(headers):
        worksheet.write(0, i, header,workbook.add_format(
                                                            {
                                                                'bg_color': '#008066',
                                                                'font_size': 12,
                                                                'bold': True,
                                                                'italic': False,
                                                            }
                                                        )
                        )

    for row, name in enumerate(student_ids):
        s_data = student_view_data_by_id(name)
        worksheet.write(row+1, 0, f"{s_data[2]} {s_data[1]}",workbook.add_format({'bg_color': '#66ffcc'}))
        worksheet.write(row+1, 1, f"{s_data[4]} {s_data[5]}",workbook.add_format({'bg_color': '#66ffcc'}))
        talabalar+=1
    for row, name in enumerate(educator_ids):
        e_data = educator_view_data_by_id(name)
        worksheet.write(row+1, 4, f"{e_data[0][2]} {e_data[0][1]}",workbook.add_format({'bg_color': '#66ffcc'}))

    for row, o_data in enumerate(data):
        if o_data[0] == '\x01':
            worksheet.write(row+1, 2, "Bor", workbook.add_format({'bg_color': '#008000'}))
        else:
            if o_data[1] == "NO":
                yoqlar+=1
                worksheet.write(row+1, 2, "Yo'q", workbook.add_format({'bg_color': '#ff1a1a'}))
            else:
                worksheet.write(row + 1, 2, o_data[1], workbook.add_format({'bg_color': 'ffff00'}))
        worksheet.write(row+1, 3, f"{year}.{month}.{day} {o_data[2]}",workbook.add_format({'bg_color': '#66ffcc'}))
    #
    worksheet.write(talabalar+1, 0, f"Talabalar: {talabalar} nafar", workbook.add_format(
                                                            {
                                                                'bg_color': '#008066',
                                                                'font_size': 12,
                                                                'bold': True,
                                                                'italic': False,
                                                            }
                                                        ))
    worksheet.write(talabalar+1, 2, f"{yoqlar}/{talabalar}",workbook.add_format(
                                                            {
                                                                'bg_color': '#008066',
                                                                'font_size': 12,
                                                                'bold': True,
                                                                'italic': False,
                                                            }
                                                        ))
    worksheet.write(talabalar + 2, 2, f"{(yoqlar / talabalar) * 100} %", workbook.add_format(
        {
            'bg_color': '#008066',
            'font_size': 12,
            'bold': True,
            'italic': False,
        }
    ))
    worksheet.write(talabalar+1, 1, f"  ",workbook.add_format(
                                                            {
                                                                'bg_color': '#008066',
                                                                'font_size': 12,
                                                                'bold': True,
                                                                'italic': False,
                                                            }
                                                        ))
    worksheet.set_column('A:A', 30)
    worksheet.set_column('D:D', 10)
    worksheet.set_column('C:C', 10)
    worksheet.set_column('E:E', 35)

    border_format = workbook.add_format({
        'border': 1,
        'border_color': 'black',
    })

    worksheet.conditional_format('A1:F'+str(talabalar+3), {'type': 'no_blanks', 'format': border_format})

    workbook.close()
#
# create_database()
#
# for i in range(3000):
#     student_insert_data(
#         name=f"student_name {i}",
#         surname=f"surname_{i}",
#         qavat=str(random.randint(1,5)),
#         room_number=str(random.randint(1,50)),
#         room_type=f"{chr(random.randint(65, 90))}",
#         gender=f"{chr(random.randint(71, 75))}",
#         photo="NO",
#         username=f"username_{i}",
#         password=f"password_{i}",
#         phone_number=str(random.randint(990000000,999999999)),
#         aloqa=f"aloqa_{i}",
#         address="Xorazm Bagat"
#     )
#
# for i in range(3):
#     educator_insert_data(
#         ism=f"educator_name_{i}",
#         familiya=f"educator_familiya_{i}",
#         telefon=str(random.randint(990000000,999999999)),
#         username=f"username_{i}",
#         parol=f"password_{i}",
#         aloqa=f"aloqa_{i}",
#     )
#
# print(student_view_data_all_id())
# for i in range(20):
#     print(i)
#     for ids in student_view_data_all_id():
#         attendance_insert_data(
#             student_id=ids[0],
#             attendance=chr(random.randint(0,1)),
#             reason="NO",
#             educator_id=str(random.randint(1,3)),
#             year=str(i),
#             month=str(i),
#             day=str(i),
#             time=str("00:00")
# #         )
# attendance_export_data_to_excel("test1",str(1),str(1),str(1))
# admin_insert_data(
#     ism="Jamshidbek",
#     familiya="Ollanazarov",
#     telefon="+998 91 277 96 93",
#     aloqa="https://t.me/mal_un",
#     username="jamshidbekollanazarov",
#     parol="Jamshid_bek2003."
# )
