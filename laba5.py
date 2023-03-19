import math as mt
import numpy as np
import matplotlib.pyplot as plt
import random
import pylab


def left_summa(a, b, n):
    int_summa = 0
    x_point = []
    y_point = []
    for x in np.arange(a, b, n):
        y = mt.sin(mt.pi*x/4) + x - 2
        int_summa += y*n
        x_point.append(x)
        y_point.append(y)
    return x_point, y_point, int_summa


def right_summa(a, b, n):
    int_summa = 0
    x_point = []
    y_point = []
    for x in np.arange(a, b, n):
        x += n
        y = mt.sin(mt.pi*x/4) + x - 2
        int_summa += y*n
        x_point.append(x)
        y_point.append(y)
    return x_point, y_point, int_summa


def average_summa(a, b, n):
    int_summa = 0
    x_point = []
    y_point = []
    for x in np.arange(a, b, n):
        x += n/2
        y = mt.sin(mt.pi*x/4) + x - 2
        int_summa += y*n
        x_point.append(x)
        y_point.append(y)
    return x_point, y_point, int_summa


def random_summa(a, b, n):
    int_summa = 0
    x_point = []
    y_point = []
    for x in np.arange(a, b, n):
        b = random.random()*n + x
        y = mt.sin(mt.pi * b / 4) + b - 2
        int_summa += y*n
        x_point.append(b)
        y_point.append(y)
    return x_point, y_point, int_summa


X_axis, Y_axis = [], []
a, b = 0, 8
d = int(input("Введите количество разбиений: "))
c = (b - a) / d  # шаг разбиения

# построение графика
for x in np.arange(a, b + c, c):
    y = mt.sin(mt.pi*x/4) + x - 2
    X_axis.append(x)
    Y_axis.append(y)

sp = [left_summa(a, b, c), right_summa(a, b, c), average_summa(a, b, c), random_summa(a, b, c)]
osn = ['Левое', 'Правое', 'Серединное', 'Случайное']
plt.suptitle(f"Лабораторная работа\nГрафики ф-ии sin(pi*x/4) + x - 2\nи визуальнуе представления интегральных сумм. "
             f"Разбиений: {d}")
plt.subplots_adjust(wspace=0.2, hspace=0.3)  # чтобы было расстояние между графиками

for i in range(4):
    #X_razb, Y_razb, pl = map(list, sp[i])
    X_razb, Y_razb, pl = sp[i][0], sp[i][1], round(sp[i][2], 4)
    #pl = pl[0]
    pylab.subplot(2, 2, i+1)
    plt.xlabel("Ось x")
    plt.ylabel("Ось у")
    plt.title(f"{osn[i]} оснащение, интегральная сумма = {pl}")
    plt.plot(X_axis, Y_axis, c='green')  # линия графика
    plt.stem(X_axis, Y_axis, 'b--')  # пунктирные стержни
    plt.axhline(y=0, c='000000')  # y = 0
    plt.scatter(X_razb, Y_razb, c='red', s=30)  # точки разбиения
    if (i == 0) or (i == 1):
        X_razb.insert(0, 0)
        Y_razb.insert(0, 0)
        X_razb.append(8)
        Y_razb.append(0)
        if i == 0:
            plt.step(X_razb, Y_razb, c='red', where='post')  # лесенка
        else:
            plt.step(X_razb, Y_razb, c='red', where='pre')  # лесенка

    if (i == 2) or (i == 3):
        Im_X, Im_Y = [0], [0]
        for i in range(len(X_axis) - 1):
            Im_X.append(X_axis[i])
            Im_X.append(X_axis[i + 1])
            Im_Y.append(Y_razb[i])
            Im_Y.append(Y_razb[i])
        Im_X.append(8)
        Im_Y.append(0)
        plt.plot(Im_X, Im_Y, c='red')  # график площадей разбиения
plt.show()
