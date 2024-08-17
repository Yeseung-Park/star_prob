# 별 찍기 - 9

N = int(input())

for i in range(N, 0, -1):
    string = ''
    string += ' '*((2*N-1)//2-(i-1))
    string += '*'*(2*i-1)
    print(string)

for i in range(2, N+1):
    string = ''
    string += ' ' * ((2 * N - 1) // 2 - (i - 1))
    string += '*' * (2 * i - 1)
    print(string)