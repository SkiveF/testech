def different(N):
    if N == 0:
        return 0
    
    sign = 1
    if N < 0:
        sign = -1
        N = abs(N)
    
    digits = [int(digit) for digit in str(N)]
    result = digits[0] * 10 ** (len(digits) - 1) + 7 * (
        10 ** (len(digits) - 2) if len(digits) > 1 else 0)
    return result * sign


if __name__ == '__main__':
    n = 901
    result = different(n)
    print(result)
