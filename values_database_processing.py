# Обработка базы данных курсов
import sqlite3



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






create_base_struct()
fill_db()