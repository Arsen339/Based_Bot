import urllib.request
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import sqlite3
crypto_upload_date = datetime.today().strftime("%Y-%m-%d")
url = "https://www.cbr.ru/hd_base/metall/metall_base_new/?UniDbQuery.Posted=True&UniDbQuery.From=23.09.2021&UniDbQuery.To=23.10.2021&UniDbQuery.Gold=true&UniDbQuery.Silver=true&UniDbQuery.Platinum=true&UniDbQuery.Palladium=true&UniDbQuery.so=1"
case_table = {
    'au': 1,
    'ag': 2,
    'pt': 3,
    'pd': 4
}


def menu(name, duration):  # name = 4 different 2 letter names. duration: days from now
    date1, date2 = get_dates(duration)
    html = get_html("tmp.html", date1, date2)
    array, dates = html_parser("tmp.html", html, name)
    numeration = sub_dates(date2, dates)
    
    array, numeration = closing_holes(array, numeration, duration)
    date_update()
    return array, numeration


def closing_holes(array, numeration, duration):
    new_arr = []
    new_num = list(range(duration))
    flag = False                 # indicator that there was an already valid element
    for i in range(duration):
        try:
            arr_elm = array[numeration.index(i)]
            new_arr.append(arr_elm)
            if not flag:
                for j in range(i):
                    new_arr[j] = new_arr[i]
                flag = True
        except ValueError:
            if flag:
                new_arr.append(new_arr[i-1])
            else:
                new_arr.append(0)
    new_arr = new_arr[0:duration]

    return new_arr, new_num


def get_dates(duration):
    curdate_raw = datetime.date(datetime.now())
    curdate_raw_split = str(curdate_raw).split("-")
    curdate = curdate_raw_split[2] + "." + curdate_raw_split[1] + "." + curdate_raw_split[0]
    startdate_raw = datetime.date(datetime.today() - timedelta(days=duration))
    startdate_raw_split = str(startdate_raw).split("-")
    startdate = startdate_raw_split[2] + "." + startdate_raw_split[1] + "." + startdate_raw_split[0]
    return startdate, curdate


def sub_dates(curdate, dates):
    date_d = []
    for date in dates:
        dat = datetime.strptime(date, "%d.%m.%Y")
        date_d.append(dat)
    curdate_d = datetime.strptime(curdate, "%d.%m.%Y")
    numbers = []
    for date in date_d:
        num = abs((date - curdate_d).days)
        numbers.append(num)
    return numbers


def get_html(filename, date1, date2):
    query = query_assemble(date1, date2)
    webfile = urllib.request.urlopen(query)
    data = webfile.read()

    with open(filename, "wb") as localFile:
        localFile.write(data)
    webfile.close()
    return data


def query_assemble(date1, date2):
    query = "https://www.cbr.ru/hd_base/metall/metall_base_new/?UniDbQuery.Posted=True&UniDbQuery.From=" + str(
        date1) + "&UniDbQuery.To" + str(date2) + \
            "&UniDbQuery.Gold=true&UniDbQuery.Silver=true&UniDbQuery.Platinum=true&UniDbQuery.Palladium=true&UniDbQuery.so=1"
    return query


def html_parser(filename, data0, name):
    with open(filename, "rb") as f:
        data = f.read()

    soup = BeautifulSoup(data, 'html.parser')
    table = soup.find("table", attrs={'class': 'data'})
    trs = table.find_all("tr")
    # print(len(trs))
    values = []
    for tr in trs:
        # ths = tr.findChildren("th")
        tds = tr.findChildren("td")
        i = 0
        row = [0, 0, 0, 0, 0]
        # for th in ths:
        #     print(th.string)
        for td in tds:
            row[i] = td.string
            i = i + 1
        values.append(row)
    # print(values)

    mode = 0
    try:
        mode = case_table[name]
    except KeyError as e:
        raise ValueError('Undefined unit: ')

    values.pop(0)
    result = []
    dates = []
    if mode > 0:
        for val in values:
            string = val[mode].replace(',', '.')
            string = string.replace(" ", '')
            num = float(string)
            result.append(num)
            dates.append(val[0])

    return result, dates

def date_update():
    DB_1 = sqlite3.connect("updates.db")
    cur = DB_1.cursor()
    cur.execute("""UPDATE update_date  SET last_update=(?) WHERE name="metal" """, (crypto_upload_date,))
    DB_1.commit()
    pass



