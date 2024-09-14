import math


class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Number(self.num + other.num)

    def __sub__(self, other):
        return Number(self.num - other.num)

    def __mul__(self, other):
        return Number(self.num * other.num)

    def __truediv__(self, other):
        return Number(self.num / other.num)

    def __str__(self):
        return str(self.num)


def main():
    n1 = Number(int(25))
    n2 = Number(int(5))
    res1 = n1 + n2
    res2 = n1 - n2
    res3 = n1 * n2
    res4 = n1 / n2
    res5 = (res1 + res2 * res4) / res3
    res4.num, res5.num = int(res4.num), int(res5.num)
    print(f"{n1} + {n2} = {res1}")
    print(f"{n1} - {n2} = {res2}")
    print(f"{n1} * {n2} = {res3}")
    print(f"{n1} / {n2} = {res4}")
    print(f"({res1} + {res2} * {res4}) / {res3} = {res5}")


if __name__ == "__main__":
    main()
