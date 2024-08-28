# N = int(input())

# def make_star(shape, n):    # shape: 기준이 되는 모양, n은 시행하는 횟수
#     if n == int(N**(1/3)):
#         return shape
#     else:
#         new_shape = shape*3+'\n'+f'{shape}'+' '*(3**n)+f'{shape}'+'\n'+shape*3
#         n += 1
#         return make_star(new_shape, n)

# temp = 'hi'+'hi'
# result = make_star('*', 0)
# print(result)
# print(temp)

temp = 'hi\nhi'
print(temp)

print(temp*2)