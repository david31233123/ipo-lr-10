class RectCorrectError(Exception):
    pass

def intersectionAreaMultiRect(rects):
    if not rects:
        return 0
    for r in rects:
        (x1, y1), (x2, y2) = r
        if not (x1 < x2 and y1 < y2):
            raise RectCorrectError("Некорректный прямоугольник")
    x_left, y_bottom = rects[0][0]
    x_right, y_top = rects[0][1]
    for r in rects[1:]:
        (cx1, cy1), (cx2, cy2) = r
        x_left = max(x_left, cx1)
        y_bottom = max(y_bottom, cy1)
        x_right = min(x_right, cx2)
        y_top = min(y_top, cy2)
        if x_right <= x_left or y_top <= y_bottom:
            return 0
    return (x_right - x_left) * (y_top - y_bottom)

if __name__ == "__main__":
    rects = [
        [[0, 0], [4, 4]],
        [[1, 1], [3, 3]],
        [[2, 2], [4, 4]]
    ]
    print(intersectionAreaMultiRect(rects))
    rects_invalid = [
        [[0, 0], [4, 4]],
        [[5, 5], [3, 3]]
    ]
    try:
        print(intersectionAreaMultiRect(rects_invalid))
    except RectCorrectError as e:
        print(e)
