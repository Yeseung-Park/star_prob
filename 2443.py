# 별 찍기 - 6

N = int(input())

for i in range(N, 0, -1):
    string = ''
    string += ' '*((2*N-1)//2-(i-1))
    string += '*'*(2*i-1)
    print(string)