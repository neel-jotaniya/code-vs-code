class Calculator:
    def add(self, x, y):
        return x + y

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to Calculator!")
    print("Current feature: Addition")
    print("Example: 5 + 3 =", calc.add(5, 3))