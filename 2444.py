# 별 찍기 - 7

N = int(input())

for i in range(1, N+1):
    string = ''
    string += ' '*((2*N-1)//2-(i-1))
    string += '*'*(2*i-1)
    print(string)

for i in range(N-1, 0, -1):
    string = ''
    string += ' '*((2*N-1)//2-(i-1))
    string += '*'*(2*i-1)
    print(string)