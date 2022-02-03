# Fibonacci
print('Задача:')
print('Написать функцию возвращающую четные элементы последовательности Фибоначчи.\nНапример, f(4) вернет 0,2,8,34\n')

print('Решение:')

fibCH = 10 # вернуть чётных чисел
che_arr = []
pri_arr = []

def Fibo_Che(che):
    fibA = 0
    fibB = 0
    i = 0
    while True:
        fibS = fibA + fibB
        fibA = fibB
        fibB = fibS

        if fibS % 2 == 0:
            che_arr.append(fibS)

        if fibA == 0 + fibB == 0:
            fibB = fibB + 1

        if len(che_arr) + 1 > che:
            break

    return(che_arr)

pri_arr = Fibo_Che(fibCH)



print('')
print(f'Fibo_Che({fibCH})')
print(f'Чётные числа :: {pri_arr} в колличестве :: {len(pri_arr)}')


#index=0
#for fib in pri_arr:
#    print(pri_arr[index], end=", ")
#    index += 1


#print('')
#print(f'Fibo_Che({fibCH}) :: {Fibo_Che(fibCH)}')