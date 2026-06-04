def to_system(sys: int, n: int) -> str:
    if n == 0:
        return "0"

    if n == 1:
        return "1"

    result = ""
    while n > 0:
        result += str(n % sys)
        n //= sys

    return result[::-1]

def from_system(sys: int, n: str) -> int:
    result = 0
    for c in n:
        result = result * sys + int(c)
    return result
