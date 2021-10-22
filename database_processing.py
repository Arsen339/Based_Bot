# Обработка базы данных
import sqlite3

def create_base_struct():
    """Вызывается для первичной инициализации и в последствии для изменения структуры таблицы"""
    DB_1 = sqlite3.connect("users.db")
    cur = DB_1.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS all_users
    (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        surname VARCHAR,
        birth_year INT,
        License_type INT
        
        );
    """ )

def fill_db():
    DB_1 = sqlite3.connect("users.db")
    cur = DB_1.cursor()
    # Заполнение базы даных
    # В дальнейшем новые пользователи вписываются администратором вручную
    # В случае необходимости раскомментить
    # cur.execute(""" INSERT INTO all_users  VALUES(NULL, "Alexey", "Kozin", 2001, 1)""")
    # cur.execute(""" INSERT INTO all_users VALUES(NULL, "Artyom", "Gromov", 1999, 1)""")
    # cur.execute(""" INSERT INTO all_users VALUES(NULL, "Arsen", "Pitometz", 2000, 0)""")
    # cur.execute(""" INSERT INTO all_users VALUES(NULL, "Alexey", "Djakov", 2002, 0)""")
    # cur.execute(""" INSERT INTO all_users VALUES(NULL, NULL, NULL, NULL)""")
    # DB_1.commit()
    pass


def find_person(user_input):
    """По введенным пользователем имени, фамилии и дате рождения функция
    определяет, есть ли юзер в базе данных. return 0 - нет в базе, return 1 - есть в базе
    """
    person_info = [0, 0]
    DB_1 = sqlite3.connect("users.db")
    cur = DB_1.cursor()
    cur.execute("""SELECT * FROM all_users""")
    all_users = cur.fetchall()
    # print(all_users)
    for user in all_users:
        if user[1] == user_input[0] and user[2] == user_input[1] and user[3] == user_input[2]:
            person_info[0] = 1
            person_info[1] = user[4]
    return person_info


def output_all_db():
    """Функция только для back_end!"""
    DB_1 = sqlite3.connect("users.db")
    cur = DB_1.cursor()
    cur.execute("""SELECT * FROM all_users""")
    all_users = cur.fetchall()
    print(all_users)


test_arg = ["Alexey", "Kozin", 2001]
test_arg_1 = ["Sanya", "Poggi", 1950]
test_arg_2 = ["Arsen", "Pitometz", 2000]

print(find_person(test_arg))
print(find_person(test_arg_1))
print(find_person(test_arg_2))

output_all_db()