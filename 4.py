years = int(input("Введите количество лет:"))

print("Число просмотренных экспонатов:", years*365*60*8//5)

exhibits = int(input("Введите количество экспонатов:"))

minutes = exhibits*5  

days = minutes // 480

minutes -= days*480

years = days // 365 

days %= 365

print("Количество лет:", years, "Количество дней:", days, "Количество минут:", minutes)