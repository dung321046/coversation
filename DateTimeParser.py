import re
import datetime
import calendar
def detectNumer(sentence):
    re_float = re.compile(r'\d*\.?\d+')
    data = re.findall(re_float, sentence)
    result = []
    for item in data:
        if '.' in item:
            result.append(float(item))
        else:
            result.append(int (item))
    return result

def addMonths(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = int(sourcedate.year + month / 12 )
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    return datetime.date(year,month,day)

def dateParse(sentence):
    date = None
    time = None
    tokens = sentence.split(' ')
    date = getDate(tokens[0])
    n = len(tokens)
    for i in range(n-1):
        if tokens[i] == 'OFFSET':
            token = tokens[i + 1]
            if token[0] == 'P':
                num = int(token[1:-1])
                print(num)
                unit = token[len(token) - 1]
                if unit == 'M':
                    date = addMonths(date, num)
                elif unit == 'D':
                    date = date + datetime.timedelta(days=num)
                elif unit == 'W':
                    date = date + datetime.timedelta(days=num * 7)
    for token in tokens:
        if ':' in token:
            time = getTime(token[1:])
            break
    return date, time


def getDate(tokens):
    if '-' in tokens:
        items = tokens.split('-')
        y = items[0]
        mw = items[1]
        d = items[2]
        if('X' not in y):
            y = int(y)
        else:
            y = datetime.datetime.now().year
        if 'W' in mw:
            if 'X' not in mw:
                mw = mw[1:]
                mw = int(mw)
            else:
                mw = datetime.datetime.now().isocalendar()[1]
            if int(d) != None:
                d = int(d)
            else:
                d = datetime.datetime.now().isocalendar()[3]
            return iso_to_gregorian(y, mw, d)
        else:
            if 'X' not in mw:
                mw = mw[1:]
                mw = int(mw)
            else:
                mw = datetime.datetime.now().month
            if 'X' not in d:
                d = int(d)
            else:
                d = datetime.datetime.now().day
            return datetime.datetime(y, mw, d)
    elif tokens == "THIS":
        return datetime.datetime.now()
    else:
        return datetime.datetime.now()


def getTime(item):
    tokens = item.split(':')
    h = int(tokens[0])
    m = int(tokens[1])
    return datetime.time(h, m)


def iso_year_start(iso_year):
    "The gregorian calendar date of the first day of the given ISO year"
    fourth_jan = datetime.date(iso_year, 1, 4)
    delta = datetime.timedelta(fourth_jan.isoweekday() - 1)
    return fourth_jan - delta


def iso_to_gregorian(iso_year, iso_week, iso_day):
    "Gregorian calendar date for the given ISO year, week and day"
    year_start = iso_year_start(iso_year)
    return year_start + datetime.timedelta(days=iso_day - 1, weeks=iso_week - 1)