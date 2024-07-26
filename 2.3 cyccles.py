"""
#A
inputdata = input()
while inputdata != 'Три!':
    print('Режим ожидания...')
    inputdata = input()
print('Ёлочка, гори!')

#B
inputdata = str(input())
rabitcount = 0
while inputdata != 'Приехали!':
    if 'зайка' in inputdata:
        rabitcount += 1
    inputdata = str(input())
print(rabitcount)
"""
#C
