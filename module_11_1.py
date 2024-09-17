import pandas as pd    # установила pandas через терминал - pip install pandas
import numpy as np
import matplotlib.pyplot as plt      # установила matplotlib через терминал - pip install matplotlib
import gdown           # pip install gdown==4.6.0, с другой версией могут возникнуть проблемы со скачиванием
import os


if not os.path.exists('pizza.csv'):    # проверка наличия файла, если нет, то скачать
    gdown.download(id='1YjYU5S99o49tX_HWyGjp2JgZbEkAklnM')    # загрузка файла с Google Drive по ID файла

# Библиотека pandas
pd.set_option('display.max_columns', None)   # сброс ограничений на количество выводимых  столбцов, чтобы посмотреть все заголовки
pd.set_option('display.max_rows', 7)    # посмотреть начало и конец таблицы, также для полного вывода таблицы с днями недели - далее
pizza_df = pd.read_csv('pizza.csv', sep=';', low_memory=False)  # чтение файла целиком и удаление символов
# print(pizza_df)    # посмотрим таблицу и заголовки столбцов(данных) в консоли с учетом ранее выставленных настроек

# Посчитаем зависимость проданной пиццы от дня недели
pizza_df['order_day'] = pd.to_datetime(pizza_df['order_date']).dt.day_name('ru')    # конвертирование даты в удобный формат (дата без указания времени), после конвертирование даты в дни недели ('dt.day_name()')
# print(pizza_df)    # посмотрим, что столбец с днями недели добавился в конец
day_sales = pizza_df['order_day'].value_counts().reset_index()    # подсчёт частоты уникальных значений в колонке order_day, так узнаем сколько пицц в какой день недели продалось
day_sales.columns = ['День недели', 'Количество проданной пиццы, шт.']    # присвоила название столбцам для обращения к ним при построении будущего графика графика
print(day_sales)


# Библиотека matplotlib
fig, ax = plt.subplots(figsize=(10, 6)) # создание окна, в котором будет нарисован график, а также указание размера окна
values = day_sales['Количество проданной пиццы, шт.']
index = day_sales['День недели']
colors = ['#FC6C85', '#A890F0', '#9966CC', '#6890F0', '#1b9e77', '#a9f971', '#D5713F']
ax.barh(index, values, color=colors)
ax.set_title('Диаграмма зависимости количества проданной пиццы от дня недели', fontsize=12)
ax.set_xlabel('Количество проданной пиццы, шт.', fontsize=10)
ax.set_ylabel('Продажи по дням недели', fontsize=10)
plt.xticks(fontsize=10)  # размер шрифта обозначений по X
plt.yticks(rotation=30, fontsize=8)  # наклон обозначений по Y и размер шрифта по Y
plt.grid()  # отображение сетки
plt.show()  # отображение окна


# Библиотека numpy
arr = np.array([x * y for x in range(1, 11) for y in range(3, 8)])  # создали массив чисел
# print(arr)    # посмотреть что получилось
arr_3D = arr.reshape(2, 5, 5)  # преобразовали в трехмерный массив
print(arr_3D, '\n--------------------------')  # посмотреть что получилось и проверить дальнейшие расссчеты

# Математические операции
sum_arr_3D_0 = np.sum(arr_3D, axis=0)  # cложение вдоль оси 0 - поэлементное сложение двух матриц.
print(sum_arr_3D_0, '\n--------------------------')

sum_arr_3D_1 = np.sum(arr_3D, axis=1)  # cложение вдоль оси 1 - складываются столбцы каждой матрицы
print(sum_arr_3D_1, '\n--------------------------')

sum_arr_3D_2 = np.sum(arr_3D, axis=2)  # cложение вдоль оси 2 - складываются строки каждой матрицы
print(sum_arr_3D_2, '\n--------------------------')

arr_3D_new = arr_3D / np.arange(1, 6)  # операция деления
print(arr_3D_new)
