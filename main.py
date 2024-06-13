from PIL import Image
import pandas as pd

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def get_pixel_data(image_path):
    # Открытие изображения
    img = Image.open(image_path)

    # Получение размеров изображения
    width, height = img.size

    # Создание списка для хранения данных о пикселях
    pixel_data = []

    # Итерация по пикселям
    for y in range(height):
        for x in range(width):
            # Получение координат пикселя
            coordinates = (x, y)

            # Получение цвета пикселя
            color = img.getpixel(coordinates)

            # Преобразование цвета в HEX
            hex_color = rgb_to_hex(color)

            # Добавление данных в список
            pixel_data.append((coordinates[0], coordinates[1], hex_color))

    return pixel_data

# Путь к изображению
image_path = 'path/image_name.jpg'
pixels = get_pixel_data(image_path)

# Создание DataFrame из данных
df = pd.DataFrame(pixels, columns=['X', 'Y', 'Color'])

# Имя Excel файла
#excel_file = 'output_data.xlsx'
#df.to_excel(excel_file, index=False)

#print(f"Данные сохранены в файл: {excel_file}")

# Вывод данных
##for pixel in pixels:
    #print(df)
##    print(f"{pixel[0]}, {pixel[1]}, {pixel[2]}")

# Путь и имя файла-результата
output_file_path = 'path/file_name.txt'

# Открытие файла на запись ('w' означает режим записи)
with open(output_file_path, 'w') as file:
    # Запись данных в файл
    for pixel in pixels:
        file.write(f"{pixel[0]}, {pixel[1]}, {pixel[2]}\n")

print(f"Данные сохранены в файл: {output_file_path}")
