def to_binary(n):
    if n == 0:
        return "0"

    if n == 1:
        return "1"

    result = ""
    while n > 0:
        result += str(n % 2)
        n //= 2

    return result[::-1]

def to_ternary(n):
    if n == 0:
        return "0"

    if n == 1:
        return "1"

    result = ""
    while n > 0:
        result += str(n % 3)
        n //= 2

    return result[::-1]