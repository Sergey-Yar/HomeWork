n = int(input('Введите число на камне (от 3 до 20): '))
result = []
if n < 3:
    print('Число меньше 3.')
elif n > 20:
    print('Число больше 20.')
else:
    for x in range(1, n):
        for y in range(x+1, n):
            if n % (x + y) == 0:
                result.extend([x,y])
            else:
                continue
result_1 = ''.join(str(item) for item in result)
print(f'Пароль: {result_1}')