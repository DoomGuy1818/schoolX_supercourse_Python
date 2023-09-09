

def square_of_list(num_in_cells : int):
     
    ints : list = []

    # Первый очень сложный способ 


    

    # for n in range(num_of_cells+1):
    #     if n == 0:
    #         continue
    #     ints.append((n**2))
        
    # ints.reverse()

    

    # for n in range(num_of_cells + 1):
    #     ints.append(n**2)
    
    # return ints

    # Второй простой
    for n in range(-num_in_cells, num_in_cells+1):
        ints.append(n**2)

    return ints



print(square_of_list(int(input("введите число "))))
    



