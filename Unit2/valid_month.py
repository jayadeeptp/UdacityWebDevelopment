# -----------
# User Instructions
# 
# Modify the valid_month() function to verify 
# whether the data a user enters is a valid 
# month. If the passed in parameter 'month' 
# is not a valid month, return None. 
# If 'month' is a valid month, then return 
# the name of the month with the first letter 
# capitalized.
#
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
          
##def valid_month(month):
##    this_month=month.lower()
##    for m in range(len(months)):
##        if month.lower()==months[m].lower():
##            print months[m]
##            return months[m]
##    else:
##        print 'None'
##        return 'None'
       
month_abbvs = dict((m[:3].lower(),m) for m in months)

def valid_month(month):
    if month:
        short_month=month[:3].lower()
        return month_abbvs.get(short_month)

##print valid_month('feb')

