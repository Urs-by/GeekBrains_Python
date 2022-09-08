# файл отвечающий за кодирование-декодирование
#import random

alfavit = ['а', 'б', 'в', 'г', 'д', 'е',
           'ё', 'ж', 'з', 'и', 'й', 'к',
           'л', 'м', 'н', 'о', 'п', 'р',
           'с', 'т', 'у', 'ф', 'х', 'ц',
           'ч', 'ш', 'щ', 'ъ', 'ы', 'ь',
           'э', 'ю', 'я']

code_matrix = [84, 63, 76, 90, 82, 59,
               75, 83, 62, 53, 52, 74,
               50, 58, 72, 77, 70, 78,
               88, 51, 55, 69, 66, 80,
               60, 85, 57, 67, 79, 61,
               64, 89, 71]

# метод создания произвольной матрицы уникальных элементов
# code_matrix = [0] * 33
# used = [0]
# for i in range(33):
#     number = 0
#     while number in used:
#         number = random.randint(50, 90)
#     code_matrix[i] = number
#     used.append(number)


def coding(leter):
    index_letter = alfavit.index(leter)
    code_letter = code_matrix[index_letter] - 33
    return code_letter


def decoding(number):
    number = number + 33
    index_letter = code_matrix.index(number)
    return alfavit[index_letter]