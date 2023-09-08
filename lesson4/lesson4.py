from module import greet

x = 42

# def answer(x):
#     x = 12
#     return x

# # print(

# #     greet("Vova")
# # )

# if __name__ == '__main__':
#     x = 42
#     print(

#         answer()
#     )


def outer():
    y = 12
    def answer():
        return x
    return answer()

if __name__ == '__main__':
    x = 42

    print(
        y
    )


