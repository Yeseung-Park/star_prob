# 별 찍기 - 8

N = int(input())

for i in range(1, N+1):
    string = ''
    string += '*'*i
    string += ' '*(2*N-i*2)
    string += '*'*i
    print(string)

for i in range(N-1, 0, -1):
    string = ''
    string += '*' * i
    string += ' ' * (2 * N - i * 2)
    string += '*' * i
    print(string)