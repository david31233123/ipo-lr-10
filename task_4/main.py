def intersectionAreaRect(rect1, rect2):
    (x1_left, y1_bottom), (x1_right, y1_top) = rect1
    (x2_left, y2_bottom), (x2_right, y2_top) = rect2

    if not (x1_left < x1_right and y1_bottom < y1_top):
        raise ValueError("Некорректный первый прямоугольник")
    if not (x2_left < x2_right and y2_bottom < y2_top):
        raise ValueError("Некорректный второй прямоугольник")

    x_left = max(x1_left, x2_left)
    y_bottom = max(y1_bottom, y2_bottom)
    x_right = min(x1_right, x2_right)
    y_top = min(y1_top, y2_top)

    if x_right <= x_left or y_top <= y_bottom:
        return 0
    return (x_right - x_left) * (y_top - y_bottom)

# Примеры использования:
if __name__ == "__main__":
    rectA = [[0, 0], [2, 2]]
    rectB = [[1, 1], [3, 3]]
    rectC = [[3, 3], [4, 4]]
    rectD = [[-1, -1], [1, 1]]
    rectE = [[2, 2], [1, 1]]

    print(intersectionAreaRect(rectA, rectB))  # 1.0
    print(intersectionAreaRect(rectA, rectC))  # 0
    print(intersectionAreaRect(rectA, rectD))  # 1.0
    try:
        print(intersectionAreaRect(rectA, rectE))
    except ValueError as e:
        print(e)
