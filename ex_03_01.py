payperhr = input("How much for an hour of your time?")
hrs = input("Enter Hours:")
h = float(hrs)
payperhr = float(payperhr)
if h > 40:
    ovr_tm = h - 40
    salary = 40 * payperhr + (ovr_tm * 1.5 * payperhr)
else:
    salary = h * payperhr
print(salary)
