from math import floor as f
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def get_closest_point(x1, y1, x2, y2):
    result = (f(x1), f(y1))
    if x2 * x2 + y2 * y2 < x1 * x1 + y1 * y1:
        result = (f(x2), f(y2))

    return result

print(get_closest_point(x1, y1, x2, y2))