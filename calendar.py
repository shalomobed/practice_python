def output_semester(month, day):
    monthdict = {"January": 1,
                 "February": 2,
                 "March": 3,
                 "April": 4,
                 "May": 5,
                 "June": 6,
                 "July": 7,
                 "August": 8,
                 "September": 9,
                 "October": 10,
                 "November": 11,
                 "December": 12}
    month_place = monthdict[month]
    if 1 == month_place and 8 <= day <= 30:
        return "spring semester"
    if 2 <= month_place <= 4 and 1 <= day <= 30:
        return "spring semester"

    if 5 <= month_place <= 7 and 1 <= day <= 30:
        return "summer break"
    if month_place == 8 and 1 <= day <= 20:
        return "summer break"

    if month_place == 8 and 21 <= day <= 31:
        return "fall semester"
    if 9 <= month_place <= 11 and 1 <= day <= 30:
        return "fall semester"
    if month_place == 12 and 1 <= day <= 12:
        return "fall semester"

    if month_place == 12 and 13 <= day <= 31:
        return "winter break"
    if month_place == 1 and 1 <= day <= 7:
        return "winter break"


month = str(input("Please enter the month: "))
day = int(input("Please enter the day: "))
print(f"{month} {day} is during GSU's {(output_semester(month, day))}.")
