"""Avg Day"""
import json
def main():
    """Find AVG"""
    print("Input list")
    text = input()
    lst = json.loads(text)
    day = "monday"
    mtotal = 0
    mcount = 0
    tutotal = 0
    tucount = 0
    wtotal = 0
    wcount = 0
    thtotal = 0
    thcount = 0
    ftotal = 0
    fcount = 0
    satotal = 0
    sacount = 0
    sutotal = 0
    sucount = 0
    for i in lst:
        if day == "monday":
            mtotal += i
            mcount += 1
            day = "tuesday"
        elif day == "tuesday":
            tutotal += i
            tucount += 1
            day = "wednesday"
        elif day == "wednesday":
            wtotal += i
            wcount += 1
            day = "thursday"
        elif day == "thursday":
            thtotal += i
            thcount += 1
            day = "friday"
        elif day == "friday":
            ftotal += i
            fcount += 1
            day = "saturday"
        elif day == "saturday":
            satotal += i
            sacount += 1
            day = "sunday"
        else:
            sutotal += i
            sucount += 1
            day = "monday"
    mday = mtotal/mcount
    tuday = tutotal/tucount
    wday = wtotal/wcount
    thday = thtotal/thcount
    fday = ftotal/fcount
    saday = satotal/sacount
    suday = satotal/sacount
    print("Monday average: %i" %mday)
    print("Tuesday average: %i" %tuday)
    print("Wednesday average: %i" %wday)
    print("Thursday average: %i" %thday)
    print("Friday average: %i" %fday)
    print("Saturday average: %i" %saday)
    print("Sunday average: %i" %suday)
main()
