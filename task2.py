" Расчёт количества книг на дискете "
volume = 1.44
pages = 100
lines = 50
chars = 25
bytes_one_chars = 4

total_chars = pages * lines * chars
total_volume = total_chars * bytes_one_chars

disk_size = volume * 1024 * 1024
number_books = disk_size // total_volume
print('Количество книг на дискете:', number_books)

" Расчёт периметра и площади геометрических фигур "
pi = 3.1415
radius = 5
side = 5
square_circule = pi * radius ** 2
length_circule = 2 * pi * radius
perimetr = 4 * side
square = side * 2

print("Периметр:", perimetr)
print("Длина окружности:", round(length_circule, 2))
print("Площадь круга:", round(square_circule, 2))
print("Площадь квадрата:", square)

" Формирование строки из повторяющихся чисел "
" str numbers "
str_numbers = '0' * 20 + '1' * 50 + '2' * 30
print(" str numbers ", str_numbers)

