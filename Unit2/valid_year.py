def valid_year(year):
    if year and year.isdigit():
        if int(year)>1900 and int(year)<2020:
            return int(year)

print valid_year('1990')
