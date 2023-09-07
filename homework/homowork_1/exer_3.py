def convert(seconds : int) -> str:
    hours : int = 0
    minutes : int = 0

    if seconds / 3600 > 0:
        hours = seconds // 3600

        if seconds / 60 > 0 and hours == 0:
            minutes = seconds // 60
    
    
    else: 
        hours, minutes = 0, 0
    
    
    
    return f"{hours} час(а/ов) и {minutes} минут(а/ы)"

print(convert(int(input("Введите секунды:"))))
