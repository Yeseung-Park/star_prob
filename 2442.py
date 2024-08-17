# 별 찍기 - 5

N = int(input())

for i in range(1, N+1):
    string = ''
    string += ' '*((2*N-1)//2-(i-1))
    string += '*'*(2*i-1)
    print(string)