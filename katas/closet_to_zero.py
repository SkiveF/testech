def closest_to_zero(numbers):
    min_num = min(numbers, key=lambda x: abs(x))
    return min_num


if __name__ == '__main__':
    numbers = [-15, -5, 2, 8, 9]
    s = closest_to_zero(numbers)
    print("Number closest to zero:", s)
