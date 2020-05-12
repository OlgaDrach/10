#Сформувати функцію для обчислення індексу максимального елемента масиву
#n*n, де 1<=n<=5.
#Драч Ольга Олександрівна, 122-Д

from random import randint
import numpy as np
import timeit
def X(z):     #Функція для перевірки
    t_max = 0
    w_max = 0
    max1 = 0    #max елемент
    for c in range(len(z)):
        for d in range(len(z)):
            if z[c][d] > z[t_max][w_max]:
                max1 = z[c][d]
                t_max = c
                w_max = d
    return (f'Max:{max1} on {t_max+1},{w_max+1}')
n = int(input('Введіть число:'))
if 1 <= n <= 5:     #Створюємо масив
    m = n
    p = np.zeros((n,m),dtype=int)
    for h in range(n):
        for q in range(m):
            p[h][q] = randint(1,40)
    print('Індекс максимального елемента масиву:')
    print(X(p))
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=9999)
print(f'Програма працювала {t} секунд')

''''----------------------------------------------------------------------'''''

def A(z, v = 0, r = 0, v_max = 0, r_max = 0, max = 0):  #Функція для перевірки
    if r == len(z[v]):
        v += 1    #Рядок
        r = 0    #Стовпчик
    if v == len(z):
        return v_max, r_max
    if z[v][r] > z[v_max][r_max]:
        max = z[v][r]
        v_max = v
        r_max = r
    r += 1
    return A(z, v, r, v_max, r_max)
r = int(input('Введіть число:'))
if 1 <= r <= 5:    #Масив
    m = r
    z = np.zeros((r, m), dtype = int)
    for v in range(r):
        for r in range (m):
            z[v][r] = randint(1, 40)
    print('Індекс максимального елемента масиву:')
    print(A(z))
t = timeit.timeit('"-".join(str(n) for n in range(100))', number = 9999)
print(f'Програма працювала {t} секунд')

#Другий код зайняв приблизно пів дня написання,з перервами звісно,
#а ось перша приблизно дві години. 
#Перша читається краще другої.
#Рекурсія працює швидше ніж ітерація і займають однакову кількість пам'яті.
