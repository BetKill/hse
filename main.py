import os
from PIL import Image, ImageFilter, ImageDraw


try:
    original = Image.open(input('Введите название и расширение файла\n'))
    print("Изображение найдено\n")

    y = str(input('Применить эффект "черно-белый"?\n'))
    original.show()
    img = original
    draw = ImageDraw.Draw(img)  # Создаем инструмент для рисования
    width = img.size[0]  # Определяем ширину
    height = img.size[1]  # Определяем высоту
    pix = img.load()  # Выгружаем значения пикселей
    if y == "Да" or y == "да" or y == "yes" or y == "Yes" or y == "y" or y == "Y":
        for x in range(width):
            for y1 in range(height):
                r = pix[x, y1][0]
                g = pix[x, y1][1]
                b = pix[x, y1][2]
                sr = (r + g + b) // 3
                draw.point((x, y1), (sr, sr, sr))
        img.show()
        y1 = str(input('Сохранить?\n'))
        if y1 == "Да" or y1 == "да" or y1 == "ДА" or y1 == "yes" or y1 == "Yes" or y1 == "y" or y1 == "Y" or y1 == "д" or y1 == "Д":
            y = input('Введите название и расширение файлы\n')
            img.save(y)

    y = input('Применить фильтр размытия? \n')
    if y == "Да" or y == "да" or y == "ДА" or y == "yes" or y == "Yes" or y == "y" or y == "Y" or y == "д" or y == "Д":
        BLUR_1 = original.filter(ImageFilter.BLUR)
        original.show()
        BLUR_1.show()
        save_img = input('Сохранить?\n')
        if save_img == "Да" or save_img == "да" or save_img == "yes" or save_img == "Yes" or save_img == "y" or save_img == "Y":
            format_image = input('Введите название и расширение файлы \n')
            BLUR_1.save(format_image)

    y1 = input('Применить фильтр контура? \n')
    if y1 == "Да" or y1 == "да" or y1 == "ДА" or y1 == "yes" or y1 == "Yes" or y1 == "y" or y1 == "Y" or y1 == "д" or y1 == "Д":
        CONTOUR_1 = original.filter(ImageFilter.CONTOUR)
        original.show()
        CONTOUR_1.show()
        y1 = input('Сохранить?\n')
        if y1 == "Да" or y1 == "да" or y1 == "yes" or y1 == "Yes" or y1 == "y" or y1 == "Y":
            y = input('Введите название и расширение файлы \n')
            CONTOUR_1.save(y)

    y1 = input('Применить фильтр маскирование? \n')
    if y1 == "Да" or y1 == "да" or y1 == "ДА" or y1 == "yes" or y1 == "Yes" or y1 == "y" or y1 == "Y" or y1 == "д" or y1 == "Д":
        EDGE_ENHANCE_MORE_1 = original.filter(ImageFilter.EDGE_ENHANCE_MORE)
        original.show()
        EDGE_ENHANCE_MORE_1.show()
        y1 = input('Сохранить?\n')
        if y1 == "Да" or y1 == "да" or y1 == "ДА" or y1 == "yes" or y1 == "Yes" or y1 == "y" or y1 == "Y" or y1 == "д" or y1 == "Д":
            y = input('Введите название и расширение файлы \n')
            EDGE_ENHANCE_MORE_1.save(y)

    y1 = input('Применить фильтр FIND_EDGES? \n')
    if y1 == "Да" or y1 == "да" or y1 == "ДА" or y1 == "yes" or y1 == "Yes" or y1 == "y" or y1 == "Y" or y1 == "д" or y1 == "Д":
        FIND_EDGES_1 = original.filter(ImageFilter.FIND_EDGES)
        original.show()
        FIND_EDGES_1.show()
        y1 = input('Сохранить?\n')
        if y1 == "Да" or y1 == "да" or y1 == "ДА" or y1 == "yes" or y1 == "Yes" or y1 == "y" or y1 == "Y" or y1 == "д" or y1 == "Д":
            y = input('Введите назваение и расширение файлы \n')
            FIND_EDGES_1.save(y)

except FileNotFoundError:
    print("Файл не найден")



# print(img.size, img.format, img.mode)