'''
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
'''

x, y, z = map (int, input('Введите значения для x, y, z ').split())

if (not(x or y or z) == (not x and not y and not z)):
    print ('True')
else:
    print ('False')