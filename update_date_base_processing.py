# Обработка базы данных дат последних обновлений
import sqlite3
from datetime import datetime, timedelta
now_date = datetime.today().strftime("%Y-%m-%d")
now_date = datetime.strptime(now_date, "%Y-%m-%d")


def create_base_struct():
    """Вызывается для первичной инициализации и в последствии для изменения структуры таблицы"""
    DB_1 = sqlite3.connect("updates.db")
    cur = DB_1.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS update_date
    (
        id INTEGER PRIMARY KEY,
        name VARCHAR,
        last_update DATE

        );
    """)
    DB_1.commit()


def fill_db():
    """Заполнение базы данных"""
    DB_1 = sqlite3.connect("updates.db")
    cur = DB_1.cursor()
    # Заполнение базы даных
    # В дальнейшем новые пользователи вписываются администратором вручную
    # В случае необходимости раскомментить

    cur.execute(""" INSERT INTO update_date  VALUES(NULL, "crypto", "2022-02-02" )""")
    cur.execute(""" INSERT INTO update_date VALUES(NULL, "currency", "2022-03-02" )""")
    cur.execute(""" INSERT INTO update_date VALUES(NULL, "metal", "2022-03-02" )""")

    DB_1.commit()
    pass

# create_base_struct()
# fill_db()


def metal_update_time_check():
    """Проверяем, является ли информация в БД актуальной"""
    DB_1 = sqlite3.connect("updates.db")
    cur = DB_1.cursor()
    cur.execute("""SELECT last_update FROM update_date WHERE name = 'metal' """)

    then_date = cur.fetchall()
    then_date = datetime.strptime(then_date[0][0], "%Y-%m-%d")
    DB_1.commit()
    if now_date > then_date:
        return 0
    else:
        return 1


def crypto_update_time_check():
    """Проверяем, является ли информация в БД актуальной"""
    DB_1 = sqlite3.connect("updates.db")
    cur = DB_1.cursor()
    cur.execute("""SELECT last_update FROM update_date WHERE name = 'crypto' """)

    then_date = cur.fetchall()
    then_date = datetime.strptime(then_date[0][0], "%Y-%m-%d")
    if now_date > then_date:
        return 0
    else:
        return 1


def currency_update_time_check():
    """Проверяем, является ли информация в БД актуальной"""
    DB_1 = sqlite3.connect("updates.db")
    cur = DB_1.cursor()
    cur.execute("""SELECT last_update FROM update_date WHERE name = 'currency' """)
    then_date = cur.fetchall()
    then_date = datetime.strptime(then_date[0][0], "%Y-%m-%d")
    if now_date > then_date:
        return 0
    else:
        return 1
