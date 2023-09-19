a: list[int] = [1,2,3,4,6,7]
b: list[int] = [0,0,1,0,0,1]

answer = []

answer = [
    val*b[i] 
    for i, val in enumerate(a)
]
# answer = [i for i in a] # более простой вариант записи массива
print(answer)

for i, val in enumerate(a):
    print(f'index={i}')
    print(f'value={val}\n')

def mask_list(array: list[int], mask: list[int]) -> list[int]:
    return [val * mask[i] * .5 for i, val in enumerate(array)]

def test_mask_list():
    assert mask_list([1,2,3], [1,0,0]) == [1, 0 , 0] 