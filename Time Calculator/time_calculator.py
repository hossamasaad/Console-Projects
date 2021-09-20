def add_time(start, duration, day = None):

    # get Current time period and update the start string
    p = start[-2:]
    start = start[:-3]


    # split time
    start_hour, start_minute = splitTime(start)
    hour, minute = splitTime(duration)


    # if p = 'PM' add 12
    if p == 'PM':
        start_hour += 12

    
    # add duration
    total_hour = start_hour + hour
    total_minute = start_minute + minute
    if total_minute > 59:
        total_hour += 1
        total_minute -= 60

    

    # calaculate no of days
    no_of_days = total_hour // 24
    total_hour = total_hour % 24



    # calculate 'PM' or 'AM'
    new_p =  ""
    if total_hour >= 12:
        new_p = 'PM'
        if total_hour > 12:
            total_hour -= 12
    else:
        if total_hour == 0:
            total_hour = 12
        new_p = 'AM'


    # minute format
    if total_minute < 10:
        total_minute = '0' + str(total_minute)
    else:
        total_minute = str(total_minute)



    # new time format
    new_time = str(total_hour) + ':' + total_minute  + ' ' + new_p
    
    if no_of_days == 0:
        if day != None:
            new_time += ', ' + day
    else:
        if day != None:
            day = getDay(day, no_of_days)
            new_time += ', ' + day


        if no_of_days == 1:
            new_time += ' (next day)'
        else:
            new_time += ' (' + str(no_of_days) + ' days later)'
    return new_time


def splitTime(s):
    h = ""
    m = ""

    state = False
    for char in s:
        if char == ":":
            state = True
        else:
            if state is False:
                h += char        
            else:
                m += char

    return int(h), int(m)

def getDay(day, no_of_days):
    days = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
    day_n = {'wednesday':0, 'thursday':1, 'friday':2,
             'saturday':3, 'sunday':4, 'monday':5, 'tuesday':6}

    no = (day_n[day.lower()] + no_of_days ) % 7
    return days[no]