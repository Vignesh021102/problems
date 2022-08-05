def add_time(t1,t2,str = " "):

    print(t1,t2,str)
    t1 = t1.split(" ")
    t1 = t1[0].split(":")+ t1[1:]
    t2 = t2.split(":")
    day = 0
    hour = 0
    min = 0
    hour = int(t1[0])
    min = int(t1[1])
    if t1[2] == 'PM':
        hour += 12
    hour += int(t2[0])
    min += int(t2[1])
    # correcting min
    if min >= 60:
        hour += int(min/60)
        min = min%60
    #correcting hour
    if hour >= 24:
        day += int(hour/24)
        hour = hour%24
    M = "AM"
    if hour >= 12:
        hour -= 12
        M = "PM"
    if hour == 0:
        hour = 12
    if min <10:
        min = f"0{min}"

    if str != " ":
        str = str[0].upper()+str[1:].lower()
        daySet = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        dayNum = daySet.index(str)
        dayNum += day
        text +=f", {daySet[dayNum]}"
        
    if day == 1:
        text+=f" (next day)"
    elif day > 1:
        text +=f" ({day} days later)"
    print("=>",text,"\n")
    return text
add_time("3:58 PM", "10:10","Tuesday")
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
