def isCorrectRect(points):
    """
    Проверяет, корректно ли заданы координаты прямоугольника.
    Args:
        points (list): список из двух кортежей (x, y),
                       первый — левый нижний угол,
                       второй — правый верхний угол.
    Returns:
        bool: True, если координаты заданы правильно (x1 < x2 и y1 < y2), иначе — False.
    """
    (x1, y1), (x2, y2) = points
    return x1 < x2 and y1 < y2

# Примеры:
print(isCorrectRect([(-3.4, 1), (9.2, 10)]))  # True
print(isCorrectRect([(-7, 9), (3, 6)]))      # False
