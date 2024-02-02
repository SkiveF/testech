def solve(width, height, length, mass):
    is_bulky = width * height * length >= 1000000 or any(
        dimension >= 150 for dimension in [width, height, length])
    is_heavy = mass >= 20
    
    if is_bulky and is_heavy:
        return "rejected"
    elif is_bulky:
        return "special"
    elif is_heavy:
        return "special"
    else:
        return "standard"


if __name__ == '__main__':
    print(solve(10, 20, 30, 15))  # Output: "standard"
    print(solve(200, 100, 80, 10))  # Output: "special"
    print(solve(120, 120, 120, 25))  # Output: "rejected"
