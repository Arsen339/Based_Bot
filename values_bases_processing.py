# Обработка баз данных со значениями криптовалюты
import sqlite3
import shutil
import os
from metal_parser import menu
from crypto_parser import main
from currency_parser import menue




def create_crypto_base():
    """Вызывается для первичной инициализации и в последствии для изменения структуры таблицы"""
    DB_1 = sqlite3.connect("cryptos.db")
    cur = DB_1.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS BTC
    (
        days_ago INT,
        value REAL

        );
        """)

    cur.execute("""CREATE TABLE IF NOT EXISTS ETH
    (
        days_ago INT,
        value REAL

        );
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS LTC
    (
        days_ago INT,
        value REAL

        );
        """)
        
    cur.execute("""CREATE TABLE IF NOT EXISTS BCH
    (
        days_ago INT,
        value REAL

        ); 
         """)
        
    cur.execute("""CREATE TABLE IF NOT EXISTS XMR
    (
        days_ago INT,
        value REAL

        );
        """)

    cur.execute("""CREATE TABLE IF NOT EXISTS DASH
    (
        days_ago INT,
        value REAL

        );
    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS ZEC
    (
        days_ago INT,
        value REAL

        );
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS VTC
    (
        days_ago INT,
        value REAL

        );
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS BTS
    (
        days_ago INT,
        value REAL

        );
        """)
    cur.execute(""" CREATE TABLE IF NOT EXISTS FTC
    (
        days_ago INT,
        value REAL

        );  
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS XEM
    (
        days_ago INT,
        value REAL

        );
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS DOGE
    (
        days_ago INT,
        value REAL

        );
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS MAID
    (
        days_ago INT,
        value REAL

        );
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS DGB
    (
        days_ago INT,
        value REAL

        );
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS CLAM
    (
        days_ago INT,
        value REAL

        );
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS SC
    (
        days_ago INT,
        value REAL

        );
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS DCR
    (
        days_ago INT,
        value REAL

        );
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS EMC2
    (
        days_ago INT,
        value REAL

        );
    """)
    DB_1.commit()

# create_crypto_base_struct()


def fill_crypto_db():
    """Заполним базу данных с криптовалютами, удаляем старую и создаем новую с новыми данными"""
    os.remove("cryptos.db")
    create_crypto_base()
    DB_1 = sqlite3.connect("cryptos.db")
    cur = DB_1.cursor()

    # Заполнение базы даных
    temp_arr = main('Ethereum', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO ETH  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Bitcoin', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO BTC  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Litecoin', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO LTC  VALUES(?,?)""", (i, temp_arr[0][30 - i],))

    temp_arr = main('BitcoinCash', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO BCH  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Monero', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO XMR  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Dash', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO DASH  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Zcash', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO ZEC  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Vertcoin', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO VTC  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Bitshares', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO BTS  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Factom', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO FTC  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('XEM', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO XEM  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Dogecoin', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO DOGE  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('MaidSafeCoin', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO MAID  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Digibyte', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO DGB  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Clams', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO CLAM  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Siacoin', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO SC  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Decred', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO DCR  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = main('Einsteinium', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO EMC2  VALUES(?,?)""", (i, temp_arr[0][30 - i],))

    DB_1.commit()





def create_metal_base():
    """Вызывается для первичной инициализации и в последствии для изменения структуры таблицы"""
    DB_1 = sqlite3.connect("metals.db")
    cur = DB_1.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS AU
    (
        days_ago INT,
        value REAL

        );
        """)

    cur.execute("""CREATE TABLE IF NOT EXISTS AG
    (
        days_ago INT,
        value REAL

        );
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS PT
    (
        days_ago INT,
        value REAL

        );
        """)

    cur.execute("""CREATE TABLE IF NOT EXISTS PD
    (
        days_ago INT,
        value REAL

        ); 
         """)

    DB_1.commit()


def fill_metal_db():
    """Заполним базу данных с металлами, удаляем старую и создаем новую с новыми данными"""
    os.remove("metals.db")
    create_metal_base()
    DB_1 = sqlite3.connect("metals.db")
    cur = DB_1.cursor()

    # Заполнение базы даных
    temp_arr = menu('au', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO AU  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = menu('ag', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO AG  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = menu('pt', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO PT  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = menu('pd', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO PD  VALUES(?,?)""", (i, temp_arr[0][30 - i],))

    DB_1.commit()

def create_currency_base():
    """Вызывается для первичной инициализации и в последствии для изменения структуры таблицы"""
    DB_1 = sqlite3.connect("currencies.db")
    cur = DB_1.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS USD
    (
        days_ago INT,
        value REAL

        );
        """)

    cur.execute("""CREATE TABLE IF NOT EXISTS EUR
    (
        days_ago INT,
        value REAL

        );
        """)
    cur.execute("""CREATE TABLE IF NOT EXISTS SGD
    (
        days_ago INT,
        value REAL

        );
        """)

    cur.execute("""CREATE TABLE IF NOT EXISTS CNY
    (
        days_ago INT,
        value REAL

        ); 
         """)

    cur.execute("""CREATE TABLE IF NOT EXISTS JPY
       (
           days_ago INT,
           value REAL

           ); 
            """)

    DB_1.commit()


def fill_currency_db():
    """Заполним базу данных с валютами, удаляем старую и создаем новую с новыми данными"""
    os.remove("currencies.db")
    create_currency_base()
    DB_1 = sqlite3.connect("currencies.db")
    cur = DB_1.cursor()

    # Заполнение базы даных
    temp_arr = menue('USD', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO USD  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = menue('EUR', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO EUR  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = menue('SGD', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO SGD  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = menue('CNY', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO CNY  VALUES(?,?)""", (i, temp_arr[0][30 - i],))
    temp_arr = menue('JPY', 31)
    for i in range(0, 30):
        cur.execute(""" INSERT INTO JPY  VALUES(?,?)""", (i, temp_arr[0][30 - i],))

    DB_1.commit()


# fill_crypto_db()
# create_crypto_base_struct()
# create_metal_base()
# fill_metal_db()
# create_currency_base()
# fill_currency_db()
