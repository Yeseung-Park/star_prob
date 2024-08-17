# 별 찍기 - 4

N = int(input())

for i in range(N):
    string = ''
    string += ' '*i
    string += '*'*(N-i)
    print(string)