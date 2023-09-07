
def find_subseq(numbers : list) -> list | str:

    ints : list = []
    
    if len(numbers) == 1:
        return "Неподходящий массив"

   

    for n in range(len(numbers)):
        
        if numbers[n] - numbers[n-1] > 1:
            
            ints.append(n)
        
    if len(ints) > 0:
        return ints
    
    return "Не найдено"
    
print(find_subseq([1, 2, 4, 5, 7, 9]))
        
            


