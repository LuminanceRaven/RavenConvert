def convertCF(celsium):
    fahrenheit = (celsium * (9/5)) + 32
    return fahrenheit

def convertFC(fahrenheit):
    celsium = (fahrenheit - 32) * (5/9)
    return celsium

def convertMKM(meter):
    kilometer = meter / 1000
    return kilometer

def convertKMM(kilometer):
    meter = kilometer * 1000
    return meter

def convertCMMM(centimeter):
    millimeter = centimeter * 10
    return millimeter

def convertMMCM(millimeter):
    centimeter = millimeter / 10
    return centimeter

def convertCMDM(centimeter):
    decimeter = centimeter / 10
    return decimeter

def convertDMCM(decimeter):
    centimeter = decimeter * 10
    return centimeter

def convertMDM(meter):
    decimeter = meter * 10
    return decimeter

def convertDMM(decimeter):
    meter = decimeter / 10
    return meter

def convertSM(second):
    minute = second * 60
    return minute

def convertMS(minute):
    second = minute / 60
    return second

def convertMGG(milligram):
    gram = milligram * 1000
    return gram

def convertGMG(gram):
    milligram = gram / 1000
    return milligram

def convertGKG(gram):
    kilogram = gram * 1000
    return kilogram

def convertKGG(kilogram):
    gram = kilogram / 1000
    return gram

def convertKGC(kilogram):
    centner = kilogram * 100
    return centner

def convertCKG(centner):
    kilogram = centner / 100
    return kilogram

def convertCT(centner):
    tonne = centner * 10
    return tonne

def convertTC(tonne):
    centner = tonne / 10
    return centner

def convertMH(minute):
    hour = minute * 60
    return hour

def convertHM(hour):
    minute = hour / 60
    return minute

def convertHD(hour):
    day = hour * 24
    return day

def convertDH(day):
    hour = day / 24
    return hour

def convertDW(day):
    week = day * 7
    return week

def convertWD(week):
    day = week / 7
    return day

def convertWFN(week):
    fortnight = week * 2
    return fortnight

def convertFNW(fortnight):
    week = fortnight / 2
    return week

def convertDM(day):
    month = day * 31
    return month

def convertDM2(day):
    month = day * 30
    return month

def convertDM3(day):
    month = day * 28
    return month

def convertDM3l(day):
    month = day * 29
    return month

def convertMD(month):
    day = month / 31
    return day

def convertM2D(month):
    day = month / 30
    return day

def convertM3D(month):
    day = month / 28
    return day

def convertM3lD(month):
    day = month / 39
    return day

def convertMY(month):
    year = month * 12
    return year

def convertYM(year):
    month = year / 12
    return month

def convertWY(week):
    year = week * 52
    return year

def convertYW(year):
    week = year / 52
    return week

def convertDY(day):
    year = day * 365
    return year

def convertDYl(day):
    year = day * 366
    return year

def convertYD(year):
    day = year / 365
    return day

def convertYlD(year):
    day = year / 366
    return day

def convertSMS(second):
    millisecond = second * 100
    return millisecond

def convertMSS(millisecond):
    second = millisecond / 100
    return second
