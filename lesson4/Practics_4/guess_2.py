from import_this import RACE_DATA
from time_conversion import seconds_conversion



for curr_racist in range(1, 4):
    racist_info = f"\t на {'первом' if curr_racist == 1 else 'втором' if curr_racist == 2 else 'третьем'}: \n"
    for i in RACE_DATA.values():
            if i.get("FinishedPlace") == curr_racist:
                racist_info += f"\t\tИмя:{i.get('RacerName', 'Евгений Пригожин')}"
                racist_info += f"\t\tКоманда:{i.get('RacerTeam', 'ЧВК Ам-ням')}"
                racist_time : int = seconds_conversion(i.get('FinishedTimeSeconds', 0))
                racist_info += f"\t\t Время :{racist_time[0]}:{racist_time[1]}:{racist_time[2]}"
    print(racist_info)
