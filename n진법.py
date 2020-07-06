input = '12 3'
input2 = '444 5'

num, base = map(int, input2.strip().split(' '))

print(int(str(num), base))