from PIL import Image


def resize_image(image_path, output_size):
    """
    �������� ������ �����������.

    :param image_path: ���� � ��������� �����������.
    :param output_size: �������� ������ ����������� � ���� ������� (������, ������).
    :return: ���������� �����������.
    """
    image = Image.open(image_path)
    image.thumbnail(output_size)
    return image