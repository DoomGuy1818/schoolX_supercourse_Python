def my_personal_sum(
    x: int | float, 
    y: int | float,
) -> int | float:
    answer = x / y
    return answer


print(my_personal_sum(3,5))
print(sum([3,5]))

# def my_personal_sum(*args, **kwargs) -> int | float:
#     answer = 0
#     for num in args:



