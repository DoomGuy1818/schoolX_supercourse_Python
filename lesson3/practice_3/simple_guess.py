
def guess(num: int) ->  str | int:


    for i in range(num + 1):
      if i*i == num:
       

        return num / i  
      
    return "трудно"

print(guess(144))
    
   
    
