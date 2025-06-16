import matplotlib.pyplot as plt
import random

def create_and_save_temperature_plot(days, temp_day, temp_night, file_name='temperature_plot.png'):
    """
    Функция для создания и сохранения графика температур.

    Аргументы:
    days - список дней недели.
    temp_day - список дневных температур.
    temp_night - список ночных температур.
    file_name - имя файла для сохранения графика.

    Возвращает:
    Имя файла, в котором сохранен график.
    """
    plt.figure(figsize=(8, 6))
    plt.plot(days, temp_day, marker='o', color='r', linestyle='--', label='Дневная температура')
    plt.plot(days, temp_night, marker='o', color='b', linestyle='--', label='Ночная температура')
    plt.title('Температура по дням недели')
    plt.xlabel('Дни недели')
    plt.ylabel('Температура, °C')
    plt.grid(True)
    plt.legend()
    plt.savefig(file_name)
    plt.close()  # Закрываем фигуру, чтобы предотвратить ее отображение в текущей сессии
    return file_name

# Пример данных
degrees_d = [random.randint(10, 25) for _ in range(7)]
degrees_n = [el-random.randint(5, 10) for el in degrees_d]
week = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']

# Вызов функции и печать результата
file_path = create_and_save_temperature_plot(week, degrees_d, degrees_n)
print(f"График сохранен в файле: {file_path}")
