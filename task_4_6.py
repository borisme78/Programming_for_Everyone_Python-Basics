def computepay(hoyrs, rate):
    if hoyrs > peak_hour:
        regular_pay = peak_hour * rate
        over_time =  hoyrs - peak_hour
        overtime_pay = over_time * rate * overtime_pay_hour
        salary = regular_pay + overtime_pay
    else:
        salary = hoyrs * rate
    return salary 

hrs = input("Enter Hours:")
hour = input("Rate per hour:")
peak_hour = 40
overtime_pay_hour = 1.5

xp = computepay(float(hrs), float(hour))
print("Pay", xp)