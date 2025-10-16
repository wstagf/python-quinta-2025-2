def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    print("hello")
    print("Fibonacci de 5:", fibonacci(5))
    print("Fibonacci de 10:", fibonacci(10))

if __name__ == "__main__":
    main()
    