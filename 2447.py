N = int(input())

def make_star(shape, n):    # shape: 기준이 되는 모양, n은 시행하는 횟수
    if n == int(N**(1/3)):
        return shape
    else:
        new_shape = [shape*3, shape*1+[' ']*(3**n)+shape*1, shape*3]
        n += 1
        return make_star(new_shape, n)

result = make_star('*', 0)
for s in result:
    print(result)

# shape = ['*'*3, '*'*1+' '*1+'*'*1, '*'*3]
#
# for s in shape:
#     print(s)