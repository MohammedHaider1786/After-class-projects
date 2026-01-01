class Expression:
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def calculate(self):
        result = (self.a + self.b) * self.c - (self.d / self.e)
        return result


def main():
    print("Solve the Expression: (a + b) * c - (d / e)")

    a = float(input("Enter value of a: "))
    b = float(input("Enter value of b: "))
    c = float(input("Enter value of c: "))
    d = float(input("Enter value of d: "))
    e = float(input("Enter value of e: "))

    exp = Expression(a, b, c, d, e)
    result = exp.calculate()

    print("Result =", result)


main()
