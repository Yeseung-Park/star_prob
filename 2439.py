# 별 찍기 - 2

N = int(input())

for i in range(N-1, -1, -1):
    string = ''
    string += ' '*i
    string += '*'*(N-i)
    print(string)