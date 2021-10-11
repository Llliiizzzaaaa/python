# This is a sample Python script.
import sys
import math
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_nulli(s):
    try:
        if (float(s) == 0):
            return True
    except ValueError:
        return False
a=1
a1=2
b=2
c=1
while (is_number(a)):
    print ('Введите  а:')
    a1= input()

    if (not(is_number(a1))):
        print('Это не число!')
        continue
    elif (is_nulli(a1)):
        print ('a не может быть нулем!')
        continue
    else:
        a = float(a1)
        break

while (is_number(b)):
    print ('Введите  b:')
    b1= input()

    if (not(is_number(b1))):
        print('Это не число!')
        continue
    else:
        b = float(b1)
        break

while (is_number(c)):
    print ('Введите  c:')
    c1= input()

    if (not(is_number(c1))):
        print('Это не число!')
        continue
    else:
        c =float (c1)
        break

print ('Данные введены, идет подсчет:')
if (a == 0 ):
    print('a = 0! измените набор!')
else:
    D = b*b - 4*a*c
    if D < 0:
        print ('Действительных решений нет')

    else:
        y1 = ((-b - math.sqrt(D) )/ (2 * a))
        y2 = ((-b + math.sqrt(D) )/ (2 * a))
        print(f'Два корня из дискримината y1 и y2 : {y1} и {y2}')
        if (y1 < 0 ) and (y2 < 0):
            print('Действительных решений нет')

        else:
            if (y1 >= 0) and (y2 >= 0):
                x1 = -(math.sqrt(y1))
                x2 = -x1
                x3 = -(math.sqrt(y2))
                x4 = -x3
                print(f'Четыре корня: {x1} и {x2} и {x3} и {x4}')
            else:
                if (y1 >= 0) and (y2 < 0):
                    x1 = - (math.sqrt(y1))
                    x2 = - x1
                    print (f'Два корня: {x1} и {x2}')

                else:
                    x1 = - (math.sqrt(y2))
                    x2= - x1
                    print(f'Два корня: {x1} и {x2}')
