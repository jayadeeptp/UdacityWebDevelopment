months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = dict((m[:3].lower(),m) for m in months)

def valid_month(month):
    if month:
        short_month=month[:3].lower()
        return month_abbvs.get(short_month)

def valid_day(day):
    if day and day.isdigit():
        if int(day) in range (1,32):
            return int(day)
        else:
            return 
    else:
        return 

def valid_year(year):
    if year and year.isdigit():
        if int(year)>1900 and int(year)<2020:
            return int(year)

import cgi
def escape_html(s):
##    for (i,o) in (("&", "&amp;"),
##                  ("<", "&lt;"),
##                  (">", "&gt;"),
##                  ('"', "&quot;")):
##        s=s.replace(i,o)
    return cgi.escape(s, quote = True)
##    return s
