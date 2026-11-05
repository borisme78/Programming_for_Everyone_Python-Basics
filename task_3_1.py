hrs = input("Enter Hours:")
hour = input("Rate per hour:")
try:
    hrs1 = float(hrs)
    hour1 = float(hour)
except:
    print("Error, please enter numeric input")
    quit()
peak_hour = 40
overtime_pay_hour = 1.5
if int(hrs) > peak_hour:
    regular_pay = peak_hour * hour1
    over_time = hrs1 - float(peak_hour)
    overtime_pay = over_time * hour1 * overtime_pay_hour
    salary = regular_pay + overtime_pay
    
else:
    salary = hrs1 * hour1
print(float(salary))