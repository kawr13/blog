from PIL import Image


def resize_image(image_path, output_size):
    """
    Изменяет размер изображения.

    :param image_path: Путь к исходному изображению.
    :param output_size: Желаемый размер изображения в виде кортежа (ширина, высота).
    :return: Измененное изображение.
    """
    image = Image.open(image_path)
    image.thumbnail(output_size)
    return image