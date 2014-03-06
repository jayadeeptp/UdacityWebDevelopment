def valid_day(day):
    if day and day.isdigit():
        if int(day) in range (1,32):
            return int(day)
        else:
            return 
    else:
        return 

#print valid_day(',1')