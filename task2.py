def sort_arr(arr):
    """Функция сортировки массива"""
    n = len(arr)
    if n <= 1:
        return arr
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def get_ranks(numbers):
    """Функция вычисления рангов"""
    # Связываем числа с индексами: (число, индекс)
    indexed_numbers = []
    for i in range(len(numbers)):
        num = numbers[i]
        indexed_numbers.append((num, i))

    # Сортируем
    sorted_numbers = sort_arr(indexed_numbers)

    # Вычисляем ранги
    ranks = [0] * len(numbers)  # создание массива, заполненного нулями, той же длины, что и numbers
    n = len(sorted_numbers) # длина отсортированного массива
    i = 0
    while i < n:
        current_num = sorted_numbers[i][0]
        start_index = i
        while i < n and sorted_numbers[i][0] == current_num: # Находим все одинаковые числа
            i += 1
        end_index = i
        # Средний ранг для группы
        average_rank = (start_index + end_index + 1) / 2
        # Записываем ранги в исходные позиции
        for j in range(start_index, end_index):
            original_index = sorted_numbers[j][1]
            ranks[original_index] = average_rank
    return ranks


# Ввод данных
while True:
    try:
        nums = list(map(float, input("Введите числа через пробел: ").split()))
        break
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа через пробел.")

# Вычисляем ранги
ranks_of_nums = get_ranks(nums)

# Вывод
print("Ранги чисел:", ranks_of_nums)