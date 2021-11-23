import numpy as np
import random


# Инициализация генеротора случайных чисел
np.random.seed(100)
# Количество повторов в методе Монте-Карло
n_rep = 100
# Вероятность блокировки
p_refuse = 0
# Имитационное моделирование
for i in range(n_rep):
# Количество концентраторов
    k = 2
# Количество пакетов
    n_packets = 1000
# Текущее время
    t = 0
# текущий размер очереди
    queue = 0
# Интесивность входного потока
    lambda_day = 2
# Максимальный размер очереди
    m = 6
# Интенсивность выходного потока
    mu = 2
# время, когда прибор освободится
    t_free = []
    for j in range(k):
        t_free.append(0)
# Количество потярянных пактеов
    n_lost = 0
    for f in range(n_packets):
# время поступления нового пакета
        t += np.random.exponential(scale=1/lambda_day)
# проверяем, свободен ли концентратор
        n = 0
        if queue > 0:
            for j in range(k):
                while t_free[j] < t and queue > 0:
                    t_free[j] += np.random.exponential(scale=1/mu)
                    queue -= 1
        for h in range(k):
            if t_free[h] < t:
                t_free[h] = t + np.random.exponential(scale=1/mu)
                break
            else:
                n += 1
        if n == k:
            if queue < m:
                queue += 1
            else:
                n_lost += 1
#print('потеряно '+str(n_lost)+' из '+str(n_packets))
    p_refuse += n_lost/n_packets

# Оценка вероятности блокировки
p_refuse /= n_rep
print('average probability = '+str(p_refuse))
