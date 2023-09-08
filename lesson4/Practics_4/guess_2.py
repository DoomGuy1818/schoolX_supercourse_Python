from import_this import RACE_DATA
from time_conversion import seconds_conversion

for i in RACE_DATA.values():
     if i.get("FinishedPlace") == 1:
        racist_info = f"\n\n\nВыиграл - {i.get('RacerName', 'Евгений Пригожин').upper()}!!! Поздравляем!!"
        print(racist_info)
        print("\n\n\n____________________\n\n\n\n\n")
     


for curr_racist in range(1, 4):
    racist_info = f"\t на {'первом' if curr_racist == 1 else 'втором' if curr_racist == 2 else 'третьем'}: \n"
    for i in RACE_DATA.values():
            if i.get("FinishedPlace") == curr_racist:
                racist_info += f"\t\tИмя:{i.get('RacerName', 'Евгений Пригожин')}\n"
                racist_info += f"\t\tКоманда:{i.get('RacerTeam', 'ЧВК Ам-ням')}\n"
                racist_time : int = seconds_conversion(i.get('FinishedTimeSeconds', 0))
                racist_info += f"\t\t Время :{racist_time[0]}:{racist_time[1]}:{racist_time[2]}\n"
    print(racist_info)
