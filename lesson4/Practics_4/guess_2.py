from import_this import(
    generate_race_data,
    RaceInfo,
    
)

from time_conversion import seconds_conversion

if __name__ == "__main__":

    generate_race_data: RaceInfo = generate_race_data(5)

    winner_info: str = ""
    underscore_count: str = ""

    for i in generate_race_data.values():
     if i.get("FinishedPlace") == 1:
        winner_info = f"\n\n\nВыиграл - {i.get('RacerName', 'Евгений Пригожин').upper()}!!! Поздравляем!!"
        underscore_count = "_" * len(winner_info)
        print(f"{winner_info}\n")
        print(f"{underscore_count}\n\n\n")
        print("Первые три места:\n")
     


    for curr_racist in range(1, 4):

        racist_info : str = ""
        
        racist_info = f" на {'первом' if curr_racist == 1 else 'втором' if curr_racist == 2 else 'третьем'}: \n\n"
        for i in generate_race_data.values():
                if i.get("FinishedPlace") == curr_racist:
                    racist_info += f"\tИмя:{i.get('RacerName', 'Евгений Пригожин')}\n\n"
                    racist_info += f"\tКоманда:{i.get('RacerTeam', 'ЧВК Ам-ням')}\n\n"
                    racist_time : int = seconds_conversion(i.get('FinishedTimeSeconds', 0))
                    racist_info += f"\tВремя :{racist_time[0]}:{racist_time[1]}:{racist_time[2]}\n\n"
        
        print(racist_info)







