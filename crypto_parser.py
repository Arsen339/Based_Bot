from datetime import datetime, timedelta
import urllib.request
import shutil
import csv


crypto_names = {
    'Bitcoin': 'BTC',
    'Ethereum': 'ETH',
    'Litecoin': 'LTC',
    'BitcoinCash': 'BCH',
    'Monero': 'XMR',
    'Dash': 'DASH',
    'Zcash': 'ZEC',
    'Vertcoin': 'VTC',
    'Bitshares': 'BTS',
    'Factom': 'FTC',
    'XEM': 'XEM',
    'Dogecoin': 'DOGE',
    'MaidSafeCoin': 'MAID',
    'Digibyte': 'DGB',
    'Clams': 'CLAM',
    'Siacoin': 'SC',
    'Decred': 'DCR',
    'Einsteinium': 'EMC2'
}
crypto_extra = {
    0: '-USD',
    1: '-RUB'
}


def main(name, duration):
    date1, date2 = get_dates(duration)
    curdate = date2
    date1 = in_secs(date1)
    date2 = in_secs(date2)+10000
    query = query_assemble(name, date1, date2)
    download_file(query, "C:/Users/Admin/Desktop/dbs/tmp.csv")
    data = extract_data("C:/Users/Admin/Desktop/dbs/tmp.csv", duration)
    result = [dat[1] for dat in data]
    dates = [dat[0] for dat in data]
    numbers = sub_dates(curdate, dates)

    return result, numbers


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
    
    
def in_secs(date):
    date_d = datetime.strptime(date, "%d.%m.%Y")
    seconds = date_d.timestamp()
    return seconds


def get_dates(duration):
    curdate_raw = datetime.date(datetime.now())
    curdate_raw_split = str(curdate_raw).split("-")
    curdate = curdate_raw_split[2] + "." + curdate_raw_split[1] + "." + curdate_raw_split[0]
    startdate_raw = datetime.date(datetime.today() - timedelta(days=duration))
    startdate_raw_split = str(startdate_raw).split("-")
    startdate = startdate_raw_split[2] + "." + startdate_raw_split[1] + "." + startdate_raw_split[0]
    return startdate, curdate


def query_assemble(name, date1, date2):
    rub = 1
    name_id = crypto_names[name]
    type_id = crypto_extra[rub]
    date1 = int(date1)
    date2 = int(date2)
    query = "https://query1.finance.yahoo.com/v7/finance/download/{0}{1}?" \
            "period1={2}&period2={3}&interval=1d&events=history&includeAdjustedClose=true".format(name_id, type_id, date1, date2)
# https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1602288000&period2=1635011768&interval=1d&events=history&includeAdjustedClose=true
    return query


def download_file(query, filename):  # returns csv file
    with urllib.request.urlopen(query) as response, open(filename, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


def extract_data(filename, duration):
    result = []
    dur = 0
    with open(filename, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = []
        for row in reader:
            if dur < duration+2:
                result.append([row[0], float(row[4])])
                dur = dur + 1

    return result


def sub_dates(curdate, dates):
    date_d = []
    for date in dates:
        dat = datetime.strptime(date, "%Y-%m-%d")
        date_d.append(dat)
    curdate_d = datetime.strptime(curdate, "%d.%m.%Y")
    numbers = []
    for date in date_d:
        num = abs((date - curdate_d).days)
        numbers.append(num)

    return numbers


main('Ethereum', 10)
