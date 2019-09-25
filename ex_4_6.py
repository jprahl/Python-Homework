payperhr = input("How much for an hour of your time?")
hrs = input("Enter Hours:")
hrs = float(hrs)
payperhr = float(payperhr)
def computepay(payperhr,hrs):
    if hrs > 40:
        ovr_tm = hrs - 40
        salary = 40 * payperhr + (ovr_tm * 1.5 * payperhr)
    else:
        salary = hrs * payperhr
    return salary
print(computepay(payperhr,hrs))
