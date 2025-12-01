def isCollisionRect(rect1, rect2):
    """
    Проверяет, пересекаются ли два прямоугольника.

    Args:
        rect1 (list): список из двух кортежей: [(x1_left, y1_bottom), (x1_right, y1_top)]
        rect2 (list): список из двух кортежей: [(x2_left, y2_bottom), (x2_right, y2_top)]

    Returns:
        bool: True, если прямоугольники пересекаются, иначе False
    """
    (x1_left, y1_bottom), (x1_right, y1_top) = rect1
    (x2_left, y2_bottom), (x2_right, y2_top) = rect2

    # Проверка, что прямоугольники не пересекаются
    if x1_right < x2_left or x1_left > x2_right:
        return False
    if y1_bottom > y2_top or y1_top < y2_bottom:
        return False

    # Если ни одно условие не выполнено — прямоугольники пересекаются
    return True

# Примеры использования:
if __name__ == "__main__":
    rectA = [ (0, 0), (2, 2) ]
    rectB = [ (1, 1), (3, 3) ]
    rectC = [ (3, 3), (4, 4) ]
    rectD = [ (2, 2), (4, 4) ]

    print(isCollisionRect([rectA[0], rectA[1]], [rectB[0], rectB[1]]))  # True (пересекаются)
    print(isCollisionRect([rectA[0], rectA[1]], [rectC[0], rectC[1]]))  # False (не пересекаются)
    print(isCollisionRect([rectA[0], rectA[1]], [rectD[0], rectD[1]]))  # True (касаются, пересекаются)
