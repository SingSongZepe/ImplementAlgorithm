

from typing import List

def superPow(a: int, b: List[int], m: int) -> int:
    if a == 1:
        return 1

    a %= 1337
    temp = a * a
    cycle_len = 1
    while temp != a:
        temp = (temp * a) % 1337
        cycle_len += 1

    remainder = 0
    for i in range(len(b)):
        remainder = (remainder * 10 + b[i]) % cycle_len

    if remainder == 0:
        remainder = cycle_len  # there is not 'a', it's the last element of the cycle

    result = 1
    for i in range(remainder):
        result = (result * a) % 1337
    return result



def test1():
    a = 2
    b = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    m = 1337
    result = superPow(a, b, m)
    print(result)


def main():
    test1()

if __name__ == '__main__':
    main()

