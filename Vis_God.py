year = int(input("Введите год, который требуется: "))

def data(yr):
    count = 0
    for i in range(yr+1):
        if i<10:
            count = count + i
        else:
            SrtringDay = str(i)
            SrtringDaySymb = list(SrtringDay)
            count = count + int(SrtringDaySymb[0]) + int(SrtringDaySymb[1])
    return count

if((year % 400 == 0) or 
    (year % 100 != 0) and 
    (year % 4 == 0)):  
        print("Это високосный год!"); 
        sum = data(31) * 7 + data(30) * 4 + data(29)
        print("Итог: ", sum)
else:
        print("Это год не високосный")
        sum = data(31) * 7 + data(30) * 4 + data(28)
        print("Итог: ", sum)



